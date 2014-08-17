#Alguns modos de se inverter os elementos de uma lista

#1º
Lista_normal=[1,2,3,4,5,6,7,8,9]
Lista_invertida=[ ]
for i in Lista_normal[::-1]:
  Lista_invertida.append(i)
  
  
#2º
Lista_normal=[1,2,3,4,5,6,7,8,9]
Lista_invertida=[ i for i in Lista_normal[::-1] ]


#3º
Lista_normal=[1,2,3,4,5,6,7,8,9]
lista.sort(reverse=True)
