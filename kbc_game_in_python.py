# kbc game in python
questions=[
{
    "question":"who is the first president of india ?",
    "options":["A) DR rajendra prasad","B)jawaharlal nehru",
    "c) mahatama gandhi","d)sardar patel"],
    "answer":"A"
    },
    { "question":"which planet is known as the red planet ?",
    "options":["A) earth","B)mars ",
    "c) jupiter","d) venus"],
    "answer":"B"
    },
    { "question":"what is capital of france ?",
    "options":["A) delhi","B)france ",
    "c) tokyo","d) london"],
    "answer":"B"
    },
    { "question":"which is the largest ocean in the world ?",
    "options":["A) atlantic ocean","B)indian  ocean",
    "c) arctic ocean","d) pacific ocean"],
    "answer":"D"
    },]
def run_quiz():
    score=0
    for idx,question_data in enumerate(questions):
        print(f"questions {idx+1}:{question_data['question']}")
        for option in question_data['options']:
            print(option)

        answer=input("your answer (A/B/C/D):").upper()
        if answer ==question_data["answer"]:
            print("correct!\n")
            score=score+1
    print("your score is",score ,"out of", len(questions))                        
run_quiz()