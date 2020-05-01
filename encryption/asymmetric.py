'''
Asymmetric Encryption
---------------------

Asymmetric Encryption is a form of Encryption where keys come in pairs. What one key encrypts, only the other key in the pair can decrypt. The key pairs are often refered to the Private Key and Public Key. The Public Key is used to ENCRYPT and the Private Key is used to DECRYPT. So if you want to have someone encrypt methods that only you can decrypt then you need to send the message write your Public key so that they can encrypt the message with it before sending to you.

Note that everything is derived from the PRIVATE KEY including the corresponding PUBLIC KEY.

Example scenario 1:
------------------

* Bob need to send Anne a message and wants ONLY Anne to be able to read it.
* Bob can encrypt the message using Annes PUBLIC key.
* Bob sends the encrypted message to Anne.
* Anne can now DECRYPT the message using her PRIVATE key.

Example scenario 2:
------------------

* Tony wants to send a message to Lisa
* Tony can encrypt the message using AES
* Tony sends the encrypted message to Lisa
* Lisa asks 'how can I decrypt this?'
* Tony asks Lisa to send over her PUBLIC key
* Tony ENCRYPTS the AES key with Lisa's Public key
* Tony sends the encrypted AES Key to Lisa
* Lisa DECRYPTS the AES key with her PRIVATE KEY.
* Lisa DECRYPTS the message using the AES key

Frequently (but not necessarily), the keys are interchangeable, in the sense that if key A encrypts a message, then B can decrypt it, and if key B encrypts a message, then key A can decrypt it.

Many systems and protocols use Asymmetric Encryption. For example:

* SSL
* TLS
* SSH
* SFTP

How HTTPS Works
--------------

Scenario on how HTTPS works between a browser and a server

* Browser: requests to load a website (say youtube.com)
* Servers: YouTube.com sends back its Certificate containing youtube.com public key which is singed by Google CA
* Browser: I know and trust Google CA. I have checked that the certificate was signed by Google CA using the Google CA public key. I will now generate a new unique, random secret key, encrypt it with the youtube.com public key and send that over for you to use to encrypt messages between us for the rest of this session.
* Servers: Thank you. I can now decrypt your secret key using my Private key. Now I have the new unique key that only you and I know so I'll use this from now on to encrypt messages between us.


How to setup HTTPS
------------------

Scenario for setting up HTTPS in new site:

* Servers   : newsite.com needs a CA to sign a certificate that will be used to facilitate HTTPS encryption
* Google CA : the CA has a private and a public key pair already generated
* Servers   : newsite.com needs to genearate a private and a public key pair and they then generate a Certificate Signing Request (CSR) using their keys
* Google CA : Signs the certificate with the Private Key and returns it. Now this means anyone with the Google CA public key can confirm that it was signed by Google CA.
* Browser   : Already has a list of trusted CA's Public Keys. So therefore when a request is made to newsite.com, the signed certificate is returned and the browser can see its signed by Google CA and quickly use the Public Key of Google CA to validate that fact. Then we continue with the same steps as the above scenario between the browser and the server.

Summary

Public Key              | Private Key
------------------------------------------------------
- Share with anyone     | - Cannot share
- Not secret            | - It's secret
- Encrypts Data         | - Decrytp Datta

Asymmetric Encryption
---------------------
- Slow
- Recommend to use RSA = 2048, 4096 bits to generate the private key
- ECC (Elliptic Curve Cryptography)
- Any message encrypted with Bobs Public Key can only be decrypted with Bobs Private key
- Anyone who has Alice Public key can veryfiy the message (signature) could have only been generated by someone with Alics Private Key.
'''