def encrypt_psycho(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            result += shifted_char
        else:
            result += char
    return result

def decrypt_psycho(encrypted_text, shift):
    return encrypt_psycho(encrypted_text, -shift)

def is_encrypted(text, shift):
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 
                    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
                    'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
                    'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what']
    decrypted_version = decrypt_psycho(text, shift)
    text_lower = text.lower()
    decrypted_lower = decrypted_version.lower()
    original_matches = sum(1 for word in common_words if word in text_lower)
    decrypted_matches = sum(1 for word in common_words if word in decrypted_lower)
    return decrypted_matches > original_matches

def auto_process(text, shift):
    if is_encrypted(text, shift):
        result = decrypt_psycho(text, shift)
        print(f"Input detected as ENCRYPTED")
        print(f"Decrypted result: {result}")
        return result
    else:
        result = encrypt_psycho(text, shift)
        print(f"Input detected as DECRYPTED")
        print(f"Encrypted result: {result}")
        return result

def psycho_pentester_menu():
    print("=" * 50)
    print("PSYCHO PENTESTER")
    print("=" * 50)
    while True:
        print("\nChoose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Auto detect and process")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == '4':
            print("Goodbye!")
            break
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            continue
        text = input("Enter your text: ")
        shift = int(input("Enter shift amount: "))
        print("\n" + "-" * 50)
        if choice == '1':
            result = encrypt_psycho(text, shift)
            print(f"Encrypted: {result}")
        elif choice == '2':
            result = decrypt_psycho(text, shift)
            print(f"Decrypted: {result}")
        elif choice == '3':
            auto_process(text, shift)
        print("-" * 50)

psycho_pentester_menu()