import os
import json

base_dir = os.path.dirname(__file__)
bgm_dir = os.path.join(base_dir, 'bgm')
ads_dir = os.path.join(base_dir, 'ads')
output_js = os.path.join(base_dir, 'playlist.js')
output_json = os.path.join(bgm_dir, 'bgm_manifest.json')

extensions = ('.mp3', '.wav', '.ogg', '.m4a', '.aac', '.flac')

# 1. Quét thư mục bgm/
bgm_items = []
if os.path.exists(bgm_dir):
    bgm_files = [f for f in sorted(os.listdir(bgm_dir)) if f.lower().endswith(extensions)]
    for idx, f in enumerate(bgm_files, start=1):
        title = os.path.splitext(f)[0]
        bgm_items.append({
            "id": idx,
            "title": title,
            "artist": "VNVC BGM",
            "src": f"bgm/{f}"
        })

# 2. Quét thư mục ads/
ad_items = []
if os.path.exists(ads_dir):
    ad_files = [f for f in sorted(os.listdir(ads_dir)) if f.lower().endswith(extensions)]
    for idx, f in enumerate(ad_files, start=1):
        title = os.path.splitext(f)[0]
        ad_items.append({
            "id": idx,
            "title": title,
            "artist": "VNVC Quảng cáo",
            "src": f"ads/{f}"
        })

# Fallback nếu ads/ chưa có file
if not ad_items:
    ad_items = [{
        "id": 1,
        "title": "Phát loa Ra mắt vắc xin phòng bệnh Tay Chân Miệng",
        "artist": "VNVC • Giọng miền Nam",
        "src": "audio.mp3"
    }]

# Ghi manifest JSON cho BGM
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(bgm_items, f, ensure_ascii=False, indent=2)

# Cấu hình playlist.js
content = f"""/**
 * TỰ ĐỘNG TẠO BỞI scan_bgm.py / cap_nhat_danh_sach.bat
 * Quét toàn bộ file trong thư mục bgm/ và ads/
 */

window.AUDIO_CONFIG = {{
  ads: {json.dumps(ad_items, ensure_ascii=False, indent=4)},
  adRepeatCount: 2,
  bgmIntervalSeconds: 3600,
  fadeDurationSeconds: 2.5,
  playlist: {json.dumps(bgm_items, ensure_ascii=False, indent=4)}
}};
"""

with open(output_js, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"[THÀNH CÔNG] Đã quét {len(bgm_items)} bài BGM và {len(ad_items)} bài Quảng cáo vào playlist.js!")
