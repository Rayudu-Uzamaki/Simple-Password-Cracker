import itertools
import string

def brute_force_attack(target_password, max_length):
    """
    Attempts to brute force the target password by trying all possible
    character combinations up to the specified maximum length.

    Args:
        target_password (str): The password to crack.
        max_length (int): The maximum length of passwords to try.

    Returns:
        str: The cracked password if found, or a failure message.
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

    print(f"Starting brute force attack on password '{target_password}'...")
    for length in range(1, max_length + 1):
        print(f"Trying passwords of length {length}...")
        for attempt in itertools.product(characters, repeat=length):
            attempt = ''.join(attempt)
            if attempt == target_password:
                return f"Password cracked using brute force: {attempt}"
    return "Password not found using brute force."

def dictionary_attack(target_password, dictionary_file):
    """
    Attempts to crack the target password using a dictionary attack.

    Args:
        target_password (str): The password to crack.
        dictionary_file (str): Path to a text file containing dictionary words.

    Returns:
        str: The cracked password if found, or a failure message.
    """
    try:
        with open(dictionary_file, 'r') as file:
            print(f"Starting dictionary attack on password '{target_password}'...")
            for line in file:
                word = line.strip()
                if word == target_password:
                    return f"Password cracked using dictionary: {word}"
    except FileNotFoundError:
        return "Dictionary file not found."
    return "Password not found in dictionary."

if __name__ == "__main__":
    # User inputs
    target_password = input("Enter the password to crack: ").strip()
    attack_type = input("Choose attack type (brute/dictionary): ").strip().lower()

    if attack_type == "brute":
        max_length = int(input("Enter the maximum password length to try: ").strip())
        result = brute_force_attack(target_password, max_length)
        print(result)
    elif attack_type == "dictionary":
        dictionary_file = input("Enter the path to the dictionary file: ").strip()
        result = dictionary_attack(target_password, dictionary_file)
        print(result)
    else:
        print("Invalid attack type selected.")
