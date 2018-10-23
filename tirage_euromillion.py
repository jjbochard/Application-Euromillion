from random import randrange

numbers = [0 for j in range(50)]
numbers_picked = [0 for k in range(5)]

i = 0
f = 0
while i<5:
	random_number = randrange(1,51)
	numbers[random_number - 1] += 1
	
	for number in numbers:
		if number == 100000:
			ind = numbers.index(100000)
			ind +=1

			if ind == numbers_picked[0] or ind == numbers_picked[1]:
				f += 1
				numbers = [0 for j in range(50)]
			else:
				numbers_picked[i] = ind
				i += 1
				numbers = [0 for j in range(50)]
numbers_picked.sort()

stars = [0 for j in range(12)]
stars_picked = [0 for k in range(2)]

i = 0
f = 0
while i<2:
	random_star = randrange(1,13)
	stars[random_star - 1] += 1
	
	for star in stars:
		if star == 1000000:
			ind = stars.index(1000000)
			ind +=1

			if ind == stars_picked[0] or ind == stars_picked[1]:
				f += 1
				stars = [0 for j in range(12)]
			else:
				stars_picked[i] = ind
				i += 1
				stars = [0 for j in range(12)]
stars_picked.sort()

print("Les numeros a jouer sont :", numbers_picked[0], numbers_picked[1], numbers_picked[2], numbers_picked[3], "et", numbers_picked[4])
print("Les etoiles a jouer sont :", stars_picked[0], "et", stars_picked[1])