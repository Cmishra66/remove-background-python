from rembg import remove
import easygui
from PIL import Image

input_path = easygui.fileopenbox(title='select  image file')
output_path = easygui.filesavebox(title='save image to')
input_image = Image.open(input_path)
output = remove(input_image)
output.save(output_path)

