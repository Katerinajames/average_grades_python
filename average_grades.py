
total=0
gradecounter=0 
grade=int(input("Enter grade\n")) 
	
while grade!=-1:	
	total=total+grade
	gradecounter=gradecounter+1
	grade=int(input("Enter grade\n")) 
	
     
if gradecounter==0:
  print("No grades were entered")
else:
  
  average=total/gradecounter

  print("The class average  is %.2f "%(average))
