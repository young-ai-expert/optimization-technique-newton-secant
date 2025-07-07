from sympy import symbols, sympify

x = symbols('x')
function = input("Enter a function in terms of x: ")
epsilon = float(input("Enter epsilon value: "))
x0 = float(input("Enter 'a' value: "))
x1 = float(input("Enter 'b' value: "))

try:
    f = sympify(function)
    first_derivative = f.diff(x)
    print("f'(x) =", first_derivative)
    print()
except Exception as e:
    print("Invalid input. Please enter a valid expression. Error:", e)

val_first_derivative_1 = first_derivative.subs(x, x0)
val_first_derivative_2 = first_derivative.subs(x, x1)

z = x1 - ((val_first_derivative_2)*(x1-x0)/(val_first_derivative_2-val_first_derivative_1))
f_val = first_derivative.subs(x, z).evalf()
if (val_first_derivative_1 > 0 and f_val >0) or (val_first_derivative_1 < 0 and f_val <0):
    x0 = z
else:
    x1=z

print("x1                        x2                f'(x1)                           f'(x2)                          z                   New region")
print(x0,"          ",x1,"         ",val_first_derivative_1,"        ",val_first_derivative_2,"       ",z,"         ",f"({x0},{x1})")

while abs(f_val) > epsilon:

    if (val_first_derivative_1 > 0 and f_val >0) or (val_first_derivative_1 < 0 and f_val <0):
        x0 = z
    else:
        x1=z

    val_first_derivative_1 = first_derivative.subs(x, x0)
    val_first_derivative_2 = first_derivative.subs(x, x1)

    z = x1 - ((val_first_derivative_2)*(x1-x0)/(val_first_derivative_2-val_first_derivative_1))
    f_val = first_derivative.subs(x, z).evalf()

    print(x0,"          ",x1,"         ",val_first_derivative_1,"        ",val_first_derivative_2,"       ",z,"         ",f"({x0},{x1})")




print()
print("The minimizer is ",z)




