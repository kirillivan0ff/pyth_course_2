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
