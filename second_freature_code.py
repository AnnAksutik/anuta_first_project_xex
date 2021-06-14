# defining new function 
def equation_roots(a, b, c):
    import math
    if b**2-4*a*c==0:
        x1,x2=-b/(2*a),-b/(2*a)
    elif b**2-4*a*c>0:
        x1=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x1,x2=min(x1,x2),max(x1,x2)
    return x1,x2
# reading inputs
a, b, c = int(input()), int(input()), int(input())

# calling the function
x1, x2 = equation_roots(a, b, c)
print(x1, x2)

