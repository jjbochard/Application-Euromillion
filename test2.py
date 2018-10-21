from random import randrange

num = [0 for j in range(50)] #Tableau qui contient les numéros tirés aléatoirement
#num[49] = 50
num_picked = [0 for k in range(5)] #Tableau qui contient les numéros tirés aléatoirement un certain nombre fois


i = 0
f = 0
while i<5:
	num_aleat = randrange(1,51) #Tirage d'un numéro aléatoire
	num[num_aleat - 1] += 1 #On incrémente l'indice du numéro tiré


	#print (num_aleat)
	for elt in num: # On parcourt le tableau
		if elt == 5: # On regarde si un numéro a été tiré 5 fois
			ind = num.index(5)
			ind += 1
			print (num_picked[0], num_picked[1], num_picked[2], num_picked[3], num_picked[4])
			print (ind)	
			if ind == num_picked[0] or ind == num_picked[1] or ind == num_picked[2] or ind == num_picked[3] or ind == num_picked[4]:
				
				f += 1
				print ("Ca a fonctionné", f, "fois")
				num_picked.append(ind)
				print (num_picked)
			else:


				num_picked[i] = ind
				i += 1
				#print (num)
				#print (num_picked)
			num = [0 for j in range(50)]

"""

star = [0 for j in range(12)] #Tableau qui contient les numéros tirés aléatoirement
#num[49] = 50
star_picked = [0 for k in range(5)] #Tableau qui contient les numéros tirés aléatoirement un certain nombre fois


i = 0
f = 0
while i<5:
	star_aleat = randrange(1,13) #Tirage d'un numéro aléatoire
	star[star_aleat - 1] += 1 #On incrémente l'indice du numéro tiré


	#print (num_aleat)
	for elt in star: # On parcourt le tableau
		if elt == 5: # On regarde si un numéro a été tiré 5 fois
			ind = star.index(5)
			ind += 1
			print (star_picked[0], star_picked[1])
			print (ind)	
			if ind == star_picked[0] or ind == star_picked[1]:
				
				f += 1
				print ("Ca a fonctionné", f, "fois")
				star_picked.append(ind)
				print (star_picked)
			else:


				star_picked[i] = ind
				i += 1
				#print (num)
				#print (num_picked)
			num = [0 for j in range(50)]






print ("Les étoiles à jouer sont :", star_picked[0], "et",star_picked[1])
"""

		
