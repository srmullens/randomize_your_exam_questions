#
# TEST Exam 0
#
# Identify the True/False Questions.
# Do any special adjustments to the True/False Questions.
#
# Identify the Multiple Choice Questions.
# Do any special adjustments to the Multiple Choice Questions.
#
# Create the exam.


# Creating the exam will randomize the question wording
# the order of questions, and the order of the multiple choice options.
# But the answers are still preserved and identfied when the exam is output.


from exam_functions import random_sequence,random_choice,create_the_exam





#
# True/False Question Options
#
# This is an array of options for each question in the true/false section of the test.

true_false_questions = [
        {'question':"True or False: Albany is the capital of the state of New York.",
            'options':[''],
            'answers':[True]},

        {'question':"True or False: OPTION is the capital of the state of New York.",
            'options':['Albany','New York City'],
            'answers':[True,False]}

        ]

#
# Special changes to the True/False section.
#






#
# Multiple Choice Question Wording
#
# Give the questions, options for question wording, and multiple choice options, and answer.

multiple_choice_questions = [
    # 0
    {'question':"What is the capital of Illinois?",
            'options':[],
            'choices':['Chicago','St. Louis','Springfield','Rockport'],
            'answer':['Springfield']},

    # 1
    {'question':"What is the OPTION Illinois?",
            'options':['capital of','most populous city in'],
            'choices':['Chicago','St. Louis','Springfield','Rockport'],
            'answer':['Springfield','Chicago']}

    ]



#
# Special changes to the Multiple Choice section.
#






# Create the exam
create_the_exam(true_false_questions,multiple_choice_questions)

