#Universidad del Valle de Guatemala
#Análisis y diseño de algoritmos
#Jennifer Daniela Sandoval	18962
#Proyecto 1
#Este programa tiene como objetivo representar funciones de cálculo lambda por medio de funciones lambda de python
#Referencias: https://www.geeksforgeeks.org/nested-lambda-function-in-python/#:~:text=In%20Python%2C%20anonymous%20function%20means,is%20called%20Nested%20Lambda%20Function


x=2
y=3

#Funciones que seran aplicadas por medio del cálculo lambda
f= lambda x: x+1
print('-Función f:\n','Función aplicada: ','x+1', '\n x: ', x,'\n Resultado:', f(x))
g= lambda x: 2*x
print('-Función g:\n','Función aplicada: ','2*x', '\n x: ', x,'\n Resultado:', g(x))
h= lambda x,y: (x**2)+ (y**2)
print('-Función h:\n','Función aplicada: ','(x^2)+(y^2)', '\n x: ', x,'y: ', y ,'\n Resultado:', h(x,y))

#Numeros expresados con el cálculo lambda
cero= lambda f: lambda x: x
print('-Cero:\n','Función aplicada: ','x+1', '\n x: ', x,'\n Resultado:', cero(f)(x))
uno= lambda f: lambda x: f(x)
print('-Uno:\n','Función aplicada: ','x+1', '\n x: ', x,'\n Resultado:', uno(f)(x))
dos=  lambda f: lambda x: f(f(x))
print('-Dos:\n','Función aplicada: ','2*x', '\n x: ', x,'\n Resultado:', dos(g)(x))
tres= lambda f: lambda x: f(f(f(x))) 
print('-Tres:\n','Función aplicada: ','2*x', '\n x: ', x,'\n Resultado:', tres(g)(x))


#Funciones expresadas con el cálculo lambda
sucesor= lambda n: lambda f: lambda x: f(n(f)(x))
print('-Sucesor:\n','n: tres','\n x: ' ,x,'\n Función: ', '2*x','\n Resultado:', sucesor(tres)(g)(x))
suma= lambda a: lambda b: lambda f : lambda x: (a (f)(b (f)(x)))
print('-Suma:\n','a: uno \n b: dos','\n x: ',x,'\n Función: ', 'x+1','\n Resultado:', suma(uno)(dos)(g)(x))
multiplicacion= lambda a: lambda b: lambda f: lambda x: ((a) (b) (f))(x)
print('-Multiplicación:\n','a: uno \n b: dos','\n x: ',x,'\n Función: ', 'x+1','\n Resultado:', multiplicacion(uno)(dos)(f)(x))
