@echo off
chcp 65001 >nul
echo Đang quét thư mục bgm để cập nhật danh sách phát playlist.js...
python scan_bgm.py
if %ERRORLEVEL% NEQ 0 (
    echo [LỖI] Không thể chạy python scan_bgm.py
)
echo.
pause
