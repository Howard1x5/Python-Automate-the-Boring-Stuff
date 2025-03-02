import random
import time

# Number of questions in the quiz
number_of_questions = 10
correct_answers = 0  # Track correct responses

# Loop through 10 questions
for question_number in range(1, number_of_questions + 1):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    # Display the question
    print(f"\nQuestion {question_number}: {num1} x {num2} = ?")
    correct = False  # Track if the user gets the answer correct
    attempts = 0  # Track the number of attempts
    start_time = time.time()  # Start the timer

    # User has 3 attempts and 8 seconds to answer
    while attempts < 3:
        try:
            # Check if 8 seconds have passed
            if time.time() - start_time > 8:
                print("Out of time!")
                break  # Move to the next question

            # Get user input
            user_answer = input("Your answer: ")

            # Ensure input is numeric
            if not user_answer.isdigit():
                print("Invalid input. Please enter a number.")
                continue  # Ask again without using an attempt

            user_answer = int(user_answer)

            # Check answer correctness
            if user_answer == num1 * num2:
                print("Correct!")
                correct_answers += 1
                correct = True
                time.sleep(1)  # Pause to let user see the message
                break  # Move to next question
            else:
                print("Incorrect.")
                attempts += 1  # Increment attempts
        except Exception as e:
            print(f"Error: {e}")
            break

    # If user failed all attempts
    if not correct and attempts == 3:
        print("Out of tries!")

# Display final score
print(f"\nFinal Score: {correct_answers} / {number_of_questions}")
