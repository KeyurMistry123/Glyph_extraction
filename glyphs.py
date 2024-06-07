from PIL import Image, ImageDraw, ImageFont
import os

def extract_glyphs(font_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    font = ImageFont.truetype(font_path, size=100)
    for char_code in range(32, 127):  # ASCII range for printable characters
        char = chr(char_code)
        # Replace invalid characters with underscores
        char_safe = ''.join(e if e.isalnum() else '_' for e in char)
        image = Image.new('L', (120, 120), color=255)
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), char, font=font, fill=0)
        image_path = os.path.join(output_dir, f"{char_code}_{char_safe}.png")
        image.save(image_path)

# Actual paths
font1_path = r"C:\Users\Keyur Mistry\Desktop\Font_merge_project\Font_dataset\Foldit-VariableFont_wght.ttf"
font2_path = r"C:\Users\Keyur Mistry\Desktop\Font_merge_project\Font_dataset\Tiny5-Regular.ttf"
output_dir1 = r"C:\Users\Keyur Mistry\Desktop\Font_merge_project\Glyphs_font\glyphs_1"
output_dir2 = r"C:\Users\Keyur Mistry\Desktop\Font_merge_project\Glyphs_font\glyphs_2"

extract_glyphs(font1_path, output_dir1)
extract_glyphs(font2_path, output_dir2)

