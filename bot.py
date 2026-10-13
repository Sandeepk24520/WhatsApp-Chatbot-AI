import pyautogui
import pyperclip
import time
from google import genai

client = genai.Client(
      api_key="Your_api_key_here")

messages =(
          "You are a person named Dixcy who speaks hindi as well as english."
          "You are from India and you are a coder."
          "You analyze chat history and answered like Dixcy. No explanation, no quotes, no markdown, no emojis unless the chat uses them. "
          "Output should be the next chat answer as Dixcy.Please give short chat answer")

def is_last_message_from_sender(chat_log, sender_name="Satish"):
      messages = chat_log.strip().split("/2026]")[-1]
      if sender_name in messages:
            return True
      return False

# Click the Microsoft Edge icon
pyautogui.click(1094, 1048)
time.sleep(1)  # give time to open app

while True:
      pyautogui.moveTo(712, 257)
      pyautogui.mouseDown()
      pyautogui.moveTo(1865, 907, duration=0.5)  
      pyautogui.mouseUp()

      pyautogui.hotkey('ctrl', 'c')
      pyautogui.click(691, 259) # at whatsapp 
      time.sleep(2)  # give the OS a moment to update clipboard

      # Read clipboard into a variable
      chat_history = pyperclip.paste()

      print("Copied text:", chat_history)

      if is_last_message_from_sender(chat_history):
            interaction = client.interactions.create(
                  model = "gemini-3.5-flash-lite",
                  input = chat_history,
                  system_instruction = messages,
                  environment = "remote",
            )

            prompt = f"{messages}\n\nChat history:\n{chat_history}" 

            answer = interaction.output_text

            print(f"Output:{answer}")

            pyperclip.copy(answer)
            # coordinates of chatbox 
            pyautogui.click(1439, 968)
            time.sleep(0.1)

            pyautogui.hotkey('ctrl','v')
            time.sleep(0.1)

            pyautogui.press('enter')