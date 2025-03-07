import random

# Dictionary of US states and their capitals
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Number of quizzes to generate
num_quizzes = 35

# Loop through each quiz to generate
for quiz_num in range(1, num_quizzes + 1):
    # Open quiz file and answer key file
    quiz_filename = f'capitalsquiz{quiz_num}.txt'
    answer_key_filename = f'capitalsquiz_answers{quiz_num}.txt'

    quiz_file = open(quiz_filename, 'w')
    answer_key_file = open(answer_key_filename, 'w')

    # Write quiz header
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(f"{' ' * 20}State Capitals Quiz (Form {quiz_num})\n\n")

    # Shuffle the order of states to randomize questions
    states = list(capitals.keys())  # Get list of states
    random.shuffle(states)  # Randomize the order

    # Loop through each state to create questions
    for question_num in range(50):
        correct_answer = capitals[states[question_num]]  # Get correct capital
        wrong_answers = list(capitals.values())  # Get all possible wrong answers
        wrong_answers.remove(correct_answer)  # Remove correct answer from wrong options
        wrong_answers = random.sample(wrong_answers, 3)  # Pick 3 random wrong answers

        answer_options = wrong_answers + [correct_answer]  # Create multiple-choice options
        random.shuffle(answer_options)  # Shuffle answer order

        # Write question to quiz file
        quiz_file.write(f"{question_num + 1}. What is the capital of {states[question_num]}?\n")

        # Write answer options (A-D)
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")

        quiz_file.write('\n')  # Add space after question

        # Write correct answer to answer key file
        answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")

    # Close files after writing
    quiz_file.close()
    answer_key_file.close()

print(f"Successfully generated {num_quizzes} quiz files and answer keys.")
