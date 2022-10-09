import random
import time
bog = []
sta = str(" ")
random.seed(time.time())
choice = input('1 for Encrypt String, 2 for Decrypt Bytes\n')

def rseed ():
    for i in range (10):
        bog.append(str(random.randint(0,10)))
        sj = (''.join(bog))
    return sj

def byteenc ():
    x = int.from_bytes(sta_bytes, byteorder="big")
    y = int.from_bytes(byte_array, byteorder = "big")
    c = x ^ y
    ok = c.to_bytes(max(len(sta_bytes), len(byte_array)),byteorder ="big")
    return ok

def bytedec():
    y = int.from_bytes(byteseq, byteorder="big")
    c = int.from_bytes(bytestring, byteorder ="big")
    x = y ^ c
    ok = x.to_bytes(max(len(byteseq), len(bytestring)), byteorder="big")
    return ok


if choice == str(1):
    initstr = "Hello World!"
    encoded_string = initstr.encode()
    byte_array = bytearray(encoded_string)

    sta_bytes = random.randbytes(len(byte_array)+2)

    print('Random Seed: ', rseed())
    print('Input String: '+initstr)
    print('Pseudo Random Sequence: ',sta_bytes)
    print('Output Bytes: ', byteenc())



elif choice == str(2):
    bytestrin = input('Enter Bytearray for encrypted string:\n')
    bytestring = bytearray(bytestrin, encoding="utf-8")
    bytese = input('Enter Pseudo Random Sequence from creation of encrypted string\n')
    byteseq = bytes(bytese, encoding="utf-8")
    print(bytedec().decode())


    
else:
    print('Invalid Input')
    
