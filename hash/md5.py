import hashlib
class MD5():
     def __init__(self) -> None:
          pass
     def encode(self,text):
          try:
               if not isinstance(text, str):
                    raise TypeError("The input must be a string.")
               encoded_text = text.encode('utf-8')
               hashobject = hashlib.md5(encoded_text)
               result = hashobject.hexdigest()
               
               return result

          except TypeError as e:
               print(f"Error: {e}")
               return None
          except Exception as e:
               print(f"Unexpected error: {e}")
               return None