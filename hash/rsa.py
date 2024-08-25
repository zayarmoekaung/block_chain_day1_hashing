from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

class RSAEncryptor:
    def __init__(self) -> None:
        self.key = None

    def generate_key(self):
        try:
            # Generate a new RSA key 
            random_generator = get_random_bytes
            self.key = RSA.generate(512, random_generator)
        except Exception as e:
            print(f"Error generating key: {e}")
            self.key = None

    def encode(self, text):
        try:
            if not self.key:
                self.generate_key()
            if not self.key:
                raise ValueError("RSA key generation failed.")

            if isinstance(text, str):
                text = text.encode('utf-8')
            elif not isinstance(text, bytes):
                raise TypeError("Text must be a string or bytes.")

            # Use PKCS1_OAEP for encryption
            public_key = self.key.publickey()
            cipher_encrypt = PKCS1_OAEP.new(public_key)
            encrypted = cipher_encrypt.encrypt(text)
            return encrypted

        except Exception as e:
            print(f"Error encoding text: {e}")
            return None

    def decode(self, encrypted_text):
        try:
            if not self.key:
                raise ValueError("RSA key is not generated or set.")

            # Use PKCS1_OAEP for decryption
            cipher_decrypt = PKCS1_OAEP.new(self.key)
            decrypted = cipher_decrypt.decrypt(encrypted_text)
            return decrypted.decode('utf-8')  

        except (ValueError, TypeError) as e:
            print(f"Error decoding text: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error during decryption: {e}")
            return None
