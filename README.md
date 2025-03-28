
#### **Overview**
This project implements a **Secure Key Management System** that supports both **symmetric and asymmetric encryption**. It ensures **secure key generation, distribution, exchange, and revocation** using the following cryptographic techniques:
- **AES (Advanced Encryption Standard)** for symmetric encryption.
- **RSA (Rivest-Shamir-Adleman)** for asymmetric encryption.
- **Diffie-Hellman Key Exchange** for securely sharing keys over an untrusted network.

---

## **Project Structure**
```
/secure-key-management
│── secure_keys.py               # AES & RSA key generation and revocation
│── secure_exchange.py           # Diffie-Hellman key exchange implementation
│── main.py                      # Runs the system and tests key revocation
│── aes_key.bin                   # Generated AES key (example)
│── rsa_private.pem               # RSA Private Key (generated)
│── rsa_public.pem                # RSA Public Key (generated)
│── README.md                     # Project documentation
```

---

## **Features**
### ✅ **AES Key Generation & Storage**
- Generates a **secure 256-bit AES key**.
- Stores the AES key securely in a binary file.

### ✅ **RSA Key Pair Generation**
- Creates a **2048-bit RSA key pair**.
- Saves the **private** and **public** keys in separate files.

### ✅ **Secure Diffie-Hellman Key Exchange**
- Generates a **shared secret** between two parties without directly exchanging the key.
- Uses a **512-bit prime** and a generator to derive the shared secret.

### ✅ **Key Revocation**
- Allows **revocation of compromised keys** by renaming them to mark as revoked.

---

## **Installation**
### **Prerequisites**
- Python 3.x
- Install the required dependencies:
  ```sh
  pip install pycryptodome
  ```

---

## **Usage**
### **Step 1: Generate AES & RSA Keys**
Run the following command:
```sh
python main.py
```
This will generate:
- `aes_key.bin` (AES key)
- `rsa_private.pem` (RSA private key)
- `rsa_public.pem` (RSA public key)

---

### **Step 2: Perform Secure Key Exchange**
The **Diffie-Hellman algorithm** securely establishes a shared key between two parties.  
The shared secret key is verified to be the same on both ends.

---

### **Step 3: Revoke a Key**
To revoke an existing key, the system renames it with a `.revoked` extension.
Example:
```python
revoke_key("aes_key.bin")
```
This will rename `aes_key.bin` to `aes_key.bin.revoked`, preventing further usage.

---

## **Security Considerations**
- **Man-in-the-Middle (MITM) Protection**  
  - RSA public keys are securely stored.
  - Diffie-Hellman ensures a shared key is computed securely.

- **Key Compromise Protection**  
  - Private keys are stored in separate encrypted files.
  - Regular key rotation and revocation mechanisms are in place.

---

## **Future Improvements**
- Implement **Hardware Security Module (HSM)** for stronger key storage.
- Add **TLS encryption** to secure key exchanges.
- Introduce **automated key rotation policies**.

---

This README provides a clear guide on how to use and understand the Secure Key Management System. Let me know if you need any modifications! 🚀
