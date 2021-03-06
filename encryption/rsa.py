'''
RSA
---

Used to generate our Private and Public keys. The RSA tool stores these keys in files on our file system. Then when we want to encrypt a message we load the Public Key and the Clear Text Message into the Encrypt function of the RSA Tool which generates our Encrypted Data. To Decrypt the RSA Tool loads the Private Key and the Encrypted Text Message into the Decrypt function and this returns the Clear Text Message.

Below is an example implemtation in Python of the RSA Tool:
'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from Crypto.Hash import SHA256
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"

    def __init__(self):
        return

    def __save_file(self, contents, file_name):
        f = open(file_name, 'wb')
        f.write(contents)
        f.close()

    def __read_file(self, file_name):
        f = open(file_name,'rb')
        contents = f.read()
        f.close()
        return contents

    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key = keys.exportKey("PEM")
        public_key = keys.publickey().exportKey("PEM")
        self.__save_file(private_key,self.PRIVATE_KEY_FILE)
        self.__save_file(public_key,self.PUBLIC_KEY_FILE)
        print("Public & Private Keys; generated and saved sucessfully!")

    def encrypt(self,cleartext, public_keypath=None):
        if(public_keypath==None):
            public_keypath = self.PUBLIC_KEY_FILE

        public_key = RSA.importKey(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext)
        return base64.b64encode(encrypted_data)

    def decrypt(self,cipher_text, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE

        cipher_text = base64.b64decode(cipher_text)
        private_key = RSA.importKey(self.__read_file(private_key_path))
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(cipher_text)

# Lets try it out below!
CryptoRSA().generate_keys()
encrypted_data = CryptoRSA().encrypt(b"Hello World")
print(encrypted_data)
decrypted_data = CryptoRSA().decrypt(encrypted_data)
print(decrypted_data)