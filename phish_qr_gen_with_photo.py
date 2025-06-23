#!/usr/bin/env python3

import qrcode
from PIL import Image, ImageDraw, ImageFont
import argparse
import os
import sys

def embed_qr_on_image(phish_url, background_image_path, message, output_file, qr_size=200, qr_margin=40):
    if not os.path.exists(background_image_path):
        sys.exit(f"[-] Error: Image '{background_image_path}' not found.")
    if not phish_url.startswith("http://") and not phish_url.startswith("https://"):
        sys.exit("[-] Error: Please provide a valid URL starting with http:// or https://")

    try:
        # Load background image
        bg_image = Image.open(background_image_path).convert("RGB")
        bg_width, bg_height = bg_image.size

        # Generate QR code
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

        # Position QR bottom right
        qr_x = bg_width - qr_size - qr_margin
        qr_y = bg_height - qr_size - qr_margin
        bg_image.paste(qr_img, (qr_x, qr_y))

        # Add message below QR
        draw = ImageDraw.Draw(bg_image)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
        except:
            font = ImageFont.load_default()

        text_x = qr_x
        text_y = qr_y + qr_size + 5
        draw.text((text_x, text_y), message, fill="black", font=font)

        # Save output
        bg_image.save(output_file)
        print(f"[+] QR phishing image saved as: {output_file}")

    except Exception as e:
        sys.exit(f"[-] Error processing image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Phishing QR Generator for authorized red team operations.")
    parser.add_argument('-u', '--url', required=True, help="Phishing or redirect URL")
    parser.add_argument('-i', '--image', required=True, help="Path to background image")
    parser.add_argument('-m', '--message', required=True, help="Message to appear below QR")
    parser.add_argument('-o', '--output', required=True, help="Output file name (e.g. promo_qr.png)")
    parser.add_argument('--qrsize', type=int, default=200, help="Size of QR code in pixels (default: 200)")

    args = parser.parse_args()

    embed_qr_on_image(
        phish_url=args.url,
        background_image_path=args.image,
        message=args.message,
        output_file=args.output,
        qr_size=args.qrsize
    )

if __name__ == "__main__":
    main()
