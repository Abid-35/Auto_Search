import pyautogui
import time
import string

pyautogui.PAUSE = 1.8

# Step 1: Open the browser (Edge or Chrome)
pyautogui.press('win')
pyautogui.write('chrome', interval=0.1)  # or 'chrome' if you're using Chrome
pyautogui.press('enter')
time.sleep(3)  # wait for browser to load

# Step 2: First search - the URL
pyautogui.hotkey('ctrl', 'l')  # focus address bar
time.sleep(0.2)
pyautogui.write('https://rewards.bing.com/?ref=pin&OCID=PINREW', interval=0.1)
pyautogui.press('enter')
time.sleep(3)  # wait for the page to load

# Step 3: Prepare 35 character searches (A–Z and 0–9)
letters = list(string.ascii_lowercase)   # ['a'...'z']
digits = list('0123456789')              # ['0'...'9']
search_terms = letters + digits          # total 26 + 10 = 36 - 1 = 35

# Step 4: Loop through the characters and search each one
for term in search_terms:
    pyautogui.hotkey('ctrl', 'l')  # focus address bar
    time.sleep(0.2)
    pyautogui.write(term, interval=0.1)
    pyautogui.press('enter')
    time.sleep(2.5)  # wait between searches

# Step 5: Close the browser after all 36 searches
pyautogui.hotkey('alt', 'f4')
