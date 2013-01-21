def endings_encode(p):
    r = []
    for s in p.split(b'\n'):
        if r:
            r.append([b'\n', b' \n'])
        r.append(s.rstrip())
    return r

if __name__ == '__main__':
    from EncoderBoilerplate import encode
    encode(endings_encode)
