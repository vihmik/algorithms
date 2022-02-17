def match(n, v):   
    res = []
    for i in range(len(n)):
        if n[i] == v:
            res.append(i)
        else:
            i = i + 1
    if res == []:
        return "Nil"
    else: 
        return res
