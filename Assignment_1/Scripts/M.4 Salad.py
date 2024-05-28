def shift(c,key):
    return c+key
	
def enc(text):
    aabb = ""
    for c in text:
        ac = ord(c)
        
        if ac >= 85 and ac <= 90:
            ac = shift(ac, 6)
        
        elif ac >= 105 and ac <= 122:
            ac = shift(ac, -32)
        
        elif ac >= 40 and ac <= 47:
            ac = shift(ac, 25)
        
        elif ac >= 91 and ac <= 104:
            ac = shift(ac, -57)
        
        elif ac >= 123 and ac < 126:
            ac = shift(ac, -68)

        elif ac >= 58 and ac <= 64:
            ac = shift(ac, -10)

        elif ac >=48 and ac <=54:
            ac = shift(ac, 10)
            
        elif ac >= 55 and ac <= 58:
            ac = shift(ac, 68)
            
        elif ac >= 34 and ac <= 40:
            ac = shift(ac, 83)
            
        elif ac >= 64 and ac <= 84:
            ac = shift(ac, 32)
            
        elif ac == 126:
            ac = 33
            
        aabb += chr(ac)
    return aabb
	
print(enc('*s<;:{7M>?T=RY:FYS"B?TI{"{I:NY=NJ:&Y"rYS>L6D~~9'))