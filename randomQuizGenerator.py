import random

# 8 states and capitals

capitals = {
    'Delhi': 'New Delhi',
    'Karnataka': 'Bengaluru',
    'Telangana': 'Hyderabad',
    'Andhra Pradesh': 'Amaravathi',
    'Tamil Nadu': 'Chennai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna',
    'Delaware': 'Dover',
}

# generating 2 quiz files.

for quizNum in range(2):
    # creating the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers % s.txt' % (quizNum+1), 'w')

    # write out the header for the quiz.
    quizFile.write('Name : \n\nDate:\n\nSection:\n\n')
    quizFile.write(' '*20 + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 8 states, making a question for each.
    for questionNum in range(5):

        # Get right and Wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())

        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        wrongAnswers = random.sample(wrongAnswers, 3)

        answerOptions = wrongAnswers + [correctAnswer]

        random.shuffle(answerOptions)

        # write the question and answer options t quiz file.

        quizFile.write('%s. What is the capital of %s?\n' %
                       (questionNum+1, states[questionNum]))

        for i in range(4):
            quizFile.write('   %s.%s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer key to a file.
        answerKeyFile.write('%s.%s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)
        ]))

    quizFile.close()
    answerKeyFile.close()
