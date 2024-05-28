def shift(c,key):
    return c+key
    
def enc(text):
    aabb = ""
    for c in text:
        ac = ord(c)
        nc = 33
        
        if ac > 33 and ac <= 96:
            if ac >= 65:                        # A-H
                if ac >= 73:                    # I-Z
                    if ac >= 91:                # [\]^_`
                        ac = shift(ac,-6)       # UVWXYZ 
                        aabb += chr(ac)
                        continue
                    ac = shift(ac,32)           # i-z
                    aabb += chr(ac)
                    continue
                ac = shift(ac,-25)              # ()*+,-./
                aabb += chr(ac)
                continue
            
            if ac < 65:                         # 
                if ac < 58:                     # 0-9
                    if ac < 48:                 # "#$%&'()*+,-./
                        ac = shift(ac,57)       # [\]^_`abcdefgh
                        aabb += chr(ac)
                        continue
                    if ac >= 55:                # 789
                        ac = shift(ac,68)       # {|}
                        aabb += chr(ac)
                        continue
                    ac = shift(ac,10)           # 0-6     ->    :;<=>?@
                    aabb += chr(ac)
                    continue
                ac = shift(ac,-10)              # :;<=>?@ ->    0-6
                aabb += chr(ac)
                continue
            continue
        
        if ac >= 117 and ac < 126:              # uvwxyz{|}
            if ac >= 123:                       # {|}
                ac = shift(ac,-68)              # 789
                aabb += chr(ac)
                continue
            ac = shift(ac,-83)                  # "#$%'(
            aabb += chr(ac)
            continue
        
        if ac > 33 and ac <= 116:               # `abcdefghijklmnopqrst
            ac = shift(ac,-32)                  # @ABCDEFGHIJKLMNOPQRST
            aabb += chr(ac)
            continue
        
        if ac == 126:                           # ~
            nc = 33                             # !
        aabb += chr(nc)
    return aabb

if __name__ == "__main__":
    flag = open("flag.txt", "r").readline().strip()
    encrypted = open("salad.txt", "w")
    encrypted.writelines(enc(flag))
    encrypted.close()