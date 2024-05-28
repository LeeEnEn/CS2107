cipher_text = "890d_u890d_q8r5s_0vz88ed"

msg = ''

key = 16*3-4+3-4/2-40; #5


for x in cipher_text:
    if x != 0:
        if(x.isalpha()):
            if x.isupper():
                i = (ord(x) - ord('A') - key) % 26 + ord('A')
                msg += chr(int(i))
            else:
                i = (ord(x) - ord('a') - key) % 26 + ord('a')
                msg += chr(int(i))
        else:
            if (x.isdigit()):
                i = (ord(x) - ord('0') - key) % 10 + ord('0')
                msg += chr(int(i))
            else:
                msg += '_'

print(msg)