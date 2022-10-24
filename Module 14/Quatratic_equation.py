
def quadratic_solve(a, b, c):
    """ Solves a quadratic equation a*x**2 + b*x + c = 0. """
    D = b**2 - 4*a*c # Calculate discriminant
    if D < 0:
        return "The equation given has no real roots"
    elif D == 0:
        return -b/(2*a)
    else:
        return (-b + D**0.5) / (2*a), (-b - D**0.5) / (2*a)
      
M = {'a' : 1,
     'b' : 0,
     'c' : -1}

print(quadratic_solve(**M))
