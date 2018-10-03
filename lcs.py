def lcs(X, Y, d):
    if (X, Y) in d:
        return d[(X,Y)]
    max_length = 0 
    for i, c in enumerate(X):
        l = 0
        index = Y.find(c)
        if index >= 0:
            l = lcs(X[i+1:], Y[index+1:], d) + 1
            if l > max_length:
                max_length = l
    d[(X, Y)] = max_length
    return max_length
