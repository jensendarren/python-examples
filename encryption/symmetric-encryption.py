'''
Symmetric Key Encryption
------------------------

Symmetric encryption is a type of encryption where only one key (a secret key) is used to both encrypt and decrypt electronic information. The entities communicating via symmetric encryption must exchange the key so that it can be used in the decryption process.

* Uses an algorithm like AES


Example:

Message (Plain Text) -> Encrypt using AES(with secret-key) -> Encrypted Message
Encrypted Message -> Decrypt using AES(with secret-key) -> Decrypted (Plain Text) Message

NOTE: The same `secret-key` is used to both encrypt and decrypt the message text

Symmetric Encryption Types
--------------------------

Block Cyphers                       | Stream Cyphers
--------------------------------------------------------------------------
- Encrypts in fixed block sizes     | - Encrypts each bit/byte
- Used when size is known (files)   | - Used when size is unknown (online stream)
- Available Algorithms:             | - Available Algorithm:
-- AES (K: 128,192,256, B: 64 bits) | -- RC4 (K: 40 - 2048 bits)
-- 3DES (K: 128 bits, B: 64 bits)   |
-- DES (K: 56 bits, B: 64 bits)     |
-- Blowfish (K: 32-448, B: 64 bits) |
-- Twofish (K: 128,192,256, B: 64)  |
'''

# Generating a key (not secure!)
import random
key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
print('Genearate key:')
print('key', [x for x in key])

# AES example
from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print('AES Example Encrypted:')
print(ciphertext)
# ciphertext
# '\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
print('AES Example Decrypted:')
obj2.decrypt(ciphertext)
# 'The answer is no'