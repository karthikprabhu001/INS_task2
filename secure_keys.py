from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import os

# AES Key Generation and Storage
def generate_aes_key():
    key = os.urandom(32)
    with open("aes_key.bin", "wb") as f:
        f.write(key)
    print("AES Key Stored Securely.")

# RSA Key Pair Generation
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open("rsa_private.pem", "wb") as f:
        f.write(private_key)
    with open("rsa_public.pem", "wb") as f:
        f.write(public_key)
    
    print("RSA Key Pair Created.")

# Key Revocation
def revoke_key(key_file):
    if os.path.exists(key_file):
        os.rename(key_file, key_file + ".revoked")
        print(f"Key {key_file} has been revoked.")
    else:
        print("Key not found.")
