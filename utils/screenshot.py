import os
import time
from utils.logs import log
from PIL import Image
from io import BytesIO

def take_fullpage_screenshot(driver, path_file): 
    total_width = driver.execute_script("return document.body.scrollWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    rectangles = []
    y = 0
    while y < total_height:
        rectangles.append((0, y))
        y += viewport_height

    stitched_image = Image.new('RGB', (total_width, total_height))
    for y_position in rectangles:
        driver.execute_script(f"window.scrollTo(0, {y_position[1]});")
        time.sleep(0.4)
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        stitched_image.paste(im, (0, y_position[1]))
    os.makedirs(os.path.dirname(path_file) or ".", exist_ok=True)
    stitched_image.save(path_file)
    log(f"✅ Screenshot salvo em: {path_file}")
    return path_file

