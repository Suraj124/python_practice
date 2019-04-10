import numpy as np

arr=np.array([0,30,45,60,90])
print("Original array",arr)

# rad=arr*(np.pi/180)
# print(rad)
# print(np.sin(rad))
sin=np.sin(arr*np.pi/180)
cos=np.cos(arr*np.pi/180)
tan=np.tan(arr*np.pi/180)
print('Sin values',sin)
print('Cos values',cos)
print('Tan values',tan)

print("Sin inverse",np.degrees(np.arcsin(sin)))


