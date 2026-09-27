import os
import json

bgm_dir = os.path.join(os.path.dirname(__file__), 'bgm')
output_js = os.path.join(os.path.dirname(__file__), 'playlist.js')
output_json = os.path.join(bgm_dir, 'bgm_manifest.json')

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

# Write JSON manifest
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

# Write JS config
content = f"""/**
 * TỰ ĐỘNG TẠO BỞI scan_bgm.py / cap_nhat_danh_sach.bat
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

with open(output_js, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"[THÀNH CÔNG] Đã quét và cập nhật {len(items)} bài hát vào playlist.js và bgm/bgm_manifest.json!")
