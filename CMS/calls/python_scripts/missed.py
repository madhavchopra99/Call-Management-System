import csv


def missed_calls(ivr_file_entry, mobile_file):

	with open(mobile_file, 'r') as mobile_record_file:

		# if call is missed we open mobile file to check for outgoing to that number
		csv_mobile_file = csv.reader(mobile_record_file)

		for mobile_file_entry in csv_mobile_file:

			if mobile_file_entry[4] == ivr_file_entry[4] and (mobile_file_entry[1] == "Outgoing" or mobile_file_entry[1] == "Incoming") and mobile_file_entry[3] == 'Missed':

				return {ivr_file_entry[4]: ivr_file_entry[11]}

			elif mobile_file_entry[4] == ivr_file_entry[4] and (mobile_file_entry[1] == 'Outgoing' or mobile_file_entry[1] == 'Incoming') and mobile_file_entry[3] == 'Connected' and int(mobile_file_entry[8]) < 10:

				# in above ivr_file_entry mbivr_file_entry[3] = mobile number, mbivr_file_entry[0] = event, mbivr_file_entry[6] is duration, mobile_file_entry[2] is status
				return {ivr_file_entry[4]: ivr_file_entry[11]}

			elif mobile_file_entry[4] == ivr_file_entry[4] and (mobile_file_entry[1] == 'Outgoing' or mobile_file_entry[1] == "Incoming") and mobile_file_entry[3] == 'Connected' and int(mobile_file_entry[8]) > 10:

				return {}

	return {}
