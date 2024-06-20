from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
import time
import os
import win32clipboard
while True: # Loop to ask again in case of failure to find search box
    word = input("Enter the word, type 0 to end program\n")
    # Open up google and search for the word
    if word != "0":
        try:
            driver = webdriver.Chrome()
            driver.get("https://www.google.com")
            search = driver.find_element(By.CLASS_NAME, "gLFyf")  # Locate the search bar element via its class name
            search.send_keys("Definition of " + word + Keys.ENTER)  # Enter the word and press enter
            time.sleep(1)
            # Locate the definition box
            elem = driver.find_element(By.XPATH, "//div[contains(@class, 'lr_container') and contains(@class, 'yc7KLc') and "
                                                      "contains(@class, 'mBNN3d')]")
            if elem:
                location = elem.location
                size = elem.size  # Get the element's size and location

                # Save a screenshot of the whole page and then crop the definition box out
                screenshot = driver.save_screenshot("F:\\SS\\temp.png")
                file = Image.open("F:\\SS\\temp.png")
                final = file.crop((location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"]))
                # Save the cropped version
                final.save("F:\\SS\\crop.png")


                def send_to_clipboard(clip_type, data): # Function to copy the image to clipboard
                    win32clipboard.OpenClipboard()
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardData(clip_type, data)
                    win32clipboard.CloseClipboard()

                image = Image.open("F:\\SS\\crop.png") # Opens the required image
                bytes = BytesIO() # Creates an object to store the binary data
                imageBytes = image.convert("RGB") # Convert the image to binary in RGB form
                imageBytes.save(bytes, "BMP") # Save the binary data into the object
                data = bytes.getvalue()[14:] # Ignore the first 14 Header bytes and save it in a separate variable
                bytes.close() # Close the object so that it doesn't take any more memory
                send_to_clipboard(win32clipboard.CF_DIB, data)



                send_to_clipboard(win32clipboard.CF_DIB, "F:\\SS\\crop.png")
                print("Copied to clipboard successfully!")
                os.remove("F:\\SS\\temp.png") # Deleting the temporary files
                os.remove("F:\\SS\\crop.png")
                driver.quit() # Prompt to close the browser
            else:
                driver.close()
                print("Couldn't find the word / Google didn't present the definition box")
        except Exception as e:
            print("An error occurred: " + e)
    else:
        break