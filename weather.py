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
	print columns
