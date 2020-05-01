'''
Digital Signatures
------------------

The process by which a user digitally signs a document using their Private Key. NOTE That signing does NOT encrypt the data. What it does is it acts as a proof that the file was indeed sent by the person who sigend it.

Used for:

* Authentication
* Non-repudiation
* Integrity

Example Scenario:
----------------

* Bob signs a clear text message using his Private Key
* Bob sends the clear text message and the message signature to Lisa
* Lisa uses Bobs Public Key to confirm that the message signuture was produced using Bobs Private key thus proovign that it was Bob that sent the message

'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto import Random
from Crypto.Hash import SHA256
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"

    def __init__(self):
        return

    def __save_file(self, contents, file_name):
        f = open(file_name, 'w')
        f.write(contents)
        f.close()

    def __read_file(self, file_name):
        f = open(file_name, 'r')
        contents = f.read()
        f.close()
        return contents

    def __sha256(self,input):
        sha256 = SHA256.new()
        sha256.update(input)
        return sha256

    def sign(self,textmessage,private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE

        # Create private key object
        private_key = RSA.importKey(self.__read_file(private_key_path))
        # Create the signature
        signature = PKCS1_PSS.new(private_key)
        return signature.sign(self.__sha256(textmessage))

    def verify(self,signed_signature,textmessage,public_key_path=None):
        if public_key_path == None:
            public_key_path = self.PUBLIC_KEY_FILE

        # Create the public key object
        public_key = RSA.importKey(self.__read_file(public_key_path))
        # Create the verifier
        verifier = PKCS1_PSS.new(public_key)
        verification = verifier.verify(self.__sha256(textmessage),signed_signature)
        print("Is this verified?")
        print(verification)


# Class Test
# Note assumes you have already generated key files private_key.pem and public_key.pem in the current directory. If not then use the rsa.py file to generate your keys (or use any keys that you already own) then come back here to try this!
message = b"Hello World"
signed_message = CryptoRSA().sign(message)
print("The Signed Message....")
print(signed_message)
CryptoRSA().verify(signed_message,message)