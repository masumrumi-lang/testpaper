import os
from PIL import Image, ImageDraw, ImageFont

img_width = 800
img_height = 400
img = Image.new('RGB', (img_width, img_height), color='white')
draw = ImageDraw.Draw(img)

try:
    # Try multiple common fonts
    font_path = "arial.ttf"
    if not os.path.exists("C:/Windows/Fonts/arial.ttf"):
        font_path = "segoeui.ttf"
    font_large = ImageFont.truetype(font_path, 32)
    font_medium = ImageFont.truetype(font_path, 28)
except IOError:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()

# Define boxes
top_box = [260, 20, 540, 140]
draw.rectangle(top_box, outline="black", width=6)
text_top = "Boro Rice\nCultivation\nMethod"
bbox = draw.multiline_textbbox((0, 0), text_top, font=font_large, align="center")
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.multiline_text(((top_box[0]+top_box[2])/2 - w/2, (top_box[1]+top_box[3])/2 - h/2 - 5), text_top, fill="black", font=font_large, align="center")

left_box = [40, 240, 340, 360]
draw.rectangle(left_box, outline="black", width=6)
text_left = "Fewer than one\nseedling per hill"
bbox = draw.multiline_textbbox((0, 0), text_left, font=font_medium, align="center")
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.multiline_text(((left_box[0]+left_box[2])/2 - w/2, (left_box[1]+left_box[3])/2 - h/2 - 5), text_left, fill="black", font=font_medium, align="center")

right_box = [460, 240, 760, 360]
draw.rectangle(right_box, outline="black", width=6)
text_right = "3-4 seedlings\n(30-40 days old)\nper hill"
bbox = draw.multiline_textbbox((0, 0), text_right, font=font_medium, align="center")
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.multiline_text(((right_box[0]+right_box[2])/2 - w/2, (right_box[1]+right_box[3])/2 - h/2 - 5), text_right, fill="black", font=font_medium, align="center")

line_color = "black"
line_width = 4
arrow_size = 12

# Vertical line from top box down
draw.line([(400, 140), (400, 190)], fill=line_color, width=line_width)
draw.polygon([(400, 190), (392, 178), (408, 178)], fill=line_color)

# Horizontal line
draw.line([(190, 187), (610, 187)], fill=line_color, width=line_width)

# Vertical line left
draw.line([(190, 187), (190, 240)], fill=line_color, width=line_width)
draw.polygon([(190, 240), (182, 228), (198, 228)], fill=line_color)

# Vertical line right
draw.line([(610, 187), (610, 240)], fill=line_color, width=line_width)
draw.polygon([(610, 240), (602, 228), (618, 228)], fill=line_color)

output_path = 'c:/Users/BMTF/.antigravity/testpaper/assets/images/agr1/ch2/agri1_ch2_cq12_recreated.png'
img.save(output_path)
print(f"Image saved to {output_path}")
