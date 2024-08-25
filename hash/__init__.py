from .md5 import MD5
from .sha1 import SHA1
from .rsa import RSAEncryptor
class Hash():
    md5 = None
    sha1 = None
    rsa  = None
    def __init__(self) -> None:
          pass
    def encode(self,text,algo):
        if(algo == 'MD5'):
            self.md5 = MD5()
            return  self.md5.encode(text)
        if(algo == 'SHA1'):
            self.sha1 = SHA1()
            return self.sha1.encode(text)
        if(algo == 'RSA'):
            self.rsa = RSAEncryptor()
            return self.rsa.encode(text)
        else:
            return None

    def decode(self,encoded,algo):
        if(algo == 'RSA'):
            if(self.rsa):
                return self.rsa.decode(encoded) 
        else:
            return None