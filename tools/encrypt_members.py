#!/usr/bin/env python3
"""Verschlüsselt den Mitgliederbereich.
Aufruf: python3 tools/encrypt_members.py <klartext.json> <passwort>
Schreibt data/mitglieder.enc.json (AES-256-GCM, Schlüssel per PBKDF2-SHA256, 310000 Iterationen).
Die Klartextdatei gehört NICHT ins Repository."""
import sys,os,json,base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
src,pw=sys.argv[1],sys.argv[2]
data=open(src,'rb').read();json.loads(data)
salt=os.urandom(16);iv=os.urandom(12);it=310000
key=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=it).derive(pw.encode())
ct=AESGCM(key).encrypt(iv,data,None)
b=lambda x:base64.b64encode(x).decode()
out=os.path.join(os.path.dirname(__file__),'..','data','mitglieder.enc.json')
json.dump({"v":1,"kdf":"PBKDF2-SHA256","it":it,"salt":b(salt),"iv":b(iv),"ct":b(ct)},open(out,'w'))
print("geschrieben:",os.path.abspath(out))
