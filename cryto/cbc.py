# line 2 - 4 input key, plain_msg
print("key : ",end="")
key = input()
print("plain_msg : ",end="")
plain_msg = input()

# line 8 - 9 reset encryt_msg, pad, tmp_encryt_msg
encryt_msg = []
pad = len(key)-len(plain_msg)%len(key)
tmp_encryt_msg = ""

# line 13 - 29 encryt
for i in range(len(plain_msg)):
	if len(tmp_encryt_msg) == len(key) :
		encryt_msg.append(tmp_encryt_msg)
		tmp_key = ""
		for j in range(len(key)):
			if key[j].isupper():
				tmp_key[j] += chr(ord('A') + (ord(tmp_encryt_msg[j]) ^ ord(key[j])) % 26)
			else :
				tmp_key += chr(ord('a') + (ord(tmp_encryt_msg[j]) ^ ord(key[j])) % 26)
		tmp_encryt_msg = ""
		key = tmp_key

	if plain_msg[i].isupper() :
		tmp_encryt_msg += chr(ord('A') + (ord(plain_msg[i])^ord(key[i%len(key)])) % 26)
	else :
		tmp_encryt_msg += chr(ord('a') + (ord(plain_msg[i])^ord(key[i%len(key)])) % 26)
encryt_msg.append(tmp_encryt_msg)

# line 32 - 35 print encryt_msg
for i in encryt_msg:
	print(i, end="")
if pad != len(key):
	print('=' * pad)