import hashlib

def hash_string(string):
    # Create a hashlib object
    hasher = hashlib.sha256()
    
    # Update the hasher with the string
    hasher.update(string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hashed_string = hasher.hexdigest()
    
    return hashed_string

def main():
    while True:
        user_input = input("Enter a string to hash (press Enter to quit): ")
        
        if not user_input:
            print("No input provided. Exiting...")
            break
        
        hashed_result = hash_string(user_input)
        print("Hashed Result:", hashed_result)

if __name__ == "__main__":
    main()