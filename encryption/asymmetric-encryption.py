'''
Asymmetric Encryption
---------------------

Asymmetric Encryption is a form of Encryption where keys come in pairs. What one key encrypts, only the other key in the pair can decrypt. The key pairs are often refered to the Private Key and Public Key. The Public Key is used to ENCRYPT and the Private Key is used to DECRYPT. So if you want to have someone encrypt methods that only you can decrypt then you need to send the message write your Public key so that they can encrypt the message with it before sending to you.

Note that everything is derived from the PRIVATE KEY including the corresponding PUBLIC KEY.

Bob need to send Anne a message and wants ONLY Anne to be able to read it.
Bob can encrypt the message using Annes PUBLIC key.
Bob sends the message to Anne.
Anne can now DECRYP the message using her PRIVATE key.

Frequently (but not necessarily), the keys are interchangeable, in the sense that if key A encrypts a message, then B can decrypt it, and if key B encrypts a message, then key A can decrypt it.
'''