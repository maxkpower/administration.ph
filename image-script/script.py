import os
from PIL import Image

# Define the desired width and height
desired_width = 414
desired_height = 458

# Define the input and output directories
input_dir = 'input-img'
output_dir = 'output-webp'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def crop_image_to_size(image, width, height):
    img_width, img_height = image.size

    # Calculate the new dimensions while maintaining aspect ratio
    aspect_ratio = img_width / img_height
    target_aspect_ratio = width / height
    
    if aspect_ratio > target_aspect_ratio:
        # Image is wider than the target aspect ratio: crop the width
        new_width = int(height * aspect_ratio)
        new_height = height
    else:
        # Image is taller than the target aspect ratio: crop the height
        new_width = width
        new_height = int(width / aspect_ratio)

    # Resize the image to the new dimensions
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # Calculate the cropping box to center the image
    left = (new_width - width) / 2
    top = (new_height - height) / 2
    right = (new_width + width) / 2
    bottom = (new_height + height) / 2
    
    # Crop the image
    return resized_image.crop((left, top, right, bottom))

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
        # Open the image file
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        
        # Crop the image to the desired size
        cropped_img = crop_image_to_size(img, desired_width, desired_height)
        
        # Create the output file path
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')
        
        # Save the cropped image in WEBP format
        cropped_img.save(output_path, 'WEBP')

print(f"Images have been cropped to {desired_width}x{desired_height} and saved as WEBP in the '{output_dir}' directory.")
