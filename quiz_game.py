# quiz game
# entry to quiz game
print("Welcome to the Quiz Game!")
playing = input("Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    print("Maybe next time!")
    quit()
print("Great! Let's start the quiz :)")
# questions and answers 
#1
score = 0
answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")
#2
answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Jupiter.")
#3
answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is H2O.")
#4
answer = input("What is the fastest land animal? ")
if answer.lower() == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Cheetah.")
#5
answer = input("What is the world's largest ocean? ")
if answer.lower() == "pacific":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Pacific.")

print("The Quiz is now over!")
print("Your final score is: " + str(score) + " out of 5")
print("Thank you for playing the Quiz Game!")

print("Press any key to exit...")
input()
