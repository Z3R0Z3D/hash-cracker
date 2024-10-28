import hashlib
from colorama import init, Fore, Style

init(autoreset=True)

def hash_password(password, hash_type):
    hash_functions = {
        'lm': lambda p: "LM_HASH",
        'ntlm': lambda p: hashlib.new('md4', p.encode('utf-16le')).hexdigest(),
        'md2': lambda p: hashlib.md2(p.encode()).hexdigest(),
        'md4': lambda p: hashlib.new('md4', p.encode()).hexdigest(),
        'md5': lambda p: hashlib.md5(p.encode()).hexdigest(),
        'sha1': lambda p: hashlib.sha1(p.encode()).hexdigest(),
        'sha224': lambda p: hashlib.sha224(p.encode()).hexdigest(),
        'sha256': lambda p: hashlib.sha256(p.encode()).hexdigest(),
        'sha384': lambda p: hashlib.sha384(p.encode()).hexdigest(),
        'sha512': lambda p: hashlib.sha512(p.encode()).hexdigest(),
        'ripemd160': lambda p: hashlib.new('ripemd160', p.encode()).hexdigest(),
        'whirlpool': lambda p: hashlib.new('whirlpool', p.encode()).hexdigest(),
    }

    if hash_type in hash_functions:
        return hash_functions[hash_type](password)
    else:
        raise ValueError("Unsupported hash type")

def crack_hash(hash_to_crack, wordlist_file, hash_type):
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as file:
            for line in file:
                password = line.strip()
                hashed_password = hash_password(password, hash_type)
                if hashed_password == hash_to_crack:
                    return password
        return None
    except FileNotFoundError:
        print(f"File '{wordlist_file}' Not Found")
        return None

def main():
    print("""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                           ---   Hash Cracker   ---                              ║
║                                                                                 ║
║ Supports: lm, ntlm, md2, md4, md5, sha1, sha224, sha256, sha384, sha512,        ║
║ ripemd160, whirlpool                                                            ║
║                                                                                 ║
║ Channel  = >  @zero0sec                                                         ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
""")
    
    hash_input = input(f"{Fore.GREEN}Please enter your hash: {Style.RESET_ALL}").strip()
    wordlist_path = input(f"{Fore.GREEN}Please enter your wordlist: {Style.RESET_ALL}").strip()
    hash_type = input(f"{Fore.GREEN}Please enter the hash type: {Style.RESET_ALL}").strip().lower()

    cracked_password = crack_hash(hash_input, wordlist_path, hash_type)

    if cracked_password:
        print(f"Success!: '{cracked_password}'")
    else:
        print("Not Found!")

if __name__ == "__main__":
    main()