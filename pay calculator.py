
# Calculate estimated paycheck after deductions.

def pay():
	ST_hours = input("Enter number of standard hours: ")
	OT_hours = input("Enter number of overtime hours: ")
	ST_pay = float(ST_hours) * 24
	OT_pay = float(OT_hours) * 36
	gross_pay = ST_pay + OT_pay
	net_pay = gross_pay - (gross_pay * 0.305835)
	print("Gross income: $" + str(round(gross_pay,2)))
	print("Net income: $" + str(round(net_pay,2)))

	restart = str(input("Press y to restart: "))
	if restart == 'y':
		print("")
		pay()
	else:
		print("")
		print("Ok bye.")
pay()
