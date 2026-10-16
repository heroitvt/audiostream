# HƯỚNG DẪN THÊM NHẠC & QUẢNG CÁO VÀO HỆ THỐNG PHÁT THANH VNVC

## 1. Cấu trúc thư mục
```
audio stream/
├── index.html               # Trang web phát thanh tự động
├── playlist.js              # File danh sách nhạc và quảng cáo tự động
├── cap_nhat_danh_sach.bat   # Nhấp đúp để tự động quét BGM và Ads mới
├── chay_web.bat             # Nhấp đúp để mở trang web
├── ads/                     # THƯ MỤC CHỨA CÁC FILE QUẢNG CÁO / PHÁT LOA
│   ├── 01_tay_chan_mieng.mp3
│   ├── 02_tiem_chung_cum.mp3
│   └── ...
└── bgm/                     # THƯ MỤC CHỨA CÁC FILE NHẠC NỀN
    ├── bai_01.mp3
    ├── bai_02.mp3
    └── ... (50+ bài)
```

## 2. Cách thêm bài mới (Cực kỳ đơn giản):
1. **Thêm Quảng Cáo:** Copy file âm thanh (`.mp3`, `.wav`) vào thư mục `ads/`.
2. **Thêm Nhạc Nền:** Copy file âm thanh vào thư mục `bgm/`.
3. **Cập nhật danh sách:** Nhấp đúp chuột vào file **`cap_nhat_danh_sach.bat`**. Hệ thống sẽ tự động quét toàn bộ bài hát và quảng cáo đưa vào hệ thống!

## 3. Quy trình phát tự động (State Machine):
- **Bắt đầu:** Phát **bài Quảng cáo đầu tiên đủ 2 lần liên tiếp**.
- **Sau 2 lần QC:** Tự động chuyển sang phát **Nhạc nền không lời** trong thư mục `bgm/`.
- **Sau mỗi 60 phút (3600s):** Nhạc nền sẽ **nhỏ dần âm lượng (Fade-out trong 2.5s) rồi tạm dừng đúng vị trí đang phát dở**.
- **Chuyển sang Quảng cáo:** Phát **1 file quảng cáo tiếp theo trong thư mục `ads/` đủ 2 lần liên tiếp** (xoay vòng tuần tự bài 1 $\rightarrow$ bài 2 $\rightarrow$ bài 3...).
- **Hết 2 lần QC:** Nhạc nền **phát tiếp tục ngay tại đoạn đang hát dở lúc nãy (Fade-in êm tai)**.
- **Vòng lặp:** Cứ thế tiếp diễn liên tục không ngắt quãng!
