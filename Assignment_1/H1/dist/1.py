import crt

e = 5

with open('output.txt') as f:
    lines = f.readlines()
    
    aArray = []
    bArray = []
    cArray = []
    nArray = []
    
    i = 0
    
    while i < len(lines):
        print(i)
        aArray.append(int(lines[i]))
        bArray.append(int(lines[i + 1]))
        cArray.append(int(lines[i + 2]))
        nArray.append(int(lines[i + 3]))
        
    TArray = [-1]*e
    for i in range(e):
        arrayToCRT = [0]*e
        arrayToCRT[i] = 1
        TArray[i] = crt(arrayToCRT,nArray)
    P = PolynomialRing(Zmod(prod(nArray)), names=('x',)); (x,) = P._first_ngens(1)
    gArray = [-1]*e
    for i in range(e):
        gArray[i] = TArray[i]*(pow(aArray[i]*x + bArray[i],e) - cArray[i])
    g = sum(gArray)
    g = g.monic()
    # Use Sage's inbuilt coppersmith method
    roots = g.small_roots(epsilon=eps)
    if(len(roots)== 0):
        print("No Solutions found")
    print(roots[0])