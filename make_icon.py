# Dependencies:
# pip3 install -U requests --user

# Gets emojis from https://emojiapi.dev/
# E.g. https://emojiapi.dev/api/v1/shushing_face/512.png

import icnsutil
import io
import requests
from PIL import Image

EMOJI_NAME = "shushing_face"
ICNS_FILE = "icon.icns"
ICON_SIZES = [(32,32), (128,128), (256,256), (512,512)]
DEBUG = False

def get_emoji_pil(name, size):
  format = "png"
  r = requests.get(f"https://emojiapi.dev/api/v1/{name}/{size}.{format}")
  return Image.open(io.BytesIO(r.content))

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

def create_emoji_icns_file(icns_file, name, sizes):
  orig_image = get_emoji_pil(name, 512)
  imgs = []
  for size in sizes:
    resized_image = orig_image.resize(size)
    if DEBUG:
      resized_image.show()
    imgs.append((size, pil_to_bytes(resized_image)))
  write_icns(icns_file, imgs)

if __name__ == '__main__':
  create_emoji_icns_file(ICNS_FILE, EMOJI_NAME, ICON_SIZES)
