from colorama import *

init()


def replay():
    while True:
        x = input("Игра окончена. Хотите ли вы (выйти) или начать (заново)?\n").lower()
        if x == "заново":
            game()
        elif x == "выйти":
            exit()
        else:
            print("Ошибка ввода. Попробуйте снова.")


def color_red(text):
    print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)


def color_blue (text):
    print(Fore.BLUE + Style.BRIGHT + text + Style.RESET_ALL)


def color_green (text):
    print(Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL)


def color_yellow (text):
    print(Fore.YELLOW + Style.BRIGHT + text + Style.RESET_ALL)


def color_magenta(text):
    print(Fore.MAGENTA + Style.BRIGHT + text + Style.RESET_ALL)


def color_cyan(text):
    print(Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL)


def labirynth(a,b,c):
    while True:
        if a == 3 and b == 5:
            while True:
                x = input("Вы можете пойти (налево), (направо) или (назад)\n").lower()
                if x == "налево":
                    a -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                elif x == "назад":
                    return 6,0
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 4 and b == 5:
            while True:
                x = input("Вы можете пойти (налево) или (направо)\n").lower()
                if x == "налево":
                    a -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 5 and b == 5:
            while True:
                x = input("Вы можете пойти (вперёд) или (налево)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 5 and b == 4:
            while True:
                x = input("Вы можете пойти (налево) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 4 and b == 4:
            while True:
                x = input("Вы можете пойти (налево) или (направо)\n").lower()
                if x == "направо":
                    a += 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 3 and b == 4:
            if c == 0:
                print("Вы нашли что-то блестящее в темноте. Это монетка!")
                return 6,1
            elif c == 1:
                while True:
                    x = input("Тупик! Вы можете пойти только (направо)\n").lower()
                    if x == "направо":
                        a += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        if a == 2 and b == 5:
            while True:
                x = input("Вы можете пойти (вперёд) или (направо)\n").lower()
                if x == "вперёд":
                    b += -1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 1 and b == 5:
            while True:
                x = input("Тупик! Вы можете пойти только (вперёд)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 1 and b == 4:
            while True:
                x = input("Вы можете пойти (направо) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 2 and b == 4:
            while True:
                x = input("Вы можете пойти (вперёд), (налево) или (назад)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                if x == "назад":
                    b += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 1 and b == 3:
            while True:
                x = input("Вы можете пойти (вперёд) или (направо)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 2 and b == 3:
            while True:
                x = input("Вы можете пойти (налево) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 3 and b == 3:
            while True:
                x = input("Тупик! Вы можете пойти только (вперёд)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 4 and b == 3:
            while True:
                x = input("Вы можете пойти (вперёд) или (направо)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 5 and b == 3:
            while True:
                x = input("Вы можете пойти (вперёд) или (налево)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 1 and b == 2:
            while True:
                x = input("Вы можете пойти (направо) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 2 and b == 2:
            while True:
                x = input("Вы можете пойти (налево) или (направо)\n").lower()
                if x == "налево":
                    a -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 3 and b == 2:
            while True:
                x = input("Вы можете пойти (вперёд), (налево), (направо) или (назад)\n").lower()
                if x == "налево":
                    a -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                if x == "вперёд":
                    b -= 1
                    break
                if x == "назад":
                    b += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 4 and b == 2:
            while True:
                x = input("Вы можете пойти (налево) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 5 and b == 2:
            while True:
                x = input("Вы можете пойти (вперёд) или (назад)\n").lower()
                if x == "вперёд":
                    b -= 1
                    break
                if x == "назад":
                    b += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 1 and b == 1:
            print("Вы наступили на нажимную плиту и провалились в яму.")
            return 6,2
        if a == 2 and b == 1:
            while True:
                x = input("Вы можете пойти (налево) или (направо)\n").lower()
                if x == "налево":
                    a -= 1
                    break
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 3 and b == 1:
            while True:
                x = input("Вы можете пойти (налево) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 4 and b == 1:
            print("Вы слышите звуки льющейся воды. Выход близко!")
            while True:
                x = input("Вы можете пойти (вперёд) или (направо)\n").lower()
                if x == "вперёд":
                    return 6,3
                elif x == "направо":
                    a += 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        if a == 5 and b == 1:
            while True:
                x = input("Вы можете пойти (налево) или (назад)\n").lower()
                if x == "назад":
                    b += 1
                    break
                elif x == "налево":
                    a -= 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")


def game():
    room = 0
    scene = 0
    item_metal_pipe = 0
    item_rusty_key = 0
    item_torch = 0
    item_potion_red = 0
    item_potion_green = 0
    item_potion_blue = 0
    item_coin_labyrinth = 0
    item_coin_lockbox = 0
    item_coin_laboratory = 0
    item_coins = 0
    item_kitchen_brownie = 0
    item_kitchen_applepie = 0
    item_kitchen_carrotcake = 0
    item_cleaning_powder = 0
    item_cleaning_soap = 0
    item_cleaning_liquid = 0
    item_flower_rose = 0
    item_flower_tulip = 0
    item_flower_peony = 0
    fountain_entrance = 0
    fountain_counter = 0
    item_chisel = 0
    knowledge = 0
    item_shield = 0

    game_core = True
    while game_core:
        if room == 0:
            print("Здравствуйте! В ходе этой игры вам регулярно будет предоставляться выбор между несколькими возможными действиями.")
            print("В таком случае, слово, обозначающее этот выбор будет выделяться круглыми скобочками. Вам необходимо будет ввести это слово в командную строку.")
            while True:
                x = input("Например сейчас Вы можете либо (продолжить), либо (выйти) из игры. Регистр введённого слова не имеет значения.\n").lower()
                if x == "выйти":
                    exit()
                elif x == "продолжить":
                    room = 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 0:
            print("Вы просыпаетесь на холодном каменном полу. Ваше тело ломит, а голова ноет от всех возможных видов боли")
            print("С трудом поднявшись, Вы осматриваетесь по сторонам и понимаете что оказались за решёткой")
            while True:
                x = input("Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 1:
            print("Вы подходите к кровати. От неё несёт плесенью и сыростью. Голова трещит и вас резко клонит в сон.")
            while True:
                x = input("Вы можете (лечь) на кровать или (отойти) от неё.\n").lower()
                if x == "лечь":
                    scene = 11
                    break
                elif x == "отойти" and item_rusty_key == 0:
                    scene = 12
                    break
                if x == "отойти" and item_rusty_key == 1:
                    scene = 15
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 11:
            print("Вы ложитесь на мокрый рваный матрац. Долго пролежать у Вас не получается, так как под Вашим весом кровать разваливается.")
            print("Одна из её ножек выглядит достаточно крепкой, может пригодиться.")
            color_blue("*Вы получаете ржавую железяку!*")
            item_metal_pipe = 1
            while True:
                x = input("Вы можете (отойти) от развалин кровати в центр комнаты.\n").lower()
                if x == "отойти" and item_rusty_key == 0:
                    scene = 13
                    break
                if x == "отойти" and item_rusty_key == 1:
                    scene = 14
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 12:
            print("Вы преодалеваете сонливость и возвращаетесь в центр комнаты.")
            while True:
                x = input(
                    "Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 15:
            print("Вы преодалеваете сонливость и возвращаетесь в центр комнаты.")
            while True:
                x = input(
                    "Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 13:
            print("Вы возвращаетесь в центр комнаты.")
            while True:
                x = input(
                    "Вы видите перед собой груду металла и тряпок, (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 14:
            print("Вы возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой груду металла и тряпок, (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 2:
            print("Вы подходите к миске. От одного запаха чего бы то ни было съедобного Ваш живот начинает урчать.")
            while True:
                x = input("Вы можете (съесть) еду из миски или (отойти) от неё.\n").lower()
                if x == "съесть":
                    scene = 21
                    break
                elif x == "отойти" and item_metal_pipe == 0 and item_rusty_key == 0:
                    scene = 22
                    break
                elif x == "отойти" and item_metal_pipe == 1 and item_rusty_key == 0:
                    scene = 23
                    break
                elif x == "отойти" and item_metal_pipe == 0 and item_rusty_key == 1:
                    scene = 24
                    break
                elif x == "отойти" and item_metal_pipe == 1 and item_rusty_key == 1:
                    scene = 25
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 21:
            print("Вы нагибаетесь над миской и начинаете жадно пожирать её содержимое голыми руками.")
            print("Меньше чем через минуту миска стоит абсолютно пустая, а ваш желудок полон.")
            print("Вы присаживаетесь, чтобы передохнуть от сытного приёма пищи.")
            print("В Ваших глазах темнеет и Вы падаете на пол, ударяясь об него головой.")
            color_red("*Вы умерли от пищевого отравления*")
            replay()
        elif room == 1 and scene == 22:
            print("Вы преодалеваете чувство голода и возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 23:
            print("Вы преодалеваете голод и возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой груду металла и тряпок, (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 24:
            print("Вы преодалеваете голод и возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 25:
            print("Вы преодалеваете голод и возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой груду металла и тряпок, (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 3:
            print("Вы подходите к двери и видите тёмный каменный коридор с парой тусклых факелов по ту сторону решётки.")
            print("Вы пытаетесь открыть дверь, но она не поддаётся.")
            if item_metal_pipe == 0 and item_rusty_key == 0:
                while True:
                    x = input("Вы можете (отойти) от двери.\n").lower()
                    if x == "отойти":
                        scene = 31
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif item_metal_pipe == 1 and item_rusty_key == 0:
                while True:
                    x = input("Вы можете (отойти) от двери или попытаться (сломать) дверь железякой.\n").lower()
                    if x == "отойти":
                        scene = 13
                        break
                    elif x == "сломать":
                        scene = 34
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif item_metal_pipe == 0 and item_rusty_key == 1:
                while True:
                    x = input("Вы можете (отойти) от двери или попытаться (открыть) дверь ключём.\n").lower()
                    if x == "отойти":
                        scene = 32
                        break
                    elif x == "открыть":
                            scene = 33
                            break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif item_metal_pipe == 1 and item_rusty_key == 1:
                while True:
                    x = input("Вы можете (отойти) от двери, попытаться (сломать) дверь железякой или попытаться (открыть) дверь ключём.\n").lower()
                    if x == "отойти":
                        scene = 14
                        break
                    elif x == "открыть":
                            scene = 33
                            break
                    elif x == "сломать":
                        scene = 34
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 31:
            print("Вы возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 32:
            print("Вы возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 33:
            print("Вы слышите щелчок. Дверь со скрипом открывается. Вы слышите ещё один щелчок. Ключ ломается в ваших руках.")
            color_blue("*Вы теряете ржавый ключ!*")
            item_rusty_key = 0
            print("Вы слышите как потолок в Вашей камере начинает трескаться и обваливаться")
            while True:
                x = input("Вы можете (выбежать), либо (остаться) внутри\n").lower()
                if x == "выбежать":
                    room = 2
                    scene = 0
                    break
                elif x == "остаться":
                    scene = 39
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 34:
            print("Вы начинаете яростно бить по замку двери железной трубой. Через пару ударов дверь раскрывается на распашкуи вы держите в руке погнутую трубу")
            color_blue("*Вы теряете ржавую железяку!*")
            item_metal_pipe = 0
            print("Вы слышите как потолок в Вашей камере начинает трескаться и обваливаться")
            while True:
                x = input("Вы можете (выбежать), либо (остаться) внутри\n").lower()
                if x == "выбежать":
                    room = 2
                    scene = 0
                    break
                elif x == "остаться":
                    scene = 39
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 39:
            print("Вы решаете посчитать трещины на потолке и оказываетесь задавлены тоннами камня")
            color_red("*Вас расплющило*")
            replay()
        elif room == 1 and scene == 4:
            print("Вы подходите к ведру наполненному жижей неизвестного происхождения серо-бур-малинового оттенка. Один только запах вызывает у вас рвотные позывы, закладывает нос и заставляет глаза слезиться.")
            while True:
                x = input("Вы можете (порыться) в ведре или (отойти) от него.\n").lower()
                if x == "порыться":
                    scene = 41
                    break
                elif x == "отойти" and item_metal_pipe == 0:
                    scene = 42
                    break
                elif x == "отойти" and item_metal_pipe == 1:
                    scene = 43
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 41:
            print("Вы садитесь на корточки перед ведром. Ваш живот начинает крутить, будто ваш желудок сжали в кулик.")
            print("Ваша голова начинает кружиться. Вы опускаете руку в ведро.")
            print("Как только ваша кожа касается поверхности жижи, Вас начинает рвать прямо себе на колени.")
            print("Вы подскальзываетесь, опрокидываете ведро и падаете лицом в его содержимое.")
            while True:
                x = input("Вы можете (подняться) или (сдаться).\n").lower()
                if x == "подняться":
                    scene = 44
                    break
                if x == "сдаться":
                    scene = 45
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 42:
            print("Вы затыкаете нос и возвращаетесь в центр комнаты.")
            while True:
                x = input(
                    "Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 43:
            print("Вы затыкаете нос и возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой груду металла и тряпок, (миску) с похлёбкой на полу, (дверь) и (ведро) в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                elif x == "ведро":
                    scene = 4
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 45:
            print("Оно того не стоит...")
            color_red("*Вы задыхаетесь в луже отходов на холодном полу*")
            replay()
        elif room == 1 and scene == 44:
            print("Вы с поднимаетесь на ноги, протирая лицо, и замечаете что-то блестящее в разлитых на полу отходах")
            color_blue("*Вы получаете ржавый ключ!*")
            item_rusty_key = 1
            while True:
                x = input("Вы можете (отойти) от разлитого ведра.\n").lower()
                if x == "отойти" and item_metal_pipe == 0:
                    scene = 46
                    break
                elif x == "отойти" and item_metal_pipe == 1:
                    scene = 47
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 46:
            print("Вы затыкаете нос и возвращаетесь в центр комнаты.")
            while True:
                x = input(
                    "Вы видите перед собой ржавую железную (кровать), (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "кровать":
                    scene = 1
                    break
                elif x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 1 and scene == 47:
            print("Вы затыкаете нос и возвращаетесь в центр комнаты.")
            while True:
                x = input("Вы видите перед собой груду металла и тряпок, (миску) с похлёбкой на полу, (дверь) и разлитое ведро в углу комнаты. Что бы вы хотели осмотреть?\n").lower()
                if x == "миску":
                    scene = 2
                    break
                elif x == "дверь":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 0:
            print("Вы выскакиваете из комнаты в последнюю секунду. Оборачиваясь Вы видите как потолок начинает обрушиваться и полностью заваливает проход обратно.")
            print("Решётка с тяжёлым скрежетом гнётся под весом камня.")
            print("Вы осматриваетесь.")
            while True:
                x = input("Вы можете пойти (налево), пойти (направо) или снять (факел) со стены.\n").lower()
                if x == "налево":
                    scene = 1
                    break
                elif x == "направо":
                    scene = 2
                    break
                elif x == "факел":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 1:
            print("Вы поворачиваете налево и начинаете двигаться по коридору, освещаемому лишь тусклым светом факелов.")
            print("По обе стороны от Вас Вы видите десятки камер, похожих на ту, из которой Вы только что выбрались. Они кажутся пустыми.")
            if item_torch == 1:
                print("Как вдруг Вы замечаете движение в одной из них.")
                while True:
                    x = input("Хотители ли вы подойти (поближе) или пройти (мимо).\n").lower()
                    if x == "поближе":
                        scene = 11
                        break
                    elif x == "мимо":
                        scene = 12
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            if item_torch == 0:
                scene = 13
        elif room == 2 and scene == 11:
            print("Вы подходите ближе к камере и пытаетесь рассмотреть двигающуюся фигуру в свете своего факела.")
            print("Как вдруг она устремляется в Вашу сторону и зватает Вас за горло через решётку.")
            while True:
                x = input("Вы можете попытаться (вырваться) или (сдаться).\n").lower()
                if x == "вырваться":
                    print("Вы пытаетесь убрать руки существа от своей шеи, что лишь провоцирует его сильнее.")
                    print("Вскоре в Ваших глазах темнеет и вы теряете сознание.")
                    color_red("*Вы погибли от удушья*")
                    replay()
                elif x == "сдаться":
                    print("Вы принимаете свою судьбу и расслабляете своё тело, что вводит существо в замешательство.")
                    print("Его хватка ослабевает и вы падаете на пол тяжело вздыхая.")
                    print("Отдышавсшись в отходите от решётки и решаете больше не рисковать.")
                    scene = 13
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 12:
            print("Вы проходите мимо существа в клетке. Вам достаточно своих проблем.")
            print("Вы слышите тихие всхлипы за своей спиной.")
            scene = 13
        elif room == 2 and scene == 13:
            print("Двигаясь дальше по коридору Вы добираетесь до неплохо сохранившейся деревянной двери")
            while True:
                x = input("Вы можете (войти) или (вернуться) назад.\n").lower()
                if x == "войти" and item_coin_lockbox == 1 or item_coin_lockbox == 2:
                    room = 3
                    scene = 11
                    break
                if x == "войти" and item_coin_lockbox == 0:
                    room = 3
                    scene = 0
                    break
                elif x == "вернуться" and item_torch == 0:
                    scene = 32
                    break
                elif x == "вернуться" and item_torch == 1:
                    scene = 33
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 0:
            print("Вы открываете дверь и входите внутрь.")
            print("Вашему взору предстают потрёпанные казармы: несколько кроватей, стол, груда проржавевшего насквозь оружия и крепкая дверь на противоположной стене. Вы также замечаете небольшую шкатулку на столе.")
            while True:
                x = input("Вы можете осмотреть (дверь), попытаться открыть (шкатулку) или (вернуться) в коридор.\n").lower()
                if x == "дверь":
                    scene = 1
                    break
                elif x == "шкатулку":
                    scene = 2
                    break
                elif x == "вернуться" and item_torch == 1:
                    room = 2
                    scene = 33
                    break
                elif x == "вернуться" and item_torch == 0:
                    room = 2
                    scene = 32
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 1 and item_potion_blue == 0:
            print("Вы подходите к массивной усиленной деревянной двери со стальными украшениями. Такую просто так не сломаешь.")
            while True:
                x = input("Вы видите под дверью достаточно крупную щель, размером где-то с Ваш кулак. Вы не уверены как её открыть. Вы можете (отойти) от двери.\n").lower()
                if x == "отойти" and item_coin_lockbox == 0:
                    scene = 0
                    break
                elif x == "отойти" and item_coin_lockbox == 1 or item_coin_lockbox == 2:
                    scene = 11
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 1 and item_potion_blue == 1:
            print("Вы подходите к массивной усиленной деревянной двери со стальными украшениями. Такую просто так не сломаешь.")
            while True:
                x = input("Вы видите под дверью достаточно крупную щель, размером где-то с Ваш кулак. Вы можете использовать Ваше (зелье) или (отойти) от двери.\n").lower()
                if x == "отойти" and item_coin_lockbox == 0:
                    scene = 0
                    break
                elif x == "отойти" and item_coin_lockbox == 1 or item_coin_lockbox == 2:
                    scene = 11
                    break
                elif x == "зелье":
                    scene = 12
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 2 and item_rusty_key == 0:
            print("Вы подходите к резной деревянной шкатулке, которая, судя по всему, прибита к столешнице на которой стоит.")
            print("Вы видите маленькую замочную скважину. Вы не знаете чем её открыть")
            while True:
                x = input("Вы можете (отойти) от шкатулки.\n").lower()
                if x == "отойти":
                    item_coin_lockbox = 2
                    scene = 11
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 2 and item_rusty_key == 1:
            print("Вы подходите к резной деревянной шкатулке, которая, судя по всему, прибита к столешнице на которой стоит.")
            print("Вы видите маленькую замочную скважину.")
            while True:
                x = input("Вы можете попробовать (открыть) её ключом. Вы можете (отойти) от шкатулки.\n").lower()
                if x == "открыть":
                    print("Вы открываете шкатулку и видите как она заполнена до краёв... одной золотой монетой")
                    item_coin_lockbox = 1
                    color_blue("*Вы получаете золотую монету!*")
                    item_coins += 1
                    color_blue("*Вы теряете ржавый ключ!*")
                    item_rusty_key = 0
                    scene = 11
                    break
                elif x == "отойти" and item_coin_lockbox == 0:
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 11:
            print("Вашему взору предстают потрёпанные казармы: несколько кроватей, стол, груда проржавевшего насквозь оружия и крепкая дверь на противоположной стене.")
            while True:
                x = input("Вы можете осмотреть (дверь) или (вернуться) в коридор.\n").lower()
                if x == "дверь":
                    scene = 1
                    break
                elif x == "вернуться" and item_torch == 1:
                    room = 2
                    scene = 33
                    break
                elif x == "вернуться" and item_torch == 0:
                    room = 2
                    scene = 32
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 3 and scene == 12:
            print("Вы достаёте бутылёк с синим элексиром и сделав пару быстрых вздохов выпиваете его до дна.")
            color_blue("*Вы теряете синее зелье!*")
            print("Вы чувствуете как Ваше тело начинает стремительно уменьшаться в размерах пока вы не становитесь ростом с полевую мышь.")
            print("Вы ощущаете как Ваше тело отвергает трансформацию и пытается вернуться в своё нормальное состояние. Нужно действовать быстро.")
            while True:
                x = input("Вы можете (протиснуться) под дверью, либо (остаться) с этой стороны.\n").lower()
                if x == "протиснуться":
                    scene = 0
                    room = 7
                    break
                elif x == "остаться":
                    print("Вы решаете остаться на этой стороне и начинаете пятиться назад.")
                    print("Не заметив трещину в полу вы проваливаетесь между досок.")
                    print("Эффект зелья оканчивается, вы стремительно возвращаетесь к своему привычноми размеру, а окружающие вас строительные материалы стремительно делают из Вашего туловища кашу.")
                    color_red("*Вы застряли в текстурах*")
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 3:
            print("Вы видите горящий факел в пределах досягаемости.")
            while True:
                x = input("Вы можете (взять) факел или (отойти) от него.\n").lower()
                if x == "взять":
                    scene = 31
                    break
                elif x == "отойти":
                    scene = 32
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 31:
            print("Вы достаёте факел из металлического держателя.")
            color_blue("*Вы получаете факел!*.")
            item_torch = 1
            scene = 33
        elif room == 2 and scene == 32:
            print("Вы снова стоите у обвалившегося входа в Вашу камеру заключения.")
            while True:
                x = input("Вы можете пойти (налево), пойти (направо) или снять (факел) со стены.\n").lower()
                if x == "налево":
                    scene = 1
                    break
                elif x == "направо":
                    scene = 2
                    break
                elif x == "факел":
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 33:
            print("Вы снова стоите у обвалившегося входа в вашу камеру заключения.")
            while True:
                x = input("Вы можете пойти (налево) или пойти (направо).\n").lower()
                if x == "налево":
                    scene = 1
                    break
                elif x == "направо":
                    scene = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 2:
            print("Вы приходите к развилке.")
            while True:
                if item_potion_red == 0 and item_potion_green == 0 and item_potion_blue == 0:
                    x = input("Вы можете пойти (прямо) в неосвещённый проход или пойти (налево) в открытую комнату с подгоревшей деревянной дверью, либо вернуться (назад). Проход налево завален камнями.\n").lower()
                    if x == "прямо":
                        room = 6
                        scene = 0
                        break
                    elif x == "налево":
                        room = 4
                        scene = 0
                        break
                    elif x == "назад" and item_torch == 1:
                        scene = 33
                        break
                    elif x == "назад" and item_torch == 0:
                        scene = 32
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_potion_red == 1:
                    x = input("Вы можете пойти (прямо) в неосвещённый проход, либо вернуться (назад). Проход налево завален камнями. Вы можете попыпаться (расчистить) его зельем.\n").lower()
                    if x == "прямо":
                        room = 6
                        scene = 0
                        break
                    elif x == "налево":
                        room = 4
                        scene = 0
                        break
                    elif x == "расчистить":
                        scene = 23
                        break
                    elif x == "назад" and item_torch == 1:
                        scene = 33
                        break
                    elif x == "назад" and item_torch == 0:
                        scene = 32
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_potion_blue == 1 or item_potion_green == 1:
                    x = input("Вы можете пойти (прямо) в неосвещённый проход, либо вернуться (назад). Проход налево завален камнями.\n").lower()
                    if x == "прямо":
                        room = 6
                        scene = 0
                        break
                    elif x == "налево":
                        room = 4
                        scene = 0
                        break
                    elif x == "назад" and item_torch == 1:
                        scene = 33
                        break
                    elif x == "назад" and item_torch == 0:
                        scene = 32
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 2 and scene == 23:
            print("Вы достаёте свою недавнюю находку в виде красной бутылки из кармана, делаете пару шагов назад и швыряете её в груду камней.")
            color_blue("*Вы теряете красное зелье!*")
            item_potion_red = 0
            print("Как только склянка касается твёрдой поверхности, она разбивается и взрывается отталкивая вас на пару метров и разбрасывая загорождение во все стороны.")
            print("Вы снова слышите как потолок начинает трескаться.")
            while True:
                x = input("Вы можете взять (забежать) в образовавшийся проход или (остаться) на этой стороне.\n").lower()
                if x == "забежать":
                    room = 5
                    scene = 0
                    break
                elif x == "остаться":
                    print("Вы решаете посчитать трещины на потолке и оказываетесь задавлены тоннами камня")
                    color_red("*Вас расплющило*")
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 4 and scene == 0:
            print("Вы заходите в тёмную комнату, в которой пахнет серой, порохом и морской солью.")
            print("Вы видите кучу поломаной мебели, груду посуды и кучи разбитого стекла.")
            print("В дальнем углу комнаты вы замечаете треугольный стол с тремя стеклянными бутылками разной формы, наполненные жидкостями разного цвета.")
            while True:
                if item_torch == 0:
                    x = input("Вы можете взять (красную) бутылку, взять (синюю) бутылку, взять (зелёную) бутылку, или (вернуться) в коридор.\n").lower()
                    if x == "красную":
                        scene = 1
                        break
                    elif x == "синюю":
                        scene = 2
                        break
                    elif x == "зелёную":
                        scene = 3
                        break
                    elif x == "вернуться":
                        scene = 2
                        room = 2
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                if item_torch == 1:
                    x = input("Вы можете взять (красную) бутылку, взять (синюю) бутылку, взять (зелёную) бутылку, либо (осмотреть) их поближе или (вернуться) в коридор.\n").lower()
                    if x == "красную":
                        scene = 1
                        break
                    elif x == "синюю":
                        scene = 2
                        break
                    elif x == "зелёную":
                        scene = 3
                        break
                    elif x == "вернуться":
                        scene = 2
                        room = 2
                        break
                    elif x == "осмотреть":
                        scene = 5
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 4 and scene == 5:
            print("Вы подносите факел ближе к склянкам")
            print("Вы видите на красной этикетку с изображением взрыва, на синей этикетку с изображением двух кубов со стрелочкой от большего к меньшему и на зелёной этикетку с изображением щита.")
            while True:
                    x = input("Вы можете взять (красную) бутылку, взять (синюю) бутылку, взять (зелёную) бутылку, или (вернуться) в коридор.\n").lower()
                    if x == "красную":
                        scene = 1
                        break
                    elif x == "синюю":
                        scene = 2
                        break
                    elif x == "зелёную":
                        scene = 3
                        break
                    elif x == "вернуться":
                        scene = 2
                        room = 2
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 4 and scene == 1:
            print("Вы берёте красную бутылку в руки.")
            print("Как только вы это делаете стол державший их перекашивается и оставшиеся две склянки падают на пол, разбиваясь в дребезги, образуя на полу маленький камушек.")
            color_blue("*Вы получаете красное зелье!*")
            item_potion_red = 1
            while True:
                x = input("Больше тут делать нечего, вы можете (вернуться) в коридор.\n").lower()
                if x == "вернуться":
                    scene = 2
                    room = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 4 and scene == 2:
            print("Вы берёте синюю бутылку в руки.")
            print("Как только вы это делаете стол державший их перекашивается и оставшиеся две склянки падают на пол, разбиваясь в дребезги, взрываясь и тут же застывая в хаотическое каменное изваяние.")
            color_blue("*Вы получаете синее зелье!*")
            item_potion_blue = 1
            while True:
                x = input("Больше тут делать нечего, вы можете (вернуться) в коридор.\n").lower()
                if x == "вернуться":
                    scene = 2
                    room = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 4 and scene == 3:
            print("Вы берёте зелёную бутылку в руки.")
            print("Как только вы это делаете стол державший их перекашивается и оставшиеся две склянки падают на пол, разбиваясь в дребезги, создавая взрыв диаметром с Ваш указательный палец.")
            color_blue("*Вы получаете зелёное зелье!*")
            item_potion_green = 1
            while True:
                x = input("Больше тут делать нечего, вы можете (вернуться) в коридор.\n").lower()
                if x == "вернуться":
                    scene = 2
                    room = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 5 and scene == 0:
            print("Пытаясь скрыться от обломков Вы забегаете внутрь.")
            print("Вы всё ещё не чувствуете себя в безопасности, необходимо двигаться быстро.")
            print("Вы осматриваетесь и обнаруживаете себя в какой-то лаборатории.")
            print("Повсюду разбросаны стеклянные банки, склянки, пробирки и прочее оборудование.")
            print("Вы видите несколько крупных стеклянных ёмкостей, стоящих вдоль стен лаборатории.")
            print("Большая часть из них разбита.")
            print("Вы видите лестницу наверх с люком в противоположной стороне комнаты.")
            while True:
                x = input("Вы можете (осмотреть) ёмкости или (продолжить) двигаться дальше.\n").lower()
                if x == "осмотреть":
                    scene = 1
                    break
                elif x == "продолжить":
                    scene = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 5 and scene == 1:
            print("Вы подходите к одной из разбитых ёмкостей и впервые за чёрт знает сколько времени видите своё отражение.")
            print("Вы двигаетесь дальше и осматриваете одну из уцелевших ёмкостей. Она наполнена полупрозрачной зеленоватой жидкостью.")
            print("Вы наблюдаете как что-то начинает шевелиться по ту сторону стекла, как вдруг Вы видите собственное лицо, озлобленно смотрящее на Вас из своей подводной тюрьмы.")
            print("Вы слышите как потолок начинает трескаться и в этой комнате. Пора убираться от сюда.")
            while True:
                x = input("Вы можете (бежать) до лестницы с люком.\n").lower()
                if x == "бежать":
                    print("Вы устремляетесь к лестнице и взбираетесь по ней как можно быстрее. Вы слышите треск камня, скрежет металла и бьющееся стекло за своей спиной.")
                    print("Отперев засов на люке, Вы выбираетесь наверх. Только Вы убираете свою ногу с лестницы, как она обваливается вниз, во тьму.")
                    scene = 0
                    room = 9
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 5 and scene == 2:
            print("Вы начинаете двигаться в сторону лестницы, как вдруг замечаете что-то блестящее на одном из столов неподалёку.")
            print("Это золотая монетка в чашке Петри.")
            color_blue("*Вы получаете золотую монету!*")
            item_coins += 1
            item_coin_laboratory = 1
            scene = 3
        elif room == 5 and scene == 3:
            print("Вы слышите как потолок начинает трескаться и в этой комнате. Пора убираться от сюда.")
            while True:
                x = input("Вы можете (бежать) до лестницы с люком.\n").lower()
                if x == "бежать":
                    print("Вы устремляетесь к лестнице и взбираетесь по ней как можно быстрее. Вы слышите треск камня, скрежет металла и бьющееся стекло за своей спиной.")
                    print("Отперев засов на люке, Вы выбираетесь наверх. Только Вы убираете свою ногу с лестницы, как она обваливается вниз, во тьму.")
                    print("Вы закрываете люк за собой, он сразу же защёлкивается с другой стороны.")
                    scene = 0
                    room = 9
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 6 and scene == 0 and item_torch == 0:
            print("Вы оказываетесь на входе в беспросветно тёмную комнату.")
            while True:
                x = input("Вы можете пойти (вперёд) или вернуться (назад).\n").lower()
                if x == "вперёд":
                    print("Вы делаете пару шагов вперёд, но утыкаетесь в стену.")
                    print("Вскоре вам приходится двигаться наощупь. Вы понимаете, что оказались в каком-то лабиринте.")
                    print("Вы также понимаете, что не имеете ни малейшего представления где находится выход из этого лабиринта. Или вход.")
                    print("Следующие несколько дней Вы пытаетесь выбраться из этой ловушки, но безуспешно. В ваших глазах темнеет.")
                    color_red("*Вы погибли от обезвоживания*")
                    replay()
                    break
                elif x == "назад":
                    room = 2
                    scene = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 6 and scene == 0 and item_torch == 1:
            print("Вы оказываетесь на входе в беспросветно тёмную комнату. Посветив в неё факелом, Вы понимаете, что это лабиринт.")
            while True:
                if item_coin_labyrinth == 0:
                    x = input("Вы можете пойти (вперёд) или вернуться (назад).\n").lower()
                    if x == "вперёд":
                        room, scene = labirynth(3,5,0)
                        break
                    elif x == "назад":
                        room = 2
                        scene = 2
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth == 1:
                    x = input("Вы можете пойти (вперёд) или вернуться (назад).\n").lower()
                    if x == "вперёд":
                        room, scene = labirynth(3, 5, 1)
                        break
                    elif x == "назад":
                        room = 2
                        scene = 2
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 6 and scene == 1:
            color_blue("*Вы получаете золотую монету*!")
            item_coin_labyrinth = 1
            item_coins += 1
            room, scene = labirynth(3, 4, 1)
        elif room == 6 and scene == 2:
            print("Пролетев с десяток метров вниз и упав плашмя на живот, вам уже мало что светит.")
            print("Даже ваш факел потух.")
            print("У вас в глазах темнеет.")
            color_red("*Вы повернули не туда*")
            replay()
        elif room == 6 and scene == 3:
            print("Журчание воды усиливается и вскоре Вам виден свет.")
            print("Но не свет вашего факела, дневной свет.")
            print("Вы видите небо.")
            print("Забыв обо всём другом, вы устремляетесь вперёд, навстречу лазурному полотну.")
            print("Вы даже не задумываетесь о том, что потушили собственный факел, пробежав через искуственный водопад.")
            color_blue("*Вы теряете факел!*")
            item_torch = 0
            room = 8
            scene = 0
        elif room == 7 and scene == 0:
            print("Вы с лёгкостью протискиваетесь под дверью и через пару мгновений возвращаетесь к своему обычному размеру.")
            print("Вас немного подташнивает, и вы, опираись на ближайшую стену, поднимаетесь на ноги.")
            print("Вы осматриваетесь по сторонам и видите перед собой кухню. Дверь за вашей спиной всё так же заперта.")
            scene = 1
        elif room == 7 and scene == 1:
            print("Куча посуды, ингридиентов и всё свежее, в хорошем состоянии.")
            while True:
                x = input("Ваш живот урчит. Вы можете (выйти) из кухни или (приготовить) что-нибудь.\n").lower()
                if x == "выйти":
                    room = 10
                    scene = 0
                    break
                elif x == "приготовить":
                    scene = 10
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 10:
            print("Вы решаете что сейчас самое время потренировать своё кулинарное мастерство.")
            while True:
                x = input("Вы можете приготовить (брауни), (шарлотку) или морковный (торт) из доступных ингредиентов, либо (выйти) из кухни.\n").lower()
                if x == "выйти":
                    room = 10
                    scene = 0
                    break
                elif x == "брауни":
                    scene = 11
                    break
                elif x == "шарлотку":
                    scene = 12
                    break
                elif x == "торт":
                    scene = 13
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 11 and item_torch == 0 and item_coins < 1:
            print("Вам безумно хочется брауни.")
            print("Собрав шоколад, сливочное масло, сахар, яйца, муку и соль Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...и вы с позором её покидаете.")
            room = 10
            scene = 11
        elif room == 7 and scene == 11 and item_torch == 0 and item_coins > 0:
            print("Вам безумно хочется брауни.")
            print("Собрав шоколад, сливочное масло, сахар, яйца, муку и соль Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...к счастью у Вас есть монетка, которой вы можете попытаться разжечь огонь.")
            while True:
                x = input("Вы можете (приготовить) брауни или (выйти) из кухни.\n").lower()
                if x == "приготовить":
                    print("В процессе розжига, Вы роняете монетку в печь, но огонь разгарается.")
                    color_blue("*Вы теряете монетку!*")
                    item_coins += -1
                    print("Вы полностью переворачиваете кухню, но у вас получается приготовить достаточно большую порцию брауни.")
                    print("Наевшись до отвала, у вас всё равно остаётся запас.")
                    color_blue("*Вы получаете брауни!*")
                    item_kitchen_brownie = 1
                    room = 10
                    scene = 11
                    break
                elif x == "выйти":
                    room = 10
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 11 and item_torch == 1:
            print("Вам безумно хочется брауни.")
            print("Собрав шоколад, сливочное масло, сахар, яйца, муку и соль Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...к счастью у вас есть факел.")
            while True:
                x = input("Вы можете (приготовить) брауни или (выйти) из кухни.\n").lower()
                if x == "приготовить":
                    print("Вы полностью переворачиваете кухню, но у вас получается приготовить достаточно большую порцию брауни.")
                    print("Наевшись до отвала, у вас всё равно остаётся запас.")
                    color_blue("*Вы получаете брауни!*")
                    item_kitchen_brownie = 1
                    room = 10
                    scene = 11
                    break
                elif x == "выйти":
                    room = 10
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 12 and item_torch == 0  and item_coins < 1:
            print("Вам безумно хочется шарлотки.")
            print("Собрав яблоки, сахар, яйца и муку Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...и вы с позором её покидаете.")
            room = 10
            scene = 11
        elif room == 7 and scene == 12 and item_torch == 0 and item_coins > 0:
            print("Вам безумно хочется шарлотки.")
            print("Собрав яблоки, сахар, яйца и муку Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...к счастью у Вас есть монетка, которой вы можете попытаться разжечь огонь.")
            while True:
                x = input("Вы можете (приготовить) шарлотку или (выйти) из кухни.\n").lower()
                if x == "приготовить":
                    print("В процессе розжига, Вы роняете монетку в печь, но огонь разгарается.")
                    color_blue("*Вы теряете монетку!*")
                    item_coins += -1
                    print(
                        "Вы полностью переворачиваете кухню, но у вас получается приготовить достаточно большую порцию шарлотки.")
                    print("Наевшись до отвала, у вас всё равно остаётся запас.")
                    color_blue("*Вы получаете шарлотку!*")
                    item_kitchen_applepie = 1
                    room = 10
                    scene = 11
                    break
                elif x == "выйти":
                    room = 10
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 12 and item_torch == 1:
            print("Вам безумно хочется шарлотки.")
            print("Собрав яблоки, сахар, яйца и муку Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...к счастью у вас есть факел.")
            while True:
                x = input("Вы можете (приготовить) шарлотку или (выйти) из кухни.\n").lower()
                if x == "приготовить":
                    print("Вы полностью переворачиваете кухню, но у вас получается приготовить достаточно большую порцию шарлотки.")
                    print("Наевшись до отвала, у вас всё равно остаётся запас.")
                    color_blue("*Вы получаете шарлотку!*")
                    item_kitchen_applepie = 1
                    room = 10
                    scene = 11
                    break
                elif x == "выйти":
                    room = 10
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 13 and item_torch == 0  and item_coins < 1:
            print("Вам безумно хочется морковного торта.")
            print("Собрав морковь, растительное масло, сахар, яйца, сметану, корицу, мёд и муку Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...и вы с позором её покидаете.")
            room = 10
            scene = 11
        elif room == 7 and scene == 13 and item_torch == 0 and item_coins > 0:
            print("Вам безумно хочется морковного торта.")
            print("Собрав морковь, растительное масло, сахар, яйца, сметану, корицу, мёд и муку Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...к счастью у Вас есть монетка, которой вы можете попытаться разжечь огонь.")
            while True:
                x = input("Вы можете (приготовить) морковный торт или (выйти) из кухни.\n").lower()
                if x == "приготовить":
                    print("В процессе розжига, Вы роняете монетку в печь, но огонь разгарается.")
                    color_blue("*Вы теряете монетку!*")
                    item_coins += -1
                    print("Вы полностью переворачиваете кухню, но у вас получается приготовить достаточно большую порцию морковного торта.")
                    print("Наевшись до отвала, у вас всё равно остаётся запас.")
                    color_blue("*Вы получаете морковный торт!*")
                    item_kitchen_carrotcake += 1
                    room = 10
                    scene = 11
                    break
                elif x == "выйти":
                    room = 10
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 7 and scene == 13 and item_torch == 1:
            print("Вам безумно хочется морковного торта.")
            print("Собрав морковь, растительное масло, сахар, яйца, сметану, корицу, мёд и муку Вы готовы приступить к готовке.")
            print("К сожалению на кухне нет ничего чем можно было бы зажечь печь...")
            print("...к счастью у вас есть факел.")
            while True:
                x = input("Вы можете (приготовить) морковный торт  или (выйти) из кухни..\n").lower()
                if x == "приготовить":
                    print("Вы полностью переворачиваете кухню, но у вас получается приготовить достаточно большую порцию морковного торта.")
                    print("Наевшись до отвала, у вас всё равно остаётся запас.")
                    color_blue("*Вы получаете морковный торт!*")
                    item_kitchen_carrotcake += 1
                    room = 10
                    scene = 11
                    break
                elif x == "выйти":
                    room = 10
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 10 and scene == 0:
            print("Вы стоите в коридоре. На стенах висят картины, вдоль них стоят вазы, а пол покрывает ковровая дорожка")
            while True:
                x = input("Вы можете пойти в сторону (кухни), в сторону (кладовой) или выйти в (сад).\n").lower()
                if x == "кухни":
                    print("Вы направляетесь в кухню, следуя указателям на стенах.")
                    room = 7
                    scene = 1
                    break
                elif x == "кладовой":
                    print("Вы направляетесь в кладовую, следуя указателям на стенах.")
                    room = 9
                    scene = 0
                    break
                elif x == "сад":
                    print("Вы направляетесь в сад, выходя на улицу.")
                    room = 11
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 10 and scene == 11:
            print("Вы стоите в коридоре. На стенах висят картины, вдоль них стоят вазы, а пол покрывает ковровая дорожка")
            while True:
                x = input("Вы можете пойти в сторону (кладовой) или выйти в (сад), на кухне делать больше нечего.\n").lower()
                if x == "кладовой":
                    print("Вы направляетесь в кладовую, следуя указателям на стенах.")
                    room = 9
                    scene = 0
                    break
                elif x == "сад":
                    print("Вы направляетесь в сад, выходя на улицу.")
                    room = 11
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 9 and scene == 0 and item_cleaning_soap == 0 and item_cleaning_liquid == 0 and item_cleaning_powder == 0:
            print("Вы оказались в кладовой. Куча полок с разного вида бутылками, коробками и мешками стоят вдоль стен.")
            print("Возможно вы найдёте здесь что-нибудь полезное.")
            while True:
                x = input("Вы можете взять (мешочек), (бутылку) или (ящичек), либо (выйти) из кладовой.\n").lower()
                if x == "мешочек":
                    print("Вы проверяете близлежащий мешочек. Стиральный порошок... Вы быстро осматриваете другие ёмкости. Пусто. Чтож, главное его в дёсны не втирать.")
                    color_blue("*Вы получаете стиральный порошок!*")
                    item_cleaning_powder = 1
                    break
                elif x == "бутылку":
                    print("Вы проверяете близлежащую бутылку. Моющее средство... Вы быстро осматриваете другие ёмкости. Пусто. Жаль им совесть не отмоешь.")
                    color_blue("*Вы получаете моющее средство!*")
                    item_cleaning_liquid = 1
                    break
                elif x == "ящичек":
                    print("Вы проверяете близлежащий ящичек. Мыло... Вы быстро осматриваете другие ёмкости. Пусто. Главное его не ронять.")
                    color_blue("*Вы получаете мыло!*")
                    item_cleaning_soap = 1
                    break
                elif x == "выйти" and item_kitchen_applepie == 0 and item_kitchen_carrotcake == 0 and item_kitchen_brownie == 0:
                    room = 10
                    scene = 0
                    break
                elif x == "выйти" and item_kitchen_applepie == 1 or item_kitchen_carrotcake == 1 or item_kitchen_brownie == 1:
                    room = 10
                    scene = 11
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 9 and scene == 0 and (item_cleaning_soap == 1 or item_cleaning_liquid == 1 or item_cleaning_powder == 1):
            print("Вы оказались в кладовой. Куча полок с разного вида бутылками, коробками и мешками стоят вдоль стен.")
            print("Здесь очень пусто и грустно, зато пахнет вкусно.")
            while True:
                x = input("Вы можете (выйти) из кладовой.\n").lower()
                if x == "выйти" and item_kitchen_applepie == 0 and item_kitchen_carrotcake == 0 and item_kitchen_brownie == 0:
                    room = 10
                    scene = 0
                    break
                elif x == "выйти" and item_kitchen_applepie == 1 or item_kitchen_carrotcake == 1 or item_kitchen_brownie == 1:
                    room = 10
                    scene = 11
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 8 and scene == 0 and item_flower_tulip == 0 and item_flower_peony == 0 and item_flower_rose == 0:
            print("Вы оказались в оранжерее. Солнечный свет проникает сквозь окна и мягко ложится на пёстрое разнообразие цветов.")
            print("Вам хочется взять несколько с собой.")
            while True:
                x = input("Вы можете нарвать (роз), (тюльпанов) или (пионов), либо (выйти) из оранжереи.\n").lower()
                if x == "роз":
                    print("Вы набираете полный букет роз. В процессе вы задеваете локтём лейку с тёмной жидкостью.")
                    print("Она покрывает оставшиеся цветы и те моментальнор чернеют и вянут.")
                    color_blue("*Вы получаете букет роз!*")
                    item_flower_rose = 1
                    break
                elif x == "тюльпанов":
                    print("Вы набираете полный букет тюльпанов. В процессе вы задеваете локтём лейку с тёмной жидкостью.")
                    print("Она покрывает оставшиеся цветы и те моментальнор чернеют и вянут.")
                    color_blue("*Вы получаете букет тюльпанов!*")
                    item_flower_tulip = 1
                    break
                elif x == "пионов":
                    print("Вы набираете полный букет пионов. В процессе вы задеваете локтём лейку с тёмной жидкостью.")
                    print("Она покрывает оставшиеся цветы и те моментальнор чернеют и вянут.")
                    color_blue("*Вы получаете букет пионов!*")
                    item_flower_tulip = 1
                    break
                elif x == "выйти":
                    room = 11
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 8 and scene == 0 and (item_flower_tulip == 1 or item_flower_peony == 1 or item_flower_rose == 1):
            print("Вы оказались в оранжерее. Солнце заволокло тучами, а все цветы завяли.")
            while True:
                x = input("Вы решаете, что лучше их не трогать. Вы можете (выйти) из оранжереи.\n").lower()
                if x == "выйти":
                    room = 11
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 11 and scene == 0 and fountain_entrance == 0:
            print("Вы стоите в саду, в центре которого возвышается громадный фонтан.")
            print("Вы видите застеклённое здание оранжереи, покрытое вьюном и лозой.")
            print("Вы видите двери, ведущие внутрь белокаменного особняка.")
            print("Чуть поотдаль путь из усадьбы преграждают позолоченные ворота, сверкающие на солнце.")
            while True:
                x = input("Вы можете осмотреть (фонтан), пройти в (оранжерею), зайти (внутрь) или пройти в (ворота).\n").lower()
                if x == "фонтан":
                    room = 11
                    scene = 1
                    break
                elif x == "оранжерею":
                    room = 8
                    scene = 0
                    break
                elif x == "ворота":
                    room = 13
                    scene = 0
                    break
                elif x == "внутрь" and item_kitchen_applepie == 0 and item_kitchen_carrotcake == 0 and item_kitchen_brownie == 0:
                    room = 10
                    scene = 0
                    break
                elif x == "внутрь" and item_kitchen_applepie == 1 or item_kitchen_carrotcake == 1 or item_kitchen_brownie == 1:
                    room = 10
                    scene = 11
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 11 and scene == 1 and item_coins > 0:
            print("Вы подходите ближе к фонтану и рассматриваете его.")
            print("Он выглядит как Ваша статуя, держащая глобус, из которого и выливается поток воды.")
            print("У подножия статуи вы видите три круглых отверстия размером примерно с монетку.")
            while True:
                x = input("Вы можете (отойти) от фонтана, либо попытаться (вставить) в одно из отверстий монетку.\n").lower()
                if x == "отойти":
                    room = 11
                    scene = 0
                    break
                elif x == "вставить":
                    room = 11
                    scene = 2
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 11 and scene == 1 and item_coins == 0:
            print("Вы подходите ближе к фонтану и рассматриваете его.")
            print("Он выглядит как Ваша статуя, держащая глобус, из которого и выливается поток воды.")
            print("У подножия статуи вы видите три круглых отверстия размером примерно с монетку.")
            while True:
                x = input("У вас нет мелочи. Вы можете (отойти) от фонтана.\n").lower()
                if x == "отойти":
                    room = 11
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 11 and scene == 2:
            print("Вы подходите ближе к основанию фонтана.")
            if fountain_counter == 0:
                print("В основании фонтана три пустующих отверстия.")
            if fountain_counter == 1:
                print("В основании фонтана два пустующих отверстия и одна монета, намертво сидящая в третьем.")
            if fountain_counter == 2:
                print("В основании фонтана одно пустующее отверстие и две монеты, намертво сидящие двух других.")
            if fountain_counter == 3:
                print("В основании фонтана три монеты, намертво сидящие в трёх отверстиях.")
            while True:
                if item_coin_labyrinth == 1 and item_coin_lockbox == 1 and item_coin_laboratory == 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (лабиринте), в (шкатулке) или в (лаборатории), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "лабиринте":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_labyrinth = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    elif x == "шкатулке":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_lockbox = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    elif x == "лаборатории":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_laboratory = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth != 1 and item_coin_lockbox == 1 and item_coin_laboratory == 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (шкатулке) или в (лаборатории), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "шкатулке":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_lockbox = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    elif x == "лаборатории":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_laboratory = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth == 1 and item_coin_lockbox != 1 and item_coin_laboratory == 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (лабиринте) или в (лаборатории), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "лабиринте":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_labyrinth = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    elif x == "лаборатории":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_laboratory = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth == 1 and item_coin_lockbox == 1 and item_coin_laboratory != 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (лабиринте) или в (шкатулке), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "лабиринте":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_labyrinth = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    elif x == "шкатулке":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_lockbox = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth != 1 and item_coin_lockbox != 1 and item_coin_laboratory == 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (лаборатории), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "лаборатории":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_laboratory = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth == 1 and item_coin_lockbox != 1 and item_coin_laboratory != 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (лабиринте), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "лабиринте":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_labyrinth = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth != 1 and item_coin_lockbox == 1 and item_coin_laboratory != 1:
                    x = input("Вы можете вставить монету, которую вы нашли в (шкатулке), либо Вы можете (отойти) от фонтана.\n").lower()
                    if x == "отойти":
                        room = 11
                        scene = 0
                        break
                    elif x == "шкатулке":
                        print("Вы вставляете найденную Вами монету в основание фонтана, она входит как литая.")
                        color_blue("*Вы теряете золотую монетку!*")
                        item_coin_lockbox = 0
                        item_coins += -1
                        fountain_counter += 1
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
                elif item_coin_labyrinth != 1 and item_coin_lockbox != 1 and item_coin_laboratory != 1:
                    print("Вы слышите механический щелчок, а затем скрежет исходящий от противоположной стороны статуя.")
                    room = 12
                    scene = 0
                    fountain_entrance = 1
                    break
        elif room == 11 and scene == 0 and fountain_entrance == 1:
            print("Вы стоите в саду, в центре которого возвышается громадный фонтан.")
            print("Вы видите застеклённое здание оранжереи, покрытое вьюном и лозой.")
            print("Вы видите двери, ведущие внутрь белокаменного особняка.")
            print("Чуть поотдаль путь из усадьбы преграждают позолоченные ворота, сверкающие на солнце.")
            while True:
                x = input("Вы можете осмотреть (фонтан), пройти в (оранжерею), зайти (внутрь) или пройти в (ворота).\n").lower()
                if x == "фонтан":
                    room = 12
                    scene = 0
                    break
                elif x == "оранжерею":
                    room = 8
                    scene = 0
                    break
                elif x == "ворота":
                    room = 13
                    scene = 0
                    break
                elif x == "внутрь" and item_kitchen_applepie == 0 and item_kitchen_carrotcake == 0 and item_kitchen_brownie == 0:
                    room = 10
                    scene = 0
                    break
                elif x == "внутрь" and item_kitchen_applepie == 1 or item_kitchen_carrotcake == 1 or item_kitchen_brownie == 1:
                    room = 10
                    scene = 11
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 12 and scene == 0 and item_chisel == 0:
            print("Вы обходите фонтан и видите открывшуюся в нём выемку. Внутри неё вы видите только каменную табличку с какой-то надписью и зубило.")
            x = input("Вы можете прочитать (надпись) на табличке, взять (зубило), либо Вы можете (отойти) от фонтана.\n").lower()
            while True:
                if x == "отойти":
                    room = 11
                    scene = 0
                    break
                elif x == "надпись":
                    print("Вы подходите ближе к табличке и рассматриваете её.")
                    print("Часть текста написана на языке который вы не понимаете и выглядит древней.")
                    print("Другая же часть текста была вырезана совсем недавно.")
                    room = 12
                    scene = 1
                    break
                elif x == "зубило":
                    print("Вы подбираете зубило. Может пригодиться.")
                    item_chisel = 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 12 and scene == 0 and item_chisel == 1:
            print("Вы обходите фонтан и видите открывшуюся в нём выемку. Внутри неё вы видите только каменную табличку с какой-то надписью и зубило.")
            x = input("Вы можете прочитать (надпись) на табличке, либо (отойти) от фонтана.\n").lower()
            while True:
                if x == "отойти":
                    room = 11
                    scene = 0
                    break
                elif x == "надпись":
                    print("Вы подходите ближе к табличке и рассматриваете её.")
                    print("Часть текста написана на языке который вы не понимаете и выглядит древней.")
                    print("Другая же часть текста была вырезана совсем недавно.")
                    room = 12
                    scene = 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 12 and scene == 1:
            print("Текст на табличке:")
            color_green('"Мне удалось убедить их, что я тоже клон"')
            color_green('"Я не знаю как долго я смогу продержаться"')
            color_green('"Чтобы не вызывать подозрений я их задабриваю"')
            color_green('"Они все выглядят как я, но чем-то всё равно отличаются"')
            color_green('"Стражник на воротах обожает деньги и тюльпаны"')
            color_green('"Мечник готов продать почку за морковный торт"')
            color_green('"Лучник до ненормальной степени любит стиральный порошок"')
            color_green('"Я не спрашиваю что он с ним делает"')
            color_green('"Пока что предпочту отсидеться вне усадьбы"')
            color_green('"Мало ли кого мы пропустили при зачистке"')
            color_green('"Буду потихоньку готовить план отступления"')
            color_green('"Может смастерю лодку на озере, да уплыву"')
            color_green('"Надеюсь эта памятка поможет мне в будущем"')
            color_green('"Главное не растерять монеты"')
            if knowledge != 1:
                color_blue("*Вы получаете знание!*")
            knowledge = 1
            x = input("Вы можете (отойти) от таблички.\n").lower()
            while True:
                if x == "отойти":
                    room = 12
                    scene = 0
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 0:
            print("У вас в груди появляется ощущение, что если Вы пройдёте через это ворота, то обратно вернуться уже не получится.")
            x = input("Вы можете (отойти) от ворот, либо двигаться (вперёд).\n").lower()
            while True:
                if x == "отойти":
                    room = 11
                    scene = 0
                    break
                if x == "вперёд":
                    print("Чтож, была не была.")
                    print("Вы делаете шаг вперёд и перестуаете через ворота, покидая усадьбу.")
                    room = 13
                    scene = 1
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 1:
            color_yellow('"Кто это тут у нас?"')
            print("Вы оборачиваетесь и видите человека, с лицом идентичным вашему.")
            print("Вы не успеваете обронить и слова, как он закрывает ворота с громким щелчком.")
            print("Человек хватается за арбалет, висящий у него на поясе и направляет его на Вас.")
            color_yellow('"ГОВОРИ!"')
            x = input("Вы можете (поговорить) с ним, (напасть) на него, либо попытаться (сбежать).\n").lower()
            while True:
                if x == "сбежать":
                    print("Как только вы разворачиваете и начинаете бежать, вы слышите щелчок.")
                    color_yellow('"Не так быстро."')
                    print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                    print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                    color_yellow('"Надо доложить в лагерь..."')
                    print("В Ваших глазах темнеет. В последний раз вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                    color_red("Вас застрелили.")
                    replay()
                elif x == "напасть":
                    print("Вы начинаете двигаться в сторону арбалетчика.")
                    room = 13
                    scene = 2
                    break
                elif x == "поговорить":
                    print("Вы поднимаете руки и начинаете говорить.")
                    room = 13
                    scene = 3
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 2 and (item_potion_blue == 1 or item_potion_green == 1 or item_potion_red == 1):
            print("Что бы вы хотели сделать?")
            x = input("Вы можете (наброситься) на него, либо использовать (зелье).\n").lower()
            while True:
                if x == "наброситься":
                    print("Как только вы начинаете бежать на арбалетчика, вы слышите щелчок.")
                    color_yellow('"Не так быстро."')
                    print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                    print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                    color_yellow('"Надо доложить в лагерь..."')
                    print("В Ваших глазах темнеет. В последний раз вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                    color_red("Вас застрелили.")
                    replay()
                elif x == "зелье":
                    print("Как только вы начинаете тянуться за бутылкой, вы слышите щелчок.")
                    color_yellow('"Не так быстро."')
                    print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                    print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                    color_yellow('"Надо доложить в лагерь..."')
                    print("В Ваших глазах темнеет. В последний раз вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                    color_red("Вас застрелили.")
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 2 and item_potion_blue != 1 and item_potion_green != 1 and item_potion_red != 1:
            print("Что бы вы хотели сделать?")
            x = input("Вы можете (наброситься) на него.\n").lower()
            while True:
                if x == "наброситься":
                    print("Как только вы начинаете бежать на арбалетчика, вы слышите щелчок.")
                    color_yellow('"Не так быстро."')
                    print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                    print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                    color_yellow('"Надо доложить в лагерь..."')
                    print("В Ваших глазах темнеет. В последний раз вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                    color_red("Вас застрелили.")
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 3 and (item_coins > 0 or (item_kitchen_brownie == 1 or item_kitchen_carrotcake == 1 or item_kitchen_applepie == 1) or (item_flower_tulip == 1 or item_flower_rose == 1 or item_flower_peony == 1) or (item_cleaning_soap == 1 or item_cleaning_liquid == 1 or item_cleaning_powder == 1)):
            print("Что бы вы хотели сделать?")
            x = input("Вы можете (заговорить) с ним, либо попытаться его (подкупить).\n").lower()
            while True:
                if x == "заговорить":
                    print("Вы начинаете объяснять ему свою ситуацию.")
                    print("Он не тронут.")
                    color_yellow('"Откуда мне знать что ты не этот психопат?"')
                    if knowledge == 1:
                        room = 13
                        scene = 31
                        break
                    else:
                        print("Вы пытаетесь достучаться до него, но он вас не слушает.")
                        print("Вы чувствуете как с каждым вашим словом его раздражение растёт.")
                        color_yellow('"Хорошая попытка"')
                        print("Вы слышите щелчок.")
                        print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                        print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                        color_yellow('"Надо доложить в лагерь..."')
                        print("В Ваших глазах темнеет. В последний раз Вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                        color_red("Вас застрелили.")
                        replay()
                elif x == "подкупить":
                    room = 13
                    scene = 32
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 3 and (item_coins == 0 and item_kitchen_brownie != 1 and item_kitchen_carrotcake != 1 and item_kitchen_applepie != 1):
            print("Что бы вы хотели сделать?")
            x = input("Вы можете (заговорить) с ним.\n").lower()
            while True:
                if x == "заговорить":
                    print("Вы начинаете объяснять ему свою ситуацию.")
                    print("Он не тронут.")
                    color_yellow('"Откуда мне знать что ты не этот психопат?"')
                    if knowledge == 1:
                        room = 13
                        scene = 31
                        break
                    else:
                        print("Вы пытаетесь достучаться до него, но он вас не слушает.")
                        print("Вы чувствуете как с каждым вашим словом его раздражение растёт.")
                        color_yellow('"Хорошая попытка"')
                        print("Вы слышите щелчок.")
                        print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                        print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                        color_yellow('"Надо доложить в лагерь..."')
                        print("В Ваших глазах темнеет. В последний раз Вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                        color_red("Вас застрелили.")
                        replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 31:
            print("Вы объясняете ему то, что видели на табличке, и говорите как до неё добраться.")
            color_yellow('"Не двигайся!"')
            print("Он открывает ворота одной рукой, всё ещё направляя на вас арбалет второй, затем заходит в усадьбу и закрывает ворота за собой.")
            color_yellow('"Стой здесь."')
            print("Вы ожидаете возвращения арбалетчика.")
            print("Через пару минут он уже бежит к воротам, больше не целясь в Вас арбалетом.")
            color_yellow('"Этот урод..."')
            color_yellow('"Тебе надо предупредить остальных, иди к лагерю, дальше по тропинке."')
            color_yellow('"Вот, возьми мой щит, скажи им, что нас обвели вокруг пальца, я поищу что-нибудь полезное и вернусь к вам."')
            color_blue("*Вы получаете щит!*")
            item_shield = 1
            print("Вы киваете ему в ответ и начинаете двигаться глубже в лес.")
            room = 14
            scene = 0
        elif room == 13 and scene == 32:
            print("Вы говорите ему, что у вас что-то для него есть.")
            color_yellow('"Без резких движений!"')
            if (item_kitchen_applepie == 1 or item_kitchen_brownie == 1 or item_kitchen_carrotcake == 1) or (item_flower_tulip == 1 or item_flower_rose == 1 or item_flower_peony == 1) or (item_cleaning_soap == 1 or item_cleaning_powder == 1 or item_cleaning_liquid == 1) and item_coins > 0:
                x = input("Вы можете предложить ему что-нибудь из своих (вещей), либо (денег).\n").lower()
                while True:
                    if x == "вещей":
                        room = 13
                        scene = 33
                        break
                    if x == "денег":
                        room = 13
                        scene = 34
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif (item_kitchen_applepie == 1 or item_kitchen_brownie == 1 or item_kitchen_carrotcake == 1) or (item_flower_tulip == 1 or item_flower_rose == 1 or item_flower_peony == 1) or (item_cleaning_soap == 1 or item_cleaning_powder == 1 or item_cleaning_liquid == 1) and item_coins < 1:
                x = input("Вы можете предложить ему что-нибудь из своих (вещей).\n").lower()
                while True:
                    if x == "вещей":
                        room = 13
                        scene = 33
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif (item_kitchen_applepie != 1 and item_kitchen_brownie != 1 and item_kitchen_carrotcake != 1) and (item_flower_tulip != 1 and item_flower_rose != 1 and item_flower_peony != 1) and (item_cleaning_soap != 1 and item_cleaning_powder != 1 and item_cleaning_liquid != 1) and item_coins > 0:
                x = input("Вы можете предложить ему (денег).\n").lower()
                while True:
                    if x == "денег":
                        room = 13
                        scene = 34
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 13 and scene == 33:
            print("Вы показываете ему, всё что у Вас есть с собой.")
            if item_flower_tulip == 1:
                print("Он медленно просматривает Ваши вещи с дистанции, с отвращением в глазах.")
                print("Пока его взгляд не падает на букет роз.")
                color_yellow('"Дай ка мне вот это."')
                print("Вы, будучи на прицеле заряженного арбалета, вы с радость избавляетесь от цветов.")
                color_blue("*Вы теряете букет тюльпанов!*")
                color_yellow('"Вали отсюда, пока я не передумал."')
                print("Без лишних раздумий, Вы продолжаете путь глубже в лес.")
                room = 14
                scene = 0
            elif item_flower_tulip != 1:
                print("Он медленно просматривает Ваши вещи с дистанции, с отвращением в глазах.")
                color_yellow('"У меня нет на это времени."')
                print("Вы слышите щелчок.")
                print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                color_yellow('"Надо доложить в лагерь..."')
                print("В Ваших глазах темнеет. В последний раз Вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                color_red("*Вас застрелили!*")
                replay()
        elif room == 13 and scene == 34:
            print("Вы подкидываете в воздух золотую монету.")
            print("Его глаза загораются первобытной жадностью.")
            color_yellow('"Выворачивай карманы!"')
            if item_coins == 3:
                print("Будучи на прицеле, Вы протягиваете ему все свои сбережения.")
                color_yellow('"Приятно иметь с вами дело."')
                color_blue("*Вы теряете все свои монеты!*")
                item_coins = 0
                color_yellow('"Вот, равноценный обмен."')
                print("Он бросает в Вашу сторону свой щит.")
                color_blue("*Вы получаете щит!*")
                item_shield = 1
                color_yellow('"Теперь убирайся отсюда."')
                print("Без лишних раздумий, Вы продолжаете путь глубже в лес.")
                room = 14
                scene = 0
            elif item_coins == 2:
                print("Будучи на прицеле, Вы протягиваете ему все свои сбережения.")
                color_yellow('"Не густо."')
                color_blue("*Вы теряете все свои монеты!*")
                item_coins = 0
                color_yellow('"Теперь убирайся отсюда."')
                print("Без лишних раздумий, Вы продолжаете путь глубже в лес.")
                room = 14
                scene = 0
            elif item_coins == 1:
                print("Будучи на прицеле, Вы протягиваете ему все свои сбережения.")
                color_yellow('"Ты меня разочаровываешь."')
                color_blue("*Вы теряете все свои монеты!*")
                print("Вы слышите щелчок.")
                print("Вы чувствуете резкую боль в районе спины и живота, прямо под рёбрами.")
                print("Опуская взгляд, Вы видите как багровое пятно начинает расползаться по ващей одежде.")
                color_yellow('"Надо доложить в лагерь..."')
                print("В Ваших глазах темнеет. В последний раз Вы бросаете взгляд на лесные просторы, расстилающиеся перед вами.")
                color_red("Вас застрелили.")
                replay()
        elif room == 14 and scene == 0:
            print("Быстрым шагом двигаясь по тропинке Вы вскоре натыкаетесь на лагерь.")
            print("Столп дыма лениво поднимается из еле горящего костерка.")
            print("Вокруг него сидят два человека. Заметив Вас, они тут же переворят на Вас всё своё внимание, занимая боевые позиции.")
            print("Вы замечаете у одного из них лук и стрелы, у второго длинный меч на готове.")
            print("Вы также замечаете, что их лица идентичны вашему.")
            print("Первым к вам обращается мечник, пока лучник натягивает тетеву.")
            color_cyan('"Ни шагу вперёд! Стой где стоишь."')
            if item_shield == 1:
                color_magenta('"И откуда у тебя этот щит?"')
            x = input("Вы можете попытаться с ними (поговорить) или (напасть).\n").lower()
            while True:
                if x == "поговорить":
                    room = 14
                    scene = 1
                    break
                if x == "напасть":
                    room = 14
                    scene = 22
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 14 and scene == 22:
            print("Как только Вы совершаете малейшее агрессивное движение, мечник сразу же делает шаг в сторону.")
            print("Вы на мгновение чувствуете резкую колющую боль, а затем падаете на землю, со стрелой в одной из глазниц.")
            color_cyan('"Надо было сначала допросить бедолагу."')
            color_magenta('"Ты знаешь, что мы не можем рисковать."')
            print("Всё темнеет.")
            color_red("*Вы лишились глаза! И жизни!*")
            replay()
        elif room == 14 and scene == 1:
            print("Вы поднимаете руки и начинаете говорить.")
            if knowledge == 1:
                print("Вы объясняете им что произошло, как Вы здесь оказались.")
                print("Вы рассказываете им про табличку и про то как их друг отдал Вам свой щит.")
                print("Вы видите на их лице недоверие, как вдруг из кустов неподолёку выбегает арбалетчик.")
                color_yellow('"Как я погляжу вы уже знакомы. Пойдёмте, нам надо застать этого психа врасплох."')
                print("Лучник и мечник переглядываются.")
                color_cyan('"Чтож, мы знаем, что их не может быть двое."')
                color_magenta('"Хорошо, но новенький идёт первым. Он пошёл к озеру."')
                print("Арбалетчик кивает и начинает двигаться в неизвестном Вам направлении.")
                color_magenta('"Давай, за ним."')
                print("Лучник подталкивает Вас в спину, и вы все следуете за арбалетчиком.")
                x = input("(продолжить).\n").lower()
                while True:
                    if x == "продолжить":
                        room = 15
                        scene = 10
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            if knowledge == 0:
                print("Вы объясняете им что произошло, как Вы здесь оказались.")
                print("Вы видите на их лице недоверие и растущее напряжение.")
                print("Вам срочно нужно что-то сделать.")
                x = input("Вы можете попытаться их (подкупить), либо (молить) о пощаде.\n").lower()
                while True:
                    if x == "молить":
                        print("Вы падаете на колени и начинаете упрашивать их пощадить Вас.")
                        print("К сожалению, это лишь усиливает их недоверие.")
                        color_cyan('"Даже жалко как-то становится."')
                        color_magenta('"Никакой пощады."')
                        print("Мечник делает один широкий шаг и размашистый удар в Вашу сторону.")
                        print("Всё темнеет.")
                        color_red("*Вы лишились головы! И жизни!*")
                        replay()
                    elif x == "подкупить":
                        print("Вы предлагаете им взять у Вас всё что они хотят в обмен на свою жизнь.")
                        color_cyan('"Без резких движений."')
                        room = 14
                        scene = 2
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 14 and scene == 2:
            print("Вы показываете им, всё что у Вас есть с собой.")
            if item_kitchen_carrotcake == 1 and item_cleaning_powder == 1:
                print("Мечник увидев морковный торт отталкивает Вас в сторону и начинает в него вгрызаться.")
                print("Лучник подходит ближе и его глаза загораются когда он видит маленький холщёвый мешочек.")
                color_magenta('"Это стиральный порошок???"')
                print("Вы киваете. Лучник выхватывает мешочек и отходит на безопасное растояние.")
                color_magenta('"Ты можешь идти. Только не возвращайся!"')
                print("Глубоко вздохнув, Вы продолжаете бежать в неизвестном направлении.")
                room = 15
                scene = 0
            elif item_kitchen_carrotcake != 1 and item_cleaning_powder == 1:
                print("Мечник без интереса оглядывает Ваши пожитки.")
                color_cyan('"И это всё?"')
                print("Вы киваете. Не успевает Ваша голова вернуться в изначальное положение, как Вы чувствуете холодную сталь у себя меж рёбер.")
                color_cyan('"Жаль."')
                print("Мечник отворачивается.")
                color_cyan('"Иди проверь ты, может найдёшь что для себя."')
                print("Вы слышите приближающиеся шаги.")
                color_magenta('"Это стиральный порошок???"')
                print("Всё темнеет.")
                color_red("*Вы истекли кровью!*")
                replay()
            elif item_kitchen_carrotcake == 1 and item_cleaning_powder != 1:
                print("Мечник увидев морковный торт отталкивает Вас в сторону и начинает в него вгрызаться.")
                print("Лучник подходит ближе, но не выглядит таким заинтересованным.")
                color_magenta('"И это всё?"')
                print("Вы киваете. Не успевает Ваша голова вернуться в изначальное положение, как Вы чувствуете стрелу у себя меж рёбер.")
                color_magenta('"Пустая трата времени."')
                print("Всё темнеет.")
                color_red("*Вы истекли кровью!*")
                replay()
            elif item_kitchen_carrotcake != 1 and item_cleaning_powder != 1:
                print("Мечник без интереса оглядывает Ваши пожитки.")
                color_cyan('"И это всё?"')
                print("Вы киваете. Не успевает Ваша голова вернуться в изначальное положение, как Вы чувствуете холодную сталь у себя меж рёбер.")
                color_cyan('"Жаль."')
                print("Мечник отворачивается.")
                color_cyan('"Иди проверь ты, может найдёшь что для себя."')
                print("Вы слышите приближающиеся шаги.")
                color_magenta('"Нет, пустая трата времени."')
                print("Всё темнеет.")
                color_red("*Вы истекли кровью!*")
                replay()
        elif room == 15 and scene == 0:
            print("Пробираясь через дебри, Вы вскоре выходите к озеру.")
            print("Там Вы видите ещё одну фигуру, стоящую у пришвартованного плота, загружающую на него вещи.")
            print("Заметив Ваше присутствие фигура поворачивается.")
            color_green('"Ещё один? Чтож, слишком позно, ты меня не остановишь."')
            print("Солнечный луч падает на лицо говорящего. Оно идентично Вашему.")
            x = input("Вы можете (напасть) на  него, либо попытаться (поговорить).\n").lower()
            while True:
                if x == "напасть":
                    room = 15
                    scene = 1
                    break
                elif x == "поговорить":
                    print("Вы поднимаете свои руки к небу и начинаете медленно двигаться вперёд, пытаясь завести беседу.")
                    color_green('"Знаешь что отличает меня от моих клонов..."')
                    color_green('"... от тебя?"')
                    color_green('"Они могут быть безжалостными, но только когда не получают то что хотят."')
                    print("Вы чувствуете что-то неладное.")
                    color_green('"Я могу быть безжалостным просто так."')
                    print("Вы видите как эта фигура достаёт из за спины арбалет и стреляет в Вашу сторону.")
                    color_green('"По тебе не будут скучать."')
                    print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                    print("Всё темнеет.")
                    color_red("*Вы почти выбрались!*")
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 15 and scene == 1:
            print("Вы срываетесь с места и устремляетесь в сторону говорящего.")
            print("Вы видите как он дёргает за какую-то верёвочку и из соседних кустов вылетает залп из нескольких сотен стрел.")
            color_green('"Я ожидал, что это может произойти."')
            if item_potion_green == 1:
                x = input("Вы можете выпить (зелье) или попытаться (увернуться).\n").lower()
                while True:
                    if x == "зелье":
                        room = 15
                        scene = 2
                        break
                    elif x == "увернуться":
                        print("Вы пытаетесь уклониться от града стрел.")
                        print("По началу всё идёт неплохо, но вскоре Вы чувствуете резкую боль в своём колене и падаете на землю.")
                        print("Не проходит и секунды как ещё одна стрела впивается Вам в плечо, затем в шею.")
                        color_green('"По тебе не будут скучать."')
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif item_shield == 1:
                x = input("Вы можете (прикрыться) щитом или попытаться (увернуться).\n").lower()
                while True:
                    if x == "прикрыться":
                        room = 15
                        scene = 3
                        break
                    elif x == "увернуться":
                        print("Вы пытаетесь уклониться от града стрел.")
                        print("По началу всё идёт неплохо, но вскоре Вы чувствуете резкую боль в своём колене и падаете на землю.")
                        print("Не проходит и секунды как ещё одна стрела впивается Вам в плечо, затем в шею.")
                        color_green('"По тебе не будут скучать."')
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 15 and scene == 2:
            print("Вы выхватываете склянку с зелёным эликсиром и выпиваете её.")
            print("Вы ощущаете как ваша кожа начинает твердеть и становиться сероватого оттенка.")
            print("Вы всё ещё можете двигаться, хоть это и значительно сложнее.")
            print("Пара стрел ударяет по Вам, затем ещё десяток и все отскакивают.")
            color_green('"КАКОГО ЧЁРТА?!"')
            print("Вы начинаете бежать в сторону голоса.")
            if item_metal_pipe == 1:
                x = input("Вы можете попытаться (наброситься) на фигуру или достать (железяку).\n").lower()
                while True:
                    if x == "наброситься":
                        print("Вы чувствуете как эффект зелья начинает заканчиваться.")
                        print("Собрав все силы в кулак Вы бросаетесь на свою цель.")
                        color_green('"Ну уж нет!"')
                        print("Вы видите как эта фигура достаёт из за спины арбалет и стреляет в Вашу сторону.")
                        color_green('"По тебе не будут скучать."')
                        print("Вы падаете на землю в метре от неё.")
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
                        break
                    elif x == "железяку":
                        room = 15
                        scene = 4
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            elif item_metal_pipe == 0:
                x = input("Вы можете попытаться (наброситься) на фигуру.\n").lower()
                while True:
                    if x == "наброситься":
                        print("Вы чувствуете как эффект зелья начинает заканчиваться.")
                        print("Собрав все силы в кулак Вы бросаетесь на свою цель.")
                        color_green('"Ну уж нет!"')
                        print("Вы видите как эта фигура достаёт из за спины арбалет и стреляет в Вашу сторону.")
                        color_green('"По тебе не будут скучать."')
                        print("Вы падаете на землю в метре от неё.")
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 15 and scene == 3:
            print("Вы выхватываете щит и поднимаете его у себя над головой, начиная бежать в сторону фигуры.")
            print("Вы видите как небо темнеет от количества стрел, летящих в Вашем направлении.")
            print("Пара стрел ударяет по щиту, затем ещё десяток и все отскакивают.")
            color_green('"КАКОГО ЧЁРТА?!"')
            print("Вы начинаете бежать в сторону голоса.")
            x = input("Вы можете попытаться (наброситься) на фигуру.\n").lower()
            while True:
                if x == "наброситься":
                    print("Собрав все силы в кулак Вы бросаетесь на свою цель.")
                    color_green('"Ну уж нет!"')
                    print("Вы видите как эта фигура достаёт из за спины арбалет и стреляет в Вашу сторону.")
                    color_green('"По тебе не будут скучать."')
                    print("Вы видите это и пытаетесь прикрыться щитом, но не успеваете.")
                    print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                    print("Всё темнеет.")
                    color_red("*Вы почти выбрались!*")
                    replay()
                    break
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 15 and scene == 4:
            print("Вы чувствуете как эффект зелья начинает заканчиваться.")
            print("Вы выхватываете железную трубу.")
            print("Собрав все силы в кулак Вы бросаетесь на свою цель.")
            color_green('"Ну уж нет!"')
            print("Вы видите как эта фигура достаёт из за спины арбалет, но Вы успеваете выбить его у неё из рук.")
            color_green('"Подожди, давай договоримся, я могу..."')
            print("Вы с размаха ударяете её трубой по челюсти и она без сознания падает на землю.")
            print("Вы берёте тело под плечи и сбрасываете в озеро.")
            x = input("Вы можете забраться на (плот) и уплыть.\n").lower()
            while True:
                if x == "плот":
                    print(Style.BRIGHT + "Вы свободны!" + Style.RESET_ALL)
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")
        elif room == 15 and scene == 10:
            print("Пробираясь через дебри, Ваша группа вскоре выходит к озеру.")
            print("Там Вы видите ещё одну фигуру, стоящую у пришвартованного плота, загружающую на него вещи.")
            print("Заметив Ваше присутствие фигура поворачивается.")
            color_green('"Что вы здесь делаете? Я сказал вам ждать в лагере."')
            color_yellow('"Закрой пасть, мы всё знаем!"')
            color_magenta('"Он и вправду пытается сбежать!"')
            color_cyan('"От нас всех ты не уйдёшь!"')
            color_green('"Вот оно как значит? Чтож, ладно, ваши похороны."')
            print("Солнечный луч падает на лицо говорящего. Оно идентично Вашему.")
            print("Вы видите как он дёргает за какую-то верёвочку и из соседних кустов вылетает залп из нескольких сотен стрел.")
            color_green('"Я ожидал, что это может произойти."')
            if item_shield == 1:
                x = input("Вы можете (прикрыться) щитом или попытаться (увернуться).\n").lower()
                while True:
                    if x == "прикрыться":
                        room = 15
                        scene = 11
                        break
                    elif x == "увернуться":
                        print("Вы пытаетесь уклониться от града стрел.")
                        print("По началу всё идёт неплохо, но вскоре Вы чувствуете резкую боль в своём колене и падаете на землю.")
                        print("Не проходит и секунды как ещё одна стрела впивается Вам в плечо, затем в шею.")
                        print("Лёжа на земле, Вы видите рядом с собой тело арбалетчика, лучника и мечника, нашпигованные стрелами.")
                        color_green('"По вам не будут скучать."')
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
        elif room == 15 and scene == 11:
            print("Вы выхватываете щит и поднимаете его у себя над головой, начиная бежать в сторону фигуры.")
            print("Вы видите как небо темнеет от количества стрел, летящих в Вашем направлении.")
            print("Оглядываясь по сторонам вы видите как одно за другим падают тела арбалетчика, лучника и мечника, нашпигованные стрелами.")
            print("Пара стрел ударяет по щиту, затем ещё десяток и все отскакивают.")
            color_green('"КАКОГО ЧЁРТА?!"')
            print("Вы начинаете бежать в сторону голоса.")
            if item_chisel == 1:
                x = input("Вы можете попытаться (наброситься) на фигуру или достать (зубило).\n").lower()
                while True:
                    if x == "наброситься":
                        print("Собрав все силы в кулак Вы бросаетесь на свою цель.")
                        color_green('"Ну уж нет!"')
                        print("Вы видите как эта фигура достаёт из за спины арбалет и стреляет в Вашу сторону.")
                        color_green('"По тебе не будут скучать."')
                        print("Вы видите это и пытаетесь прикрыться щитом, но не успеваете.")
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
                    elif x == "зубило":
                        room = 15
                        scene = 12
                        break
                    else:
                        print("Ошибка ввода. Попробуйте снова.")
            if item_chisel == 0:
                x = input("Вы можете попытаться (наброситься).\n").lower()
                while True:
                    if x == "наброситься":
                        print("Собрав все силы в кулак Вы бросаетесь на свою цель.")
                        color_green('"Ну уж нет!"')
                        print("Вы видите как эта фигура достаёт из за спины арбалет и стреляет в Вашу сторону.")
                        color_green('"По тебе не будут скучать."')
                        print("Вы видите это и пытаетесь прикрыться щитом, но не успеваете.")
                        print("Вы видите как фигура забирается на плот и отталкивается от берега.")
                        print("Всё темнеет.")
                        color_red("*Вы почти выбрались!*")
                        replay()
        elif room == 15 and scene == 12:
            print("Вы выхватываете зубило и, собрав все силы в кулак, бросаетесь на свою цель.")
            color_green('"Ну уж нет!"')
            print("Вы видите как эта фигура достаёт из за спины арбалет, но вы швыряете зубило прямо ей в руку.")
            print("Фигура кричит и хватается за раненую руку второй. Вы подбегаете.")
            color_green('"Подожди, давай договоримся, я могу..."')
            print("Вы с размаха ударяете её щитом по челюсти и она без сознания падает на землю.")
            print("Вы берёте тело под плечи и сбрасываете в озеро.")
            print("Вы осматриваете поле боя. Выживших не осталось.")
            x = input("Вы можете забраться на (плот) и уплыть.\n").lower()
            while True:
                if x == "плот":
                    print(Style.BRIGHT + "Вы свободны!" + Style.RESET_ALL)
                    replay()
                else:
                    print("Ошибка ввода. Попробуйте снова.")


game()
