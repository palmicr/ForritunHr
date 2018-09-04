def Verkefni1():
	m_str = input('Input m: ')  # do not change this line
	# change m_str to a float
	m_str = float(m_str)
	# remember you need c
	c = int(300000000)
	# e = 
	e = m_str * c ** 2 
	print("e =", e)  # do not change this line
	pass

def Verkefni2():
	in_str = input("Input s: ")
	in_int = int(in_str)
	print("in_int = ", in_int)
	in_float = float(in_int)
	print("in_float = ", in_float)
	pass

def Verkefni3():
	x1_str = input("Input x1: ")  # do not change this line
	y1_str = input("Input y1: ")  # do not change this line
	x2_str = input("Input x2: ")  # do not change this line
	y2_str = input("Input y2: ")  # do not change this line

	# convert strings to ints
	x1_int = int(x1_str)
	y1_int = int(y1_str)
	x2_int = int(x2_str)
	y2_int = int(y2_str)
	#  d =
	d = (math.sqrt((x1_int - x2_int)** 2 + (y2_int - y1_int)**2))
	print("d =",d)  # do not change this line
	pass

def Verkefni4():
	x_str = input("Input x: ")
	# remember to convert to an int
	x_int = int(x_str)
	first_three = x_int//1000
	last_two = x_int - (x_int//100) * 100
	middle_two = x_int//100 - (x_int//10000)*100
	print("original input:", x_str)
	print("first_three:", first_three)
	print("last_two:", last_two)
	print("middle_two:", middle_two)
	pass

def Verkefni5():
	secs_str = input("Input seconds: ") # do not change this line
	secs_int = int(secs_str)
	hours = secs_int // 3600
	minutes = (secs_int % 3600) // 60
	seconds = (secs_int % 3600) % 60
	print(hours,":",minutes,":",seconds) # do not change this line
	pass

def Verkefni6():
	weight_str = input("Weight (kg): ") # do not change this line
	height_str = input("Height (cm): ") # do not change this line
	weight_f = float(weight_str)
	height_f = float(height_str)
	bmi = (weight_f / ((height_f / 100)**2))
	print("BMI is: ", bmi) # do not change this line
	pass

def Verkefni7():
	years_str = input("Years: ") # do not change this line
	years_int = int(years_str)
	# Missing lines here
	new_population = 307357870
	new_population += ((years_int*365*24*3600)/7)
	new_population -= ((years_int*365*24*3600)/13)
	new_population += ((years_int*365*24*3600)/35)

	print("New population after", years_int, " years is ", int(new_population)) # do not change this line
	pass



