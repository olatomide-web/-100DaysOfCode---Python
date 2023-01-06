##number = int(input("enter a number: "))
##
##if number % 2 = 0:
##    print("this is an even number")
##else:
##    print("this is an odd number")
    
###########solution####################

##number = int(input("enter a number: "))
##
##if number % 2 == 0:
##    print("this is an even number")
##else:
##    print("this is an odd number")
##

# == - equals to
# = assignment



#########################################

##year = input("which year do you want to check?: ")
##
##if year % 4 == 0:
##    if year % 100 == 0:
##        if year % 400 == 0:
##            print("Leap Year")
##        else:
##            print("Not a leap year")
##    else:
##        print("leap year")
##else:
##    print("Not a leap year")


############solution#########################

##year = int(input("which year do you want to check?: "))
##
##if year % 4 == 0:
##    if year % 100 == 0:
##        if year % 400 == 0:
##            print("Leap Year")
##        else:
##            print("Not a leap year")
##    else:
##        print("leap year")
##else:
##    print("Not a leap year")


#########################################

##for number in range(1,101):
##    if number % 3 == 0 or number % 5 == 0:
##        print("FizzBuzz")
##    if number % 3 == 0:
##        print("Fizz")
##    if number % 5 == 0:
##        print("Buzz")
##    else:
##        print([number])


##########solution#######################

##for number in range(1,101):
##    if number % 3 == 0 and number % 5 == 0:
##        print("FizzBuzz")
##    elif number % 5 == 0:
##        print("Buzz")
##    elif number % 3 == 0:
##        print("Fizz")  
##    else:
##        print(number)
