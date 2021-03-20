print("India Covid-19 Cases")
covid19_india={
    "confimed":11385395,
     "Active":216349,
     "recovered":11050628,
    "Deceased":158764
}
print(covid19_india)

name_of_state={
    "Maharashtra": 2314413,
    "kerala":1091271,
}
print()

cart = []

choice = "yes"
"""state1 = input("enter the state1:")
cart.append(name_of_state[state1])

state2 = input("enter the state2:")
cart.append(name_of_state[state2])

print("the above states have Covid-19 cases")
print(cart)"""


while choice == "yes":
    item = input("enter the state:")
    cart.append(name_of_state[item])

    choice = input(" ADD the Covid-19 states(yes/no)")

print("Covid-19 cases[{}]:".format(len(cart)))
print(cart)

total_cases = sum(cart)
print("total", total_cases)

vaccine_code = input("you any enter vaccine code if you have")
if vaccine_code == "MODI":
    print("VACCINE CODE APPLIED")
    total_cases = total_cases - (0.20 * total_cases)

    print("Amount After Promo Code",total_cases)

    total_cases = total_cases+(0.18 * total_cases)
    print("final vaccine dose",total_cases)

"""Maharashtra={
    "name":"maharashta",
     "confimed":2314413,
     "Active":126231,
     "recovered":2134072,
     "Deceased":52861,
    "tested":"1.8cr"
}


name_of_state = name_of_state, "kerala"
print( input ("enter the state:", name_of_state))"""

