from PIL import ImageGrab
import requests
from openai import OpenAI
from termcolor import colored
import re
import subprocess
import pyautogui
import platform

class State:
    def __init__(self):
        self.focus_app = get_focused_app_name()
        self.chrome_tab_url = None if self.focus_app is not 'Google Chrome' else get_chrome_current_url()

def get_focused_app_name():
    applescript_command = '''
    tell application "System Events"
        get name of first application process whose frontmost is true
    end tell
    '''
    process = subprocess.run(['osascript', '-e', applescript_command], capture_output=True, text=True)    
    app_name = process.stdout.strip()
    return app_name

def quit_app(app_name):
    applescript_command = f'''
    tell application "{app_name}"
        quit
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript_command])

def close_chrome_current_tab():
    applescript_command = '''
    tell application "Google Chrome"
        close active tab of front window
    end tell
    '''    
    subprocess.run(['osascript', '-e', applescript_command])

def get_chrome_current_url():
    applescript_command = '''
    tell application "Google Chrome"
        get URL of active tab of front window
    end tell
    '''    
    process = subprocess.run(['osascript', '-e', applescript_command], capture_output=True, text=True)
    current_url = process.stdout.strip()
    return current_url

def take_screenshot():
    screenshot_filename = f"image.png"
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_filename)
    return screenshot_filename

def upload_image(image_name):
    worker_url = "https://r2-worker.mhamzaqayyum.workers.dev/image.png"
    auth_token = "koan"
    file_path = "./image.png" 

    with open(file_path, 'rb') as file:
        file_data = file.read()

    response = requests.put(worker_url, headers={
        "Authorization": f"Bearer {auth_token}"
    }, data=file_data)

    if response.status_code != 200:
        print(f"Failed to upload image. Status code: {response.status_code}, Message: {response.text}")
    
    return worker_url

def analyze_image_with_text(client, image_url, prompt):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview", # Adjust the model name if necessary
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": image_url},
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

def run_loop(prompt):
    client = OpenAI(api_key="")
    try:
        while 1:
            screenshot_filename = take_screenshot()
            state1 = State()

            image_url = upload_image(screenshot_filename)
            full_prompt = f"I am currently working on: {prompt}. That is the work I am occupied with. Please have a look at the attached screenshot of my current desktop. Then, tell me, in a DISTRACTED/NOT DISTRACTED answer, am I working on what I am supposed to be working on, as I described it? Or am I distracted? I repeat your answer should be only either DISTRACTED or NOT DISTRACTED. No more words."
            
            result = analyze_image_with_text(client, image_url, full_prompt)
            state2 = State()
            

            distracted = 'DISTRACTED'
            not_distracted = 'NOT DISTRACTED'

            if not_distracted in result:
                print(colored('NOT DISTRACTED', 'green'))
            elif distracted in result:
                print(colored('DISTRACTED', 'red'))

                if state1.focus_app == state2.focus_app:
                    if state1.focus_app == 'Google Chrome':
                        if state1.chrome_tab_url == state2.chrome_tab_url:
                            print(colored('action: CLOSE', 'yellow'))
                            close_chrome_current_tab()
                        else:
                            print(colored('action: nothing (changed tab)', 'yellow'))
                    else:
                        app_name = state1.focus_app
                        if app_name != 'Finder':
                            print(colored('action: CLOSE', 'yellow'))
                            quit_app(app_name)
                else:
                    print(colored('action: nothing (changed applications)', 'yellow'))
            else:
                print(colored(result, 'dark_grey'))
    except KeyboardInterrupt:
        pass