# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:51:04 2016

@author: Artur
"""

import random

print("\tEsse é um jogo de adivinhação de números!")
print("\tVocê jogará esse jogo contra mim, o computador!")
print("\tPense em um número entre 1 e 100 e não se esqueça dele!")
print("\tEu também vou pensar em um número entre 1 e 100 e você "
    "terá que adivinhar!")
print("\tPrepare-se!")

guess = int(input("Tente adivinhar o meu número: "))

number_human = random.randint(1,100)
tries_human = 1
tries_pc = 1

#print(number_pc)
while guess != number_human:
    if guess > number_human:
        print("É menor que isso...")
    
    elif guess < number_human:
        print("É maior que isso...")
        
    tries_human += 1
        
    print("Agora é a minha vez!")
    
    number_pc = random.randint(1,100)
    
    print("O número secreto é...:", number_pc,"?")
    
    resposta = str(input(""))
    
    if resposta == str("Sim"):
        print("UHUL! GANHEI! Eu precisei de", tries_pc, "tentativas!"
        " Foi um jogo difícil, você jogou muito bem!")
        break
                
    else:
        print("Ok, valeu a tentativa. Agora é sua vez de novo!")
        tries_pc += 1
        guess = int(input("Coloque aqui o seu número: "))
        continue 

if guess == number_human: 
    print("UHUL! VOCÊ GANHOU! Você precisou de", tries_human, 
          " tentativas! Foi uma partida disputada, mas você jogou"
          "muito bem!")