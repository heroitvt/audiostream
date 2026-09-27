# HƯỚNG DẪN THÊM NHẠC NỀN VÀO HỆ THỐNG PHÁT THANH VNVC

## 1. Cấu trúc thư mục
```
audio stream/
├── index.html               # Trang web phát thanh tự động
├── playlist.js              # File danh sách nhạc và cài đặt chu kỳ
├── audio.mp3                # File âm thanh quảng cáo phát thanh
├── chay_web.bat             # Nhấp đúp để mở trang web
└── bgm/                     # THƯ MỤC CHỨA CÁC FILE NHẠC NỀN
    ├── bgm_demo_1.mp3
    ├── bgm_demo_2.mp3
    ├── bai_03.mp3
    └── ... (tới 25+ bài)
```

## 2. Cách thêm nhạc mới (2 bước đơn giản):
1. **Bước 1:** Copy các file nhạc `.mp3` của bạn vào thư mục `bgm/` (ví dụ: `bgm/bai_03.mp3`).
2. **Bước 2:** Mở file `playlist.js` bằng Notepad hoặc VS Code, thêm các dòng tương ứng vào danh sách `playlist`:
   ```javascript
   playlist: [
     { id: 1, title: "Tên bài 01", artist: "Tên ca sĩ", src: "bgm/bgm_demo_1.mp3" },
     { id: 2, title: "Tên bài 02", artist: "Tên ca sĩ", src: "bgm/bgm_demo_2.mp3" },
     { id: 3, title: "Tên bài 03", artist: "Tên ca sĩ", src: "bgm/bai_03.mp3" },
     // Thêm thoải mái tới 25 hoặc 50 bài...
   ]
   ```

## 3. Quy trình phát tự động (State Machine):
- **Bắt đầu:** Phát bài **Quảng cáo (audio.mp3) đủ 2 lần liên tiếp**.
- **Sau 2 lần QC:** Tự động chuyển sang phát **Nhạc nền không lời** trong thư mục `bgm/`.
- **Đếm đủ 60 phút (3600s):** Nhạc nền sẽ **nhỏ dần âm lượng (Fade-out trong 2.5s) rồi tạm dừng đúng vị trí đang phát dở**.
- **Chuyển sang Quảng cáo:** Phát bài quảng cáo **2 lần**.
- **Hết 2 lần QC:** Nhạc nền **phát tiếp tục ngay tại đoạn đang hát dở lúc nãy (Fade-in êm tai)** mà không bị ngắt hoặc hát lại từ đầu!
- **Vòng lặp:** Cứ thế lặp lại vô tận.
