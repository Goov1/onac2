# made by Goov.
# ver 1.1 FIX RELEASE.
import random
import time
import sys

i = 0
ldoor = "open"
rdoor = "open"
ven = "open"
energy = 4
camw = 4

print("-----ONAC 2-----")
print("-----START (s)-----")
print("----HELP (h)-----")
a = input("~1: ")
if a == "s" or a == "S":
    rand1 = random.randint(1, 2)
    camb = 1
    print("* Звуки хорошего котячего сна *")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")
    camw = 3
    print("Мяяу!")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")

    if ven == "open":
        print("- Игра проигранна. На вас напал чёрный кот с вентиляции. -")
        sys.exit()
    elif ven == "close":
        print("+ Вы отбились от атаки с вентиляции. +")
        ldoor = "open"
        rdoor = "open"
        ven = "open"
        print("+ Все двери с вентиляцией открылись. +")

    camb = 0
    camw = 3
    print("Мяяу!")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")
    camw = 2
    print("* Шорох корма *")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")
    camw = 1
    print("Привет?...")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")

    if rand1 == 1:
        if ldoor == "open":
            print("- Игра проигранна. На вас напал белый кот слева.")
            sys.exit()
        elif ldoor == "close":
            print("+ Вы отбились от атаки слева. +")
            ldoor = "open"
            rdoor = "open"
            ven = "open"
            print("+ Все двери с вентиляцией открылись. +")
    if rand1 == 2:
        if rdoor == "open":
            print("- Игра проигранна. На вас напал белый кот справа.")
            sys.exit()
        elif rdoor == "close":
            print("+ Вы отбились от атаки справа. +")
            ldoor = "open"
            rdoor = "open"
            ven = "open"
            print("+ Все двери с вентиляцией открылись. +")

    camw = 4
    camb = 1
    print("Два на одного не чесно!...")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")
    camw = 3
    print("* Звуки близкого сна *")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")

    if ven == "open":
        print("- Игра проигранна. На вас напал чёрный кот с вентиляции. -")
    elif ven == "close":
        print("+ Вы отбились от атаки с вентиляции. +")
        ldoor = "open"
        rdoor = "open"
        ven = "open"
        print("+ Все двери с вентиляцией открылись. +")

    camw = 2
    print("МЯЯУ!")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")
    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")
    camw = 1
    print("Опять?...")
    b = input("~1: ")
    if b == "lo" or b == "Lo":
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    if b == "ro" or b == "Ro":
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    if b == "veno" or b == "Veno":
        ven = "open"
        print("+ Вентиляция открылась. +")
    if b == "vens" or b == "Vens":
        if camb == 1:
            print("+ Чёрный кот у вас в вентиляции! +")
        elif camb == 0:
            print("+ Чёрного кота не найденно в вентиляции. +")
    if b == "lc" or b == "Lc":
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    if b == "rc" or b == "Rc":
        door = "close"
        print("+ Правая дверь закрылась. +")
    if b == "venc" or b == "Venc":
        ven = "close"
        print("+ Вентиляция закрылась. +")
    if energy <= 0:
        print("- У вас закончилась енергия. Вы проиграли. -")
        sys.exit()
    if b == "cupoftea" or b == "Cupoftea":
        if camb == 1:
            print("- Чёрный кот у вас в вентиляции! -")
        elif camb == 0:
            print("- Чёрного кота не найденно в вентиляции. -")
        if rand1 == 1:
            print("- Белый кот будет идти с левой стороны. -")
        elif rand1 == 2:
            print("- Белый кот будет идти с правой стороны. -")
    if b == "cam" or b == "Cam":
        print("+ Белый кот на " + str(camw) + " камер от вас. +")

    if ldoor == "close" or rdoor == "close" or ven == "close":
        energy -= 1
        print("- Утрата енергии! У вас осталось " + str(energy) + " енергии. -")
    if rand1 == 1:
        if ldoor == "open":
            print("- Игра проигранна. На вас напал белый кот слева.")
            sys.exit()
        elif ldoor == "close":
            print("+ Вы отбились от атаки слева. +")
            ldoor = "open"
            rdoor = "open"
            ven = "open"
            print("+ Все двери с вентиляцией открылись. +")
    if rand1 == 2:
        if rdoor == "open":
            print("- Игра проигранна. На вас напал белый кот справа.")
            sys.exit()
        elif rdoor == "close":
            print("+ Вы отбились от атаки справа. +")
            ldoor = "open"
            rdoor = "open"
            ven = "open"
            print("+ Все двери с вентиляцией открылись. +")

    print("6 УТРА")
    print("+ Вы прошли onac 2! +")
    print("+ Субтитров не будет, всё зделал Goov ;) +")

    
        
elif a == "h" or a == "H":
    print("-----КОМАНДЫ-----")
    print("1. lo-открыть левую дверь.")
    print("2. ro-открыть правую дверь.")
    print("3. veno-открыть вентиляцию.")
    print("4. vens-есть ли в вентиляции кот.")
    print("5. lc-закрыть левую дверь.")
    print("6. rc-закрыть правую дверь.")
    print("7. venc-закрыть вентиляцию.")
    print("8. cam-на сколько камер от вас белый кот.")
    print("Перезапустите игру.")