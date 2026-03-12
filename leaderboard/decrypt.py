import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def decrypt_file():
    private_key_pem = os.getenv("PRIVATE_KEY")
    if not private_key_pem:
        print("Erreur : Clé privée manquante dans les secrets.")
        return

    # Charger la clé privée
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None
    )

    # Chercher le fichier .enc dans submissions/
    sub_dir = 'submissions'
    files = [f for f in os.listdir(sub_dir) if f.endswith('.enc')]
    
    if not files:
        print("Aucun fichier .enc trouvé.")
        return

    for file_name in files:
        with open(os.path.join(sub_dir, file_name), "rb") as f:
            encrypted_data = f.read()
        
        # Décryptage
        decrypted_data = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Sauvegarder le résultat pour le leaderboard
        with open("leaderboard/last_result.csv", "wb") as f:
            f.write(decrypted_data)
        print(f"Fichier {file_name} décrypté avec succès.")

if __name__ == "__main__":
    decrypt_file()
