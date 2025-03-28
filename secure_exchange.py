from Crypto.Util import number

def diffie_hellman_key_exchange():
    p = number.getPrime(512)  # Large prime
    g = 2  # Generator

    # Simulating two parties
    a = number.getRandomRange(1, p)
    A = pow(g, a, p)
    
    b = number.getRandomRange(1, p)
    B = pow(g, b, p)

    # Shared secret calculation
    shared_secret_A = pow(B, a, p)
    shared_secret_B = pow(A, b, p)

    assert shared_secret_A == shared_secret_B  # Should be the same for both
    print("Secure DH Key Exchange Completed.")
