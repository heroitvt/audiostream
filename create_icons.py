import math
from PIL import Image, ImageDraw, ImageFilter

def draw_app_icon(size):
    # Create image with RGBA
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Scale factor relative to 512
    s = size / 512.0
    
    # 1. Background rounded rectangle (Squircle)
    margin = int(16 * s)
    radius = int(108 * s)
    
    # Outer Glow layer
    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=(6, 182, 212, 100) # Cyan glow
    )
    glow = glow.filter(ImageFilter.GaussianBlur(int(20 * s)))
    img = Image.alpha_composite(glow, img)
    draw = ImageDraw.Draw(img)
    
    # Main Base gradient fill (simulated via concentric/linear)
    for i in range(margin, size - margin):
        ratio = (i - margin) / float(size - 2 * margin)
        # Gradient from #091e3a (deep navy) to #030712 (dark slate)
        r = int(9 * (1 - ratio) + 2 * ratio)
        g = int(30 * (1 - ratio) + 6 * ratio)
        b = int(58 * (1 - ratio) + 18 * ratio)
        draw.line([(margin, i), (size - margin, i)], fill=(r, g, b, 255))
        
    # Mask rounded rectangle
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=255
    )
    
    # Border stroke
    border_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(border_img)
    b_draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        outline=(56, 189, 248, 140), # Sky blue border
        width=int(5 * s)
    )
    
    # Composite base with mask
    base = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    base.paste(img, (0, 0), mask=mask)
    img = Image.alpha_composite(base, border_img)
    draw = ImageDraw.Draw(img)

    cx, cy = size // 2, size // 2

    # 2. Draw Broadcast Radio Waves (Arcs)
    cyan = (6, 182, 212, 255)
    blue = (59, 130, 246, 255)
    
    # Concentric glowing signal rings (Left & Right)
    for ring_r, width, alpha in [(140 * s, 12 * s, 210), (105 * s, 10 * s, 230), (72 * s, 8 * s, 255)]:
        # Left arc
        bbox_l = [cx - ring_r, cy - ring_r - 20 * s, cx + ring_r, cy + ring_r - 20 * s]
        draw.arc(bbox_l, start=135, end=225, fill=(6, 182, 212, alpha), width=int(width))
        # Right arc
        draw.arc(bbox_l, start=-45, end=45, fill=(59, 130, 246, alpha), width=int(width))

    # 3. Central Broadcast Tower / Beacon
    top_y = cy - int(45 * s)
    bottom_y = cy + int(120 * s)
    
    # Beacon light ball at top
    ball_r = int(24 * s)
    # Glow around beacon
    draw.ellipse([cx - ball_r*1.8, top_y - ball_r*1.8, cx + ball_r*1.8, top_y + ball_r*1.8], fill=(6, 182, 212, 80))
    draw.ellipse([cx - ball_r, top_y - ball_r, cx + ball_r, top_y + ball_r], fill=(255, 255, 255, 255))

    # Tower legs (A-frame structure)
    tower_w = int(60 * s)
    # Left leg
    draw.line([(cx, top_y), (cx - tower_w, bottom_y)], fill=(224, 242, 254, 255), width=int(10 * s))
    # Right leg
    draw.line([(cx, top_y), (cx + tower_w, bottom_y)], fill=(224, 242, 254, 255), width=int(10 * s))
    # Center vertical beam
    draw.line([(cx, top_y), (cx, bottom_y - 20 * s)], fill=(56, 189, 248, 200), width=int(6 * s))

    # Cross beams
    cross_y1 = top_y + int(60 * s)
    w1 = int(28 * s)
    draw.line([(cx - w1, cross_y1), (cx + w1, cross_y1)], fill=(56, 189, 248, 255), width=int(7 * s))

    cross_y2 = top_y + int(110 * s)
    w2 = int(48 * s)
    draw.line([(cx - w2, cross_y2), (cx + w2, cross_y2)], fill=(56, 189, 248, 255), width=int(8 * s))

    # Cross X truss
    draw.line([(cx - w2, cross_y2), (cx + w1, cross_y1)], fill=(14, 165, 233, 180), width=int(4 * s))
    draw.line([(cx + w2, cross_y2), (cx - w1, cross_y1)], fill=(14, 165, 233, 180), width=int(4 * s))

    return img

if __name__ == "__main__":
    icon_512 = draw_app_icon(512)
    icon_512.save("icon-512.png", "PNG")
    
    icon_192 = draw_app_icon(192)
    icon_192.save("icon-192.png", "PNG")

    icon_180 = draw_app_icon(180)
    icon_180.save("apple-touch-icon.png", "PNG")

    icon_64 = draw_app_icon(64)
    icon_64.save("favicon.png", "PNG")
    icon_64.save("favicon.ico", "ICO")
    print("Icons generated successfully!")
