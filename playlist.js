/**
 * TỰ ĐỘNG TẠO BỞI cap_nhat_danh_sach.bat
 * Quét toàn bộ file trong thư mục bgm/
 */

window.AUDIO_CONFIG = {
  ad: {
    title: "Phát loa Ra mắt vắc xin phòng bệnh Tay Chân Miệng",
    artist: "VNVC • Giọng miền Nam",
    src: "audio.mp3",
    repeatCount: 2,
  },
  bgmIntervalSeconds: 3600,
  fadeDurationSeconds: 2.5,
  playlist: [
    {
        "id": 1,
        "title": "bgm_demo_1",
        "artist": "VNVC BGM",
        "src": "bgm/bgm_demo_1.mp3"
    },
    {
        "id": 2,
        "title": "bgm_demo_2",
        "artist": "VNVC BGM",
        "src": "bgm/bgm_demo_2.mp3"
    }
]
};
