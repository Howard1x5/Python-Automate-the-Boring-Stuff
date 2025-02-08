# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. 
# Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the 
# second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what 
# percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 
# 0 value 50% of the time and a 1 value the other 50% of the time.

# You can start with the following template:

# import random
# numberOfStreaks = 0
# for experimentNumber in range(10000):
#     # Code that creates a list of 100 'heads' or 'tails' values.

#     # Code that checks if there is a streak of 6 heads or tails in a row.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# PseudoCode
#     Outer loop (10,000 times) → Runs the experiment multiple times.
#     Inner loop (100 times) → Generates one sequence of coin flips.

#  Use append() to avoid overwriting values.
# Sytax of append Method - testList.append(random.randint(0, 1))

## First Iteration
# import random

# numberOfStreaks = 0

# for experimentNumber in range(10000):  # Outer loop → Run experiment 10,000 times
#     testList = []  # Create a new empty list for each experiment
    
#     for listCreate in range(100):  # Inner loop → Generate 100 random coin flips
#         testList.append(random.randint(0, 1))  # Append 0 (Tails) or 1 (Heads)
    
#     # Check for Streak Code

# print("Test run complete!")  # Just to verify it ran

### Streak Code
# Plan:

#  Loop through the list of 100 flips.
#  Check if the current value matches the next five values.
#  If we find a streak of six 0s or six 1s, increase numberOfStreaks.



    # Check for streaks
#     streakCount = 1  # Start at 1 because we compare with the previous flip
    
#     for i in range(1, len(testList)):  # Start loop at index 1 (compare with previous)
#         if testList[i] == testList[i - 1]:  # If the current flip matches the last one
#             streakCount += 1  # Increase streak count
#         else:
#             streakCount = 1  # Reset streak if sequence is broken

#         if streakCount == 6:  # If a streak of 6 is found
#             numberOfStreaks += 1
#             break  # Stop checking further in this experiment

# # Calculate the probability
# print(f'Chance of streak: {numberOfStreaks / 10000 * 100:.2f}%')


# Full Program

import random

numberOfStreaks = 0  # Track total streaks

for experimentNumber in range(10000):  # Run 10,000 experiments
    testList = []  # Generate a new list for each experiment

    for i in range(100):  # Generate 100 coin flips
        testList.append(random.randint(0, 1))  

    # Check for streaks
    streakCount = 1  # Start at 1 because we compare with the previous flip
    
    for i in range(1, len(testList)):  # Start loop at index 1 (compare with previous)
        if testList[i] == testList[i - 1]:  # If the current flip matches the last one
            streakCount += 1  # Increase streak count
        else:
            streakCount = 1  # Reset streak if sequence is broken

        if streakCount == 6:  # If a streak of 6 is found
            numberOfStreaks += 1
            break  # Stop checking further in this experiment

# Calculate the probability
print(f'Chance of streak: {numberOfStreaks / 10000 * 100:.2f}%')
