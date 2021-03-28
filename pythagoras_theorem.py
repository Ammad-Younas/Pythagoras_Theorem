import os
os.system("")
class color():
    bold = '\033[1m'
    gold = '\033[33m'
    green = '\033[32m'
    blue = '\033[34m'
    red = '\033[31m'
    purple = '\033[35m'
    cyan = '\033[36m'
def pethagorustheorem():
	try:
		print(color.green,"==================================================")
		print(color.bold,color.green,"\t   Which side you want to check...?")
		print(color.bold,color.green,"\t\t H for Hypotenuse")
		print(color.bold,color.green,"\t\t  A for Altitude")
		print(color.bold,color.green,"\t\t    B for Base")
		print(color.green,"==================================================")
		print(color.green,"Enter your choice: ",end="")
		first = input().upper()
		if first == 'H':
			print(color.gold,"Enter Base: ",end="")
			second = float(input())
			print(color.gold,"Enter Altitude: ",end="")
			third = float(input())
			print(color.cyan,"The Hypotenuse Is: ",((second*second)+(third*third))**0.5)
			again()
		elif first == 'A':
			print(color.blue,"Enter Hypotenuse: ",end="")
			fourth = float(input())
			print(color.blue,"Enter Base: ",end="")
			fifth = float(input())
			print(color.cyan,"The Altitude Is: ",((fourth*fourth)-(fifth*fifth))**0.5)
			again()
		elif first == 'B':
			print(color.purple,"Enter Hypotenuse: ",end="")
			sixth = float(input())
			print(color.purple,"Enter Altitude: ",end="")
			seventh = float(input())
			print(color.cyan,"The Base Is: ",((sixth*sixth)-(seventh*seventh))**0.5)
			again()
		else:
			print(color.red,"Please Select Only H, A & B")
			again()
	except Exception as error:
		print(color.red,"You Entered Somthing Wrong")
		again()
def again():
	print(" Do you want to run again[Y/N]: ",end="")
	user_decision = input().upper()
	if user_decision == 'Y':
		pethagorustheorem()
	elif user_decision == 'N':
		print(" See you next time !!!")
	else:
		again()
pethagorustheorem()