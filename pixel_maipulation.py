from PIL import Image

def encrypt(image_path, output_path):
    
    image = Image.open(image_path)
    
    image = image.convert("RGB")
    pixels = image.load()

   
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            
            pixels[i, j] = (255 - r, 255 - g, 255 - b)
    
 
    image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt(image_path, output_path):
   
    encrypt(image_path, output_path)  
    print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
   
    input_image = "python_img.png"
    encrypted_image = "encrypted.jpg"
    decrypted_image = "decrypted.jpg"

   
    encrypt(input_image, encrypted_image)
    decrypt(encrypted_image, decrypted_image)
