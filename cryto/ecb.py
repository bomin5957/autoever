# line 1 - 4 input - key, plain_msh
print("key : ", end = "")
key = input()
print("plain_msg : ", end = "")
plain_msg = input()

# line 8 - 9 reset - encryt_msg, pad 
encryt_msg = ""
pad = len(key)-len(plain_msg)%len(key)

# line 12 - 16 encryt
for i in range(len(plain_msg)):
	if plain_msg[i].isupper():
		encryt_msg += chr(ord('A') + (ord(plain_msg[i])+ord(key[i%len(key)])) % 26)
	else :
		encryt_msg += chr(ord('a') + (ord(plain_msg[i])+ord(key[i%len(key)])) % 26)

# line 19 - 21 print encryt_msg
print(encryt_msg, end="")
if pad != len(key):
	print('=' * pad)