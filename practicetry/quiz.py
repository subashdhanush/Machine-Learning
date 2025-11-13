# quiz_app.py

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    }
]

score = 0

print("🧠 Welcome to the Python Quiz!\n")

for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

print(f"🎯 Quiz Over! You scored {score} out of {len(questions)}.")
