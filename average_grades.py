
total=0
gradecounter=1 

while gradecounter <=5:
	grade=int(input("Enter grade\n")) 
	total=total+grade
	gradecounter=gradecounter+1


average=total/5

print("The class average  is %.2f "%(average))
