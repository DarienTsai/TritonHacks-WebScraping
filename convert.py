"""
[list of string prices (e.g. [$, $$])] => float
"""
def avg_price(prices):
    sum = 0
    for i in range(len(prices)):
        sum += len(prices[i])
    
    print(sum / len(prices))
    return sum / len(prices)

"""
[list of numbers] => float
"""
def avg_rating(ratings):
    return sum(ratings) / len(ratings)
   