# 3 * cherry => 1
# 1 * apple => 3
# 1 * pear => 5

# Must buy 100 fruits
# Budget 100 AZN

count = 100
budget = 100

cherries_in_bunch = 3 # :D

cherry_bunch_price = 1 #azn
apple_price = 3 #azn
pear_price = 5 #azn

for pear in range(0, count // pear_price + 1): 
    count -= pear 
    budget -= pear * pear_price
    if count < 0 or budget < 0: break
    for cherry in range(0, count//cherry_bunch_price + 1, cherries_in_bunch): 
        apple = count - cherry
        if apple < 0: break
        if (budget - (cherry/cherries_in_bunch)*cherry_bunch_price) == apple * apple_price:
            print("pear:{}, cherry:{}, apple:{}, ".format(pear, cherry, apple))
    count = 100
    budget = 100
