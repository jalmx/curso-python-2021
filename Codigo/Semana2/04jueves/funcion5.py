def formula_general(a,b,c):
    x1 = a + b
    x2 = b + c

    return x1, "x2"

y1, y2 = formula_general(6,83,2)# destructuracion

print(y1, y2)
print(formula_general(6,83,2))


