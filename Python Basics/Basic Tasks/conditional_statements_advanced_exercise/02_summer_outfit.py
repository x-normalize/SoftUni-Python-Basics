degree = int(input())
time = input()
outfit = ""
shoes = ""

if time == 'Morning':
    if 10 <= degree <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

if time == 'Afternoon':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degree <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

if time == 'Evening':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
