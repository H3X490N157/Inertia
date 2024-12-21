from math import gcd

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


x = input("Расположение плоскости, относительно которой считаем моменты. Напишите 1, если для центра. Напишите 2 для края.В противном случае счёт выполняется для плоскости с выбранным расстоянием от края (в этом режиме вывод целой дроби недоступен): ")
m = float(input("Введите массу стержня в кг: "))
L = float(input("Введите длину стержня в м: "))
quantity = int(input("Введите целочисленную точность. Рекомендуемая - 1000 шагов. После 10000 скорость вычислений существенно падает: "))
if x == "1":
    for i in range(1, quantity + 1):
        ans = 0
        pivot = L / 2 / i  # положение центра масс первого фрагмента
        delta = L / i  # сдвиг, позволяющий перейти от центра масс одного фрагмента к другому
        center = L / 2 # позиция центра
        chislitel = 0
        znamenatel = 4 * i ** 3
        for j in range(0, i):
            ans += (m / i) * (pivot + j * delta - center) * (pivot + j * delta - center)
            chislitel += 4 * j * j + 4 * j + 1 - 4 * j * i - 2 * i + i * i
        true_chislitel, true_znamenatel = simplify_fraction(chislitel, znamenatel)
        print(f"Для шага номер {i} момент инерции для плоскости, проходящей через один из концов стержня, будет составлять: {true_chislitel}/{true_znamenatel}*ml^2, что эквивалентно {ans}")
elif x == "2":
    for i in range(1, quantity + 1):
        ans = 0
        pivot = L / 2 / i  # положение центра масс первого фрагмента
        delta = L / i  # сдвиг, позволяющий перейти от центра масс одного фрагмента к другому
        chislitel = 0
        znamenatel = 4 * i ** 3
        for j in range(0, i):
            ans += (m / i) * (pivot + j * delta) * (pivot + j * delta)
            chislitel += 1 + 4 * j + 4 * j * j
        true_chislitel, true_znamenatel = simplify_fraction(chislitel, znamenatel)
        print(f"Для шага номер {i} момент инерции для плоскости, проходящей через один из концов стержня, будет составлять: {true_chislitel}/{true_znamenatel}*ml^2, что эквивалентно {ans}")
else:
    z = float(input("Введите расстояние (в метрах) по оси кооридинат, параллельной стержню, от любого края стержня. Расстояние должно быть меньше или равно длине стержня: "))
    if (z > L):
        print("Некорректный ввод") # завершение программы при некорректном вводе
    else:
        for i in range(1, quantity + 1):
            ans = 0
            pivot = L / 2 / i  # положение центра масс первого фрагмента
            delta = L / i  # сдвиг, позволяющий перейти от центра масс одного фрагмента к другому
            for j in range(0, i):
                ans += (m / i) * (pivot + j * delta - z) * (pivot + j * delta - z)
            print(
                f"Для шага номер {i} момент инерции для плоскости, проходящей через один из концов стержня, будет составлять: {ans}")
