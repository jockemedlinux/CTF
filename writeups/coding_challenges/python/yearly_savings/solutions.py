def yearly_savings(name, income):
    print(f"Wow! ${income} is a nice daily income")
    calculate = income * 365
    print("That means you can earn $" + str(calculate) + " every year! Amazing")
    print(f'You can probably save around 10% of that')
    savings = calculate * 0.1
    print("That roughly equals $" + str(savings))
    print("Good job bro!")

name = input("Hello sir, what is your name?: ")
print("Hello "+ name + ". Happy to meet you!")
income = int(input("How much do you make in a day?: "))

yearly_savings(name, income)
