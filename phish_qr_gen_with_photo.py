#!/usr/bin/env python3

import qrcode
from PIL import Image, ImageDraw, ImageFont

def embed_qr_on_image(phish_url, background_image_path, message, output_file, qr_size=200, qr_position=(50, 50)):
    try:
        bg_image = Image.open(background_image_path).convert("RGB")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )
        qr.add_data(phish_url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        qr_img = qr_img.resize((qr_size, qr_size))

        bg_image.paste(qr_img, qr_position)

        draw = ImageDraw.Draw(bg_image)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
        except:
            font = ImageFont.load_default()

        text_position = (qr_position[0], qr_position[1] + qr_size + 10)
        draw.text(text_position, message, fill="black", font=font)

        bg_image.save(output_file)
        print(f"[+] Phishing image created: {output_file}")

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    print("""
  ____  _     _     _     ____  ____  ____ 
 /  __\/ \ /\/ \ /\/ \ /\/  _ \/ ___\/  _ \\
 | | //| | ||| | ||| | ||| / \||    \| / \|
 | |_\\| \_/|| \_/|| \_/|| \_/|\___ || \_/|
 \____/\____/\____/\____/\____/\____/\____/

 Embed QR Code on Photo (Phishing Tool)
     Authorized Testing Use Only
""")

    phish_url = input("[?] Enter phishing URL: ").strip()
    background_image_path = input("[?] Path to background image (e.g., poster.jpg): ").strip()
    message = input("[?] Message to display (e.g., 'Scan to get free Wi-Fi'): ").strip()
    output_file = input("[?] Output filename (e.g., final_qr_promo.png): ").strip()

    embed_qr_on_image(phish_url, background_image_path, message, output_file)
