from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
import time
import win32clipboard
# Open up google and search for the word
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search = driver.find_element(By.CLASS_NAME, "gLFyf")  # Locate the search bar element via its class name
search.send_keys("Destruction" + Keys.ENTER)  # Enter the word and press enter
time.sleep(2)
# Locate the definition box
elem = driver.find_element(By.XPATH, "//div[contains(@class, 'lr_container') and contains(@class, 'yc7KLc') and "
                                          "contains(@class, 'mBNN3d')]")
location = elem.location
size = elem.size  # Get the element's size and location

# Save a screenshot of the whole page and then crop the definition box out
screenshot = driver.save_screenshot("F:\\SS\\temp.png")
file = Image.open("F:\\SS\\temp.png")
final = file.crop((location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"]))
# Save the cropped version
final.save("F:\\SS\\crop.png")


def send_to_clipboard(clip_type, filepath):
    image = Image.open(filepath)
    bytes = BytesIO()
    imageBytes = image.convert("RGB")
    imageBytes.save(bytes, "BMP")
    


send_to_clipboard(win32clipboard.CF_DIB, "F:\\SS\\crop.png")
print("Copied to clipboard successfully!")
driver.quit()