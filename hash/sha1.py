import hashlib

class SHA1():
    def __init__(self) -> None:
          pass
    def encode(self,text):
        try:
            if not isinstance(text, str):
                text = str(text)
            hashobject = hashlib.sha1()
            hashobject.update(text.encode('utf-8'))
            return hashobject.hexdigest()

        except Exception as e:
            print(f"Error: {e}")
            return None