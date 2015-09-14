def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

cipherText = '20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d'.split(' ')

IV = cipherText[0].decode('hex')
C0 = cipherText[1].decode('hex')

plainText = 'Pay Bob 100$'
plainTextTarget = 'Pay Bob 500$'

newIV = strxor(IV, strxor(plainText, plainTextTarget))

print 'New Cipher Text:\n', newIV.encode('hex'), cipherText[1]