import os, time
import urllib.request
from typing import Callable, Dict, List, Optional, Union

cls: Callable[[], None] = lambda: os.system('cls || clear')

cali_console_path = "Cali_Console.py"
cali_chat_path = "Cali_Chat.py"

if os.path.exists(cali_console_path):
    os.remove(cali_console_path)
    print("Cali_Console.py deleted.")
else:
    print("Cali_Console.py not found.")

if os.path.exists(cali_chat_path):
    os.remove(cali_chat_path)
    print("Cali_Chat.py deleted.")
else:
    print("Cali_Chat.py not found.")

cali_console_url = "https://raw.githubusercontent.com/LibertyWalk999/Cali-Plug-Nuker/main/src/Cali_Console.py"
cali_chat_url = "https://raw.githubusercontent.com/LibertyWalk999/Cali-Plug-Nuker/main/src/Cali_Chat.py"

# Download and save the files
urllib.request.urlretrieve(cali_console_url, cali_console_path)
print("Cali_Console.py downloaded.")

urllib.request.urlretrieve(cali_chat_url, cali_chat_path)
print("Cali_Chat.py downloaded.")
time.sleep(1)
cls()
print("Cali Plug has been updated! Please run 'Cali.py'")
time.sleep(5)