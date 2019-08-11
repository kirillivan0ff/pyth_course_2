import random

def checkLetters():
	for x in word2:
		if x == "\u25A0":
			return True
	return False

def letterCheck(letter, wordArr):
	i = 0
	arr = []
	while i < len(wordArr):
		if letter == wordArr[i]:
			arr.append(i)
		i += 1
	return(arr)

words = ["книга", "месяц", "ручка", "шарик", "олень", "носок"]
rand = random.randrange(0, 5)
word = words[rand]
wordArr = list(word)
lives = 3
word2 = []

for x in word:
	word2.append("\u25A0")

print(word)


while lives > 0:
	
	if not checkLetters():
		print("Вы угадали слово!")
		print(word.upper())
		break
	
	for x in word2:
		print(x, end=' ')
	print(f"\nУ вас осталось {lives} жизней")
	letter = input("Введите букву или слово: ")

	letter = str(letter)

	if len(letter) == 1:
		letterResult = letterCheck(letter, wordArr)
		if len(letterResult) > 0:
			lives += 1
			print(f"Вы угадали букву {letter}")
		for x in letterResult:
			word2[x] = letter

	else:
		if letter == word:
			print("Вы угадали слово!")
			print(word.upper())
			lives = 0
			break
	lives -= 1        

