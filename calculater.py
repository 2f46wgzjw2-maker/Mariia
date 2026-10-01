print("калькулятор")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

znak = input("Введите операцию (+, -, *, /, //, %, **): ")

if znak == "+":
    print("Результат:", a + b)

elif znak == "-":
    print("Результат:", a - b)

elif znak == "*":
    print("Результат:", a * b)

elif znak == "/":
    if b == 0:
        print("Ошибка: на ноль делить нельзя")
    else:
        print("Результат:", a / b)

elif znak == "//":
    if b == 0:
        print("Ошибка: на ноль делить нельзя")
    else:
        print("Результат:", a // b)

elif znak == "%":
    if b == 0:
        print("Ошибка: на ноль делить нельзя")
    else:
        print("Результат:", a % b)

elif znak == "**":
    print("Результат:", a ** b)

else:
    print("Ошибка: такой операции нет")


print("сравнение чисел")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


print("логические операторы")

print("Оба числа положительные:", a > 0 and b > 0)
print("Хотя бы одно число положительное:", a > 0 or b > 0)
print("Числа не равны:", not a == b)


print("операторы принадлежности")

znaki = ["+", "-", "*", "/", "//", "%", "**"]

print("Знак есть в списке:", znak in znaki)
print("Знака нет в списке:", znak not in znaki)


print("операторы тождественности")

x = []
y = x
z = []

print("x is y:", x is y)
print("x is not z:", x is not z)