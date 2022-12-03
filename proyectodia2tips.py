#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Bienvenido a calculadora de cuentas')
bill=float(input('Introduzca cuenta total a pagar\n'))
person=float(input('Introduzca numero de personas a repartir\n'))
tip=float(input('Introduzca % del tip\n'))*0.01
billperson=(bill+(bill*tip))/person
print(f"La cuenta total es {bill:.0f} a repartir entre {person:.0f} personas con un tip\n de {tip*100} %. Cada persona pagara {billperson:.2f}$ cada una.")