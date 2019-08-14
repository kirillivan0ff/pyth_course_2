#fileName = input("Введите имя файла: ")
fileCont = ''
try:
    fileCont = open('mod7test.txt', mode='r').read()

    try:
        fileCont = fileCont.split("\n")
        
        for x in fileCont:
            if not x.isnumeric():
                raise Exception("Not numeric")
                
        
        fileCont = fileCont[1:]    
        fileCont = fileCont[:(len(fileCont)-1)] 
    except:
        print("Файл содержит неверные данные")
    print(fileCont)
except:
    print("Введено неверное имя файла")
