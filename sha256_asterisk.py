import hashlib
import getpass

def asciify_advanced(inp):
    out = ""
    for i in range(0,32):
        # Take 2 hex characters from hash and convert to ASCII
        # range from '!' (33) to 'z' (122)
        out += chr((int(inp[i*2:i*2+2],16) % 90) + 33)
    return out

def asciify_basic(inp):
    out = ""
    temp = ""
    for i in range(0,32):
        # Choose which bucket the character falls into
        # Then take 2 hex characters from hash and convert to ASCII
        # range based on bucket
        temp = int(inp[i*2:i*2+2],16) % 3
        if temp == 0:
            # Lowercase ASCII a-z (97-122)
            out += chr((int(inp[i*2:i*2+2],16) % 26) + 97)
        elif temp == 1:
            # Uppercase ASCII A-Z (65-90)
            out += chr((int(inp[i*2:i*2+2],16) % 26) + 65)
        else:
            # Numbers 0-9 (48-57)
            out += chr((int(inp[i*2:i*2+2],16) % 10) + 48)
    return out

def main():
    # getpass used to remove seeing input in terminal window
    code = getpass.getpass("")

    # Hashing 6 times because why not
    hash1 = hashlib.sha256(code.encode("utf-8")).hexdigest()
    hash2 = hashlib.sha256(hash1.encode("utf-8")).hexdigest()
    hash3 = hashlib.sha256(hash2.encode("utf-8")).hexdigest()
    hash4 = hashlib.sha256(hash3.encode("utf-8")).hexdigest()
    hasha = hashlib.sha256(hash4.encode("utf-8")).hexdigest()
    hashb = hashlib.sha256(hasha.encode("utf-8")).hexdigest()

    # Last two hashes are used for generation
    # Two are used instead of one because generation consumes
    # two hash hex characters for one generated character
    ascii_hash_advanced_a = asciify_advanced(hasha)
    ascii_hash_advanced_b = asciify_advanced(hashb)

    ascii_hash_basic_a = asciify_basic(hasha)
    ascii_hash_basic_b = asciify_basic(hashb)

    ascii_hash_advanced_final = ascii_hash_advanced_a + ascii_hash_advanced_b
    ascii_hash_basic_final = ascii_hash_basic_a + ascii_hash_basic_b

    print(ascii_hash_advanced_final)
    print(ascii_hash_advanced_final[:20])
    print(ascii_hash_advanced_final[:12])
    print()
    print(ascii_hash_basic_final)
    print(ascii_hash_basic_final[:20])
    print(ascii_hash_basic_final[:12])
    print()
    print("----------------------------------------------------------------")

while True:
    main()
