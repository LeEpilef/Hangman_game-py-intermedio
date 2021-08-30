import os
import time
from random import choice
from ascii_hangman import HANGMANPICS


def clear():
    os.system('clear')


def welcome():
    text = ["JUEGO DEL AHORCADO", "Has sido sentenciado a muerte por un crimen que no cometiste, pero resulta imposible comprobarte inocente o culpable.", "Por esta razón se te concede la oportunidad de salvar tu vida haciendo uso de tu astucia.", "¿Podras deducir la palabra correcta y evitar ser ahorcado?"]
    
    for phrase in text:
        if phrase == "JUEGO DEL AHORCADO":
            print("_"*(len(phrase)+2))
            print("|"+phrase+"|")
            print("*"*(len(phrase)+2))
            print(HANGMANPICS[6])
            continue

        for letter in phrase:
            print(letter, end="")
            time.sleep(0.05)
        print("\n")


def choose_word():
        with open("./data.txt", "r", encoding="utf-8") as dat:
            words_base = [word for word in dat]
            word = choice(words_base).strip().upper()
        return(word)


def check_attemp(letter, word, answer,life):
    i=-1
    strike = False
    for char in word:
        i +=1
        if letter == char:
            answer[i] = letter
            strike = True
    
    if not strike:
        life -=1
    
    return answer, life


def run():
    clear()
    game = True
    word = choose_word()
    answer = ["_ " for _ in range(len(word))]
    life = 7

    welcome()
    time.sleep(3)


    while game:
        clear()
        print('Intentos: ', life)
        print(HANGMANPICS[life-1])
        print(*(answer))
        print('\n')
        letter = input("Igresa una letra: ")

        if len(letter) !=1 or not letter.isalpha():
            print("EROR: Ingresa únicamente una letra")
            continue
        else:
            letter = letter.upper()
        
        answer, life = check_attemp(letter, word, answer, life)

        if "_ " not in answer:
            clear()
            print("¡Ganaste!")
            print("La palabra era: "+word)
            print("Vivirás para ver la luz del día una vez más.")
            game = False
        
        if life == 0:
            clear()
            print("¡Perdiste!")
            print("La palabra era: "+word)
            print("Serás ejecutado a primera hora.")
            game = False

if __name__ == "__main__":
    run()