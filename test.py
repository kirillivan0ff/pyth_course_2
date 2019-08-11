word2 = ["A", "1"]

def checkLetters():
	for x in word2:
		if x == "\u25A0":
			print(x)
			return True
	return False
	
if checkLetters():
	print("Da!")

else:
	print("Net!")
