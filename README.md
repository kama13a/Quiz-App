# 🧠 Quizzler

A desktop True/False trivia quiz built with Python and Tkinter. Fetches live
questions from the Open Trivia Database API, tracks your score, and gives
instant green/red feedback for correct/incorrect answers.

---

## 🎯 Project Overview

This project is a desktop quiz app that pulls True/False questions from the
Open Trivia Database (OpenTDB) API and presents them one at a time in a
Tkinter GUI. The user answers with ✅ or ❌ buttons; the canvas flashes green
for correct and red for wrong, the score updates live, and the quiz ends
when all questions are answered.

It's a project from **100 Days of Code: The Complete Python Pro Bootcamp**,
built to practice **OOP, type hints, API calls, and Tkinter**.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| Live Questions | Fetches True/False trivia from the OpenTDB API |
| Tkinter GUI | Score label, question canvas, image buttons |
| Instant Feedback | Canvas turns green (correct) or red (wrong) |
| Live Scoring | Score updates after every answer |
| End Screen | Disables buttons and shows a message when the quiz ends |
| OOP Structure | Clean separation between UI and quiz logic |

---

## 📁 Project Structure
Quiz-App/

├── .venv/ # Virtual environment (not committed)

├── images/

│ ├── true.png # ✅ Correct button image

│ └── false.png # ❌ False button image

├── data.py # Loads question data from the API

├── question_model.py # Question class

├── quiz_brain.py # Quiz logic (score, next question, check answer)

├── ui.py # Tkinter UI (QuizInterface)

├── main.py # Entry point — wires everything together

└── README.md # Documentation

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Tkinter** — GUI library (built-in)
- **requests** — HTTP calls to the OpenTDB API
- **OpenTDB API** — `https://opentdb.com/api.php`

---

## 🧠 Concepts Practiced

- **Object-Oriented Programming** — `Question`, `QuizBrain`, `QuizInterface`
- **Type hints** — `quiz_brain: QuizBrain`, `-> bool`, `-> str`, `list[dict]`
- **API consumption** — `requests.get`, `params`, `response.json()`, `raise_for_status()`
- **Tkinter GUI** — `Canvas`, `Label`, `Button`, `PhotoImage`, `grid`
- **Event-driven programming** — `command=`, `window.after()`
- **Separation of concerns** — UI (`ui.py`) vs logic (`quiz_brain.py`)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone git@github.com:kama13a/Quiz-App.git
git checkout develop
cd Quiz-App

