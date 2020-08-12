import random

# If I get REALLY ambitious, this could even create LATEX code 
# for the exam, which could easily be coverted to a PDF.

#
# Functions to create exams.
#

# These are the functions to be used to change the order of my options.

def random_option(array):
    random.seed()
    result = random.randint(1,len(array))
    return result

def random_sequence(array):
    random.seed()
    result = random.sample(array,k=len(array))
    return result

def random_choice(array):
    random.seed()
    result = random.choice(array)
    return result



################
# True / False #
################

# Randomize True False Question Wording
# Now lets randomize the key words that make particular questions true or false.

def true_false(true_false_questions):
    true_false_questions_answers = []

    # Go through each question 
    for i,question in enumerate(true_false_questions):

        # Choose an option and the answer associated with it.
        choice = random_choice(question['options'])
        answer = question['answers'][question['options'].index(choice)]

        # Insert the chosen option into the question.
        question['question'] = question['question'].replace("OPTION",choice)

        # Save the matched results.
        true_false_questions_answers.append([question['question'],answer])

    return true_false_questions_answers



###################
# Multiple Choice #
###################
# 1) Choose an option for the question. 
# 2) Put that option into the question. Use .replace()
# 3) Scramble the answer order.
# 4) Figure out which answer is correct.
# 5) Put it all together.

def multiple_choice(multiple_choice_questions):
    multiple_choice_questions_answers = []

    # Go through each question
    for i,question in enumerate(multiple_choice_questions):

        # Step 1 - Choose an option for the question.
        if len(question['options'])>1:
            choice = random_choice(question['options'])
            answer = question['answer'][question['options'].index(choice)]

        else:
            choice = False
            if len(question['answer'])==1:
                answer = question['answer'][0]
            else:
                raise UserWarning(f'Multiple Choice question {i}: No options, but multiple answers?')

        # Step 2 - Put that option into the question.
        if choice:
            question['question'] = question['question'].replace('OPTION',choice)

        # Step 3 - Scramble the answer order.
        question['choices'] = random_sequence(question['choices'])

        # Step 4 - Figure out which answer is correct.
        answer_letter = False
        try: index = question['choices'].index(answer)
        except: raise ValueError(f'Index {i}: {answer} not among options {question["options"]}')

        if index==0: answer_letter = 'A'
        elif index==1: answer_letter = 'B'
        elif index==2: answer_letter = 'C'
        elif index==3: answer_letter = 'D'

        # Step 5 - Put it all together.
        if answer_letter: multiple_choice_questions_answers.append([question['question'],question['choices'],answer_letter])
        else: raise UserWarning(f'Multiple Choice question {i}: answer not among the choices.')

    return multiple_choice_questions_answers



##########
# Output #
##########

# We have randomized all the questions and the multiple choice order.
# Now, lets randomize the order of the true/false questions and the
# multiple-choice questions. Output the True/False questions, the
# multiple choice questions and choices, and the answer key.

def output_quiz(true_false_questions_answers,multiple_choice_questions_answers):

    question_number = 1

    # True-False Questions
    true_false_questions_answers = random_sequence(true_false_questions_answers)

    true_count = 0; false_count = 0
    for question in true_false_questions_answers:   # [question,answer]
        # Print question
        print(f'{question_number}-{question[1]}\t\t{question[0]}\n')
        question_number += 1

        # Count true and false answers
        if question[1]==True: true_count+=1
        elif question[1]==False: false_count+=1

    print('\n')


    # Multiple Choice Questions
    multiple_choice_questions_answers = random_sequence(multiple_choice_questions_answers)

    #A_count = 0; B_count = 0; C_count = 0; D_count = 0
    letters_count = [0] * 26
    for question in multiple_choice_questions_answers:   # [question,options,answer]
        print(f'{question_number}\t{question[0]}\n')

        # Count letter answers and replace correct answer with *
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        letters = ['*' if question[2]==x else x for x in letters]
        letters_count = [x+1 if letters[i]=='*' else x for i,x in enumerate(letters_count)]

        # Print answers.
        for i,option in enumerate(question[1]):
            print(f'\t{letters[i]}\t{option}')

        print('\n')
        question_number += 1

    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    end_i = [i for i, e in enumerate(letters_count) if e != 0][-1]+1

    print("\nTrue/False: "+str(true_count),str(false_count))
    print(f"{', '.join(letters[:end_i])}: {', '.join(map(str,letters_count[:end_i]))}")
    print()



###################
# Create the exam #
###################
def create_the_exam(true_false_questions,multiple_choice_questions):
    # True / False
    true_false_questions_answers = true_false(true_false_questions)

    # Multiple Choice
    multiple_choice_questions_answers = multiple_choice(multiple_choice_questions)

    # Output
    output_quiz(true_false_questions_answers,multiple_choice_questions_answers)

