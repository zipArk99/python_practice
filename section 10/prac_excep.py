def ask():
    while True:
        try:
            num = int(raw_input('enter a number:'))
            print(num**2)
        except:
            print('Please enter appropriate number')
            continue
        else:
            pass
            break


ask()