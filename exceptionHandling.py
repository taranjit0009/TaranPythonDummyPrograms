

def haldinngException():

    try:
        a = int(input('Enter the 1st Numerical value = '))
        b = int(input('Enter the 2nd Numerical value = '))
        c= a/b
        print(c)
    except Exception as e:
        print(e)


haldinngException()