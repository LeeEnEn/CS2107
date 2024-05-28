import math
import binascii

key1 = "d11f5c4991188186d7666b6cf1b09231a63c1b5042ee42cae4780e9f519df447f7dc8266d2ad29b4557b1fe9"
key2 = "3cf2b5be58edc7e3c48bdf3007b3be54abc3f78369f673e8e0cb051302f0903cbe839b043cd56b1eab1393d0"
key3 = "4141414141414141414141414141414141414141414141414141414141414141414141414141414141414141"
key4 = "96d65d1a24429926cc44762d86d71ddfbdd774a1da9be1bf152ca5d4bb1afda93dd11a0e9159a17923b5a677"
enc_msg = "7929c79d9cc1e54faabbf70363ca409dae08975081f1ff880fa6df4bf642ebd07da1735c4b53d1b3bdbd4a72"

b_msg = "{0:08b}".format(int(enc_msg, 16))
b_4 = "{0:08b}".format(int(key4, 16))
b_3 = "{0:08b}".format(int(key3, 16))
b_2 = "{0:08b}".format(int(key2, 16))
b_1 = "{0:08b}".format(int(key1, 16))

output = int(b_msg, 2) ^ int(b_4, 2) ^ int(b_3, 2) ^ int(b_2, 2) ^ int(b_1, 2)

print(binascii.unhexlify('%x' % output))