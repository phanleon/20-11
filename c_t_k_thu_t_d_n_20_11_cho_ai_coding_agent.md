# Dự Án: Thiệp Điện Tử Tri Ân Ngày Nhà Giáo Việt Nam 20/11 (Luxury Interactive Web App)

> **Hướng dẫn dành cho AI Coding Agent:** Đọc kỹ toàn bộ đặc tả dưới đây và thực thi tuần tự các bước: (1) Tạo mã nguồn ứng dụng web tĩnh đơn tệp (`index.html`), (2) Khởi tạo Git & đẩy lên GitHub repository, (3) Kích hoạt GitHub Pages, và (4) Tạo mã QR trỏ trực tiếp tới URL công khai.

---

## 1. Mục Tiêu & Kiến Trúc Tổng Quan
- **Mục tiêu:** Xây dựng trang web thiệp chúc mừng Ngày Nhà Giáo Việt Nam (20/11) mang phong cách sang trọng, giàu bản sắc văn hóa Việt Nam, tối ưu hóa trải nghiệm chạm trên thiết bị di động khi người nhận quét mã QR.
- **Kiến trúc Zero-Build (Không cần bước biên dịch):** Toàn bộ HTML, CSS và JavaScript nằm gọn trong một tệp duy nhất `index.html` để triển khai tức thì lên **GitHub Pages** mà không phụ thuộc vào bundler (Webpack/Vite) hay tài nguyên media bên ngoài (không dùng file `.mp3` hay ảnh rời dễ lỗi đường dẫn).
- **Thư viện CDN cho phép:**
  - Tailwind CSS CDN (`https://cdn.tailwindcss.com`)
  - Google Fonts hỗ trợ đầy đủ dấu tiếng Việt: `Cormorant Garamond`, `Playfair Display`, và `Be Vietnam Pro`.

---

## 2. Hệ Thống Thiết Kế (Design System)
- **Bảng màu chủ đạo (Royal Navy & Champagne Gold):**
  - Nền tối hoàng gia: `#040917` (Navy 950), `#081229` (Navy 900), `#0e1f45` (Navy 800), `#162f66` (Navy 700).
  - Vàng ánh kim: `#fbf5df` (Gold 100), `#f3e3b3` (Gold 200), `#e6c875` (Gold 300), `#d4af37` (Gold 400), `#b89020` (Gold 500), `#8f6b10` (Gold 600).
- **Typography:**
  - Tiêu đề & Lời trích trang trọng: `Cormorant Garamond` / `Playfair Display` (hiệu ứng chữ gradient ánh kim).
  - Nội dung lời chúc & UI controls: `Be Vietnam Pro` (trọng lượng 300–600, khoảng cách dòng thoáng dễ đọc trên màn hình nhỏ).

---

## 3. Đặc Tả Tính Năng Chi Tiết

### 3.1. Màn Hình Mở Đầu: Phong Bì 3D & Dấu Sáp Vàng (`#introSection`)
- Hiển thị chiếc phong bì màu xanh Navy đậm với các nếp gấp viền chỉ vàng sắc nét bằng SVG.
- **Dấu sáp 3D (`#waxSealBtn`):** Nằm chính giữa giao điểm nắp phong bì, hiệu ứng dập nổi 3D kim loại vàng với dòng chữ `"20.11 / TRI ÂN"` và hiệu ứng nhịp thở phát sáng (`sealPulse`).
- **Tương tác mở thiệp:** Khi người dùng chạm/nhấn vào dấu sáp:
  1. Dấu sáp mờ dần và phóng nhẹ; nắp phong bì xoay 3D (`rotateX(180deg)` trong `0.95s`); lá thư bên trong trượt nhẹ lên.
  2. Kích hoạt đồng thời pháo hoa bụi vàng trên Canvas và khởi động nhạc nền du dương.
  3. Chuyển cảnh mượt mà sang màn hình thiệp chính.

### 3.2. Thiệp Chính Glassmorphism & Họa Tiết Di Sản (`#mainCardSection`)
- **Hiệu ứng kính mờ & Nghiêng 3D:** Card chính sử dụng `backdrop-filter: blur(18px)`, viền vàng kim loại, tự động nghiêng nhẹ theo tọa độ chuột (`mousemove`) hoặc thao tác vuốt (`touchmove`) kèm lớp phản chiếu ánh sáng (`--glare-x`, `--glare-y`).
- **Biểu tượng văn hóa Việt Nam (Vẽ bằng Inline SVG sắc nét):**
  - **Trống Đồng Đông Sơn:** Họa tiết mặt trời 12 tia và chim Lạc xoay chậm chìm ở nền card (`opacity: 0.065`, chu kỳ `110s`).
  - **Hoa Sen Vàng:** Đặt trang trọng phía trên tiêu đề `20 • 11`.
  - **Hoa văn góc:** 4 góc card được trang trí họa tiết khung viền cổ điển đối xứng.
- **Nút tương tác "Gửi ngàn hoa tri ân":** Khi bấm sẽ bắn pháo hoa bụi vàng, thả mưa cánh hoa sen vàng rơi khắp màn hình, phát âm thanh chuông lấp lánh và tăng bộ đếm số lượng đóa sen đã gửi.

### 3.3. Hệ Thống Hiệu Ứng HTML5 Canvas (`#fxCanvas`)
- Canvas phủ toàn màn hình (`pointer-events: none`), tự động scale theo `window.devicePixelRatio` (tối đa `2x`) để giữ mượt 60fps trên mọi điện thoại.
- Quản lý 3 lớp hạt chuyển động độc lập:
  1. **Bụi vàng lơ lửng:** Bay nhẹ từ dưới lên và nhấp nháy liên tục ở nền.
  2. **Pháo hoa bụi vàng:** Bung tỏa theo vật lý trọng lực và lực cản không khí khi mở dấu sáp hoặc bấm nút gửi hoa.
  3. **Mưa cánh hoa sen vàng:** Các cánh sen cách điệu bằng Bezier curve kết hợp đốm sáng sao 4 cánh rơi chao lượn theo hàm sin.

### 3.4. Bộ Tổng Hợp Nhạc Nền Web Audio API (`AmbientMusicEngine`)
- Không dùng file âm thanh ngoài. Sử dụng `AudioContext` kết hợp sóng `sine` và họa âm `triangle` tạo tiếng đàn harp / hộp nhạc pha lê êm dịu theo vòng hợp âm F Major / D Minor ấm áp.
- Có nút Bật/Tắt nhạc cố định ở góc trên bên phải màn hình và hiệu ứng chuông hợp âm rải (`playSparkleChime`) khi tương tác.

### 3.5. Cá Nhân Hóa Liên Kết & Chia Sẻ QR (`?to=...&from=...`)
- Đọc tự động hai tham số URL `to` (Tên Thầy/Cô nhận thiệp) và `from` (Tên người gửi/tập thể lớp) ngay khi tải trang qua `URLSearchParams`.
- **Modal Cá Nhân Hóa:** Cho phép người dùng nhập tên người nhận, tên người gửi (có sẵn nút chọn nhanh gợi ý như *"Tập thể Sinh viên – Học viện Hàng không Việt Nam"*), cập nhật URL bằng `window.history.replaceState` và sao chép liên kết vào Clipboard (có fallback `document.execCommand('copy')` để hoạt động ổn định trong mọi trình duyệt in-app như Zalo, Messenger).
- Sử dụng thông báo Toast nổi thay vì `window.alert()`.

---

## 4. Cấu Trúc Thư Mục Dự Án
```text
chuc-mung-20-11/
├── index.html          # Toàn bộ giao diện, CSS, SVG, Canvas & Web Audio logic
├── generate_qr.py      # (Tùy chọn) Script Python xuất mã QR chất lượng cao
├── qr_20_11.png        # Ảnh mã QR trỏ đến trang GitHub Pages sau khi deploy
└── README.md           # Tài liệu hướng dẫn sử dụng & cấu trúc URL cá nhân hóa
```

---

## 5. Quy Trình Thực Thi Cho Agent (GitHub & Tạo Mã QR)

Agent hãy thực hiện lần lượt các bước sau trong Terminal:

### Bước 1: Tạo tệp `index.html` và `README.md`
- Ghi toàn bộ mã nguồn hoàn chỉnh đạt chuẩn đặc tả ở Mục 2 & Mục 3 vào `index.html`.
- Kiểm tra đảm bảo không còn lỗi cú pháp HTML/JS và hiển thị tốt ở chiều rộng `375px` (iPhone SE/Mini) đến `1440px` (Desktop).

### Bước 2: Đẩy dự án lên GitHub & Bật GitHub Pages
```bash
git init
git add .
git commit -m "feat: create luxury 20/11 Vietnamese Teachers' Day interactive e-card"
git branch -M main

# Tạo repo công khai và đẩy code bằng GitHub CLI (nếu đã cài gh)
gh repo create chuc-mung-20-11 --public --source=. --remote=origin --push

# Kích hoạt GitHub Pages từ nhánh main (thư mục gốc /)
gh api -X POST "repos/$(gh api user -q .login)/chuc-mung-20-11/pages" \
  -f source[branch]=main \
  -f source[path]=/
```
*(Lưu ý: Nếu môi trường chưa đăng nhập `gh`, hãy hướng dẫn người dùng gán `git remote add origin <URL>` và bật Pages trong **Settings > Pages**).*

### Bước 3: Tạo Mã QR Từ URL GitHub Pages
Sau khi có URL dạng `https://<username>.github.io/chuc-mung-20-11/`, chạy lệnh sau để tạo mã QR độ phân giải cao (`qr_20_11.png`):

```bash
python3 -c "
import urllib.request, urllib.parse
url = 'https://<USERNAME>.github.io/chuc-mung-20-11/'
qr_api = 'https://api.qrserver.com/v1/create-qr-code/?size=1000x1000&margin=20&color=081229&bgcolor=fbf5df&data=' + urllib.parse.quote(url)
urllib.request.urlretrieve(qr_api, 'qr_20_11.png')
print('Đã tạo thành công mã QR tại qr_20_11.png trỏ tới:', url)
"
```

---

## 6. Tiêu Chí Nghiệm Thu (Acceptance Criteria)
- [ ] Trang web mở trực tiếp trên trình duyệt di động khi quét mã QR mà không gặp lỗi CORS hay thiếu tài nguyên.
- [ ] Dấu sáp vàng 3D phản hồi nhạy với thao tác chạm (`click` / `touch`), mở phong bì mượt mà kèm pháo hoa bụi vàng.
- [ ] Nhạc nền du dương phát ổn định sau cú chạm mở thiệp đầu tiên và có thể tắt/bật bất kỳ lúc nào.
- [ ] Truy cập URL kèm tham số `?to=Thầy%20Nguyễn%20Văn%20A&from=Lớp%2012A1` hiển thị chính xác tên người nhận và người gửi trên cả phong bì lẫn nội dung thiệp chính.