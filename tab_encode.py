def tab_cover(p):
	covertext = None
	for s in p.split(b'\n'):
		if covertext:
			covertext[-1] += b'\n'
		else:
			covertext = ['']
		if s[0:1] == b'\t':
			p = 1
			while s[p:p+1] == b'\t':
				p += 1
			covertext.append([b'\t' * p, b'        ' * p])
			covertext.append(s[p:])
		elif s[0:8] == b'        ':
			p = 1
			while s[p*8:(p+1)*8] == b'        ':
				p += 1
			covertext.append([b'\t' * p, b'        ' * p])
			covertext.append(s[p*8:])
		else:
			covertext[-1] += s
	return covertext

if __name__ == '__main__':
	from EncoderBoilerplate import encode
	encode(tab_cover)
