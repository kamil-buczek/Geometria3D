from sympy.interactive.printing import init_printing
import sympy
import numpy as np
import glm
init_printing()



print('policzmy w OpenGL-u -biblioteka GLM')
n=0.01 #początek bryły
f=100; #koniec bryły

FOV=90
FOVrad=FOV*np.pi/180

F=glm.perspective(FOVrad,1.0,1,10)
print(F)



