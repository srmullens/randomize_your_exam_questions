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

### Index 5: "T/F? The atmosphere is layered in this order: ... ?"
order = true_false_questions[5]['options']
random = random_sequence(order)
    # Put the randomized order in a sentence.
sentence = random[0] + ", " + random[1] + ", " + random[2] + ", and " + random[3]
    # Put the sentence as the option.
true_false_questions[5]['options'] = [sentence]
    # Adjust whether the answer is correct or not.
for i,item in enumerate(order):
    if random[i] != order[i]: true_false_questions[5]['answers'] = [False]





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

### Index 12: An air parcel moves up to OPTION. What temperature will it have?
    # Get the options for question wording and list of answer choices.
options = multiple_choice_questions[12]['options']
choices = multiple_choice_questions[12]['choices']
    # Select what the question will say.
option = random_choice(options)
    # Based on the chosen question wording, get the correct answer.
answer = multiple_choice_questions[12]['answer'][options.index(option)]
print(answer)
    # Based on the chosen question wording, change the last two answer choices.
choices[3] = answer
if options.index(option)==0:
    choices[2] = '8C'
else:
    index_two = str(30-(10*(options.index(option)+1)))+'C'
    choices[2] = index_two

    # Put items back in the list.
multiple_choice_questions[12]['options'] = [option]
multiple_choice_questions[12]['choices'] = choices
multiple_choice_questions[12]['answer'] = [answer]





# Create the exam
create_the_exam(true_false_questions,multiple_choice_questions)

