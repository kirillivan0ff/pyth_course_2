def unique(arr):
	unique_arr = []
	
	for x in arr:
		if x not in unique_arr:
			unique_arr.append(x)
	return unique_arr

def unique_alpha(arr):
	unique_arr = []
	
	for x in arr:
		if x not in unique_arr:
			unique_arr.append(alphabet(x))
	
	unique_arr = unique(unique_arr)
	return unique_arr

def alphabet(word):
	word = list(word)
	i = 0
	end = 0

	#if the world starts with aimed symbols

	for x in word:
		i += 1
		if not x.isalpha() and end != 1:
			word = word[i:]
		else:
			end = 1
			continue

	#if the world ends with symbols

	i = 0
	if end == 1:
		for x in word:
			if not x.isalpha():
				word = word[:i]
			i += 1
	s = ","
	return ''.join(word)

def read_file(fileName):
	f = open(fileName, mode='r', encoding='utf-8').read()
	
	f = unique(f.split())
	
	print(f"Колличество слов: {len(f)}")
	print("=================================")
	for x in f:
		if not x.isalpha():
			print(alphabet(x))
		else:
			print(x)
	
read_file('data.txt')
