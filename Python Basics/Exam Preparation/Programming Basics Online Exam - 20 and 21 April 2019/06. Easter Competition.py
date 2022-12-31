import sys
# Задача 6. Великденски конкурс
# С наближаването на Великден, пекарна организира конкурс за направата на
# най-хубав козунак. Напишете програма, която да намира сладкаря с най-висок
# резултат. В началото на конкурса се въвежда броя на козунаците, които ще бъдат
# дегустирани от посетителите на пекарната, като за всеки козунак различен брой
# посетители, ще дадат оценка от 1 до 10.
# Вход
# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
# След това за всеки козунак се прочита:
# •	Името на пекаря, който е направил козунака – текст
# •	До получаване на командата "Stop" се прочита
# o	оценка за козунак от един човек  – цяло число в интервала [1... 10]
# Изход
# След получаване на командата "Stop" се печата един ред:
# •	"{името на пекаря} has {общият брой получени точки} points."
# Ако след командата "Stop", пекарят е с най-много точки до момента, да се отпечата допълнителен ред:
# •	"{името на пекаря} is the new number 1!"
# След дегустация на всички козунаци, да се отпечата един ред:
# •	"{името на пекаря с най-много точки} won competition with {точките на пекаря} points!"
easter_bread = int(input())
name_of_the_best = ''
max_points = -sys.maxsize
for c in range(1 ,easter_bread + 1):
    name = input()
    all_points = 0
    command = input()
    while command!= "Stop":
        grade = int(command)
        all_points += grade
        command = input()
    print(f"{name} has {all_points} points.")
    if max_points < all_points:
        max_points = all_points
        name_of_the_best = name
        print(f"{name} is the new number 1!")
print(f"{name_of_the_best} won competition with {max_points} points!")

