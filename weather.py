# Initialize variables to hold day with biggest spread and biggest spread
day_with_biggest_spread = None
biggest_spread = None

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
	#remove the asterics bound with numbers in the respective columns
	max_temp = columns[1].rstrip('*') 
	min_temp = columns[2].rstrip('*')
	# print day_of_month
	# print max_temp
	# print min_temp
	#first line contains text elements, so go immediately to the next line
	if day_of_month.isalpha():
		continue
	spread = int(max_temp) - int(min_temp)
	# print spread

	if day_with_biggest_spread is None and biggest_spread is None:
		day_with_biggest_spread = day_of_month
		biggest_spread = spread
	else:
		if spread > biggest_spread:
			biggest_spread = spread
			day_with_biggest_spread = day_of_month

file_pointer.close()

print day_with_biggest_spread, biggest_spread
