# Setup:
# pip3 install -U Pillow --user
# pip3 install -U icnsutil --user

import icnsutil
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# U+1F92B Shushing face / Face with Finger Covering Closed Lips
STATUS_BAR_EMOJI = "\U0001F92B"

ICON_SIZES = [(32,32), (128,128), (256,256)]

FONT_FILE = "Apple Color Emoji"

DEBUG = False

def draw_emoji_pil(text):
  width,height = 160,160
  font_size = 160
  im = Image.new("RGBA", (width,height), color="white" if DEBUG else (0,0,0,0))
  draw = ImageDraw.Draw(im)
  unicode_font = ImageFont.truetype(FONT_FILE, size=font_size)
  _,_,tw,th = draw.textbbox((0,0), text, font=unicode_font, embedded_color=True)
  x = int((width - tw) / 2)
  y = int((height - th) / 2)
  draw.text((x,y), text, font=unicode_font, embedded_color=True)
  return im

def pil_to_bytes(im):
  buf = io.BytesIO()
  im.save(buf, format='PNG')
  return buf.getvalue()

def write_icns(icns_file, imgs):
  icns = icnsutil.IcnsFile()
  for (w,h),img in imgs:
    print(f"Adding {w}x{h}...")
    icns.add_media(file=f"{w}x{h}.png",data=img)
  icns.write(icns_file)
  print("Wrote", icns_file)

def create_emoji_icns_file(icns_file, unicode_text, sizes):
  orig_image = draw_emoji_pil(unicode_text)
  imgs = []
  for size in sizes:
    resized_image = orig_image.resize(size)
    if DEBUG:
      resized_image.show()
    imgs.append((size, pil_to_bytes(resized_image)))
  write_icns(icns_file, imgs)

if __name__ == '__main__':
  create_emoji_icns_file("icon.icns", STATUS_BAR_EMOJI, ICON_SIZES)
