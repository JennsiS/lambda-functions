#Universidad del Valle de Guatemala
#Análisis y diseño de algoritmos
#Jennifer Daniela Sandoval

f= lambda x: x+1
g= lambda x: 2*x
h= lambda x,y: (x**2)+ (y**2)
cero= lambda f: lambda x: x
uno= lambda f: lambda x: f(x)
dos=  lambda f: lambda x: f(f(x))
tres= lambda f: lambda x: f(f(f(x)))
sucesor= lambda n: lambda f: lambda x: f(n*f(x))


print(f(2))
