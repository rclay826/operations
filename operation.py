#This function adds two numbers 
def add(x,y):
    return x + y

#This function subtracts two numbers
def subtract(x,y):
    return x - y

#This function multiplies two numbers
def multiply(x,y):
    return x * y

#This function divides two numbers
def divide(x,y):
    return x / y

#This function squares one number
def get_squared(num):
    return num * num

def show_menu():
    print("Select operation.")    
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Square")
    

if __name__ == "__main__":
    show_menu()

    while True:
        #take input from the user
        choice = input("Enter choice(1/2/3/4/5):")
        #check if choice is one of the four options
        if choice in ("1","2","3","4","5"):
            try:
                num1 = float(input("Enter first number:"))
                
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == '1': 
                num2 = float(input("Enter second number:"))
                print(num1 , "+" , num2, "=", add(num1 , num2))
            elif choice == '2':
                num2 = float(input("Enter second number:"))
                print(num1 , "-", num2, "=", subtract(num1 , num2))
            elif choice == '3':
                num2 = float(input("Enter second number:"))
                print(num1,"*", num2, "=", multiply(num1 , num2))
            elif choice == '4':
                num2 = float(input("Enter second number:"))
                print(num1,"/", num2, "=", divide(num1 , num2))
            elif choice == '5':
                print(num1, "^2", "=", get_squared(num1))

            #check if user wants another calculation
            #break the while loop if answer is no
            next_calculation = input("Lets do next calculation? (yes/no):")
            if next_calculation == "no":
                break
        else:
            print("Invalid Input")