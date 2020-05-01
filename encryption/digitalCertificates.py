'''
Digital Certificates
--------------------

These are used in HTTPS secure communication.

A Digital Certificate contains:

* The Public Key of the website owner
* The Validity Dates of the certificate
* A serial number - a uniueq id of the ertificate
* Issuer (CA)
* Subject - the domain name of the site being accessed
* Usage - what usage scenarioes this certificate covers like encryption, authentication or maybe both

Role of the Certificate Authority
---------------------------------

* Creates the certificate upon receiving a CSR (Certificate Sign Request) from the site owner
* Validates the certificate each time a user wants to access the site and verifiy the authenticity of the certificate passed to them from the remote server.
* Revokes the certificate. If a certificate is revoked then your site will no longer work.

Certificate Types
-----------------

* Self-Signged - meaning that the certificate is signed by the website owner themselves and not via a CA
* Wildcard - *.mysite.com for supporing all sub-domains

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

TLS
---

TLS is the newer version of SSL used for HTTPS communication.

TLS takes advantage of both symetric and asymmetric encryption to secure communications.

'''