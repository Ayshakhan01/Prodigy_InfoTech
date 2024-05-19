# from PIL import Image
# import numpy as np

# def encrypt_image(image_path, key):
#     # Open the image
#     img = Image.open(image_path)
    
#     # Convert image to numpy array
#     img_array = np.array(img)
    
#     # Apply encryption algorithm (example: XOR with key)
#     encrypted_img_array = img_array ^ key
    
#     # Convert back to image
#     encrypted_img = Image.fromarray(encrypted_img_array)
    
#     return encrypted_img

# def decrypt_image(encrypted_image, key):
#     # Convert image to numpy array
#     encrypted_img_array = np.array(encrypted_image)
    
#     # Apply decryption algorithm
#     decrypted_img_array = encrypted_img_array ^ key
    
#     # Convert back to image
#     decrypted_img = Image.fromarray(decrypted_img_array)
    
#     return decrypted_img

# def main():
#     # Path to the input image
#     image_path = "mango.jpeg"
    
#     # Encryption key
#     key = 123
    
#     # Encrypt the image
#     encrypted_img = encrypt_image(image_path, key)
#     encrypted_img.show()
    
#     # Save the encrypted image
#     encrypted_img.save("encrypted_image.jpg")
    
#     # Decrypt the image
#     decrypted_img = decrypt_image(encrypted_img, key)
#     decrypted_img.show()
    
#     # Save the decrypted image
#     decrypted_img.save("decrypted_image.jpg")

# if __name__ == "__main__":
#     main()


from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Apply encryption algorithm (example: XOR with key)
    encrypted_img_array = img_array ^ key
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_img_array)
    
    return encrypted_img

def decrypt_image(encrypted_image, key):
    # Convert image to numpy array
    encrypted_img_array = np.array(encrypted_image)
    
    # Apply decryption algorithm
    decrypted_img_array = encrypted_img_array ^ key
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_img_array)
    
    return decrypted_img

def main():
    # Path to the input image
    image_path = input("Enter the path to the input image: ")
    
    # Encryption key
    key = int(input("Enter the encryption/decryption key: "))
    
    # Ask user whether to encrypt or decrypt
    operation = input("Do you want to encrypt or decrypt the image? (encrypt/decrypt): ").lower()
    
    if operation == "encrypt":
        # Encrypt the image
        encrypted_img = encrypt_image(image_path, key)
        encrypted_img.show()
        
        # Save the encrypted image
        encrypted_img.save("encrypted_image.jpg")
        
    elif operation == "decrypt":
        # Decrypt the image
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        encrypted_img = Image.open(encrypted_image_path)
        
        decrypted_img = decrypt_image(encrypted_img, key)
        decrypted_img.show()
        
        # Save the decrypted image
        decrypted_img.save("decrypted_image.jpg")
        
    else:
        print("Invalid operation. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
