
from DissidentXEncoding import prepare_message, pack_and_encode_messages
from sys import argv

f = open(argv[1], 'br')
p = f.read().split(b'\n')
f.close()
plaintext = []
for s in p:
	if plaintext:
		plaintext[-1] += b'\n'
	if s[0:1] == b'\t':
		p = 1
		while s[p:p+1] == b'\t':
			p += 1
		plaintext.append([b'\t' * p, b'        ' * p])
		plaintext.append(s[p:])
	elif s[0:8] == b'        ':
		p = 1
		while s[p*8:(p+1)*8] == b'        ':
			p += 1
		plaintext.append([b'\t' * p, b'        ' * p])
		plaintext.append(s[p*8:])
	else:
		if plaintext:
			plaintext[-1] += s
		else:
			plaintext = [s]
messages = [prepare_message(argv[i].encode('utf-8'), argv[i+1].encode('utf-8')) for i in range(2, len(argv), 2)]
m = pack_and_encode_messages(messages, plaintext)
if m is None:
	print('Error')
else:
	f = open(argv[1], 'bw')
	f.write(m)
	f.close()




