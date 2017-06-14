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
        ciphertext += chr(abs(ord(c)-ord(key[l%len_key])))
        l+=1
    return ciphertext
def decode(ciphertext, key):
    text = ""
    l=0
    len_key = len(key)
    for c in ciphertext:
        text += chr(abs(ord(c)-ord(key[l%len_key])))
        l+=1
    return text

if __name__ == '__main__':
    text = "Hello you are so cute"
    key = "สวัสดี"
    ciphertext = encode(text, key)
    text = decode(ciphertext, key)
    print("ciphertext:"+ciphertext)
    print("text:"+text)
    
