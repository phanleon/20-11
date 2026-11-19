# Hướng Dẫn Cấu Hình Firebase (Bầu Trời Đèn Chung & Tải Ảnh Thật Của Lớp)

Cơ sở dữ liệu: `https://thiep-20-11-default-rtdb.asia-southeast1.firebasedatabase.app/`

Để hệ thống vừa đồng bộ được đèn hoa đăng chung, vừa cho phép các bạn học sinh tải lên album ảnh thật của lớp để tạo mã QR riêng, bạn vào mục **Rules** trên Firebase Console và dán quy tắc sau:

### Quy tắc bảo mật chuẩn (Rules JSON):

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
    },
    "custom_cards": {
      ".read": true,
      "$id": {
        ".write": "!data.exists()",
        ".validate": "newData.hasChildren(['to','from','photos'])"
      }
    }
  }
}
```

### Các bước thực hiện (mất 10 giây):
1. Vào Firebase Console: https://console.firebase.google.com/project/thiep-20-11/database/thiep-20-11-default-rtdb/rules
2. Bấm vào tab **Rules** (Quy tắc).
3. Xóa code cũ, dán đoạn JSON ở trên vào.
4. Bấm **Publish** (Xuất bản) là xong!
