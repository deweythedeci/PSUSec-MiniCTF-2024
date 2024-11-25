import random

M = 256

def generate_keys(seed):
    random.seed()
    private_key = random.randint(1,M)
    public_key = None
    for i in range(1, M):
        if (private_key * i) % M == 1:
            public_key = i
            break
    return private_key, public_key

def encrypt(public_key, plaintext):
    ciphertext = ""
    for char in plaintext:
        ciphertext += hex((ord(char) * int(public_key)) % M)[2:].zfill(2)
    return ciphertext

def decrypt(private_key, ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += chr((int(ciphertext[i:i+2],16) * int(private_key)) % M)
    return plaintext

def main():
    while True:
        print("1. Generate keys")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Quit")

        choice = input("Enter an option: ").strip()

        if choice == '1':
            seed = input("Enter a seed for key generation: ").strip()
            public_key, private_key = generate_keys(seed)
            print(f"Keys generated! Public Key: {public_key}, Private Key: {private_key}")

        elif choice == '2':
            public_key = input("Enter the public key: ").strip()
            text = input("Enter the text you want to encrypt: ").strip()
            result = encrypt(public_key, text)
            print("Encrypted text: ", result)

        elif choice == '3':
            private_key = input("Enter the private key: ").strip()
            text = input("Enter the text you want to decrypt: ").strip()
            result = decrypt(private_key, text)
            print("Decrypted text: ", result)

        elif choice == '4' or choice.lower() == 'quit':
            print("Exiting program...")
            break

        else:
            print("Invalid input. Please enter a value 1 through 4.")

        print("")

if __name__ == "__main__":
    main()
