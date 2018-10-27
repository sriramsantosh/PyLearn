def division(x,y):
    if y ==0:
        print("Y cannot be 0")
        return 0
    return float(x)/y

if __name__ == '__main__':

    x, y = 3, 7

    print("{0} divided by {1} is {2}".format(x,y,division(x,y)))
