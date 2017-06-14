"""A simple cryptography create for encryption text massage
It's one layer unicode text to unicode text cryptography.
Massage: Unicode Text
Key: Unicode Text
"""

def encode(text, key):
    ciphertext = ""
    l=0
    len_key = len(key)
    for c in text:
        #ciphertext += chr(ord(c)+ord(key[l%len_key]))
        fullpart = "1"+str(ord(c)*ord(key[l%len_key]))
        print(fullpart)
        firstPart=int(fullpart[0::2])
        endPart=int(fullpart[1::2])
        #print(firstPart, chr(firstPart), endPart, chr(endPart))
        ciphertext += chr(firstPart)+chr(endPart)
        l+=1
    return ciphertext
def decode(ciphertext, key):
    text = ""
    l=0
    len_key = len(key)
    for i, j in zip(ciphertext[0::2], ciphertext[1::2]):
        k = ord(key[l%len_key])
        firstPart=str(ord(i))
        endPart=str(ord(j))+" "
        fullpart="".join(i+j for i, j in zip(firstPart, endPart))[1:]
        print(fullpart)
        text+= chr(int(fullpart)//k)
        l+=1
    return text

if __name__ == '__main__':
    text = "ควยไรสัส"
    key = "ntsd"
    print("text:"+text)
    ciphertext = encode(text, key)
    print("ciphertext:"+ciphertext)
    text = decode(ciphertext, key)
    
    print("text:"+text)
    
