import openai
import pyperclip
import time
import os
import keyboard
import winreg
import logging
import apikey  # Import the dynamically created file containing the API key

# Set up the API key from apikey.py
openai.api_key = apikey.api_key

# Set up logging to discard messages
logging.basicConfig(filename=os.devnull, level=logging.ERROR)

def get_gpt4o_mini_answer(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who gives concise and accurate answers. If presented with multiple-choice questions, simply provide the correct answer. For any type of question, including math, just give the best short answer based on the context, without unnecessary explanation. Just give text, don't style the text. Please do not use any formatting elements like **, ###, or bullet points. Instead, use plain text. Provide the answer in a simple and straightforward manner, without any styled text. If you are working on a math question, provide the steps and the final answer without any explanation. No additional commentary is needed, just the steps and the answer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error in getting response: {e}")
        return "Error in generating response."

def process_clipboard():
    global latest_clipboard
    print("Ctrl+X pressed. Sending clipboard content to GPT-4o-mini...")
    answer = get_gpt4o_mini_answer(latest_clipboard)
    pyperclip.copy(answer)
    print(f"Copied response to clipboard: {answer}")

def monitor_clipboard():
    global latest_clipboard
    last_clipboard = ""
    latest_clipboard = ""

    while True:
        time.sleep(0.5)
        current_clipboard = pyperclip.paste().strip()

        if current_clipboard != last_clipboard and current_clipboard != latest_clipboard:
            print(f"New clipboard content detected: {current_clipboard}")
            last_clipboard = current_clipboard
            latest_clipboard = last_clipboard

def disable_clipboard_history():
    try:
        # Open the registry key for clipboard settings
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Clipboard",
            0,
            winreg.KEY_SET_VALUE
        )
        # Set the Clipboard history value to 0 (off)
        winreg.SetValueEx(registry_key, "EnableClipboardHistory", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(registry_key)
        print("Clipboard history disabled successfully.")
    except FileNotFoundError:
        logging.error("Registry key not found. Clipboard history might not be supported on this system.")
    except PermissionError:
        logging.error("Permission denied. Please run the script as an administrator.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def terminate_script():
    print("Ctrl+B pressed. Disabling clipboard history, clearing clipboard, and exiting script...")
    disable_clipboard_history()
    pyperclip.copy("")  # Clear the clipboard
    os._exit(0)

if __name__ == "__main__":
    disable_clipboard_history()
    pyperclip.copy("")  # Clear the clipboard at startup
    print("Starting clipboard monitor...")

    keyboard.add_hotkey('ctrl+x', process_clipboard)
    keyboard.add_hotkey('ctrl+b', terminate_script)

    monitor_clipboard()import openai
import pyperclip
import time
import os
import keyboard
import winreg
import logging

# Import the dynamically generated file for the API key
import apikey

# Set up the API key from apikey.py
openai.api_key = apikey.api_key

# Set up logging to discard messages
logging.basicConfig(filename=os.devnull, level=logging.ERROR)

def get_gpt4o_mini_answer(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who gives concise and accurate answers. If presented with multiple-choice questions, simply provide the correct answer. For any type of question, including math, just give the best short answer based on the context, without unnecessary explanation. Just give text, don't style the text. Please do not use any formatting elements like **, ###, or bullet points. Instead, use plain text. Provide the answer in a simple and straightforward manner, without any styled text. If you are working on a math question, provide the steps and the final answer without any explanation. No additional commentary is needed, just the steps and the answer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error in getting response: {e}")
        return "Error in generating response."

def process_clipboard():
    global latest_clipboard
    print("Ctrl+X pressed. Sending clipboard content to GPT-4o-mini...")
    answer = get_gpt4o_mini_answer(latest_clipboard)
    pyperclip.copy(answer)
    print(f"Copied response to clipboard: {answer}")

def monitor_clipboard():
    global latest_clipboard
    last_clipboard = ""
    latest_clipboard = ""

    while True:
        time.sleep(0.5)
        current_clipboard = pyperclip.paste().strip()

        if current_clipboard != last_clipboard and current_clipboard != latest_clipboard:
            print(f"New clipboard content detected: {current_clipboard}")
            last_clipboard = current_clipboard
            latest_clipboard = last_clipboard

def disable_clipboard_history():
    try:
        # Open the registry key for clipboard settings
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Clipboard",
            0,
            winreg.KEY_SET_VALUE
        )
        # Set the Clipboard history value to 0 (off)
        winreg.SetValueEx(registry_key, "EnableClipboardHistory", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(registry_key)
        print("Clipboard history disabled successfully.")
    except FileNotFoundError:
        logging.error("Registry key not found. Clipboard history might not be supported on this system.")
    except PermissionError:
        logging.error("Permission denied. Please run the script as an administrator.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def terminate_script():
    print("Ctrl+B pressed. Disabling clipboard history, clearing clipboard, and exiting script...")
    disable_clipboard_history()
    pyperclip.copy("")  # Clear the clipboard
    os._exit(0)

if __name__ == "__main__":
    disable_clipboard_history()
    pyperclip.copy("")  # Clear the clipboard at startup
    print("Starting clipboard monitor...")

    keyboard.add_hotkey('ctrl+x', process_clipboard)
    keyboard.add_hotkey('ctrl+b', terminate_script)

    monitor_clipboard()
