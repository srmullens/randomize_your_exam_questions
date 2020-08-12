# randomize_your_exam_questions
Takes True/False and Multiple Choice questions and randomizes the question wording and order while keeping the correct answer. The primary functions are in *exam_functions.py*, and the questions (and any special code for the questions) are to be put in *new_exam.py*.

## True or False Questions
In this section of *new_exam.py*, you will find code that looks like:

```python
true_false_questions = [
        {'question':"",
            'options':[''],
            'answers':[]},
        ]
```

true_false_questions is a Python list, which should contain each question and all the details pertaining to it. Each question consists of a Python dictionary with three entries.
* **'question'** is where you write your question. The quotations are a reminder that this should be a string. This uses " so an apostrophe can be inserted without any issues.
* **'options'** contains a list of ways you want your question to vary. Inside the [ ] to indicate a list are ' symbols showing this should be a list of strings. Similar to above, if an apostrophe is needed the " symbol can be used around the string instead.
* **'answers'** contains a list of what the answer should be, based on what option is chosen for your question. Because these are true or false questions, the answer must just be the word True or the word False. These are not to be entered as strings, and should not use quotations.

### Example 1
A simple question without any options will look like this. With no options in the question, the 'options' entry contains an empty list. Do this instead of removing the 'options' entry altogether, as this may cause an error. With only one option, only one answer is given.

```python
true_false_questions = [
        {'question':"True or False: Albany is the capital of the state of New York.",
            'options':[],
            'answers':[True]}
        ]
```

### Example 2
A question with two options for how it might be worded can be given. To do this, put the all-capitalized word "OPTION" where the words should be inserted into the sentence. Then, the list of strings for what can go in that location is given in the list of options. The correct answer associated with each option is then provided in the list of answers.

```python
true_false_questions = [
        {'question':"True or False: OPTION is the capital of the state of New York.",
            'options':['Albany','New York City'],
            'answers':[True,False]}
        ]
```


## Multiple Choice Questions
In this section of *new_exam.py*, you will find code that looks like:

```python
multiple_choice_questions = [
    # 0
    {'question':"",
            'options':[],
            'choices':[''],
            'answer':['']},
    ]
```

multiple_choice_questions is also a Python list, which should contain each question and all the details pertaining to it. Each question consists of a Python dictionary with four entries. The commented zero just indicates what index the question is in the list, which can be helpful when many questions are entered.
* **'question'** is where you write your question. The quotations are a reminder that this should be a string. This uses " so an apostrophe can be inserted without any issues.
* **'options'** contains a list of ways you want your question to vary. Inside the [ ] to indicate a list are ' symbols showing this should be a list of strings. Similar to above, if an apostrophe is needed the " symbol can be used around the string instead.
* **'choices'** contains a list of potential answers. You can have any number of choices here; two, four, ten, whatever.
* **'answers'** contains a list of a single item, which should be the exact string as one of the choices. Because these are strings, the answer must use quotations, which was not true of the true/false section.

### Example 1
A simple question without any options will look like this. With no options in the question, the 'options' entry contains an empty list. Do this instead of removing the 'options' entry altogether, as this may cause an error.

```python
multiple_choice_questions = [
    # 0
    {'question':"What is the capital of Illinois?",
            'options':[],
            'choices':['Chicago','St. Louis','Springfield','Rockport'],
            'answer':['Springfield']},
    ]
```

### Example 2
A question with two options for how it might be worded can be given. To do this, put the all-capitalized word "OPTION" where the words should be inserted into the sentence. Then, the list of strings for what can go in that location is given in the list of options. The correct answer associated with each option is then provided in the list of answers.

```python
multiple_choice_questions = [
    # 0
    {'question':"What is the OPTION Illinois?",
            'options':['capital of','most populous city in'],
            'choices':['Chicago','St. Louis','Springfield','Rockport'],
            'answer':['Springfield','Chicago']},
    ]
```

### Example 3
Unfortunately, more complex changes are difficult to do. In the below example, the state is what changes instead of some trivia about Illinois. This might prompt a change in what choices you want displayed. But to do that, you're going to need some special code. And that's what the `# Special changes to the Multiple Choice section.` items are for. It's where you can replicate what the normal functions do, but do it in a specialized way for this particular question prior to running the code for all questions. You could do it for every question, but...(ugh)...why?

```python
multiple_choice_questions = [
    # 0
    {'question':"What is the capital of OPTION?",
            'options':['Illinois','Missouri'],
            'choices':['Chicago','St. Louis','Springfield','Rockport'],
            'answer':['Springfield','Jefferson City']},
    ]

#
# Special changes to the Multiple Choice section.
#

## Index 0: What is the capital of OPTION?
options = multiple_choice_questions[0]['options']
choices = multiple_choice_questions[0]['choices']
## Select a question option.
option = random_choice(options)
## Based on the chosen question wording, get the correct answer.
answer = multiple_choice_questions[0]['answer'][options.index(option)]
## Based on the chosen question wording, change the choices.
if option == 'Missouri': 
    choices[0] = 'Kansas City'
    choices[2] = 'Jefferson City'
    choices[3] = 'Columbia'
## Put items back in the list.
multiple_choice_questions[0]['options'] = [option]
multiple_choice_questions[0]['choices'] = [choices]
multiple_choice_questions[0]['answer'] = [answer]
```

Following these special changes, the question choices will have already been made.
If Illinois was chosen, the result should be:
```python
    {'question':"What is the capital of OPTION?",
            'options':['Illinois'],
            'choices':['Chicago','St. Louis','Springfield','Rockport'],
            'answer':['Springfield']},
```
If Missouri was chosen, the result should be:
```python
    {'question':"What is the capital of OPTION?",
            'options':['Missouri'],
            'choices':['Kansas City','St Louis','Jefferson City','Columbia'],
            'answer':['Jefferson City']},
```
