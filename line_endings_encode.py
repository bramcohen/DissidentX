
from DissidentXEncoding import prepare_message, pack_and_encode_messages
from sys import argv

f = open(argv[1], 'br')
p = f.read().split(b'\n')
f.close()
plaintext = [p[0]]
for s in p[1:]:
	plaintext.append([b'\n', b' \n'])
	plaintext.append(s.rstrip())
messages = [prepare_message(argv[i].encode('utf-8'), argv[i+1].encode('utf-8')) for i in range(2, len(argv), 2)]
m = pack_and_encode_messages(messages, plaintext)
if m is None:
	print('Error')
else:
	f = open(argv[1], 'bw')
	f.write(m)
	f.close()




