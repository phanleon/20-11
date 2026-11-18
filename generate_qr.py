#!/usr/bin/env python3
"""
Script tạo mã QR độ phân giải cao cho Thiệp Điện Tử 20/11
Trỏ trực tiếp đến URL GitHub Pages công khai:
https://phanleon.github.io/20-11/
"""

import urllib.request
import urllib.parse
import os

def generate_qr():
    url = "https://phanleon.github.io/20-11/"
    output_file = "qr_20_11.png"
    
    # Sử dụng bảng màu Royal Navy & Champagne Gold (#081229 và #fbf5df)
    qr_api = (
        "https://api.qrserver.com/v1/create-qr-code/?"
        "size=1000x1000&margin=20&color=081229&bgcolor=fbf5df&data="
        + urllib.parse.quote(url)
    )
    
    print(f"[*] Đang tải mã QR từ API cho URL: {url} ...")
    try:
        urllib.request.urlretrieve(qr_api, output_file)
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            print(f"[✓] Đã tạo thành công mã QR chất lượng cao tại '{output_file}'!")
            print(f"[✓] Kích thước tệp: {os.path.getsize(output_file)} bytes")
            print(f"[✓] Đích đến: {url}")
        else:
            print("[!] Cảnh báo: Tệp tạo ra có kích thước 0 byte.")
    except Exception as e:
        print(f"[X] Lỗi khi tạo mã QR: {e}")

if __name__ == "__main__":
    generate_qr()
