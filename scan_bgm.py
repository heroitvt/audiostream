import os
import json
import glob

bgm_dir = os.path.join(os.path.dirname(__file__), 'bgm')
output_file = os.path.join(os.path.dirname(__file__), 'playlist.js')

extensions = ('.mp3', '.wav', '.ogg', '.m4a', '.aac', '.flac')
files = [f for f in sorted(os.listdir(bgm_dir)) if f.lower().endswith(extensions)]

items = []
for idx, f in enumerate(files, start=1):
    title = os.path.splitext(f)[0]
    items.append({
        "id": idx,
        "title": title,
        "artist": "VNVC BGM",
        "src": f"bgm/{f}"
    })

content = f"""/**
 * TỰ ĐỘNG TẠO BỞI cap_nhat_danh_sach.bat
 * Quét toàn bộ file trong thư mục bgm/
 */

window.AUDIO_CONFIG = {{
  ad: {{
    title: "Phát loa Ra mắt vắc xin phòng bệnh Tay Chân Miệng",
    artist: "VNVC • Giọng miền Nam",
    src: "audio.mp3",
    repeatCount: 2,
  }},
  bgmIntervalSeconds: 3600,
  fadeDurationSeconds: 2.5,
  playlist: {json.dumps(items, ensure_ascii=False, indent=4)}
}};
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"[THÀNH CÔNG] Đã quét và cập nhật {len(items)} bài hát vào playlist.js!")
