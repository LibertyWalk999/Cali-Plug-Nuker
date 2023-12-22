import os
import urllib.request

cali_console_path = "../src/Cali_Console.py"
cali_chat_path = "../src/Cali_Chat.py"

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