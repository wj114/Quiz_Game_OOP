from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank, import from data
question_bank = []

for i in question_data:
    question = i["text"]
    ans = i["answer"]
    new_question = Question(question,ans)
    question_bank.append(new_question)

quiz =QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

