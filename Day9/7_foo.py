def Gryffindor(x):
	print("Gryffindor: ", x)

def Ravenclaw(x):
	print("Ravenclaw: ", x)

def bar(x):
	if x == "Luna":
		temp(x)

#Ravenclaw("Luna")
#Ravenclaw("Harry")

temp = Ravenclaw
Ravenclaw = bar
Ravenclaw("Luna")
Ravenclaw("Harry")

temp = Gryffindor
Gryffindor = bar
Gryffindor("Luna")
Gryffindor("Harry")

Ravenclaw("Luna")  # oh no! Ravenclaw calls bar => bar calls temp... but temp is no longer original Ravenclaw, but has changed to Gryffindor. 

# exercise: fix this using decorator!



