# WhatsApp AI Reply Bot
A Python bot that reads a WhatsApp Web chat and writes a short reply as "Dixcy" using Gemini.


# How it works
1. Select and copies the chat text from WhatsApp Web 
2. Sends the latest messages to Google Gemini
3. Pastes reply into the message box

# Requirements
- We have used Interpreter Python 3.12 version.
- WhatsApp Web open in Microsoft Edge browser.
- A free Google Gemini API key from https://aistudio.google.com/apikey

# Setup
1. Install the packages:
```
   pip install -r requirements.txt
```
2. Create a `.env` file in the project folder:
```
   GEMINI_API_KEY=your_key_here
```. Create a file named `.env` and add your key: =your_key_here

```
Don't share this file with anyone.

python main.py
```
Switch to WhatsApp Web within 3 seconds. Move the cursor to a screen corner to stop the script.

Notes
- `AUTO_SEND = False` by default, so you can read each reply before sending.
Use it only with chats you have permission to process.

License
MIT
