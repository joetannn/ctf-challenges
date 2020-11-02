flag = "fibonaccidecimalhah"
answer = '011235955056179775'
cipher_string = ""
for i in range(len(answer)):
    cipher_string += chr(ord(flag[i]) + int(answer[i]))

print(cipher_string)
