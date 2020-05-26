from random import randrange

numbers = [0 for j in range(50)] # Array of the index of the numbers chosen randomly
numbers_picked = [0 for k in range(5)] # Array of the final numbers

i = 0
#f = 0
while i<5:
	random_number = randrange(1,51) # We randomly choose à number between 1 & 50
	numbers[random_number - 1] += 1 # We increment the index of the chosen number by substract 1 to it
	
	for number in numbers: # We read the array
		if number == 10: # if an index of number has been picked 100 times
			ind = numbers.index(10) # We check the index of the number
			ind +=1 # and add it +1 to get the final number

			if ind == numbers_picked[0] or ind == numbers_picked[1] or ind == numbers_picked[2] or ind == numbers_picked[3]: # We check if a number has been chosen several times
				#f += 1
				print ("Le numero", ind, "a ete tire plusieurs fois")

				numbers = [0 for j in range(50)] # If so, we reinizialize the array of the numbers'index
			else:
				numbers_picked[i] = ind # Else, we add the picked number to the final array
				i += 1
				numbers = [0 for j in range(50)] # And we reinizialize the array of the number's index
numbers_picked.sort()

# We do the same for the star numbers
stars = [0 for j in range(12)]
stars_picked = [0 for k in range(2)]

i = 0
#f = 0
while i<2:
	random_star = randrange(1,13)
	stars[random_star - 1] += 1
	
	for star in stars:
		if star == 10:
			ind = stars.index(10)
			ind +=1

			if ind == stars_picked[0]:
				#f += 1
				print ("L'etoile", ind, "a ete tire plusieurs fois")
				stars = [0 for j in range(12)]
			else:
				stars_picked[i] = ind
				i += 1
				stars = [0 for j in range(12)]
stars_picked.sort()

print("Les numeros a jouer sont :", numbers_picked[0], numbers_picked[1], numbers_picked[2], numbers_picked[3], "et", numbers_picked[4])
print("Les etoiles a jouer sont :", stars_picked[0], "et", stars_picked[1])

"""fichier = open("test.txt", "a")
fichier.write("Numéros : "numbers_picked[0], numbers_picked[1], numbers_picked[2], numbers_picked[3], numbers_picked[4], "  Etoiles : ", stars_picked[0], "et", stars_picked[1], "\n")
fichier.close"""