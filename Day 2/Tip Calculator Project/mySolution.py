print("Welcome to the tip calculator!")
total = input("What was the total bill? : ")
tip = input("How much tip would you like to give? : ")
people = input("How many people to split the bill? : ")

print(f"Each person should pay: ${round((float(total)/int(people)) * (1 + int(tip)/100), 2)}")
