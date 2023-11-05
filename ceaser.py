def ceaser(Plaintext,key):
    ct = ' '
    for i in range(len(Plaintext)):
        c = Plaintext[i]
        if c == ' ':
            ct += ' '
        elif(c.isupper()):
            ct += chr((ord(c)+key-65)%26+65)
            
        else:
            ct += chr((ord(c)+key-97)%26+97)
           
    
    return ct
    
    
pt = input("ente the string  also too encrypt:")
k = int(input("enter the key value:"))
enc = ceaser(pt,k)
print('the encryptedd value is:',enc)

def decrypt(ciphertext,key):
    pt = ' '
    for i in range(len(ciphertext)):
        c = ciphertext[i]
        if c == ' ':
            pt += ' '
        elif(c.isupper()):
            pt += chr((ord(c)+key-65)%26+65)
            
        else:
            pt += chr((ord(c)+key-97)%26+97)
           
    
    return pt
message = (enc,k)
print("the decryption key hrishi:",message)

