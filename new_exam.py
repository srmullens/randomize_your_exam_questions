#
# METXXXX Exam X
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
        {'question':"",
            'options':[''],
            'answers':[]},

        {'question':"",
            'options':[''],
            'answers':[]}

        ]

#
# Special changes to the True/False section.
#

### Write some python 3 code to make special adjustments to one of the 
### questions, options, answers. This is useful when the typical randomization
### options provided in exam_functions.py aren't what you want for a specific
### question.





#
# Multiple Choice Question Wording
#
# Give the questions, options for question wording, and multiple choice options, and answer.

multiple_choice_questions = [
    # 0
    {'question':"",
            'options':[],
            'choices':[''],
            'answer':['']},

    # 1
    {'question':"",
            'options':[],
            'choices':[''],
            'answer':['']}

    ]



#
# Special changes to the Multiple Choice section.
#

### Write some python 3 code to make special adjustments to one of the 
### questions, options, choices, answers. This is useful when the typical randomization
### options provided in exam_functions.py aren't what you want for a specific
### question.





# Create the exam
create_the_exam(true_false_questions,multiple_choice_questions)
