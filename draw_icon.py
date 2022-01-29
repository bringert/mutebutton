# Setup:
# pip3 install -U Pillow --user

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# U+1F92B Shushing face / Face with Finger Covering Closed Lips
STATUS_BAR_EMOJI = "\U0001F92B"

def draw_emoji_pil(unicode_text):
  width = 128
  height = 128
  font_size = 96

  im = Image.new("RGBA", (width,height))
  draw = ImageDraw.Draw(im)
  ttf = "/System/Library/Fonts/Apple Color Emoji.ttc"
  unicode_font = ImageFont.truetype(ttf, size=font_size)

  _,_,tw,th = draw.textbbox((0,0), unicode_text, font=unicode_font, embedded_color=True)

  x = int((width - tw) / 2)
  y = int((height - th) / 2)
  draw.text((x,y), unicode_text, font=unicode_font, embedded_color=True)
  return im

pil_image = draw_emoji_pil(STATUS_BAR_EMOJI)
pil_image.show()
#pil_image.save("testemoji_icon.png")
