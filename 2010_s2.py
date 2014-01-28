# Create a dictionary with the information needed to decode the ciphertext.
decoding_dict = dict()
for k in range(int(input())):
    s = input().split()
    decoding_dict[s[1]] = s[0]

# Text to decode
ciphertext = input()

# Message we will output
message = ''

# Counter variable
i = 1

while len(ciphertext) > 0:
    # Checks to see if the first i bits of ciphertext match a character.
    # If not, keep incrementing i until they do.
    while ciphertext[:i] not in decoding_dict:
        i += 1
        
    # Append character corresponding to first i bits of cipher text to message.
    message += decoding_dict[ciphertext[:i]]
    
    # Remove the first i bits of ciphertext.
    ciphertext = ciphertext[i:]
    
    # Reset the counter. 
    i = 1

print(message)
