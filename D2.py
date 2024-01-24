#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total = input("What was the total bill? $")
tip = input("What percentage tip you like to give? 10, 12, or 15? ")
num_ppl = input("How many people to split the bill? ")

final = float(total) * ((float(tip) + 100) / 100) / int(num_ppl)
final_rounding = round(final, 2)
print(f"Each person should pay: ${final_rounding}")
