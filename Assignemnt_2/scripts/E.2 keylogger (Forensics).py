from scapy.all import rdpcap, bytes_hex

packets = rdpcap("chall.pcapng")[810:894]

keyboard_mappings = {
        "04": ['a', 'A'],
        "06": ['c', 'C'],
        "07": ['d', 'D'],
        "08": ['e', 'E'],
        "0a": ['g', 'G'],
        "0c": ['i', 'I'],
        "0e": ['k', 'K'],
        "0f": ['l', 'L'],
        "15": ['r', 'R'],
        "16": ['s', 'S'],
        "17": ['t', 'T'],
        "19": ['v', 'V'],
        "1c": ['y', 'Y'],
        "1f": ['2', '@'],
        "1e": ['1', '!'],
        "20": ['3', '#'],
        "24": ['7', '&'],
        "27": ['0', ')'],
        "28": ['\n', '\n'],
        "2d": ['-', '_'],
        "2f": ['[', '{'],
        "30": [']', '}']
}

result = ""

for p in packets:
    index = 0
    data = str(bytes_hex(p))[-17:-1]
    if data[0:2] == "02": # Left shift being pressed
        index = 1
    current_char = data[4:6]
    if current_char != "00" and current_char != "ff":
        result += keyboard_mappings[current_char][index]

print(result)

