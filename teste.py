import sympy as sym
import matplotlib 
 
#Derivatives of multivariable function
 
x , y = sym.symbols('x y')
f = x**4+x*y**4
 
#Differentiating partially w.r.t x
derivative_f = f.diff(x)
print(derivative_f)