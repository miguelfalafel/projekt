#funkcja liczy wariancje dochodu jednostek mniejszych (small) podlegających pod jednostke większą (big)

def var_income(small,big):
    variance=[]
    for i in list(big['id']):
        variance.append(small[small.id.str.match(i)]['avg_income'].var())
    result = big
    result['variance'] = variance
    #usunięcie pustych wartości powstałych dla M NPP
    result = result.dropna(how='any')
    return result
