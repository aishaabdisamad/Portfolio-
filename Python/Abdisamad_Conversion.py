'''You should write a program that can convert the Canadian dollar to US Dollars. The
program should first read today's price for one CAD in US Dollars; and then should read
the values (in CAD) that you want to convert to USD'''

#prompt the user for how many USD is in a CAD (according to google the conversion rate is 0.74)
conversionRate = float(input("How many USD in a CAD?"))


'''use a while loop to continue to loop or repeat the prompt almost infinitely until the condition has been met, 
then break the loop with an if statment when the canadian amount entered is 0. 
While "True" means it will loop indfinitly until checked'''

while True: 
    #prompt the user for their amount in canadian then store it to the canadianAmount variable that was declared
    canadianAmount = float(input("Enter an amount in CAD (0 to quit): "))
    #use an if statment to break the loop when the condition is meet
    if canadianAmount == 0:
        print("All done!")
        break

    '''declare a variable that will claculate the USD amount by multiplying the Canadian amount entered
    by the conversion rate then store the calculated amount'''
    usdAmount = canadianAmount * conversionRate

    #print the canadian amount then the amount in USD
    print(f"{canadianAmount} CAD is {usdAmount} USD")


