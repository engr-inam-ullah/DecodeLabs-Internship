print("Welcome to the General Knowledge Quiz!")
print("=============================================")

score = 0

# Question 1
answer = input("1. What is the national animal of pakistan ? ")

if answer.lower().strip() == "markhor":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is markhor.")

# Question 2
answer = input("2. How many muslim countries are there in the world? ")

if answer.strip() == "57":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is 57.")

# Question 3
answer = input("3. Which global city is known as the city of light ? ")

if answer.lower().strip() == "paris":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is Paris.")

# Final score
print("=============================================")
print("Your final score is:", score, "/ 3")