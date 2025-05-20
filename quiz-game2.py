
print("Hello, welocome to the quiz game ")

taking = input("Do you like to take the quiz?(yes/no) ").lower()
print(taking)

if taking != 'yes':
    print("ok maybe next time :) ")
    quit()

print("\n lets begin the quiz :) \n ")

questions = [
    ("RCB stands for?", "royal challengers bangalore"),
    ("What is the capital city of France?", "paris"),
    ("Who wrote the play Romeo and Juliet?", "william shakespeare"),
    ("What is the chemical symbol for water?", "h2o"),
    ("How many continents are there on Earth?", "7"),
    ("Which planet is known as the Red Planet?", "mars")
]

total_points = 0
life = 3

for i,(question, correct_answer) in enumerate(questions, start=1):
    print(f"Question {i}:")
    answer = input(question + " ").lower().strip()
    
    if answer == correct_answer:
        print("That's correct!\n")
        total_points += 1
    else:
        print("Incorrect.\n")
        life -= 1

    print(f"Total Score: {total_points}")
    print(f"Chances left: {life}\n")

    if life == 0:
        print("You've run out of lives. Game over!")
        break

print(f"Your final score is {total_points} out of {len(questions)}")
percentage = (total_points / len(questions)) * 100
print(f"You got {percentage:.2f}%")

if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 50:
    print("Good job! You can improve more.")
else:
    print("Keep practicing! You'll get better.")


