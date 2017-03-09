'''
Created on 9 de mar de 2017

@author: Elisson Matos 
'''
from math import log

number = int(input ("Tamanho da mensagem?"))

bits = int(log(number, 2)+1)

print("Quantidade de bits igual a {0}".format(bits))
