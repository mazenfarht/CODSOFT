import re
from tkinter import Tk, Text, Scrollbar, Button, Entry, END, Frame, Label
from tkinter.font import Font

def rule_based_chatbot(input_text):
    # Define rules for responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am a chatbot. I don\'t have feelings, but thanks for asking!',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'what is your name': 'I am a rule-based chatbot.',
        r'(\w+) weather': 'I\'m sorry, I cannot provide real-time weather information.',
        r'what can you do': 'I can chat with you and answer basic questions!',
        r'help': 'How can I assist you?',
        r'how old are you': 'I am a timeless chatbot, ageless and ever-present.',
        r'tell me a joke': 'Why did the scarecrow win an award? Because he was outstanding in his field!',
        r'where are you from': 'I exist in the digital realm, everywhere and nowhere.',
        r'what is the meaning of life': '42. According to The Hitchhiker\'s Guide to the Galaxy.',
        r'who created you': 'I was created by OpenAI to assist with various tasks.',
        r'thank you|thanks': 'You\'re welcome!',
        r'i love you': 'Me too!',
        r'default': 'I\'m not sure how to respond to that.'
        
    }

    # Check input against rules
    for pattern, response in rules.items():
        if re.search(pattern, input_text, re.IGNORECASE):
            return response

    # If no match found, use the default response
    return rules['default']

class ChatbotGUI:
    def __init__(self):
        self.app = Tk()
        self.app.title("Chatbot")
        self.app.configure(bg='#f0f0f0')  # Set background color
        
        # Custom fonts
        self.font = Font(family="Helvetica", size=12)
        self.bot_font = Font(family="Helvetica", size=12, weight="bold")
        self.user_font = Font(family="Helvetica", size=12, slant="italic")
        
        # Frame for chat display
        self.frame = Frame(self.app, bg='#f0f0f0')
        self.scrollbar = Scrollbar(self.frame)
        self.text_widget = Text(self.frame, height=20, width=50, yscrollcommand=self.scrollbar.set, wrap='word', font=self.font, bg='#ffffff', fg='#000000')
        self.scrollbar.pack(side='right', fill='y')
        self.scrollbar.config(command=self.text_widget.yview)
        self.text_widget.pack(side='left', fill='both', expand=True)
        self.frame.pack(pady=10)
        
        # Entry widget for user input
        self.entry = Entry(self.app, width=40, font=self.font, bg='#e0e0e0', fg='#000000')
        self.entry.pack(side='left', padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = Button(self.app, text="Send", command=self.send_message, font=self.font, bg='#0078D7', fg='#ffffff', activebackground='#0056a3', activeforeground='#ffffff')
        self.send_button.pack(side='left', padx=10, pady=10)
        
        # Initial message from chatbot
        self.text_widget.insert(END, "Chatbot: Hello! How can I help you?\n", 'bot')
        
        # Tag configurations for styling
        self.text_widget.tag_configure('bot', foreground='#0078D7', font=self.bot_font)
        self.text_widget.tag_configure('user', foreground='#008000', font=self.user_font)
        
    def send_message(self, event=None):
        user_input = self.entry.get()
        if user_input.strip():
            self.text_widget.insert(END, f"You: {user_input}\n", 'user')
            self.entry.delete(0, END)
            bot_response = rule_based_chatbot(user_input)
            self.text_widget.insert(END, f"Chatbot: {bot_response}\n", 'bot')
            self.text_widget.yview(END)
        
    def mainloop(self):
        self.app.mainloop()

if __name__ == '__main__':
    gui = ChatbotGUI()
    gui.mainloop()
