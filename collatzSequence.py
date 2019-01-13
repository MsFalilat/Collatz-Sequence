#This program is an implementation of the Collatz Sequence

def collatz(number):

    if (number % 2 == 0): #if value is even
        number = int(number // 2) #divide value by two and set value to output
    else: #if value is odd
        number = int(3 * number + 1) #multiply value by three and add one and set value to output

    return number #return value of function call
   
  
print('Enter a number: ') #prompts user for input
try: 
    num = int(input()) #stores user input in variable 'num'
    
    while (collatz(num) != 1): #While the value of the function call on the user input does not equate to 1
        #calls collatz function on user input and sets variable storing user input to the value evaluated by the function call
        num = collatz(num)
        print(num) #prints the current number that will be passed into the collatz function next
        
        if (collatz(num) == 1): #if the number evaluates to 1 after being passed to the collatz function, the while loop stops
            print(collatz(num))
            break
except ValueError: #ValueError exception thrown is user inputs anything but an integer 
    print('Error: must enter an integer')


