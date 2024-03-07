from data import question_data
from quiz_brain import QuizBrain
from question_modelQuiz import Question
from ui import QuizInterface

question_bank = []

for question in question_data:
    text = question["Question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)