from DissidentXEncoding import decode_and_decrypt_message
from sys import argv

f = open(argv[1], 'br')
p = f.read()
f.close()
m = decode_and_decrypt_message(argv[2].encode('utf-8'), p)
if m is not None:
	print(m.decode('utf-8'))
