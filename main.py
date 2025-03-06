import pyautogui
import time
import pyperclip
from openai import OpenAI


"""The below three lines of code  will help you to know the coordinates of your cursor.
   for example  if you want to know the know the coordinates of the cursor while performing any action,
    you can take help of this one and know the coordinates """
# while True:
 #     a=pyautogui.position()
#     print(a)



def chat(chat_history) -> str:
    client = OpenAI(
    api_key="take your OPenAI's Api_key")

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": 
        "You are user, a coder from Miryalaguda, Hyderabad, India, who speaks multiple languages, including English and Telugu. Your task is to analyze the provided chat history and generate responses naturally and conversationally, just as user would. You must identify the language used in the chat history and respond in the same language, maintaining user's personality, knowledge, and communication style."},
        {
            "role": "user",
            "content": chat_history
        }
    ]
)

    response=completion.choices[0].message.content
    message = response.split("user: ", 1)[-1]  # Extracts only the message part
    return message

def should_respond(chat_history):

    chat_lines = chat_history.strip().split("/2025] ")  # Split chat into individual messages
    
    if not chat_lines:  # If no chat history, return False
        return False

    last_message = chat_lines[-1].strip()  # Get the last message

    # Check if the last message starts with "Rajesh:" or has Rajesh's name
    if last_message.startswith("user") or "user:" in last_message:
        return False  # Do not respond if Rajesh is the sender

    return True  # Respond only if the last message is from someone else



pyautogui.click(889,1054)
time.sleep(1)
pyautogui.moveTo(717,259)
pyautogui.dragTo(726,942,duration=1.5,button='left')#drag for one second
pyautogui.hotkey('ctrl','c')
pyautogui.click(704,285)## to lose the selected area
time.sleep(1)
text=pyperclip.paste()
print(text)
print(should_respond(text))
if  (should_respond(text)):
    Response=chat(text)
    pyautogui.click(835,954)# this clicks on text board
    time.sleep(1.5)  # Wait for the chat box to open

    # Step 2: Type the response
    # Response = str(chat())
    pyautogui.typewrite(Response)

    # Step 3: Press Enter to send the message
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(1779,22)
else:
    pyautogui.click(1779,22)











