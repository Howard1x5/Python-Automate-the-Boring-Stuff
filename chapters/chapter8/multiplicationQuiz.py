import pyinputplus as pyip
import random
import time

# Total number of questions in the quiz
numberOfQuestions = 10
correctAnswers = 0  # Track correct answers

# Loop through 10 questions
for questionNumber in range(1, numberOfQuestions + 1):
    # Pick two random numbers for multiplication
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    # Create a formatted prompt for the user
    prompt = f"#{questionNumber}: {num1} x {num2} = "

    try:
        # Prompt user for input with strict validation
        # allowRegexes → Accepts only the correct answer
        # blockRegexes → Blocks all other inputs with "Incorrect!" message
        # timeout → 8 seconds per question
        # limit → Maximum 3 attempts before moving to the next question
        pyip.inputStr(
            prompt,
            allowRegexes=[f"^{num1 * num2}$"],  
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3
        )

    except pyip.TimeoutException:
        print("Out of time!")  # User failed to answer in time
    except pyip.RetryLimitException:
        print("Out of tries!")  # User failed after 3 attempts

    else:
        # If no exception was raised, user answered correctly
        print(" Correct!")
        correctAnswers += 1  # Increase score

    # Small delay to let user see the result before next question
    time.sleep(1)

# Final score display
print(f"\n Score: {correctAnswers} / {numberOfQuestions}")
