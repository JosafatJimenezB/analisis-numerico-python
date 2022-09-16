import numpy as np
import sympy as sp

x = sp.Symbol('x')
y = x**4-16
y = input('Ingrese al polinomio a resolver: ')
y = sp.sympify(y)
s = 0
while (s == 0):
    x0 = float(input('proporcione un valor inicial: '))
    x1 = float(input('Proporcione un valor final: '))
    if y.subs(x,x0)*y.subs(x,x1) < 0:
        s = 1
    else:
        print('Los valores proporcionados son incorrectos\n')

xr = 0
er = 1
i = 0

while(er > 1e-15):
    xr = float(x1-y.subs(x,x1)*(x1-x0)/(y.subs(x,x1)-y.subs(x,x0)))
    if y.subs(x,x1)*y.subs(x,xr) < 0:
        xr0=x0
        x0=xr
    else:
        xr0=x1
        x1=xr
    if y.subs(x,xr) == 0:
        er = 0
    else:
        er = float(abs((y.subs(x,xr)-y.subs(x,xr0))/y.subs(x,xr)))
    i+=1

print('La raiz del polinomio ',y, 'es',xr,'  ',i)