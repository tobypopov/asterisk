import hashlib
import getpass

def asciify_advanced(inp):
    m = ""
    for i in range(0,32):
        m = m + chr((int(inp[i*2:i*2+2],16) % 90) + 33)
    return m

def asciify_basic(inp):
    m = ""
    temp = ""
    for i in range(0,32):
        temp = int(inp[i*2:i*2+2],16) % 3
        if temp == 0:
            m = m + chr((int(inp[i*2:i*2+2],16) % 26) + 97)
        elif temp == 1:
            m = m + chr((int(inp[i*2:i*2+2],16) % 26) + 65)
        else:
            m = m + chr((int(inp[i*2:i*2+2],16) % 10) + 48)
    return m

def main():
    code = getpass.getpass("")

    hash1 = hashlib.sha256(code.encode("utf-8")).hexdigest()
    hash2 = hashlib.sha256(hash1.encode("utf-8")).hexdigest()
    hash3 = hashlib.sha256(hash2.encode("utf-8")).hexdigest()
    hash4 = hashlib.sha256(hash3.encode("utf-8")).hexdigest()
    hasha = hashlib.sha256(hash4.encode("utf-8")).hexdigest()
    hashb = hashlib.sha256(hasha.encode("utf-8")).hexdigest()

    #print(hash1+"\n"+hash2+"\n"+hash3+"\n"+hash4+"\n"+hasha+"\n"+hashb)

    asca_hasha = asciify_advanced(hasha)
    asca_hashb = asciify_advanced(hashb)

    ascb_hasha = asciify_basic(hasha)
    ascb_hashb = asciify_basic(hashb)

    finala = asca_hasha + asca_hashb
    finalb = ascb_hasha + ascb_hashb

    #print()
    #print(asca_hasha)
    #print(asca_hashb)
    #print()
    print(finala)
    print(finala[:20])
    print(finala[:12])
    #print()
    #print(ascb_hasha)
    #print(ascb_hashb)
    print()
    print(finalb)
    print(finalb[:20])
    print(finalb[:12])
    print()
    print("----------------------------------------------------------------")

while True:
    main()
