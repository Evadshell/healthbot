import tkinter as tk
import openai
import speech_recognition as sr
from gtts import gTTS
import os

languages = {
    "en": ["What is your name?", "How are you feeling today?", "What is your gender?", "What is your age?", "Have you eaten anything recently?", "What are your current symptoms?", "Tell me more about it.", "Why do you think this is so?", "What is your current body temperature?", "What is your current heart rate?", "How long have you been feeling like this?", "Can you elaborate on your answer?"],
    "chhattisgarhi": ["आपका नाम काय हवय? ", "आप आज कैसा महसूस करत हवय? ", "आप का लिंग हवय? ", "आप का उम्र हवय? ", "का आप हाल ही म कुछु खाए हवय? ", "आपके वर्तमान लक्षण काय हवय? ", "मोला एखर बारे म अउ बताओ। ", "आप काबर सोचते हवय? ", "आपके वर्तमान शरीर के तापमान काय हवय? ", "आपके वर्तमान हृदय गति काय हवय? ", "आप कब ले ए तरह महसूस करत हवय? ", "क्या आप अपन उत्तर म विस्तार ले बता सकत हव?"],
    "hindi": ["आपका नाम क्या है?", "आज आप कैसा महसूस कर रहे हैं?", "आपका लिंग क्या है?", "आपकी उम्र क्या है?", "क्या आपने हाल ही में कुछ खाया है?", "क्या हैं आपके वर्तमान लक्षण?", "मुझे इसके बारे में और बताएं।", "आपको ऐसा क्यों लगता है?", "आपके वर्तमान शरीर का तापमान क्या है?", "आपकी वर्तमान हृदय गति क्या है?", "कब तक है आप ऐसा महसूस कर रहे हैं?", "क्या आप अपना उत्तर विस्तार से बता सकते हैं?"],
    "bangla": ["হাই, আপনার নাম কী?", "কেমন লাগছে আজ?", "আপনার লিঙ্গ কি?", "আপনার বয়স কত?", "আপনি কি সম্প্রতি কিছু খেয়েছেন?", "আপনার বর্তমান উপসর্গ কি?", "এটি সম্পর্কে আমাকে আরও বলুন।", "এটা এমন কেন মনে হয়?", "আপনার শরীরের বর্তমান তাপমাত্রা কত?", "আপনার বর্তমান হার্ট রেট কত?", "আপনি কতদিন ধরে এইরকম অনুভব করছেন?", "আপনি কি আপনার উত্তর বিস্তারিত বলতে পারবেন?"],
    "bhoj": ["तोहार नाम का बा?","आज कइसन लागत बा?", "रउरा लिंग का बा?","रउरा उमिर का बा?","हाल में कुछ खइले बानी का?","रउरा वर्तमान लक्षण का बा?","एह बारे में अउरी बताईं।","रउरा का लागत बा कि ई अइसन काहे बा?","रउरा शरीर के वर्तमान तापमान का बा?","रउरा वर्तमान दिल के धड़कन का बा?","कब से रउरा अइसन महसूस करत बानी?","का रउआ अपना जवाब के बारे में विस्तार से बता सकत बानी?"],
    "malayalam": ["നിങ്ങളുടെ പേരെന്താണ്?", "ഇന്ന് നിങ്ങൾക്ക് എങ്ങനെ തോന്നുന്നു?", "നിങ്ങളുടെ ലിംഗഭേദം എന്താണ്?", "നിങ്ങളുടെ പ്രായം എന്താണ്?", "നിങ്ങൾ അടുത്തിടെ എന്തെങ്കിലും കഴിച്ചോ?", "എന്താണ്? നിങ്ങളുടെ നിലവിലെ ലക്ഷണങ്ങൾ?", "ഇതിനെക്കുറിച്ച് എന്നോട് കൂടുതൽ പറയൂ.", "എന്തുകൊണ്ടാണിത് അങ്ങനെയെന്ന് നിങ്ങൾ കരുതുന്നു?", "നിങ്ങളുടെ നിലവിലെ ശരീരത്തിന്റെ താപനില എന്താണ്?", "നിങ്ങളുടെ നിലവിലെ ഹൃദയമിടിപ്പ് എന്താണ്?", "എത്ര കാലമായി?", "നിങ്ങൾക്ക് അങ്ങനെ തോന്നുന്നുണ്ടോ?", "നിങ്ങളുടെ ഉത്തരം വിശദീകരിക്കാമോ?"],
    "marathi": ["तुमचे नाव काय आहे?", "आज कसे वाटत आहे?", "तुमचे लिंग काय आहे?", "तुमचे वय काय आहे?", "तपाईले भर्खरै केहि खानु भएको छ?", "काय आहेत तुमची सध्याची लक्षणे?", "मला याबद्दल अधिक सांगा.", "तुम्हाला असे का वाटते?", "तुमचे सध्याचे शरीराचे तापमान काय आहे?", "तुमचे सध्याचे हृदय गती काय आहे?", "किती वेळ आहे?" ,"तुम्हाला असे वाटत होते?", "तुम्ही तुमचे उत्तर सविस्तर सांगू शकाल का?"],
    "nepali": ["तिम्रो नाम के हो?", "आज कस्तो महसुस गर्दै हुनुहुन्छ?", "तिम्रो लिङ्ग के हो?", "तिम्रो उमेर के हो?", "तपाईले भर्खरै केहि खानु भएको छ?", "के हो? तपाईको हालका लक्षणहरू?", "मलाई यसको बारेमा थप बताउनुहोस्।", "तपाईलाई किन यस्तो लागछ?", "तपाईको हालको शरीरको तापक्रम कति छ?", "तपाईको हालको मुटुको दर कति छ?", "कति लामो छ?" ,"तपाईलाई यस्तो महसुस भइरहेको छ?", "के तपाई आफ्नो जवाबको बारेमा विस्तृत रूपमा बताउन सक्नुहुन्छ?"],
}

root = tk.Tk()
root.title("Multilingual Questionnaire Chat")
root.geometry("300x150")
chat_history = tk.Text(root, width=50, height=10)
chat_history.pack()
user_input = tk.Entry(root, width=80)
root.configure(bg="cyan")
root.title("personal chat")
current_language = "en"
current_question_index = 0

recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang=current_language)
    tts.save("output.mp3")
    os.system("start output.mp3")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        user_input.delete(0, tk.END)
        user_input.insert(0, "Listening...")
        user_input.update_idletasks()
        try:
            user_response = recognizer.recognize_google(audio)
            user_input.delete(0, tk.END)
            user_input.insert(0, user_response)
        except sr.UnknownValueError:
            user_input.delete(0, tk.END)
            user_input.insert(0, "Could not understand audio")
        except sr.RequestError as e:
            user_input.delete(0, tk.END)
            user_input.insert(0, f"Error: {e}")

def ask_question():
    global current_language, current_question_index

    if current_language in languages:
        questions = languages[current_language]
        if current_question_index < len(questions):
            question = questions[current_question_index]
            chat_history.insert(tk.END, f"ChatGPT ({current_language}): {question}\n")
            speak(question)  # Speak the question
            current_question_index += 1
        else:
            chat_history.insert(tk.END, "ChatGPT: No more questions in this language.\n")
    else:
        chat_history.insert(tk.END, "ChatGPT: I don't understand this language.\n")

def change_language(language):
    global current_language, current_question_index
    current_language = language
    current_question_index = 0

language_buttons = []
for lang in languages:
    button = tk.Button(root, text=lang, command=lambda l=lang: change_language(l))
    language_buttons.append(button)
    button.pack()

ask_button = tk.Button(root, text="Ask", command=ask_question)
ask_button.pack()

listen_button = tk.Button(root, text="Listen", command=listen)
listen_button.pack()

root.mainloop()

'''
import pyttsx3
import spacy
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Healthbot")

# Create other widgets and functions

# Start the GUI main loop
root.mainloop()

# Load a spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define greetings
greetings = ["hi", "hello", "hey"]

# Function to check if user input is a greeting
def is_greeting(text):
    doc = nlp(text)
    for token in doc:
        if token.text.lower() in greetings:
            return True
    return False

# Function to provide a response
def get_response(user_query):
    if is_greeting(user_query.lower()):
        return "Hello there! How can I assist you today?"
    # Implement more logic for different types of queries here
    return "I found information about your query on the internet."

# ... Rest of your code (GUI setup and send_query function)

# Modify send_query function to use get_response
def send_query():
    user_query = user_input.get()
    if user_query:
        conversation_text.config(state=tk.NORMAL)
        conversation_text.insert(tk.END, f"You: {user_query}\n")
        conversation_text.config(state=tk.DISABLED)
        user_input.delete(0, tk.END)

        response = get_response(user_query)
        
        conversation_text.config(state=tk.NORMAL)
        conversation_text.insert(tk.END, f"Healthbot: {response}\n")
        conversation_text.config(state=tk.DISABLED)
        speak(response)

# ... Rest of your code

# Start the GUI main loop
root.mainloop()
 '''