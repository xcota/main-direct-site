from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (16, 20, 24)
ACCENT = (15, 98, 254)
WHITE = (255, 255, 255)
GREY = (140, 150, 160)

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# top accent line
d.rectangle([0, 0, W, 10], fill=ACCENT)

# logo mark: rounded blue square with white "m"
d.rounded_rectangle([90, 120, 202, 232], radius=26, fill=ACCENT)
f_mark = ImageFont.truetype(BOLD, 72)
d.text((146, 176), "m", font=f_mark, fill=WHITE, anchor="mm")
d.ellipse([178, 196, 194, 212], fill=WHITE)

# wordmark: main . direct (dot in accent)
f_word = ImageFont.truetype(BOLD, 96)
x, y = 90, 300
for part, color in (("main", WHITE), (".", ACCENT), ("direct", WHITE)):
    d.text((x, y), part, font=f_word, fill=color)
    x += d.textlength(part, font=f_word)

# tagline
f_tag = ImageFont.truetype(REG, 40)
d.text((92, 452), "Verified B2B contact intelligence", font=f_tag, fill=GREY)
d.text((92, 508), "& email deliverability consulting", font=f_tag, fill=GREY)

img.save("og.png")
print("og.png saved", img.size)
