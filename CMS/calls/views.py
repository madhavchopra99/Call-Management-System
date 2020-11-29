from pathlib import Path
import csv
import calls.python_scripts.analytics as analytics
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from calls.python_scripts.main import *


def write(ivr_file_entry, redundancy_set, csv_response):

    # this function is to write data in log_file

    # used to check if value preexits in file
    if ivr_file_entry[4] not in redundancy_set:

        ivr_file_entry = list([ivr_file_entry[4], ivr_file_entry[3], ivr_file_entry[8],
                               ivr_file_entry[11], ivr_file_entry[9]])  # create the row to push in logfile

        # in above ivr_file_entry[4] is mobile number, ivr_file_entry[3] is status, ivr_file_entry[8] is duration, ivr_file_entry[11] is department

        # ivr_file_entry[0] is mobile number as it is primary key
        redundancy_set.add(ivr_file_entry[0])
        csv_response.writerow(ivr_file_entry)


def logs(request):

    context = {}

    if request.method == 'POST':

        try:

            ivr_file = request.FILES['ivr']
            mobile_file = request.FILES['mobile']

            fs = FileSystemStorage()

            if fs.exists('ivr_file.csv'):
                fs.delete('ivr_file.csv')

            if fs.exists('mobile.csv'):
                fs.delete('mobile.csv')

            fs.save('ivr_file.csv', ivr_file)
            fs.save('mobile.csv', mobile_file)

            path_ivr = settings.BASE_DIR / 'media/ivr_file.csv'
            path_mobile = settings.BASE_DIR / 'media/mobile.csv'
            path_response = settings.BASE_DIR / 'media/response.csv'

            dump_redundancy_set = main(path_ivr, path_mobile)

            with open(path_ivr) as csv_ivr, open(path_response, 'w') as response:

                csv_ivr_file = csv.reader(csv_ivr)
                next(csv_ivr_file)

                csv_response = csv.writer(response)
                csv_response.writerow(
                    ['Mobile_Number', 'Status', 'Duration', 'Department (if any)', 'Time'])

                redundancy_set = set({})

                for ivr_file_entry in csv_ivr_file:

                    if ivr_file_entry[4] in dump_redundancy_set:

                        write(ivr_file_entry, redundancy_set, csv_response)

            context['result'] = 'success'

        except Exception as e:

            context['exception'] = e
            print(e)

    return render(request, 'index.html', context)


def ivr_histogram(request):

    path_ivr = settings.BASE_DIR / 'media/ivr_file.csv'
    analytics.analyse(path_ivr)

    return render(request, 'ivr_histogram.html')


def result(request):

    context = {}
    path_response = settings.BASE_DIR / 'media/response.csv'
    with open(path_response) as response:
        csv_response = csv.reader(response)
        result = []

        for row in csv_response:
            result.append(row)

    context['heading'] = result.pop(0)
    context['result'] = result

    return render(request, 'result.html', context)
