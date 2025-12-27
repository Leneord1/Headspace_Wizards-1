import sympy as sym

problemFinder = input("What type of problem do you have today: \n"
                      "A: Finding a derivative\n"
                      "B: Finding an integral\n")

def probFinder(status):
    match status:
        case 'A':
            return "Finding a derivative" #add the logic for the derivatives
        case 'B':
            return "Finding an integral" #add the logic for integrals

print(probFinder('A'))
print(probFinder('B'))