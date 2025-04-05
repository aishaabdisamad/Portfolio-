'''You need to write a program that prints monthly paycheck for an employee.
The program should read the name and salary (hourly rates), as well as the total number
of hours worked in the past month. Make sure that your program accepts fractional hours.
Then the program should calculate the pay. If the employee is worked more than 160
hours per month, then they overtime work (over 160 hours) should be paid at 150 percent
of their regular wage. Additionally, all employees are subject to a 10% tax deduction on
their gross pay.'''


#prompt the employee for their name and store it to the employeeName variable 
employeeName = input("Employee Name: ")

#prompt the user for their hourly rate as a float and store it to the hourlyRate variable 
hourlyRate = float(input("Hourly Rate: "))

#prompt the user for the total number of hours worked in the past month as a float and save it to the totalHoursWorked Variable 
totalHoursWorked = float(input("Hours: "))

#use the min and max functions to determine when regular hours are inputed and when overtime hours are inputed 
regularHours = min(totalHoursWorked, 160)
# subtract the total hours worked inputed by the user by 160 to find the overtime hours 
overtimeHours = max(totalHoursWorked -160, 0)

# declare variables to store and calculate the infromation needed 
regularPay = regularHours * hourlyRate
overtimePay = overtimeHours * hourlyRate * 1.5
grossPay = overtimePay + regularPay 
taxDeduction = grossPay* 0.1 
netPay = grossPay - taxDeduction

# print out the employees information 
print(employeeName)
print(f"Total Hours Worked: {totalHoursWorked: .2f}")
print(f"Regular Pay: {regularPay: .2f}")
print(f"Overtime Pay: {overtimePay: .2f}")
print(f"Gross Pay: {grossPay: .2f}")
print(f"Tax Deduction: {taxDeduction: .2f}")
print(f"Net Pay: {netPay: .2f}")