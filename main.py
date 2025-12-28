import sympy as sym
from probFinder import probFinder

problem_choice = input("What type of problem do you have today: \n"  # Logic for asking user to choose between inputs
                       "A: Finding a derivative:\n"
                       "B: Finding an integral:\n"
                       "C: Finding a limit:\n"
                       "D: Computing the Series Expansion:\n").strip().upper()

probFinder(problem_choice)
