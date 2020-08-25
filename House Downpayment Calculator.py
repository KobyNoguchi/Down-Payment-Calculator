from sys import argv
prompt = '> '

#from sys import argv takes input from the user

def readInt():
    while True:
        val = input("Enter an integer etc. ")
        try:
            return(int(val)) #convert int string to int before returning
        except ValueError:
            print(val, "is not an integer")

a = int(input("What is your annual salary? \n > "))
except ValueError:
    print(a, " is not an integer")

b = int(input("What percent (%) of your salary would you like to put into savings? \n > "))
except ValueError:
    print(b, " is not an integer")

c = int(input("What is the cost of your dream home? \n > "))
except ValueError:
    print(c, " is not an integer")

d = int(input(("What is your semi annual raise? \n "))
except ValueError:
    print(d, " is not an integer")


"""------------------------------------------------------"""

print("What is your annual salary?")
a = input(prompt)
annual_salary = int(a)

print("What percent of your salary \
would you like to put away into savings?")
b = input(prompt)
portion_saved = float(b)

print("What is the cost of your dream home?")
c = input(prompt)
total_cost = int(c)

print("What is your semi anual raise?")
d = input(prompt)
semi_annual_raise = float(d)

#^^^This section takes input from the user to:
# 1. input his salary
# 2. % of salary put into his savings
# 3. The total cost of their dream home
# 4. % of their salary raised

portion_of_downpayment = .25 * total_cost
current_savings = 0
r = .04
months = 0


#Instantiated variables for use in the while loop


while current_savings < portion_of_downpayment:
    if months %6==0 and months !=0:
            annual_salary = annual_salary * semi_annual_raise + annual_salary
    current_savings += annual_salary * portion_saved/12 + current_savings*r/12

    months +=1

print(f"It will take {months} months or {months // 12} \
years and {months%12} months to afford your down payment \
on your house ".format(months))
