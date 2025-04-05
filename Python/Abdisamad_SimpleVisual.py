'''Create a program that asks the user to enter today's sales (integer values) for an unlimited
number of stores, only stopping when the user enters the word Exit.
For every entry, the app must display a bar chart representing each store's sales. The bar
chart will be made of asterisks (*) symbols, with each asterisk representing $100.
If a sales amount is not an exact multiple of 100 (e.g., 123, 450, 575), then the number of
asterisks displayed should be rounded down (e.g., $450 would display four asterisks
****).
Your code must use the following function to display the bar chart:
def print_graph(store_num, store_sales):
o Where store_num is an integer value indicating the current store.
o Where store_sales is today's sales for a given store'''

#use a method to print the graph, make sure to use storeNum and storeSales as paramters so they can be used in the method even if its decalred in the main
def printGraph(storeNum, storeSales):
    
    #divide the store sales by 100 so 1 astrict represents 100
    numAstricks = storeSales // 100

    #print out the astricks (bar grpah)
    print(f"Store {storeNum}: {'*' * numAstricks}")

    


#declare storesSales as an empty dictionary and set storeNum equal to 1 
storesSales = {}
storeNum = 1 

'''Use a while loop to infinitely repeat the prompt and increase the store number by 1 each time it loops until the condition has been met, 
Then break the loop with an if statment when the storeSales equals -1. While "True" means it will loop indfinitly until checked'''
while True: 
    
    #use a try except to throw an error of an incorrect value is entered, then repeat the code
    try: 

        # decalre storeSales (diffrent than the dictionary to store the value for each store number)
        storeSales = int(input(f"Enter todays sales for store {storeNum} in interger (or -1 to quit): "))

        #This if statment will break the loop if -1 is entered
        if storeSales == -1:
         break
        
         #assign storesales to the correct storeNum, by using the values in the storesSales dictionary
        storesSales[storeNum] = storeSales
        
        #call the print graph method
        printGraph(storeNum, storeSales)
        storeNum += 1
    
    #second part of the try exepcpt block will catch the error
    except ValueError as e: 
        print(f"Error: {e}")


