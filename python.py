import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import difflib
import random

# APP SETTINGS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_TITLE = "Smart Rule-Based ChatBot"

bot_name = "Simple ChatBot"

fail_count = 0

chat_history_file = "chat_history.txt"

#Jokes and quotes for the chatbot

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to school? To improve its class!",
    "I only know binary jokes: 0 and 1.",
    "Debugging is like being a detective in your own crime movie.",
    "Why do Java developers wear glasses? Because they can't C."
]

# QUOTES

quotes = [
    "Believe in yourself.",
    "Consistency beats motivation.",
    "Dream big and work hard.",
    "Keep learning every day.",
    "Success is built one step at a time."
]

# SIMILAR SEARCH

known_commands = [
    "hello",
    "hi",
    "help",
    "joke",
    "quote",
    "time",
    "date",
    "thanks",
    "college",
    "food",
    "color",
    "creator",
    "age",
    "weather",
    "bye"
]

def suggest_command(user_input):

    suggestion = difflib.get_close_matches(
        user_input,
        known_commands,
        n=1,
        cutoff=0.6
    )

    if suggestion:
        return suggestion[0]

    return None

# Save chat 

def save_chat(sender, message):

    with open(chat_history_file, "a", encoding="utf-8") as file:

        file.write(
            f"{sender}: {message}\n"
        )


# MAIN WINDOW

root = ctk.CTk()

root.title(APP_TITLE)

root.geometry("900x650")

root.resizable(False, False)


# START SCREEN

start_frame = ctk.CTkFrame(
    root,
    fg_color="transparent"
)

start_frame.pack(
    fill="both",
    expand=True
)


title_label = ctk.CTkLabel(
    start_frame,
    text="SMART RULE-BASED CHATBOT",
    font=("Arial", 32, "bold")
)

title_label.pack(
    pady=(150, 20)
)


welcome_label = ctk.CTkLabel(
    start_frame,
    text="Hi! How can I help you today?",
    font=("Arial", 20)
)

welcome_label.pack(
    pady=20
    )


def start_chat():
    start_frame.pack_forget()
    create_chat_window()



# HOVER EFFECT

def button_hover_enter(event):

    start_button.configure(
        width=230,
        height=55
    )

def button_hover_leave(event):

    start_button.configure(
        width=220,
        height=50
    )

start_button = ctk.CTkButton(
    start_frame,
    text="START CHAT",
    width=220,
    height=50,
    corner_radius=15,
    fg_color="#FF3B3B",
    hover_color="#FF0000",
    command=start_chat
)

start_button.pack(
    pady=30
)

start_button.bind(
    "<Enter>",
    button_hover_enter
)

start_button.bind(
    "<Leave>",
    button_hover_leave
)

# CHAT WINDOW UI

def create_chat_window():

    global chat_frame
    global chat_box
    global entry_box

    chat_frame = ctk.CTkFrame(
        root,
        fg_color="#0D0D0D"
    )

    chat_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # Chat Title
    chat_title = ctk.CTkLabel(
        chat_frame,
        text="Smart Rule-Based ChatBot",
        font=("Arial", 26, "bold")
    )

    chat_title.pack(
        pady=(10, 20)
    )

    # Chat Display
    chat_box = ctk.CTkTextbox(
        chat_frame,
        width=800,
        height=420,
        corner_radius=15,
        fg_color="#1A1A1A",
        text_color="white",
        font=("Arial", 14)
    )

    chat_box.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    chat_box.configure(
        state="disabled"
    )

    # Input Frame
    input_frame = ctk.CTkFrame(
        chat_frame,
        fg_color="transparent"
    )

    input_frame.pack(
        fill="x",
        padx=20,
        pady=15
    )

    # Grey Typing Bar
    entry_box = ctk.CTkEntry(
        input_frame,
        placeholder_text="Type your message...",
        height=45,
        corner_radius=12,
        fg_color="#2C2C2C",
        text_color="white"
    )

    entry_box.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 10)
    )

    # Press Enter to Send
    entry_box.bind(
        "<Return>",
        lambda event: process_input()
    )

    # Red Send Button
    send_button = ctk.CTkButton(
        input_frame,
        text="SEND",
        width=120,
        height=45,
        corner_radius=12,
        fg_color="#FF3B3B",
        hover_color="#FF0000",
        command=process_input
    )

    send_button.pack(
        side="left"
    )

    # Save Chat Button
    save_button = ctk.CTkButton(
        chat_frame,
        text="Save Chat",
        width=150,
        fg_color="#FF3B3B",
        hover_color="#FF0000",
        command=lambda: messagebox.showinfo(
            "Saved",
            "Chat saved to chat_history.txt"
        )
    )

    save_button.pack(
        pady=(5, 5)
    )

    # Clear Chat Button
    clear_button = ctk.CTkButton(
        chat_frame,
        text="Clear Chat",
        width=150,
        fg_color="#FF3B3B",
        hover_color="#FF0000",
        command=clear_chat
    )

    clear_button.pack(
        pady=(0, 10)
    )

    display_message(
        bot_name,
        "Hi! How can I help you today?"
    )

# DISPLAY MESSAGES

def display_message(sender, message):

    chat_box.configure(
        state="normal"
    )

    chat_box.insert(
        "end",
        f"{sender}: {message}\n\n"
    )

    chat_box.configure(
        state="disabled"
    )

    chat_box.see("end")

    save_chat(sender, message)


# ==========================
# CLEAR CHAT
# ==========================

def clear_chat():

    chat_box.configure(
        state="normal"
    )

    chat_box.delete(
        "1.0",
        "end"
    )

    chat_box.configure(
        state="disabled"
    )

    display_message(
        bot_name,
        "Chat cleared successfully."
    )
    # ==========================
# PART 3
# CHATBOT LOGIC
# ==========================

def process_input():

    global fail_count

    user_txt = entry_box.get().strip()

    if user_txt == "":
        return

    entry_box.delete(0, "end")

    display_message(
        "You",
        user_txt
    )

    lower_txt = user_txt.lower()

    # Typing Effect
    display_message(
        bot_name,
        "Typing..."
    )

    root.after(
        600,
        lambda: generate_response(lower_txt)
    )


def generate_response(lower_txt):
    
    global fail_count

    # Remove Typing...
    chat_box.configure(state="normal")

    content = chat_box.get("1.0", "end")

    if content.endswith(f"{bot_name}: Typing...\n\n"):
        chat_box.delete("end-3l", "end")

    chat_box.configure(state="disabled")

    # GREETINGS
    greetings = ["hi", "hello", "hey"]

    if lower_txt in greetings:
        display_message(
            bot_name,
            "Hello! How can I help you today?"
        )
        fail_count = 0
        return

    # HELP
    if lower_txt == "help":

        display_message(
            bot_name,
            "You can ask about:"
        )

        display_message(
            bot_name,
            "time, date, joke, quote, weather, food,"
        )

        display_message(
            bot_name,
            "college, creator, age,"
        )

        display_message(
            bot_name,
            "color, thanks or bye."
        )

        return

    # JOKES
    if "joke" in lower_txt:

        display_message(
            bot_name,
            random.choice(jokes)
        )

        return

    # QUOTES
    if "quote" in lower_txt:

        display_message(
            bot_name,
            random.choice(quotes)
        )

        return

    # TIME
    if "time" in lower_txt:

        display_message(
            bot_name,
            datetime.now().strftime(
                "Current Time: %I:%M %p"
            )
        )

        return

    # DATE
    if "date" in lower_txt:

        display_message(
            bot_name,
            datetime.now().strftime(
                "Today's Date: %d-%m-%Y"
            )
        )

        return

    # THANKS
    if "thank" in lower_txt:

        display_message(
            bot_name,
            "You're welcome!"
        )

        return

    # COLLEGE
    if "college" in lower_txt or "school" in lower_txt:

        display_message(
            bot_name,
            "I don't go to college."
        )

        display_message(
            bot_name,
            "I live inside your computer!"
        )

        return

    # FOOD
    if "food" in lower_txt:

        display_message(
            bot_name,
            "I don't eat food,"
        )

        display_message(
            bot_name,
            "but pizza sounds delicious!"
        )

        return

    # COLOR
    if "color" in lower_txt:

        display_message(
            bot_name,
            "Black and red are my favorite colors."
        )

        return

    # WEATHER
    if "weather" in lower_txt:

        display_message(
            bot_name,
            "Sorry, I can't access live weather."
        )

        return

    # CREATOR
    if "creator" in lower_txt or "who made you" in lower_txt:

        display_message(
            bot_name,
            "I was created as an internship project."
        )

        return

    # AGE
    if "age" in lower_txt:

        display_message(
            bot_name,
            "I don't have an age."
        )

        display_message(
            bot_name,
            "I simply get updated!"
        )

        return

    # EXIT
    if lower_txt in ["bye", "exit", "quit"]:

        display_message(
            bot_name,
            "Goodbye! Have a nice day."
        )

        root.after(
            1000,
            root.destroy
        )

        return

    # SUGGESTION
    suggestion = suggest_command(lower_txt)

    if suggestion:

        display_message(
            bot_name,
            f"Did you mean '{suggestion}'?"
        )

        return

    # UNKNOWN INPUT
    fail_count += 1

    if fail_count >= 3:

        display_message(
            bot_name,
            "I'm lost 😅."
        )

        display_message(
            bot_name,
            "Type 'help' to see available commands."
        )

        fail_count = 0

    else:

        display_message(
            bot_name,
            "Sorry, I didn't understand that."
        )
        return
root.mainloop()