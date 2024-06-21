print("ketaki mahajan / P1-2 / 16014022050")

def combinations(tuple1, tuple2):
    
    res = []
    
    for tup1 in tuple1:
        for tup2 in tuple2:
            res.append((tup1, tup2))
    
    return res

tuple1 = (4, 5, 6)
tuple2 = (7, 8)
res = combinations(tuple1, tuple2)

print("all pair combinations are: ", res)
