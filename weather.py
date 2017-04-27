file_pointer = open('weather.dat', 'r')
for line in file_pointer:
	# print line
	line = line.rstrip('\n')
	# print line
	# get rid of empty lines/rows
	if line == '':
		continue
	print line