from sympy import symbols, sympify

x = symbols('x')
function = input("Enter a function in terms of x: ")
epsilon = float(input("Enter epsilon value: "))
x0 = float(input("Enter initial value: "))

try:
    f = sympify(function)
    first_derivative = f.diff(x)
    second_derivative = f.diff(x, 2)
    print("f'(x) =", first_derivative)
    print("f''(x) =", second_derivative)
    print()
except Exception as e:
    print("Invalid input. Please enter a valid expression. Error:", e)

val_first_derivative = first_derivative.subs(x, x0)
val_second_derivative = second_derivative.subs(x, x0)

x1 = x0 - (val_first_derivative/val_second_derivative)
f_val = first_derivative.subs(x, x1).evalf()

print("x0               f'(x0)              f''(x0)             x1")
print(round(x0, 14),"      ",round(val_first_derivative,14),"        ",round(val_second_derivative,14),"       ",round(x1,14))

while abs(f_val) > epsilon:

    x0 = x1
    val_first_derivative = first_derivative.subs(x, x0)
    val_second_derivative = second_derivative.subs(x, x0)
    x1 = x0 - (val_first_derivative/val_second_derivative)
    f_val = first_derivative.subs(x, x1).evalf()

    print(x0,"      ",val_first_derivative,"        ",val_second_derivative,"       ",x1)

print()
print("The minimizer is ",x1)




