#!/usr/bin/env python3

import sys
from time import sleep
def magicName(nome, vogal):
    L = list(nome)
    p = 0
    while(p>-1):
        p = nome.find(vogal, p)
        if p>=0:
            if vogal == "a":
                L[p] = "@"
            elif vogal == "e":
                L[p] = "3"
            elif vogal == "i":
                L[p] = "1"
            elif vogal == "o":
                L[p] = "0"
            else:
                print("invalid format name") 
            p+=1
    nome = "".join(L)
    return nome

def magicNumber(word, born):
    dia, mes, ano = born.split("/")
    print(dia)
    print(mes)
    print(ano)
     

def vowelsbynumber(name, birth, nickname):
    print(f"{name}")	
    vowels = ['a', 'e', 'i','o']
    with open("kickpass.txt", "w") as f:
       new_word = magicName(name,     "a")
       new_word = magicName(new_word, "e")
       new_word = magicName(new_word, "i")
       new_word = magicName(new_word, "o")
       magicNumber(new_word, birth)
       f.write(new_word)
       f.write("\n")
 f.close()

if __name__== "__main__":
    name = sys.argv[1]
    birth = sys.argv[2]
    nickname = []
    nickname += sys.argv if len(sys.argv) > 3 else ''
    vowelsbynumber(name, birth, nickname)
	
