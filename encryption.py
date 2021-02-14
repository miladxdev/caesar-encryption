# Caesar cipher  @xcripts
# 
def encrypt(text, shift):
    cypher = ''
    for i in text:
        if i.isalpha():
            cypher += chr((ord(i.lower()) - shift -97) % 26 + 97)
        else: cypher += i
    print('Encrypted:', cypher, '\n')

message = ''
while message != 'exit':
    message = input('Message: ')
    encrypt(message, 5)
