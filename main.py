from secure_keys import generate_aes_key, generate_rsa_keys, revoke_key
from secure_exchange import diffie_hellman_key_exchange

generate_aes_key()
generate_rsa_keys()
diffie_hellman_key_exchange()

# Example key revocation
revoke_key("aes_key.bin")
