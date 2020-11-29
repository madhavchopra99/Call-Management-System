import csv
from calls.python_scripts.missed import missed_calls


def connected_calls(ivr_file, mobile_file):

    # function to create a call logs
    # ivr is initial file, mobile file is used in missed case and logfile is name of created file

    with open(ivr_file, 'r') as ivr_record_file:

        csv_ivr_file = csv.reader(ivr_record_file)
        next(csv_ivr_file)

        # Dict is used to avoid the overlapping values in logfile and it is hashed.
        dump_redundancy_set = {}
        # set is used to avoid the overlapping values in logfile and it is hashed.
        checked_entry = set({})

        MCDp1 = 12 + 10
        MCDp2 = 15 + 10
        MCDp3 = 18 + 10
        MCDanimesh = 15 + 10

        for ivr_file_entry in csv_ivr_file:

            notes = ivr_file_entry[15].split()
            notes.append('empty')

            if ivr_file_entry[3] == 'Missed' and ivr_file_entry[4] not in checked_entry and notes[0] != 'Spam' and notes[0] != 'NR' and notes[0] != 'spam':

                dump_redundancy_set.update(
                    missed_calls(ivr_file_entry, mobile_file))

            elif ivr_file_entry[3] == 'Connected' and ivr_file_entry[4] not in checked_entry and notes[0] != 'Spam' and notes[0] != 'NR' and notes[0] != 'spam':

                if ivr_file_entry[11] == '':

                    dump_redundancy_set[ivr_file_entry[4]] = ivr_file_entry[11]

                elif int(ivr_file_entry[8]) < MCDp1 and ivr_file_entry[11] == 'DLF Cyber City':

                    dump_redundancy_set[ivr_file_entry[4]] = ivr_file_entry[11]

                elif int(ivr_file_entry[8]) < MCDp2 and ivr_file_entry[11] == 'Reservation Team':

                    dump_redundancy_set[ivr_file_entry[4]] = ivr_file_entry[11]

                elif int(ivr_file_entry[8]) < MCDp3 and ivr_file_entry[11] == 'Sushant Lok':

                    dump_redundancy_set[ivr_file_entry[4]] = ivr_file_entry[11]

                elif int(ivr_file_entry[8]) < MCDanimesh and ivr_file_entry[11] == 'golf course road':

                    dump_redundancy_set[ivr_file_entry[4]] = ivr_file_entry[11]

            elif ivr_file_entry[3] == 'Voicemail' and ivr_file_entry[4] not in checked_entry and notes[0] != 'Spam' and notes[0] != 'NR' and notes[0] != 'spam':

                dump_redundancy_set.update(
                    missed_calls(ivr_file_entry, mobile_file))

            checked_entry.add(ivr_file_entry[4])

    return dump_redundancy_set
