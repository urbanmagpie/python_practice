import random

questions = [
    {
        "question": "What does len('hello') return?",
        "options": ["4", "5", "6", "Error"],
        "answer": "5"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "What does the 'in' operator check for?",
        "options": ["Equality", "Membership", "Identity", "None of the above"],
        "answer": "Membership"
    },
    {
        "question": "What is the correct way to write a for loop over a list named 'items'?",
        "options": [
            "for item in items:",
            "for item on items:",
            "foreach item in items:",
            "loop item in items:"
        ],
        "answer": "for item in items:"
    },
    {
        "question": "What data type is returned by the input() function?",
        "options": ["int", "str", "bool", "list"],
        "answer": "str"
    },
    {
        "question": "How do you write a comment in Python?",
        "options": ["// Comment", "# Comment", "<!-- Comment -->", "/* Comment */"],
        "answer": "# Comment"
    },
    {
        "question": "Which symbol is used for floor division in Python?",
        "options": ["/", "//", "%", "**"],
        "answer": "//"
    },
    {
        "question": "What will be the output of print('Python'[::-1])?",
        "options": ["nohtyP", "Python", "Error", "None"],
        "answer": "nohtyP"
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": ["2variable", "variable_2", "variable-2", "variable 2"],
        "answer": "variable_2"
    }
]

correct_answers = 0
questions_asked = 0

while questions:
    current_q = random.choice(questions)
    options = current_q["options"].copy()
    random.shuffle(options)

    print("\n" + current_q["question"])
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        user_input = input("Pick 1, 2, 3, 4 (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("\nYou chose to quit the quiz.")
            print(f"You answered {correct_answers} questions correctly out of {questions_asked} asked.")
            print("Thanks for playing.")
            exit()

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 4:
                break
        print("Invalid input, please enter 1, 2, 3, 4 or 'q' to quit.")

    selected_option = options[choice - 1]
    questions_asked += 1

    if selected_option == current_q["answer"]:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is: {current_q['answer']}")

    questions.remove(current_q)

print("\nQuiz complete.")
print(f"You answered {correct_answers} out of {questions_asked} questions correctly.")

if correct_answers == questions_asked:
    print("Awesome! Perfect score!")
elif correct_answers >= questions_asked / 2:
    print("Good job! Keep practicing to improve even more.")
else:
    print("Don't worry, keep practicing and you'll get there!")

