def dateIsBefore(year1, month1, day1, year2, month2, day2):
	if year1 < year2:
		return True
	if month1 < month2:
		return True
	if month1 == month2:
		return day1 < day2
	else:
		return False

print dateIsBefore(1991,06,12,2000,04,2)