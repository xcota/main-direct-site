from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
IMG = ASSETS / "img"
IMG.mkdir(parents=True, exist_ok=True)

BG=(6,9,13); PANEL=(13,18,24); ACCENT=(91,157,255); MINT=(142,240,208); WHITE=(232,238,246); GREY=(157,171,184)
BOLD="/System/Library/Fonts/Supplemental/Arial Bold.ttf"; REG="/System/Library/Fonts/Supplemental/Arial.ttf"

def rounded(size, radius, color=BG):
    im=Image.new("RGBA",(size,size),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,size-1,size-1],radius=radius,fill=color)
    return im

def icon(size, margin_ratio=.14, bg=BG, rounded_mask=False):
    canvas=rounded(size,int(size*.22),bg) if rounded_mask else Image.new("RGBA",(size,size),bg+(255,))
    d=ImageDraw.Draw(canvas)
    m=int(size*margin_ratio); box=(m,m,size-m,size-m)
    # wordmark: m + dot, fitted to a square safe area.
    font_size=int((box[3]-box[1])*.58)
    font=ImageFont.truetype(BOLD,font_size)
    text="m"; bbox=d.textbbox((0,0),text,font=font); tw=bbox[2]-bbox[0]; th=bbox[3]-bbox[1]
    x=box[0]+((box[2]-box[0])-tw-int(font_size*.24))//2-bbox[0]
    y=box[1]+((box[3]-box[1])-th)//2-bbox[1]
    d.text((x,y),text,font=font,fill=WHITE)
    dot=int(font_size*.20); dx=box[2]-dot-int(font_size*.20); dy=box[3]-dot-int(font_size*.22)
    d.ellipse([dx,dy,dx+dot,dy+dot],fill=ACCENT)
    return canvas

def save_png(im,path,optimize=True): im.save(path,optimize=optimize)

def favicon_svg():
    svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Main Direct">
  <rect width="64" height="64" rx="16" fill="#06090d"/>
  <text x="23" y="44" font-family="ui-sans-serif,-apple-system,Segoe UI,Roboto,Arial,sans-serif" font-size="36" font-weight="800" fill="#e8eef6" text-anchor="middle">m</text>
  <circle cx="47" cy="42" r="6" fill="#5b9dff"/>
</svg>'''
    (ROOT/"favicon.svg").write_text(svg)

def make_og():
    W,H=1200,630; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    # subtle structural grid, kept below 12% contrast so text remains dominant.
    for x in range(80,W,80): d.line([x,0,x,H],fill=(12,18,25))
    for y in range(70,H,70): d.line([0,y,W,y],fill=(12,18,25))
    d.rectangle([0,0,W,8],fill=ACCENT)
    d.rounded_rectangle([72,88,184,200],radius=28,fill=ACCENT)
    mark=ImageFont.truetype(BOLD,70); d.text((128,144),"m",font=mark,fill=WHITE,anchor="mm")
    d.ellipse([160,172,184,196],fill=BG)
    title=ImageFont.truetype(BOLD,72); sub=ImageFont.truetype(REG,36); small=ImageFont.truetype(REG,26)
    x=72; y=270
    for part,color in (("main",WHITE),(".",ACCENT),("direct",WHITE)):
        d.text((x,y),part,font=title,fill=color); x+=d.textlength(part,font=title)
    d.text((72,368),"B2B contact data, validation &",font=sub,fill=WHITE)
    d.text((72,420),"email deliverability infrastructure",font=sub,fill=WHITE)
    for i,label in enumerate(["Contact engineering","Independent validation","Sending-domain infrastructure"]):
        d.ellipse([72,502+i*0,82,512+i*0],fill=MINT) if i==0 else None
    d.text((100,492),"Contact engineering · Independent validation · Sending-domain infrastructure",font=small,fill=GREY)
    d.text((72,548),"main.direct",font=ImageFont.truetype(BOLD,28),fill=ACCENT)
    im.save(ROOT/"og.png",optimize=True,progressive=True)

def manifest():
    import json
    data={"name":"Main Direct","short_name":"Main Direct","description":"B2B contact data and email deliverability infrastructure.","start_url":"/","scope":"/","display":"standalone","background_color":"#06090d","theme_color":"#06090d","icons":[{"src":"/assets/img/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"/assets/img/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"},{"src":"/apple-touch-icon.png","sizes":"180x180","type":"image/png","purpose":"maskable"}]}
    (ROOT/"site.webmanifest").write_text(json.dumps(data,indent=2)+"\n")

favicon_svg()
save_png(icon(512),IMG/"icon-512.png")
save_png(icon(192),IMG/"icon-192.png")
save_png(icon(180,.16,rounded_mask=True),(ROOT/"apple-touch-icon.png"))
icon(32).save(ROOT/"favicon.ico",sizes=[(16,16),(32,48)])
make_og(); manifest()
print("assets generated")
