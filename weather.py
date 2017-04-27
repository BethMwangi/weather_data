file_pointer = open('weather.dat', 'r')
for line in file_pointer:
	# print line
	line = line.rstrip('\n')
	# print line
	# get rid of empty lines/rows
	if line == '':
		continue
	# print line
	columns = line.split(" ")
	#get rid of empty list elements created by non-uniform spaces
	# in the columns
	columns = [item for item in columns if  item != ""]
	# print columns
	day_of_month = columns[0].strip()
	max_temp = columns[1].rstrip('*')
	min_temp = columns[2].rstrip('*')
	# print day_of_month
	# print max_temp
	# print min_temp