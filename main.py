from hash import Hash
from utils import getOption,getBooleanInput,algorithums,texts

def start():
    algo = getOption(algorithums)
    print(f"\n Using ${algo} algorithum \n")
    hash = Hash()
    for text in texts:
        encoded = hash.encode(text,algo)

        if (encoded):
             print(f"Original Text : {text} \n")
             print(f"Encoded Text : \n {encoded} \n")
             decoded = hash.decode(encoded,algo)
             if(decoded):
                print("\n")                 
                print(f"Decoded Text : \n {decoded} \n")
        else:
            print(f"Encoding failed for text: {text} with algorithm: {algo}\n")
        print("_________________________________________________ \n")
    if ( getBooleanInput("Want to start aganin ?") ):
        return start()
    else:
        print("Closing")
        exit()
if __name__ == "__main__":        
    start()
