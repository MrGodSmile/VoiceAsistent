import random

number_words = {
            "ноль": 0,
            "один": 1,
            "два": 2,
            "три": 3,
            "четыре": 4,
            "пять": 5,
            "шесть": 6,
            "семь": 7,
            "восемь": 8,
            "девять": 9,
            "десять": 10,
        }

NumberToGuess = random.randint(1, 10)
print("Ну давайте сыграем, только давайте до 10-ти\nа то мы так долго будем")
print("кто загадывает?")
num = []
who_play = input()

if who_play == "хватит" or who_play == "не хочу":
    print("Ну как хотите")

if who_play == "я":
    print("Ну загадывай")
    while True:
        userGuess = input()
        int_num = number_words.get(userGuess)
        if int_num > 10 or int_num < 1:
            print("Я же сказал от 1 до 10")
        else:
            while True:
                NumberToGuessBot = random.randint(1, 10)
                while num.__contains__(NumberToGuessBot):
                    NumberToGuessBot = random.randint(1, 10)
                num.append(NumberToGuessBot)

                print(f"Я думаю {NumberToGuessBot}")
                answer = input()
                if userGuess == "хватит" or userGuess == "не хочу":
                    print("Ну как хотите")
                    break
                if answer == "да":
                    if int_num != NumberToGuessBot:
                        print(f"Дак ты не это загадывал, я же все знаю, твое число было {int_num}")
                        break
                    print("Было легко")
                    break
                if answer == "нет":
                    if NumberToGuessBot == int_num:
                        print("Не ври, ты это число загадал")
                        break
            break

if who_play == "ты" or who_play == "вы":
    print("Я загадал, угадывай")
    userChoice = input()
    int_num = number_words.get(userChoice)

    while True:
        if userChoice == "хватит" or userChoice == "не хочу":
            print("Ну как хотите")
            break
        if int_num > NumberToGuess:
            print("Число должно быть меньше!")
            userChoice = input("Попробуйте снова: ")
            int_num = number_words.get(userChoice)
        elif int_num < NumberToGuess:
            print("Число должно быть больше!")
            userChoice = input("Попробуйте снова: ")
            int_num = number_words.get(userChoice)
        elif int_num == NumberToGuess:
            print(f"Вы угадали! Это число {NumberToGuess}")
            break