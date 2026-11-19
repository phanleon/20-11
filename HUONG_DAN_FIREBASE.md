# Bật "Bầu trời đèn chung" bằng Firebase (miễn phí)

Mặc định thiệp chạy chế độ offline (đèn chỉ hiện trên máy người thả). Làm theo các bước sau để mọi người cùng thấy đèn của nhau.

1. Vào https://console.firebase.google.com → **Add project** (tắt Google Analytics cũng được).
2. Menu **Build → Realtime Database → Create Database**. Chọn vùng gần nhất (Singapore), chọn **Start in locked mode**.
3. Tab **Rules** → xoá hết, dán đoạn dưới → **Publish**:

```json
{
  "rules": {
    ".read": false,
    ".write": false,
    "lanterns": {
      ".read": true,
      ".indexOn": ["t"],
      "$id": {
        ".write": "!data.exists()",
        ".validate": "newData.hasChildren(['n','m','t']) && newData.child('n').isString() && newData.child('n').val().length <= 40 && newData.child('m').isString() && newData.child('m').val().length >= 1 && newData.child('m').val().length <= 100 && newData.child('t').val() == now"
      }
    }
  }
}
```

   Luật này chỉ cho **thêm** đèn mới (không sửa/xoá được), giới hạn độ dài tên và lời chúc.
4. Tab **Data** → copy địa chỉ ở trên cùng, dạng `https://ten-du-an-default-rtdb.asia-southeast1.firebasedatabase.app`.
5. Mở `index.html`, tìm dòng `const LANTERN_DB_URL = '';` và dán địa chỉ vào giữa hai dấu nháy. Lưu, commit, push.

## Lưu ý
- Ai có link cũng thả được đèn. Nếu có người nghịch, vào tab **Data** xoá nhánh `lanterns` hoặc từng đèn.
- Đèn được lưu: người vào sau vẫn thấy tối đa 40 đèn gần nhất bay lên.
- Gói miễn phí (Spark) đủ cho thiệp lớp/trường.
