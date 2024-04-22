def xor_encrypt(input_text, key):
    # Перетворення ключа в байти, якщо це ще не байти
    key_bytes = key.encode() if isinstance(key, str) else key
    encrypted_bytes = bytearray()
    
    # Шифрування кожного байта тексту
    for i, byte in enumerate(input_text):
        encrypted_bytes.append(byte ^ key_bytes[i % len(key_bytes)])
    
    return bytes(encrypted_bytes)

def main():
    input_file = 'Lorem-ipsum-dolor-sit-amet.txt'  # Шлях до вхідного файлу
    output_file = 'encrypted.txt'  # Шлях до вихідного файлу
    key = 'secret'  # Ключ шифрування

    # Читання тексту з файлу
    with open(input_file, 'rb') as file:
        input_text = file.read()

    # Шифрування тексту
    encrypted_text = xor_encrypt(input_text, key)

    # Запис зашифрованого тексту у файл
    with open(output_file, 'wb') as file:
        file.write(encrypted_text)

    print("Шифрування завершено. Зашифрований файл збережено як 'encrypted.txt'.")

if __name__ == '__main__':
    main()
