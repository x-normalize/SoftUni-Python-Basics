# Напишете програма, която пресмята колко общо пари има в сметката, след като направите
# определен брой вноски. На всеки ред ще получавате сумата, която трябва да внесете в сметката до
# получаване на команда “NoMoreMoney”. При всяка получена сума на конзолата трябва да се извежда
# "Increase: " + сумата и тя да се прибавя в сметката. Ако получите число по-малко от 0 на конзолата
# трябва да се изведе "Invalid operation!" и програмата да приключи. Когато програмата приключи трябва
# да се принтира "Total: " + общата сума в сметката закръглена до втория знак след десетичната запетая.
sum1 = 0
all_1 = input()
while all_1 != "NoMoreMoney":
    all_1 = float(all_1)
    if all_1 < 0:
        print("Invalid operation!")
        print(f'Total: {sum1:.2f}')
        break
    else:
        sum1 += all_1
        print(f"Increase: {all_1:.2f}")
    all_1 = (input())
else:
    print(f'Total: {sum1:.2f}')
