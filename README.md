<h1 align="center">DecodeLabs Internship — Python Projects</h1>

<p align="center">
  A collection of command-line Python applications built during the<br>
  <b>DecodeLabs Industrial Training Kit — Batch 2026</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Projects-4-green" alt="Projects">
  <img src="https://img.shields.io/badge/Interface-CLI-lightgrey" alt="CLI">
  <img src="https://img.shields.io/badge/Internship-DecodeLabs%202026-orange" alt="DecodeLabs">
</p>

# Table of Contents
- [Overview](#overview)
- [Projects](#projects)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Sample Output](#sample-output)
- [Skills Demonstrated](#skills-demonstrated)
- [Author](#author)
- 
# Overview
This repository contains the projects I completed as part of my Python internship at **DecodeLabs**. Each project focuses on a fundamental programming concept, starting from variables and control flow and moving toward functions, loops, and data storage with JSON.

The goal of the internship was to build a strong foundation in Python by creating small but complete, working applications.

## Projects
| # | Project | File | Core Concepts |
|---|---------|------|---------------|
| 1 | To-Do List | `To_do_list.py` | Functions, loops, JSON storage |
| 2 | Random Number Generator | `Random_number_generater.py` | `random` module |
| 3 | Expense Tracker | `Expense_Tracker.py` | Variables, loops, calculations |
| 4 | General Knowledge Quiz | `General_Knowledge_Quiz.py` | If-Else logic, variables, score counter |

# 1. To-Do List
A command-line application for managing daily tasks. Tasks are saved in `tasks.json`, so the data is kept between sessions.
# 2. Random Number Generator
A simple program that uses Python's built-in `random` module to generate random numbers.
# 3. Expense Tracker
A command-line tool for recording expenses and keeping track of spending.
# 4. General Knowledge Quiz
An interactive quiz game that asks 3 questions and tracks the player's score.
- Awards **+1 point** for every correct answer
- Answers are **case-insensitive** and ignore extra spaces
- Displays the **final score** at the end
- **Key skill:** Control flow, directing the program based on user choices
- 
# Tech Stack
- **Language:** Python 3
- **Data Storage:** JSON
- **Interface:** Command Line (CLI)
- **Tools:** Git, GitHub, VS Code
- 
# Repository Structure
DecodeLabs-Internship/
│
├── To_do_list.py                 # Project 1: To-Do List application
├── tasks.json                    # Saved tasks for the To-Do List
├── Random_number_generater.py    # Project 2: Random number generator
├── Expense_Tracker.py            # Project 3: Expense tracker
├── General_Knowledge_Quiz.py     # Project 4: General knowledge quiz
└── README.md                     # Project documentation
```

## Getting Started
### Prerequisites
- Python 3.x installed on your system
Check your version:
```bash
python --version
```
# Installation
```bash
git clone https://github.com/engr-inam-ullah/DecodeLabs-Internship.git
cd DecodeLabs-Internship
```
# Running a Project
```bash
python To_do_list.py
python Random_number_generater.py
python Expense_Tracker.py
python General_Knowledge_Quiz.py
```
No external libraries are required. All projects use only Python's standard library.

# Sample Output

**General Knowledge Quiz**

```
Welcome to the General Knowledge Quiz!
-------------------------------------
1. What is the national animal of pakistan ? markhor
Correct!
2. How many muslim countries are there in the world? 57
Correct!
3. Which global city is known as the city of light ? paris
Correct!
-------------------------------------
Your final score is: 3 / 3
```
---
## Skills Demonstrated

- Writing clean, readable Python code
- Using variables and handling user input
- Controlling program flow with `if / else` statements
- Working with loops and functions
- Reading and writing data using JSON files
- Version control with Git and GitHub
- ---

## Author

**Inam Ullah**

- GitHub: [@engr-inam-ullah](https://github.com/engr-inam-ullah)

Built during the **DecodeLabs Internship — Batch 2026**.
