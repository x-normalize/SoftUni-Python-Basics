# Задача 2.  Великденско парти
# Деси има рожден ден на Великден и иска да организира парти за своите приятели.
# Тя знае какъв е броят гости, които иска да покани и колко е кувертът за всеки
# гост. От броя гости зависи и каква отстъпка ще получи за куверта за един човек.
# Ако покани:
# •	Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
# •	Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
# •	Над 20 човека -> 25 % отстъпка от куверта за един човек
# Деси трябва да предвиди и закупуването на торта за партито. Цената на тортата е 10% от бюджета на Деси.
# Напишете програма, която изчислява дали бюджетът на Деси ще и е достатъчен за партито.
# Вход
# От конзолата се четат 3 реда:
# 1.	Брой гости – цяло число в интервала [1...99]
# 2.	Цена на куверт за един човек – реално число в интервала [0.00 … 99.00]
# 3.	Бюджетът на Деси  – реално число в интервала [0.00 … 9999.00]
# Изход
# На конзолата да се отпечата един ред:
# •	Ако бюджетът  е достатъчен:
# o	"It is party time! {останали пари} leva left."
# •	Ако бюджетът не е достатъчен:
# o	"No party! {недостигащи пари} leva needed."
# Резултатът да бъде форматиран до втория знак след десетичната запетая.
guests = int(input())
price_for_one = float(input())
budget = float(input())
cake = budget * 0.1
if 10 <= guests <= 15:
    price_for_one *= 0.85
elif 15 < guests <= 20:
    price_for_one *= 0.8
elif guests > 20:
    price_for_one *= 0.75
all_price = price_for_one * guests + cake
if budget >= all_price:
    print(f'It is party time! {abs(budget -all_price):.2f} leva left.')
else:
    print(f"No party! {abs(budget - all_price):.2f} leva needed.")