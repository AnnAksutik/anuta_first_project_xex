# объявление функции
def solve(a, b, c):
    if b**2-4*a*c==0:
        x1,x2=-b/(2*a),-b/(2*a)
    elif b**2-4*a*c>0:
        x1=(-b-(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b+(b**2-4*a*c)**0.5)/(2*a)
        x1,x2=min(x1,x2),max(x1,x2)
    return x1,x2
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
