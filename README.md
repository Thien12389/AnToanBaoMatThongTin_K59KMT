# Bài tập An toàn và Bảo mật thông tin - K59KMT

## Thông tin sinh viên
- **Họ và tên:** Lê Đỗ Hoàng Thiện
- **Mã sinh viên:** K235480106068
- **Lớp:** K59KMT

---

## 1. Tìm hiểu thuật toán mã hóa hiện đại DES và AES

### Thuật toán DES (Data Encryption Standard)
- **Đặc điểm:** Là thuật toán mã hóa khối đối xứng, xử lý khối dữ liệu 64-bit với độ dài khóa 56-bit.
- **Quy trình:** Dựa trên mạng Feistel gồm 16 vòng biến đổi. Dữ liệu sau khi hoán vị ban đầu được chia làm 2 nửa trái/phải, sau đó trải qua các phép toán XOR với khóa con, đi qua hộp thay thế (S-box) và hộp hoán vị (P-box).
- **Hạn chế:** Độ dài khóa 56-bit quá ngắn, hiện nay dễ bị phá vỡ bằng phương pháp vét cạn (Brute-force).

### Thuật toán AES (Advanced Encryption Standard)
- **Đặc điểm:** Là thuật toán mã hóa khối đối xứng hiện đại thay thế DES. Xử lý khối dữ liệu 128-bit với các độ dài khóa 128, 192 hoặc 256-bit.
- **Quy trình:** Dựa trên mạng thay thế-hoán vị (SPN). Quá trình mã hóa gồm các vòng lặp (10, 12 hoặc 14 vòng tùy độ dài khóa). Mỗi vòng gồm 4 bước: `SubBytes`, `ShiftRows`, `MixColumns`, và `AddRoundKey`.
- **Cài đặt AES bằng Python:**
  *(Mã nguồn chi tiết được lưu trong file `src/aes_demo.py`)*
  
  **Kết quả chạy thực tế (Minh chứng):**
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/17493366-e4d1-4bb3-9f62-5df1cdb277ae" />


---

## 2. Tìm hiểu thuật toán mã hóa bất đối xứng RSA

### Nguyên lý sinh cặp khóa (Bí mật và Công khai)
RSA dựa trên độ khó của bài toán phân tích ra thừa số nguyên tố. Quy trình sinh khóa gồm 5 bước:
1. **Chọn số:** Chọn 2 số nguyên tố lớn ngẫu nhiên $p$ và $q$.
2. **Tính n:** Tính $n = p \times q$. (Độ dài của $n$ chính là độ dài khóa, ví dụ 2048-bit).
3. **Tính hàm Euler:** Tính $\phi(n) = (p - 1)(q - 1)$.
4. **Chọn khóa công khai (e):** Chọn số $e$ sao cho $1 < e < \phi(n)$ và $e$ nguyên tố cùng nhau với $\phi(n)$. 
5. **Tính khóa bí mật (d):** Tính $d$ là nghịch đảo module của $e$ theo module $\phi(n)$ sao cho: $(d \times e) \equiv 1 \pmod{\phi(n)}$.

=> **Kết quả:** Ta có Khóa công khai (Public Key) là $(e, n)$ và Khóa bí mật (Private Key) là $(d, n)$.

---

## 3. Các mô hình áp dụng thuật toán RSA

Thuật toán RSA được áp dụng vào 3 mô hình chính:

1. **Xác thực người nhận (Đảm bảo tính bảo mật - Confidentiality):**
   - Người gửi dùng Khóa công khai của người nhận để mã hóa dữ liệu.
   - Chỉ người nhận (nắm giữ Khóa bí mật của họ) mới có thể giải mã.
2. **Xác thực người gửi (Chữ ký số - Authentication):**
   - Người gửi dùng Khóa bí mật của chính mình để mã hóa (ký) dữ liệu.
   - Bất kỳ ai có Khóa công khai của người gửi đều có thể giải mã để xác minh người gửi, chống chối bỏ.
3. **Kết hợp cả hai:**
   - Dữ liệu được ký bằng Khóa bí mật của người gửi, sau đó toàn bộ gói tin được mã hóa bằng Khóa công khai của người nhận. Đảm bảo cả tính xác thực và bảo mật.

### So sánh thời gian mã hóa/giải mã: RSA vs AES
- **Tốc độ:** AES nhanh hơn RSA hàng ngàn lần. (AES dùng các phép toán XOR, dịch bit đơn giản; trong khi RSA phải tính lũy thừa trên các số nguyên khổng lồ).
- **Dữ liệu mã hóa:** AES mã hóa được luồng dữ liệu cực lớn (GB, TB). RSA bị giới hạn bởi độ dài khóa, chỉ mã hóa được dữ liệu rất nhỏ (vài trăm byte).

### Mô hình kết hợp sức mạnh RSA và AES (Mã hóa lai - Hybrid Cryptosystem)
Để tận dụng tốc độ của AES và khả năng phân phối khóa an toàn của RSA, thực tế sử dụng mô hình kết hợp:
1. **Mã hóa dữ liệu bằng AES:** Người gửi tạo một khóa đối xứng ngẫu nhiên (Session Key) và dùng nó cùng thuật toán AES để mã hóa khối dữ liệu lớn.
2. **Mã hóa khóa AES bằng RSA:** Người gửi dùng Khóa công khai RSA của người nhận để mã hóa cái Session Key ở bước 1.
3. **Gửi đi:** Người gửi truyền cả Dữ liệu đã mã hóa và Session Key đã mã hóa cho người nhận.
4. **Giải mã:** Người nhận dùng Khóa bí mật RSA giải mã để lấy lại Session Key, sau đó dùng Session Key để giải mã dữ liệu AES.
