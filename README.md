Project Structure :
  ├───hash
  ├───keys
  └───utils
  |_main.py

  has dir  - contain all the functions for hashing and encryptions 
  keys dir - ment to store keys for rsa , not used 
  utils dir - contain utility functions

  main.py 
    - set the algorithum using getOption functions and options variable fron utils
    - create new Hash object and loop through texts variable to generate encoded and decoded texts using hash.encode/ hash.decode function
    - get user input to run the program again or close
    
  

1. Hashing Using MD5
     ![image](https://github.com/user-attachments/assets/24169348-020a-42c5-b1b2-87aeec317188)

2. Hashing usin SHA1
    ![image](https://github.com/user-attachments/assets/01fa5fca-f25b-4d01-a131-89f75b5e32c9)

    Similiraties and differences between MD5 and SHA1
         -  They are both hexadecimal strings with fixed sizes
         -  The size of MD5 hash is  16 bytes and 32 charactrers long
         - The size of SHA1 hash id 20 byytes and 40 charactrers long

3 RSA encryption and decryption
   Using 512 size key is not allowed
   ![image](https://github.com/user-attachments/assets/ca814add-2208-4aa2-94f0-913895cb9aa3)

   Using 1024 size key as suggested

   ![image](https://github.com/user-attachments/assets/54276056-79c1-4e20-8a7a-0c12024ea007)



