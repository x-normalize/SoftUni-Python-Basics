# Задача 1. Доставка на храна
# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20 процента от общата сметка
# (без доставката). Цената на доставка е 2.50лв и се начислява най-накрая.
# Вход
# От конзолата се четат 3 реда:
# •	Брой пилешки менюта – цяло число в интервала [0… 99]
# •	Брой менюта с риба - цяло число в интервала [0… 99]
# •	Брой вегетариански менюта - цяло число в интервала [0… 99]
# Изход
# Да се отпечата на конзолата един ред:  "Total: {цена на поръчката}"
# Сумата да е форматирана до втория знак след десетичната запетая.
chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegetarian_menu = int(input()) * 8.15
all_cost = chicken_menu + fish_menu + vegetarian_menu
desert = all_cost * 0.2
all_cost += desert + 2.5
print(f'Total: {all_cost:.2f}')