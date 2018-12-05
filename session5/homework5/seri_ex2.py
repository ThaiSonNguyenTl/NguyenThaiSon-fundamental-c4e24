prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
total = 0
for qua in prices:
    print(qua)
    print("prices:",prices[qua]) 
    for st in stock:
        if qua == st:
            print("stock:", stock[st])
            n = prices[qua] * stock[st]
            print(n)
            total += n
print("total =",total)