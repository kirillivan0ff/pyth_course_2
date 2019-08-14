<<<<<<< HEAD
try:
    n = 1
    try:
        s = 'a' > 1
    except:
        print('inner')
        raise Exception('')
    finally:
        print('Ok')
        
except:
    print('outer')
finally:
    print('The End')
=======
def unique(arr):
	unique_arr = []
	
	for x in arr:
		if x not in unique_arr:
			unique_arr.append(x)
	return unique_arr
>>>>>>> 1d09bd794c452353be2d310d95beee66c75458f1
