import csv
import matplotlib.pyplot as plt
import numpy as np
from django.conf import settings


def analyse(path_file):

    with open(path_file) as csv_ivr:

        csv_ivr_file = csv.reader(csv_ivr)

        Missed_calls = []

        for record in csv_ivr_file:
            notes = record[15].split(' ')
            notes.append('empty')
            if record[3] == 'Missed' and notes[0] != 'Spam' and notes[0] != 'NR' and notes[0] != 'spam':
                Missed_calls.append(int(record[8]))

        csv_ivr.seek(0)
        Connected_calls = []

        for record in csv_ivr_file:
            notes = record[15].split(' ')
            notes.append('empty')
            if record[3] == 'Connected' and notes[0] != 'Spam' and notes[0] != 'NR' and notes[0] != 'spam':
                Connected_calls.append(int(record[8]))

        csv_ivr.seek(0)
        Voicemail = []

        for record in csv_ivr_file:
            notes = record[15].split(' ')
            notes.append('empty')
            if record[3] == 'Voicemail' and notes[0] != 'Spam' and notes[0] != 'NR' and notes[0] != 'spam':
                Voicemail.append(int(record[8]))

        plt.figure(1)
        plt.hist(Missed_calls, np.arange(
            0, max(Missed_calls) + 20, 10), histtype='bar')
        plt.xlabel('Duration')
        plt.ylabel('No. of calls')
        plt.title('Missed calls in ivr file')
        plt.draw()
        plt.savefig(settings.BASE_DIR / 'media/Missed_calls.jpeg')

        plt.figure(2)
        plt.hist(Connected_calls, np.arange(
            0, max(Connected_calls) + 20, 10), histtype='bar')
        plt.xlabel('Duration')
        plt.ylabel('No. of calls')
        plt.title('Connected calls in ivr file')
        plt.draw()
        plt.savefig(settings.BASE_DIR / 'media/Connected_calls.jpeg')

        plt.figure(3)
        plt.hist(Voicemail, np.arange(
            0, max(Voicemail) + 20, 10), histtype='bar')
        plt.xlabel('Duration')
        plt.ylabel('No. of calls')
        plt.title('Voicemails in ivr file')
        plt.draw()
        plt.savefig(settings.BASE_DIR / 'media/Voicemail.jpeg')
