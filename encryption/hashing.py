'''
Hashing in Python
-----------------

Hashing == Integrity

Hashing Function
----------------

h = H(x)

where:
  h = output
  H = hashing function (MD5, SHA-256 etc)
  x = input

Requirements of Hashing Function
--------------------------------

1. Works on ANY type of input - so therefore we can hash literally any digital content!
2. The output should always be the same, fixed length
3. The output should be easy to computer
4. The output should not be reversable to its original state
5. Hx != Hy - meaning that two different input values should NEVER have the same output value. In other words the hashing function must be collision resistant.

Hashing Use Cases
-----------------

* Generate a checksum for a file
* Storeing passwords in the database
* Digital Signatures
* Intrusion Detection Systems (by comparing sha of known state)
* Anti Virus Software (by comparing sha of known virus formats)
'''

'''
Message Digest MD5
------------------

* Predecessor MD4 is no longer used.
* Output of MD5 is 128 bits 32 hex characters
* Do NOT use MD5 to store passwords

Below is an example of using MD5
'''

import hashlib
h = hashlib.md5()
message = b'Hello World'
h.update(message)
print("Example MD5")
print(h.hexdigest())

'''
Secure Hash Algorithm SHA
-------------------------

* SHA 0 - not used anymore
* SHA 1 - output 160 bits and is not used anymore
* SHA 2: has multipe sub versions
  - SHA 224
  - SHA 256 <- most commonly used
  - SHA 384
  - SHA 512
* SHA 3: has multipe sub versions, as well. These are more secure than SHA 2 and are recommended.
  - SHA 224
  - SHA 256
  - SHA 384
  - SHA 512

Below is an example of using SHA
'''

import hashlib
h = hashlib.sha512()
message = b'Hello World'
h.update(message)
print("Example SHA 512")
print(h.hexdigest())

'''
File Checksum
-------------

Get a SHA for a file
Use sha256sum command to check a downloaded files SHA like so (this is a linux command!):

sha256sum somefile.txt
'''

'''
Hashing Passwords
-----------------

* User submits a password during registration for example
* This password is hashed using SHA256
* The result of that hash is stored in the db
* When user logs in the entered pw is again hashed and compared with the pw hash in the db

When hashing passwords its good to:

* NOT use MD5/SHA1
* DO use SHA2 / SHA3 or better
* Always use salt to protect against brute force attacks since without any salt the actual pw could be guessed by repeatably hashing different potential pw to see if it ever matches the hash in the db. If we add a 'salt' to the pw
string before we hash then the hashes will not reveal any common or known pw by simply hashing since the salt will
not be known.

Quick comparion between MD5 and SHA2
------------------------------------

MD5             | SHA256
---------------------------------
Fast            | Slow
128-bit output  | 256-bit output
'''

'''
Hashed Based Message Authenticated Code
---------------------------------------

This is another hashing algorithm but this requires a secret key before applying the hash.

Joe wants to send message
Joe applys MD5 + key and then uses HMAC-MD5 to generate a hash
Joe sends the message in clear text to Jane
Jane uses the same secret key to generate the hash as produced by Joe
Jane can confirm that the message has not been tampered with.

Example below.
'''

import hmac
key = b'secret-shared-key'
message = b'Hello World'
h = hmac.new(key)
h.update(message)
print("Example HMAC")
print(h.hexdigest())

'''
Cracking Hashes
---------------

Hash Algorithm  | Speed (specific machine)
------------------------------------------
MD4             | ~ 100 GH/s
MD5             | ~ 60,000 MH/s
SHA1            | ~ 20,000 MH/s
SHA-256         | ~ 7,000 MH/s
SHA-384         | ~ 2,500 MH/s
SHA-512         | ~ 2,500 MH/s

Generally the slower the alorithm, the more secure the hash is.
This since it will take longer to crack it!

You can use hashcat to crack passwords. Set different rules to attempt to crack. The rules determin the chars to test when attempting to crack. The simplest and fastest rule is base64.

'''

'''
NTLM
----

* NTLM hashes are used on Windows to store pw.
* NTLM started off as the LM (LANMAN) hash
* LM was used on Windows 95 - 98 and was limited to 15 characters only
* LM is not secure
* NTLM Version 1 (NTLMv1) - (NT LM Manager) was introduced and Version 1 is not secure
* NTLM Version 2 (NTLMv2) - is secure and was introduced in Windows Server NT 4.0 SP4. NTLMv2 is intended as a cryptographically strengthened replacement for NTLMv1

The best way to secure your password is to make it as long as possible and difficult to crack!
'''