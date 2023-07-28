#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:04:29 2022

@author: lmordoneze
"""

"""
This problem consists on developing a calculator for dyslexic people, that replaces the numbers for its name
in letters. For instance: 2 + 2 = 4. The calculator must be able to respond to the enter "DOS MAS DOS"
and prints "CUATRO". Note: The code is in spanish

Input
Firs, will be a N (0<N<122) which will be the number of cases to calculate.
Then, the user will type N operations in the format NUMBER OPERATION NUMBER
The numbers could be from 0 to 10, and the operations could be plus and subtraction

Output
For each case must be printed "CASO N: RESULTADO". If a result is negative must be printed the word "MENOS" before the number.


La dislexia es una alteración de la capacidad para leer porque se confunden palabras, sílabas o letras. En el
caso de la dislexia numérica es la confusión del orden de los números. ¡Sin duda ser disléxico como yo es un
desafortunado caso cuando quieres realizar a la perfección tu examen de matemáticas, pero no puedes evitar
confundir el 225 con el 252!
¡Hoy te vengo a pedir ayuda para poder solucionar este desafortunado problema, consiste en realizar una
calculadora que reemplace los dígitos numéricos por su nombre!
Es decir, en vez de escribir la operación 2 + 2 = 4, la calculadora deberá ser capaz de responder a la entrada
DOS MAS DOS = CUATRO.

Entrada
La entrada para este problema tendrá el siguiente formato:
Primero habrá un N, 0<N<122, que será el número de casos a ser probados.
Luego vendrán N operaciones de forma NUMERO OPERACION NUMERO.
Los números podrán ser del 0 al 10, y las operaciones podrán ser suma o resta.

Salida
Para cada uno de los casos se imprimirá “CASO N: RESULTADO”, recuerden que en caso de que un resultado
sea negativo deberá aparecer la palabra MENOS antes del NUMERO.
"""

N=int(input("Ingrese la cantidad de operaciones que desea realizar: "))
numeros = ["CERO","UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE","DIEZ","ONCE","DOCE","TRECE","CATORCE","QUINCE","DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE","VEINTE"]
operaciones = ["MAS", "MENOS"]

if N>0 and N<122:
    j=1
    for j in range(N):  
        operacion = input("Ingrese la operación en MAYÚSCULAS. Ejemplo: DOS MAS DOS\n")        
        y=1
        i = 0 
        for i in range(len(operacion)):
            if operacion[i] == " " and y == 1:
                a=[]
                a.append(operacion[0:i])
                y=0
                cont = i
            elif operacion[i] == " " and y == 0:
                op=[]
                op.append(operacion[cont+1:i])
                cont = i
                y=2
            if operacion[i] != " " and y == 2:
                b=[]
                b.append(operacion[cont+1:len(operacion)])
                break           
        
        if a[0] in numeros and b[0] in numeros and op[0] in operaciones:
            k=0
            for k in range(len(numeros)-10):
                if a[0] == numeros[k]:
                    num1 = k
                if b[0] == numeros[k]:
                    num2 = k   
            
            if op[0] == "MAS":
                result = num1 + num2
            if op[0] == "MENOS":
                result = num1 - num2
            
            if result<0:
                print("CASO", j+1,": MENOS", numeros[result*-1])
            else:
                print("CASO", j+1,":", numeros[result])
    
        