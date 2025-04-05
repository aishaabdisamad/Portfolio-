'''
Write a program that calculates the future value of an investment given an initial balance
and an annual interest rate compounded monthly. Your program should prompt the user
for the initial balance and interest rate and print out the balance after the first four months
in a table format.
'''


'''use a method to calculate the future value using the initial balance, annual interest rate and number of months
as parameters to pass the infromation gathered from the user through in order to calculate the future value''' 
def futureValueFormula(initialBalance, annualInterestRate, numMonths, futureValues): 

# future value formula for interest compunded monthly is FV = PV(1+ r/n)^ months
    # n = the number of compounding periods 
    n = 12 
    
    '''use a for loop to claculate the future value of ivestment for each month my looping through 
    each month and using the formula to calculate the value '''
    for month in range (1, numMonths +1):
        
        #declare a variable to store the future value formula 
        futureValue = initialBalance *(1 + annualInterestRate/n) ** month
        #use the append method to add the future investment values for each month at the end of the list as the loop goes through each month
        futureValues.append(futureValue)

    return futureValues
    


'''use a method to create a table that displays the number of months as integers on the left 
    and the future investment value for each month on the right '''

def valueTable(numMonths, futureValues): 
    # print the table headers and the lines for the table 
    print("Month | Future Value")
    print("--------------------")

    #use a for loop to adjust the future value for each month
    for month, investmentValue in zip(numMonths, futureValues):
        print(f"{month}     | {investmentValue: .2f}")


#this variable will hold the number of months (4) 
numMonths = 4

# prompt the user for their initial balance 
initialBalance = float(input("what is your intial balance?: "))

#prompt the user for their annual interest rate
annualInterestRate = float(input("what is your annual interest rate in decimal?: ")) 

#decalre an array that will store a list of future values 
futureValues = []

#call the futureValueFormula to display the calculations done inside the value returning method 
futureValues = futureValueFormula(initialBalance, annualInterestRate, numMonths, futureValues)

# call the ValueTable Method print the table
valueTable(range(1, numMonths +1), futureValues)


