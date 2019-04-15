# font_alta_generator.py

import os
import json

from PIL import ImageFont, ImageDraw, Image

class FontAltasGenerator(object):
    def __init__(self, font_name, font_size):
        self.font = ImageFont.truetype(font_name, font_size)
        self.name = os.path.splitext(font_name)[0]
    
    def generate(self):
        # TODO: For now, I have no idea how to handle kerning/variable-width fonts.
        #       I don't see how to get at the base-line and advancement data, etc.
        
        character_list = [chr(i) for i in range(256)]
        
        max_char_width = 0
        max_char_height = 0
        for character in character_list:
            char_size = self.font.getsize(character)
            char_width = char_size[0]
            char_height = char_size[1]
            if char_width > max_char_width:
                max_char_width = char_width
            if char_height > max_char_height:
                max_char_height = char_height
        
        image = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        image_width = image.size[0]
        image_height = image.size[1]
        
        char_map = {}
        
        row = 0
        col = 0
        for character in character_list:
            draw.text((col, row), character, font=self.font)
            char_size = self.font.getsize(character)
            char_width = char_size[0]
            char_height = char_size[1]
            char_map[character] = {
                'row': row,
                'col': col,
                'width': char_width,
                'height': char_height,
            }
            
            col += max_char_width
            if col + max_char_width > image_width:
                col = 0
                row += max_char_height
                if row + max_char_height > image_height:
                    raise Exception('Atlas texture not big enough!')

        image.save(self.name + '.png')

        altas_data = {
            'char_map': char_map
        }
        
        with open(self.name + '.json', 'w') as handle:
            json_str = json.dumps(altas_data, indent=4, separators=(',', ': '), sort_keys=True)
            handle.write(json_str)

if __name__ == '__main__':

    # TODO: Let user specify font and size.
    generator = FontAltasGenerator('consola.ttf', 15)
    generator.generate()