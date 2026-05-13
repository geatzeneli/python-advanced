greetings="hello, judy"

def greet(name):
    global message
    message = f" {greetings},{name}"
    print(message)

greet("bob")





#make a function that you give a list where you find the even numbers  in the list and add all of them up. use modules. tell me how u solved it carefully

import math

def shuma_numrave_cift(lista):
    shuma = 0

    for numri in lista:
        if math.fmod(numri, 2) == 0:
            shuma += numri

    return shuma


numrat = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]

rezultati = shuma_numrave_cift(numrat)

print("Shuma e numrave çift është:", rezultati)