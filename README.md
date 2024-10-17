# assistant_version-o.2
Orion Personal Assistant
Orion is a personal assistant designed to help you perform various tasks like searching the web, telling jokes, managing social media, and more. It comes with voice recognition and text-to-speech capabilities, making it easy to interact with. You can issue commands via text or voice, and it supports both English and Arabic.

Features
Voice-Activated Commands: Play music, tell the time, search the web, open social media, and more.
Google Search: Perform quick web searches and get a description of the first result.
Social Media Integration: Open Facebook, WhatsApp, Instagram, YouTube with voice commands.
Jokes: Orion can tell you jokes whenever you ask.
Language Support: Switch between English and Arabic for commands.
Graphical Interface: Includes a tkinter-based GUI with a search bar, voice search, and quick command buttons.
Installation
Prerequisites
Python 3.x
Required Libraries:
speech_recognition
pyttsx3
pywhatkit
requests
bs4
numpy
tkinter
googlesearch-python (for Google search)
To install these libraries, run:

bash
Copy code
pip install SpeechRecognition pyttsx3 pywhatkit requests beautifulsoup4 numpy googlesearch-python
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/orion-assistant.git
cd orion-assistant
Running the Application
Run the main Python script:

bash
Copy code
python orion_assistant.py
The application will open a graphical interface where you can type or speak your commands.

Usage
Commands
Play Music:

English: "Play [song name]"
Arabic: "تشغيل [اسم الأغنية]"
Tell Time:

English: "What's the time?"
Arabic: "ما الوقت؟"
Joke:

English: "Tell me a joke."
Arabic: "أخبرني نكتة."
Search the Web:

English: "Search for [topic]"
Arabic: "بحث عن [موضوع]"
Social Media:

Open Facebook, WhatsApp, Instagram, or YouTube by saying the platform's name.
Switch Language:

Use the "Toggle Language" button in the GUI to switch between English and Arabic.
GUI Features
Search Bar: Enter commands manually.
Voice Search: Use the microphone button to give commands by voice.
Volume Bar: Visual indicator of the sound volume for voice input.
Quick Command Buttons: Fast access to popular commands like ChatGPT, Facebook, YouTube, and more.
Screenshots
You can add some screenshots of the app's interface here.

Contributing
Feel free to fork this project and submit pull requests if you want to contribute new features or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

