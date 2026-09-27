import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(plaintext: str, key: bytes) -> bytes:
    # Sinh ngẫu nhiên Vector khởi tạo IV (16 bytes) cho chế độ CBC
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Đệm dữ liệu theo chuẩn PKCS7 cho đủ bội số 16 bytes
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)

    # Ghép IV vào đầu bản mã để phục vụ giải mã
    return iv + ciphertext


def aes_decrypt(ciphertext_with_iv: bytes, key: bytes) -> str:
    # Tách 16 bytes đầu làm IV và phần còn lại là Ciphertext
    iv = ciphertext_with_iv[:16]
    ciphertext = ciphertext_with_iv[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)

    # Bỏ đệm PKCS7 và giải mã về chuỗi UTF-8 ban đầu
    plaintext = unpad(padded_data, AES.block_size)
    return plaintext.decode('utf-8')


# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == "__main__":
    # Khóa bí mật 128-bit (ĐÚNG 16 BYTES CHUẨN AES-128)
    key = b'K59KMT_BaoMat_12'
    message = "Lê Đỗ Hoàng Thiện - K235480106068 - Môn An toàn và Bảo mật thông tin"

    print("=== DEMO MÃ HÓA VÀ GIẢI MÃ AES (CBC MODE) ===")
    print(f"[+] Văn bản gốc: {message}\n")

    # 1. Thực hiện mã hóa
    encrypted_bytes = aes_encrypt(message, key)
    print(f"[+] Bản mã (dạng Hex): {encrypted_bytes.hex()}\n")

    # 2. Thực hiện giải mã
    decrypted_text = aes_decrypt(encrypted_bytes, key)
    print(f"[+] Kết quả giải mã: {decrypted_text}")