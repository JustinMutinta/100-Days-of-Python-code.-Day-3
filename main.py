"""
The Love Calculator will calculate the probability of love between you and another person.
You will enter your name and their name.
After adding the number of times the letters in 'true love' show up will decide how compatible you are.
"""

print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#.lower()
#.count("a")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

score = str(t + r + u + e) + str(l + o + v + e)
int_score = int(score)

#print(score)

if (int_score < 10) or (int_score > 90):
    print(f"Your score is {int_score}, you go together like coke and mentos")
elif (int_score >= 40) or (int_score <= 50):
    print(f"Your score is {int_score}, you are alright together")
else:
    print(f"Your score is {int_score}")
