def collatz(number):
    if number % 2 == 0: # if even print number divided by 2 and return number
        result = number // 2
    else: # if odd print number * 3 + 1 and return number
        result = (3 * number + 1)

    print(result) # print new number
    return(result) # return new number
    
def main():
    try:  
        number = int(input('Enter Number: ')) # user input type integer 
        while number != 1: # loop until number = 1
            number = collatz(number) # update number with return value
    except ValueError: # non-integer input
        print('Invalid Input: only integers are accepted')

main()
    


        