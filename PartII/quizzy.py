# -*- coding: UTF-8 -*-
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico':
                'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
    quizfile= open('capitalsquiz%s.txt' % (quiznum + 1), 'w')
    answerfile = open('answer%s.txt' % (quiznum + 1), 'w')

    quizfile.write('Name:\n date:\n Period\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiznum + 1))
    quizfile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)

    for i in range(50):
        correctAnswer = capitals[states[i]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctAnswer)]
        wronganswer= random.sample(wronganswer,3)
        answers= wronganswer+ [correctAnswer]
        random.shuffle(answers)
        quizfile.write('%s. What is the capital of %s?\n' % (i + 1,
            states[i]))
        for j in range(4):
            quizfile.write('%s. %s\n'% ('abcd'[j],answers[j]))
        quizfile.write("\n")
        answerfile.write('%s. %s\n' % (i + 1, 'abcd'[
            answers.index(correctAnswer)]))
    quizfile.close()
    answerfile.close()
