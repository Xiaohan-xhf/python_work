from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # question_bank.append(Question(i["text"], i["answer"]))

    # question_text = question["text"]
    # question_answer = question["answer"]
    # question_bank += [question_text, question_answer]

    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# 所以我原来是对的，但是老师命名了变量让代码可读性更强

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz! ")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")