# Thiệp Điện Tử Tri Ân Ngày Nhà Giáo Việt Nam 20/11
### Luxury Interactive Web App – Phong Cách Hoàng Gia & Di Sản Việt

Trang web thiệp điện tử tương tác cao cấp chúc mừng Ngày Nhà Giáo Việt Nam 20/11, được thiết kế theo phong cách Hoàng gia sang trọng (Royal Navy & Champagne Gold), kết hợp biểu tượng văn hóa Việt Nam (Trống Đồng Đông Sơn, Hoa Sen Vàng) và hiệu ứng thị giác 3D, hạt Canvas mượt mà, âm thanh du dương bằng Web Audio API.

---

## 🌟 Điểm Nổi Bật

- **Zero-Build Architecture:** Toàn bộ HTML, CSS (Tailwind CDN), JavaScript, inline SVG và Canvas nằm gọn trong tệp duy nhất `index.html`. Không cần bundler, không phụ thuộc file mp3 hay ảnh ngoài.
- **Phong bì 3D & Dấu sáp hoàng gia:** Chạm nhẹ vào ấn sáp 3D dập nổi phát sáng để mở nắp phong bì, kích hoạt pháo hoa bụi vàng và bật nhạc nền.
- **Thiệp chính Glassmorphism & Nghiêng 3D:** Card chính sử dụng hiệu ứng kính mờ `backdrop-filter: blur(20px)` phản chiếu ánh sáng và nghiêng theo con trỏ chuột hoặc thao tác chạm.
- **Họa tiết Di sản Văn hóa Việt Nam:**
  - **Trống đồng Đông Sơn:** Mặt trời 12 tia sáng và chim Lạc xoay chậm chìm ở nền card.
  - **Hoa sen vàng:** Biểu tượng thanh cao, thuần khiết được cách điệu tinh tế.
- **Thước Phim Ký Ức 5 Cảnh Hoạt Họa (Cinematic Memory Reel):** Trình chiếu chuyển động sống động với 5 cảnh ý nghĩa:
  1. 🌸 **Dâng Hoa Tri Ân:** Cô giáo dắt tay học trò nhỏ, các em tươi cười dâng bó hoa sen & hướng dương rực rỡ, cánh hoa bay lượn nhẹ nhàng.
  2. ✍️ **Bụi Phấn Bục Giảng:** Thầy giáo đứng bên bảng đen, bàn tay viết bài và bụi phấn rơi lấp lánh trên bục giảng, vương trên mái tóc thầy.
  3. 🪁 **Sân Trường Tuổi Thơ:** Sân trường rợp bóng cây bàng và phượng vĩ rực rỡ, học trò đọc sách, máy bay giấy chao liệng giữa trời nắng vàng.
  4. 🏆 **Cúp Vàng Thành Công:** Học trò khôn lớn tốt nghiệp áo cử nhân, giương cao Cúp Vàng vô địch và Huy Chương Vàng lấp lánh ánh hào quang.
  5. 👏 **Tự Hào Thầy Cô:** Thầy cô tóc điểm hoa râm mỉm cười tự hào, ánh mắt rạng ngời xúc động và đôi bàn tay vỗ tay chúc mừng nhịp nhàng.
- **Nhạc Nền "Bụi Phấn" Piano Solo Không Lời (Web Audio API):** Mô phỏng chân thực tiếng đàn Piano mộc mạc, sâu lắng qua hợp âm và giai điệu bài hát bất hủ *"Bụi Phấn"*, tự động phát khi mở dấu sáp và có nút bật/tắt tiện lợi.
- **Mưa cánh hoa & Pháo hoa Canvas 60 FPS:** 3 lớp hạt chuyển động độc lập (Bụi vàng lơ lửng, Pháo hoa nổ bung, Mưa cánh sen lượn sóng).
- **Cá nhân hóa linh hoạt qua URL:** Hỗ trợ tham số `?to=...&from=...` hiển thị tên người nhận và người gửi trên cả phong bì lẫn nội dung thiệp.

---

## 🔗 Liên Kết & Quét Mã QR

- **Trang chủ GitHub Pages:** [https://phanleon.github.io/20-11/](https://phanleon.github.io/20-11/)
- **Mã QR truy cập nhanh:** Quét ảnh `qr_20_11.png` có sẵn trong thư mục gốc.

![Mã QR 20/11](qr_20_11.png)

---

## 💌 Cấu Trúc URL Cá Nhân Hóa

Bạn có thể tạo link thiệp riêng biệt để gửi tặng từng Thầy Cô hoặc đại diện cho từng tập thể:

| Tham số | Ý nghĩa | Ví dụ |
| :--- | :--- | :--- |
| `to` | Tên Thầy/Cô hoặc Quý Thầy Cô nhận thiệp | `to=Thầy%20Nguyễn%20Văn%20A` |
| `from` | Tên người gửi, nhóm hoặc lớp tri ân | `from=Tập%20thể%20Lớp%2012A1` |

### Ví dụ liên kết hoàn chỉnh:
```text
https://phanleon.github.io/20-11/?to=Cô%20Nguyễn%20Thị%20Mai&from=Tập%20thể%20Sinh%20viên%20–%20Học%20viện%20Hàng%20không%20Việt%20Nam
```

Người dùng cũng có thể mở trực tiếp bảng **Cá nhân hóa lời chúc** ngay trên giao diện web (nút bút chỉnh sửa ở góc trên bên phải) để nhập tên và bấm nút **"Sao Chép Link"**.

---

## 📂 Cấu Trúc Tệp Dự Án

```text
20-11/
├── index.html          # Toàn bộ mã nguồn giao diện, Canvas FX & Web Audio Engine
├── generate_qr.py      # Script Python tạo mã QR độ phân giải cao
├── qr_20_11.png        # Hình ảnh mã QR trỏ tới GitHub Pages
└── README.md           # Tài liệu hướng dẫn sử dụng & tham số URL
```

---

## 🚀 Kích Hoạt GitHub Pages

Sau khi đẩy mã nguồn lên GitHub repository `phanleon/20-11`:
1. Vào repository trên GitHub: `https://github.com/phanleon/20-11`
2. Chọn **Settings** > **Pages** (ở cột bên trái)
3. Tại mục **Build and deployment > Source**, chọn **Deploy from a branch**
4. Chọn Branch: **`main`**, folder: **`/ (root)`**, sau đó bấm **Save**
5. Chờ 1–2 phút để trang web sẵn sàng tại: `https://phanleon.github.io/20-11/`

---

*Kính chúc Quý Thầy Cô giáo luôn tràn đầy sức khỏe, hạnh phúc và luôn giữ vững ngọn lửa nhiệt huyết vì sự nghiệp trồng người!*
