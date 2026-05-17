#!/usr/bin/env python3
"""
Regenerate the QR code that points to your live listing URL.

Usage:
    python3 generate-qr.py https://your-username.github.io/willowbrook-listing/

Requires: pip install qrcode[pil]
"""
import sys
import qrcode


def generate(url: str, output: str = "qr-placeholder.png") -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#1d1d1f", back_color="white")
    img.save(output)
    print(f"QR code saved: {output} ({img.size[0]}x{img.size[1]}px)")
    print(f"  URL: {url}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate-qr.py <URL>")
        sys.exit(1)
    generate(sys.argv[1])
