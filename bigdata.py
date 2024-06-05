from PIL import Image, ImageFilter
import pickle

binary_file_path = 'data.bin'
superdatos = []
image_path = 'cap.png'  
image = Image.open(image_path)

def map_to_hex_range(value, input_start=0, input_end=255, output_start=1, output_end=15):
    # Ensure the value is within the valid range
    if not (input_start <= value <= input_end):
        raise ValueError("Value out of range. Must be between 0 and 255.")
    
    # Map the value from input range to output range
    proportion = (value - input_start) / (input_end - input_start)
    mapped_value = output_start + proportion * (output_end - output_start)
    
    # Convert the mapped value to the nearest integer and then to hexadecimal
    hex_value = hex(int(round(mapped_value)))[2:]  # [2:] to remove the '0x' prefix
    return hex_value.upper()  # Convert to uppercase if needed  



blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5)) 

for x in range(0,100):
    for y  in range(0,100):
        mibloque = ""
        bloque = blurred_image.crop((x,y,x+10,y+10))
        pixel_data = list(bloque.getdata())
        for dato in pixel_data: 
            mibloque += (map_to_hex_range(dato[0]))
        superdatos.append(mibloque)

with open(binary_file_path, 'wb') as file:
    pickle.dump(superdatos, file)
