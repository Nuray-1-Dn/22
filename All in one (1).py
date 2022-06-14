def python_work():
    print("Python work!")


def num():
    num_ = 5
    print(num)


def comment():
    print("Comment me :)")
    # print("Comment me :)")


def number():
    number_ = 2
    print(number ** 3)


def getSix():
    getSix = 1467 // 6
    print(getSix)


def Data():
    string = "Data"
    mult = string * 4
    print(mult)


def number():
    number = 6
    if number % 2 == 0:
        print("Yes")


def square():
    i = 4
    while i <= 13:
        if i != 7 and i != 11:
            print(i ** 2)

        i += 1


def search_of_a_number():
    n = float(input("ведите число: "))
    b = (n + n * 2)
    print(b)


def variable():
    num = 46
    word = "string "
    word *= 5
    print(num)
    print(word)

def simple_variable():
    x = 5
    symbol = 'F'
    word = "Привет"
    d = 90.2
    CONST = 67
    print(word)


def Separation_of_a_number():
    number = int(input("Введите число с 4 цифрами: "))
    n1 = round(number // 1000 % 10)  # Получаем 1 число
    n2 = round(number // 100 % 10)  # Получаем 2 число
    n3 = round(number // 10 % 10)  # Получаем 3 число
    n4 = round(number % 10)  # Получаем 4 число
    print(n1, ",", n2, ",", n3, ",", n4)


def Separation_of_a_number_1():
    a = []
    b = input("Введите число с 4 знаками: ")
    for h in b:
        a.append(h)
    c = ", ".join(a)
    print(c)


def input_():
    name = input("Ваше имя: ")
    surname = input("Ваша фамилия: ")
    age = int(input("Ваш возраст числами: "))
    print(name + " " + surname + ". Ваш возраст: " + age)


def input_about_friend():
    friend_name = input("Как зовут вашего друга? ")
    print("Вашего друга зовут - ", friend_name)


def simple_math():
    print(136 // 7)


def math_operations():
    num_1 = int(input("Введите 1 число: "))
    num_2 = int(input("Введите 2 число: "))
    num_3 = int(input("Введите 3 число: "))
    res = num_1 + num_2 + num_3
    print("Добавление чисел: ", res)
    res = num_1 - num_2 - num_3
    print("Вычитание чисел: ", res)
    print("Умножение чисел: ", num_1 * num_2 * num_3)
    print("Деление чисел: ", num_1 / num_2 / num_3)
    print("Остаток при делении чисел: ", num_1 % num_2 % num_3)


def type_of_the_variable():
    a = 11
    b = 8.23
    c = "9.1"
    res = float(a) + b + float(c)
    print(res)


def check_the_number():
    a = input("Введите число: ")
    if a.isalpha():
        print("Введите числа")
    elif a.isdigit():
        print("Вы ввели число")


def Conditional_operators():
    age = int(input("Сколько вам лет?"))
    if age > 18:
        print("Вам уже все можно")
    elif age == 18:
        print("Ура, вам 18 лет!")
    else:
        print("Вы еще слишком молоды")

def calculator():
    while True:
        print("___________________________________")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print("Деление = 1",
              "\nУмножение = 2"
              "\nСложение = 3"
              "\nВычитание = 4",
              "\nВыход = 0")
        c = int(input("Выберите действие: "))
        if b == 0 and c == 1:
            print("ERROR")
        elif c == 1:
            print(a / b)
        elif c == 2:
            print(a * b)
        elif c == 3:
            print(a + b)
        elif c == 4:
            print(a - b)
        elif c == 0:
            break


# Самостоятельные задачи
def average():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    print((a + b + c) / 3)


def even():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a % 2 == 0 and b % 2 == 0:
        print("Чётные")
    else:
        print("Не четные")
