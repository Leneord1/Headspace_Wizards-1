from derivative import derivative
from integral import integral
from limits import limits
from seriesExpansion import seriesExpansion

def probFinder(problemFinder):

    match problemFinder:
        case 'A':
            return derivative()  #add the logic for the derivatives
        case 'B':
            return integral() #add the logic for integrals
        case 'C':
            return limits() #add the logic for limits
        case 'D':
            return seriesExpansion() #add the logic for series expansion
        case _:
            return print("Invalid input, please choose A or B")