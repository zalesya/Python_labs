def fizz_buzz():
    temp = ''

    for a in range(1, 102, 2):
        if (a % 3 == 0) and (a % 7 == 0):
            temp += ' FizzBuzz'
        elif a % 3 == 0:
            temp += ' Fizz'
        elif a % 7 == 0:
            temp += ' Buzz'
        else:
            if temp == '':
                temp += str(a)
            else:
                temp += (' ' + str(a))
    return temp


#if __name__ == '__main__':
    #print(fizz_buzz())
