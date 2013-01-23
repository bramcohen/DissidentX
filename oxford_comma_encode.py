def oxford_encode(p):
    r = []
    for s in p.split(b', and'):
        if r:
            r.append([b', and', b' and'])
        r.append(s)
    return r

if __name__ == '__main__':
    from EncoderBoilerplate import encode
    encode(oxford_encode)
