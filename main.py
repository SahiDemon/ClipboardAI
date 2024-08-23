from dotenv import load_dotenv
import openai
import pyperclip
import time
import os
import keyboard  


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


def get_gpt4o_mini_answer(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "You are an assistant who gives concise and accurate answers. If presented with multiple-choice questions, simply provide the correct answer. For any type of question, including math, just give the best short answer based on the context, without unnecessary explanation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,  
            temperature=0.5
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error in getting response: {e}")
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


def terminate_script():
    print("Termination hotkey pressed. Exiting script...")
    os._exit(0)

if __name__ == "__main__":
    print("Starting clipboard monitor...")  
    pyperclip.copy("") 


    keyboard.add_hotkey('ctrl+x', process_clipboard)
    keyboard.add_hotkey('ctrl+b', terminate_script)


    monitor_clipboard()
