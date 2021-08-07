"""1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

while True:
    number = input('Введите трехзначное число: ')
    if number.isdigit():
        summ = int(number[0]) + int(number[1]) + int(number[2])
        prod = int(number[0]) * int(number[1]) * int(number[2])
        print(f"Сумма цифр: {summ}")
        print(f"Произведение цифр: {prod}")
        break
    else:
        print(f"Введено не число")
        continue
