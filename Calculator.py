#Calculator for two numbers
#Kushagra

exit = False
while exit == False:
    enter = True
    a =  input("Enter the first number or type exit to end:\n")
    if a == "Exit" or a == "exit" or a == "EXIT" :
        exit = True
        break

    else:
        x = float(a)
        y = float(input("Enter the second number:\n"))

        opt = input("Choose one of them: Add or + , Subtract or - , Muiltiply or * , Divide or / \n")

        if opt == "Add" or opt == "add" or opt == "ADD" or opt == "+" :                              #Addition
            print(f"{x} + {y} = {x+y}")
            enter = True
        
        elif opt == "Subtract" or opt == "subtract" or opt == "SUBTRACT" or opt == "-" :            #Subtraction
            print(f"{x} - {y} = {x-y}")
            enter = True

        elif opt == "Muiltiply" or opt == "muiltiply" or opt == "MUILTIPLY" or opt =="*" :         #Muiltiplication
            print(f"{x} * {y} = {x*y}")
            enter = True

        elif opt == "Divide" or opt == "divide" or opt == "DIVIDE" or opt == "/" :                  #Division
            enter = True
            print(f"{x} / {y} = {x/y}")
        
        else:
            print("ERROR! \nPlease enter correct option and rewrite the  numbers")
            
         
