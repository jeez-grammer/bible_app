from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def generate_image(background_url, quote, verse):
    response = requests.get(background_url)
    background = Image.open(BytesIO(response.content)).convert("RGBA")

    # Resize the background image
    background = background.resize((800, 600))

    # Create a drawing context
    draw = ImageDraw.Draw(background)

    # Load a font
    font_path = "/path/to/your/font.ttf"  # Update this path to your font file
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    # Define text position and color
    text_color = (255, 255, 255, 255)  # White color

    # Draw the quote
    quote_position = (50, 200)
    draw.text(quote_position, quote, font=font, fill=text_color)

    # Draw the verse
    verse_position = (50, 300)
    draw.text(verse_position, verse, font=font, fill=text_color)

    # Save the image to a BytesIO object
    output = BytesIO()
    background.save(output, format="PNG")
    output.seek(0)

    return output