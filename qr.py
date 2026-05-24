import os
import re
import sys
import qrcode

def sanitize_filename(name):
    name = name.strip()
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r"\s+", "_", name)
    return name or "qr_code"


def main():
    if len(sys.argv) >= 3:
        link = sys.argv[1].strip()
        qr_name = sys.argv[2].strip()
    else:
        link = input("Masukkan link: ").strip()
        qr_name = input("Masukkan nama QR: ").strip()

    if not link:
        print("Link tidak boleh kosong.")
        return

    if not qr_name:
        print("Nama QR tidak boleh kosong.")
        return

    filename = sanitize_filename(qr_name) + ".png"
    img = qrcode.make(link)
    img.save(filename)
    print(f"QR code berhasil dibuat: {filename}")


if __name__ == "__main__":
    main()
