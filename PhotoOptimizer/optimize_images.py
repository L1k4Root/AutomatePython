import os
from PIL import Image
import io

# Script: optimize_images.py
# Usage: Place this script in your target image folder and run `python optimize_images.py`
# Requires: pip install pillow

TARGET_SIZE = 4.5 * 1024 * 1024  # 5MB threshold
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png')

def compress_image(file_path):
    img = Image.open(file_path)
    # Convert PNG to JPEG for better compression if necessary
    if img.format == 'PNG':
        img = img.convert('RGB')
        save_format = 'JPEG'
        output_path = os.path.splitext(file_path)[0] + '.jpg'
    else:
        save_format = img.format
        output_path = file_path

    quality = 85
    while quality >= 20:
        buffer = io.BytesIO()
        img.save(buffer, format=save_format, quality=quality, optimize=True)
        size = buffer.tell()
        if size <= TARGET_SIZE:
            with open(output_path, 'wb') as f:
                f.write(buffer.getvalue())
            print(f'✅ Compressed {file_path} ➞ {output_path} to {size/1024/1024:.2f}MB at quality={quality}')
            # Remove original if converted from PNG to JPG
            if file_path != output_path:
                os.remove(file_path)
            return
        quality -= 5

    print(f'⚠️ Could not compress {file_path} below 5MB (final size: {size/1024/1024:.2f}MB).')

def main():
    for filename in os.listdir('.'):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            size = os.path.getsize(filename)
            if size > TARGET_SIZE:
                compress_image(filename)
            else:
                print(f'✔️ Skipped {filename} ({size/1024/1024:.2f}MB)')

if __name__ == '__main__':
    main()