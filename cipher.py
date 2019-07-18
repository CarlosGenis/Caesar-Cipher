# Code out your function definitions here
def encode (text,shift):
    result = ''
    for char in text:
        if char == ' ':
                result = result + char
                
            
            # Will encrypt uppercase 
            
        elif char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
    return result
text = "Test"
shift = 1
print(text)
print str(shift)
print(encode(text,shift))

def decode (text,shift):
    result = ''
    for char in text:
        if char == ' ':
                result = result + char
                
            
            # Will encrypt uppercase 
            
        elif char.isupper():
            shift = 1
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            shift = -1
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result
text = "Uftu"
print(text)
print str(shift)
print(decode(text,shift))

