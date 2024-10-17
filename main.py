import speech_recognition as sr # type: ignore
import pyttsx3
import pywhatkit # type: ignore
import datetime
import pyjokes
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import numpy as np # type: ignore
from googlesearch import search # type: ignore
import requests
from bs4 import BeautifulSoup
import webbrowser

# Initialize speech recognition and text-to-speech
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def introduce_orion():
    talk("Hello, Mahmoud Sabry, I am Orion, your personal assistant. How can I help you today?")

def update_volume_bar(volume):
    canvas.delete("all")
    height = int(volume * 300)
    canvas.create_rectangle(0, 300 - height, 50, 300, fill="green")

def take_command():
    command = ""  # Initialize command with an empty string
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)  # Listen for up to 5 seconds
            
            # Convert audio data to numpy array and calculate RMS
            audio_data = np.frombuffer(voice.get_raw_data(), np.int16)
            rms = np.sqrt(np.mean(audio_data**2))
            normalized_rms = rms / 32768.0  # Normalize RMS value to range 0-1
            
            update_volume_bar(normalized_rms)
            
            command = listener.recognize_google(voice, language='en')
            command = command.lower()
            if 'Orion' in command:
                command = command.replace('Orion', '')
                print(command)
            # Check for Arabic command
            else:
                command = listener.recognize_google(voice, language='ar')
                command = command.lower()
                if 'أوريون' in command:
                    command = command.replace('أوريون', '')
                    print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        talk("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, the speech recognition service is unavailable.")
        talk("Sorry, the speech recognition service is unavailable.")
    return command

def google_search(query):
    try:
        # Perform Google search
        webbrowser.open(f"https://www.google.com/search?q={query}")
        talk('Performing a Google search for ' + query)
        search_results = search(query, num_results=1)
        if search_results:
            first_result = search_results[0]
            talk(f"The first search result is {first_result}")
            talk("Fetching a description for the result.")
            
            # Fetch the content of the URL
            response = requests.get(first_result)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract and summarize paragraphs
            paragraphs = soup.find_all('p')
            if paragraphs:
                # Create a summary from the first few paragraphs
                description = " ".join([p.get_text() for p in paragraphs[:3]])
                if len(description) > 500:
                    description = description[:500] + '...'  # Trim if too long
                talk(f"Description of the result: {description}")
            else:
                talk("Could not retrieve a description for the result.")
        else:
            talk("No results were found.")
    except Exception as e:
        talk("An error occurred while trying to fetch the result description.")
        print(f"Error: {e}")

def run_Orion(command):
    if 'play' in command or 'تشغيل' in command or 'اغنية' in command:
        song = command.replace('play', '').replace('تشغيل', '').replace('اغنية', '').strip()
        if song:
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        else:
            talk('What song would you like to play?')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'do you know' in command:
        query = command.replace('do you know', '').strip()
        if query:
            google_search(query)  # Call the new function here
        else:
            talk('What would you like to search for?')
    elif 'search for' in command:
        query = command.replace('search for', '').strip()
        if query:
            google_search(query)  # Call the new function here
        else:
            talk('What would you like to search for?')
    elif 'date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'facebook' in command:
        talk('Opening Facebook.')
        webbrowser.open('https://www.facebook.com')
    elif 'whatsapp' in command:
        talk('Opening WhatsApp.')
        webbrowser.open('https://web.whatsapp.com')
    elif 'instagram' in command:
        talk('Opening Instagram.')
        webbrowser.open('https://www.instagram.com')
    elif 'youtube' in command:
        talk('Opening Youtube.')
        webbrowser.open('https://www.youtube.com/')
    elif 'chatgpt' in command:
        talk('Opening ChatGPT.')
        webbrowser.open('https://chatgpt.com/?model=auto/')
    elif 'how are you' in command:
        talk("I'm good, and you?")
        user_reply = take_command()
        if 'good' in user_reply or 'fine' in user_reply:
            talk("You deserve all the best.")
        else:
            talk("I hope you feel better soon.")
    else:
        talk('Please repeat the command.')

def on_search():
    command = entry.get()
    run_Orion(command)

def on_voice_search():
    command = take_command()
    entry.delete(0, tk.END)  # Clear the search bar
    entry.insert(0, command)  # Insert the voice command into the search bar
    run_Orion(command)

# Create main window
root = tk.Tk()
root.title("Orion Personal Assistant")
root.geometry("1188x1177+100+100")  # Adjust window size to make it more professional
root.resizable(True, True)  # Prevent resizing the window
root.config(background="#2c3e50")  # Change background color to dark blue

# Set icon
image_icon = PhotoImage(file="Images_icon/Orion.png")
root.iconphoto(False, image_icon)

# Create main frame to organize contents
main_frame = tk.Frame(root, bg="#2c3e50")
main_frame.pack(expand=True)

# Add personal assistant logo
try:
    logo = PhotoImage(file="Images_icon/alexa_logo.png")  # Ensure logo image exists
    logo_label = tk.Label(main_frame, image=logo, bg="#2c3e50")
    logo_label.grid(row=0, column=0, columnspan=2, pady=20)
except Exception as e:
    print("Error loading logo:", e)

# Create search bar
entry_style = ttk.Style()
entry_style.configure('TEntry', foreground='black', font=('Arial', 14))

entry = ttk.Entry(main_frame, width=40, font=('Arial', 14))
entry.grid(row=1, column=0, padx=10, pady=10)

# Create search button
search_img = PhotoImage(file="Images_icon/search.png")  # Search icon
search_button = tk.Button(main_frame, image=search_img, command=on_search, borderwidth=0, bg="#2c3e50", activebackground="#34495e")
search_button.grid(row=1, column=1, padx=10, pady=10)

# Create voice search button
voice_img = PhotoImage(file="Images_icon/microphone_icon.png")  # Microphone icon
voice_button = tk.Button(main_frame, image=voice_img, command=on_voice_search, borderwidth=0, bg="#2c3e50", activebackground="#34495e")
voice_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create volume bar
canvas = tk.Canvas(main_frame, width=50, height=300, bg="#2c3e50", highlightthickness=0)
canvas.grid(row=3, column=0, columnspan=2, pady=20)

# Add quick command icons
icons_frame = tk.Frame(main_frame, bg="#2c3e50")
icons_frame.grid(row=4, column=0, columnspan=2, pady=10)

# Define quick commands and their icons
quick_commands = [
    ("ChatGPT", "Images_icon/chatgpt (2).png", lambda: run_Orion("chatgpt")),
    ("Time", "Images_icon/time.png", lambda: run_Orion("time")),
    ("Joke", "Images_icon/joke.png", lambda: run_Orion("joke")),
    ("Facebook", "Images_icon/facebook.png", lambda: run_Orion("facebook")),
    ("WhatsApp", "Images_icon/whatsapp.png", lambda: run_Orion("whatsapp")),
    ("Instagram", "Images_icon/instagram.png", lambda: run_Orion("instagram")),
    ("YouTube", "Images_icon/youtube.png", lambda: run_Orion("youtube")),
    ("Instagram", "Images_icon/instagram .png", lambda: run_Orion("instagram"))

]

# Add buttons for quick commands
for idx, (text, icon_path, command) in enumerate(quick_commands):
    try:
        icon = PhotoImage(file=icon_path)
        btn = tk.Button(icons_frame, image=icon, command=command, borderwidth=0, bg="#2c3e50", activebackground="#34495e")
        btn.image = icon  # Keep a reference to prevent garbage collection
        btn.grid(row=0, column=idx, padx=10)
        
        # Add tooltip on hover
        btn_tooltip = CreateToolTip(btn, text) # type: ignore
    except Exception as e:
        print(f"Error loading icon {icon_path}: {e}")

# Define class for tooltips
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # Delay before showing the tooltip (milliseconds)
        self.wraplength = 180   # Width of tooltip text
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # Create tooltip window
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)  # Remove border
        self.tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tw, text=self.text, justify='left',
background="#ffffff", relief='solid', borderwidth=1,
    wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

# متغير لتحديد اللغة الحالية (الإنجليزية افتراضياً)

current_language = 'en'

def toggle_language():
    global current_language
    if current_language == 'en':
        current_language = 'ar'
        talk("Language switched to Arabic")
    else:
        current_language = 'en'
        talk("Language switched to English")

def take_command():
    command = ""  # Initialize command with an empty string
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)  # Listen for up to 5 seconds
            
            # Convert audio data to numpy array and calculate RMS
            audio_data = np.frombuffer(voice.get_raw_data(), np.int16)
            rms = np.sqrt(np.mean(audio_data**2))
            normalized_rms = rms / 32768.0  # Normalize RMS value to range 0-1
            
            update_volume_bar(normalized_rms)
            
            # Recognize command based on the current language
            command = listener.recognize_google(voice, language=current_language)
            command = command.lower()
            if current_language == 'en' and 'Orion' in command:
                command = command.replace('Orion', '')
                print(command)
            elif current_language == 'ar' and 'أوريون' in command:
                command = command.replace('أوريون', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        talk("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, the speech recognition service is unavailable.")
        talk("Sorry, the speech recognition service is unavailable.")
    return command
  
  
  ##################################
def update_language(event):
    global language
    language = language_combobox.get().lower()
    talk(f"Language set to {language.capitalize()}")

    
#     # Create language combobox
# language_combobox = ttk.Combobox(main_frame, values=['English', 'Arabic'], state='readonly', font=('Arial', 14))
# language_combobox.grid(row=3, column=0, columnspan=2, pady=10)
# language_combobox.bind('<<ComboboxSelected>>', update_language)
# language_combobox.set('English')  # Set default value

  ################################

# Create language toggle button
toggle_lang_button = tk.Button(main_frame, text="Toggle Language", command=toggle_language, borderwidth=0, bg="#2c3e50", activebackground="#34495e", fg="white", font=('Arial', 12))
toggle_lang_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run main loop
root.after(1000, introduce_orion)  # Delay introduction by 1 second after window appears
root.mainloop()