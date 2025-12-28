def probFinder(problemFinder):

    match problemFinder:
        case 'A':
            return derivative()  #add the logic for the derivatives
        case 'B':
            return integral() #add the logic for integrals
        case _:
            return print("Invalid input, please choose A or B")