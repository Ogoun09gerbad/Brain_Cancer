import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt_file(input_path, public_key_path, output_path):
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    with open(input_path, "rb") as f:
        data = f.read()
    
    # Chiffrement par blocs (RSA)
    chunk_size = 190
    encrypted = b""
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        encrypted += public_key.encrypt(
            chunk,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
    with open(output_path, "wb") as f:
        f.write(encrypted)
    print(f"✅ Fichier chiffré créé : {output_path}")

if __name__ == "__main__":
    encrypt_file(sys.argv[1], sys.argv[2], sys.argv[3])
