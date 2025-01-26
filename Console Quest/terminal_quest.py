from art import tprint
from rich.console import Console
import time
import os
import dumb_menu
import random

step = 0


green_num = random.randint(10, 99)
green_string = str(green_num)
blue_num = random.randint(10, 99)
blue_string = str(blue_num)

console = Console(width=90)


def info():
    tprint("The Console Quest")  # название игры
    console.print(
        'Добро пожаловать в [bold yellow]"The Console Quest"[/]!', justify="center"
    )
    time.sleep(5)
    console.print(
        "Вам предстоит выбраться из ловушки, используя лишь ваше воображение и ввод текста с клавиатуры.",
        justify="center",
    )
    time.sleep(5)
    console.print(
        'В игре три концовки. Если вы застряли, используйте команду [bold red]"HELP"[/].',
        justify="center",
    )
    time.sleep(5)
    console.print(
        "Удачного прохождения!",
        justify="center",
    )


def clear():
    print("\033[H\033[J", end="")
    time.sleep(2)


def game():
    # step = 1
    chest_opened = False
    key_taken = False
    cleaned = False
    reaction = ""

    if reaction == "":
        step = 1

    while step == 1:
        clear()
        console.print(
            "Вы проснулись в неизвестной комнате. Что вы будете делать? Подсказка: попробуйте 'осмотреться'.",
            justify="center",
        )
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
            console.print("Вы осмотрелись.", justify="center")
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)

    while step == 2:
        clear()
        console.print(
            "Вдоль северной стены стоит [bold yellow]шкаф[/]. Вдоль южной стены стоит [bold yellow]стол[/]. На восточной стене висит [bold yellow]картина[/]. В западной стене [bold yellow]дверь.[/]",
            justify="center",
        )
        reaction = input()
        if ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 3:
        clear()
        console.print(
            "Вы подошли к шкафу. В нём стоит запертый ящик.", justify="center"
        )
        reaction = input()
        if "ящик" in reaction and key_taken == False:
            step = 7
        if ("ящик" in reaction or "ключ" in reaction) and key_taken == True:
            step = 8
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 4:
        clear()
        console.print(
            "Вы подошли к столу. На нём лежит ключ и кружка.", justify="center"
        )
        reaction = input()
        if "ключ" in reaction:
            step = 9
        elif "переверн" in reaction:
            step = 14
        elif "кружк" in reaction:
            step = 10
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 5:
        clear()
        console.print(
            "Вы подошли к картине. Она весьма пыльна. На ней изображён какой-то человек.",
            justify="center",
        )
        reaction = input()
        if "пыль" in reaction:
            step = 12
        elif "переверн" in reaction:
            step = 15
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 6:
        clear()
        console.print(
            "Вы подошли к двери. Выглядит прочной. На ней висит [bold yellow]кодовый замок[/].",
            justify="center",
        )
        reaction = input()
        if "код" in reaction or "набрать" in reaction or "ввести" in reaction:
            step = 13
        elif (reaction == "осмотреться") or ("вокруг" in reaction):
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 7:
        clear()
        console.print(
            "Вы пытаетесь открыть ящик, но вам мешает [bold yellow]замок[/].",
            justify="center",
        )
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 8:
        clear()
        console.print(
            "Вы открываете ящик, внутри записка: «Нередко, обратная сторона вещей сокрывает в себе истину.»",
            justify="center",
        )
        chest_opened = True
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 9:
        clear()
        console.print("Вы берёте ключ.", justify="center")
        key_taken = True
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 10:
        clear()
        console.print(
            "Зеленая кружка с ромашками. Ничего примечательного.", justify="center"
        )
        reaction = input()
        if "переверн" in reaction:
            step = 14
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 11:
        clear()
        console.print("Вы подошли к столу. На нём стоит кружка.", justify="center")
        reaction = input()
        if "перевен" in reaction:
            step = 14
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 12:
        clear()
        console.print(
            "Теперь вы четко видете подпись портета синими чернилами: «Блез Паскаль, 1623-1662 гг.»",
            justify="center",
        )
        cleaned = True
        reaction = input()
        if "переверн" in reaction:
            step = 15
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 13:
        clear()
        console.print("Вы набираете код на замке:", justify="center")
        reaction = input()
        if reaction == blue_string + green_string:
            step = 16
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 14:
        clear()
        console.print(
            f"Вы переворачиваете кружку. На дне написан номер {green_string}",
            justify="center",
        )
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 15:
        clear()
        console.print(
            f"На задней стороне холста написан номер {blue_string}", justify="center"
        )
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif (
            ("стол" in reaction)
            or ("южн" in reaction)
            or ("юг" in reaction)
            and (key_taken == False)
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 16:
        clear()
        console.print("Дверь открылась. Вы смогли выбраться. Победа!", justify="center")
        time.sleep(10)
        exit()
    while step == 17:
        clear()
        console.print(
            "Вы подошли к шкафу. В нём стоит открытый ящик.", justify="center"
        )
        reaction = input()
        if ("ящик" in reaction or "ключ" in reaction) and key_taken == True:
            step = 18
        elif reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)
    while step == 18:
        clear()
        console.print(
            "Внутри ящика записка: «Нередко, обратная сторона вещей сокрывает в себе истину.»",
            justify="center",
        )
        reaction = input()
        if reaction == "осмотреться" or "вокруг" in reaction:
            step = 2
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == False):
            step = 3
        elif ("шкаф" in reaction or "север" in reaction) and (chest_opened == True):
            step = 17
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == False
        ):
            step = 4
        elif ("стол" in reaction or "южн" in reaction or "юг" in reaction) and (
            key_taken == True
        ):
            step = 11
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == False):
            step = 5
        elif (
            "картин" in reaction or "восточн" in reaction or "восток" in reaction
        ) and (cleaned == True):
            step = 12
        elif "двер" in reaction or "запад" in reaction:
            step = 6
        else:
            console.print(
                "Некорректное действие. Попробуйте другой запрос или перефразировать этот.",
                justify="center",
            )
            time.sleep(2)

    if reaction == "осмотреться" or "вокруг" in reaction:
        step = 2


options = ["Start the game", "Info", "Exit"]
index = dumb_menu.get_menu_choice(options, isclean=True)
os.system("cls")

match index:
    case 0:
        game()
    case 1:
        info()
    case 2:
        exit()
input("Press ENTER to continue...")
