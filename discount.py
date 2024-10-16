discount = [["PVFC7","CPU5","BGF2"], [10,5,15]]

def checkdiscount(price, code):
    newprice = price
    size = len(discount[0])
    for x in range(size):
        if discount[0][x] == code:
            newprice = newprice - discount[1,x]
    return newprice