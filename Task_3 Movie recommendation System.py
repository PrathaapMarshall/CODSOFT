import tkinter as tk
from tkinter import messagebox



window_width = 850
window_height = 700

root = tk.Tk()

root.title("Movie Recommendation System")

root.geometry(f"{window_width}x{window_height}")

root.configure(bg="#0B1026")

root.resizable(False, False)


BG_COLOR = "#0B1026"
TITLE_COLOR = "#FFD700"
BUTTON_COLOR = "#7C3AED"
HOVER_COLOR = "#EC4899"
TEXT_COLOR = "white"
BOX_COLOR = "#111827"



movies = {

    "Action": [
        "Avengers Endgame",
        "John Wick",
        "Mad Max Fury Road",
        "Mission Impossible",
        "Black Panther"
    ],

    "Comedy": [
        "The Mask",
        "Home Alone",
        "Mr Bean's Holiday",
        "Jumanji",
        "Free Guy"
    ],

    "Sci-Fi": [
        "Interstellar",
        "The Martian",
        "Avatar",
        "Star Wars",
        "Dune"
    ],

    "Horror": [
        "The Conjuring",
        "Insidious",
        "IT",
        "Annabelle",
        "The Nun"
    ],

    "Romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You",
        "The Vow"
    ],

    "Animation": [
        "Toy Story",
        "Frozen",
        "Finding Nemo",
        "Up",
        "Kung Fu Panda"
    ]
}


start_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

start_frame.pack(
    fill="both",
    expand=True
)

title_label = tk.Label(

    start_frame,

    text="MOVIE RECOMMENDATION SYSTEM",

    bg=BG_COLOR,

    fg=TITLE_COLOR,

    font=("Arial", 26, "bold")

)

title_label.pack(
    pady=(180, 20)
)

subtitle_label = tk.Label(

    start_frame,

    text="Find Movies You'll Love",

    bg=BG_COLOR,

    fg=TEXT_COLOR,

    font=("Arial", 18)

)

subtitle_label.pack(
    pady=10
)

def hover_enter(event):

    start_button.config(
        bg=HOVER_COLOR
    )

def hover_leave(event):

    start_button.config(
        bg=BUTTON_COLOR
    )

#start button function

def start_app():

    start_frame.pack_forget()

    create_main_screen()

#Start

start_button = tk.Button(

    start_frame,

    text="START",

    width=15,

    height=2,

    bg=BUTTON_COLOR,

    fg="white",

    font=("Arial", 16, "bold"),

    command=start_app

)

start_button.pack(
    pady=40
)

start_button.bind(
    "<Enter>",
    hover_enter
)

start_button.bind(
    "<Leave>",
    hover_leave
)

#main_screen

def create_main_screen():

    global main_frame
    global recommendation_box

    main_frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main_frame.pack(
        fill="both",
        expand=True
    )

    #title

    heading = tk.Label(

        main_frame,

        text="Choose Your Favorite Genre",

        bg=BG_COLOR,

        fg=TITLE_COLOR,

        font=("Arial", 22, "bold")

    )

    heading.pack(
        pady=20
    )

#Buttons for genres

    button_frame = tk.Frame(
        main_frame,
        bg=BG_COLOR
    )

    button_frame.pack(
        pady=10
    )


    action_btn = tk.Button(

        button_frame,

        text="Action",

        width=15,

        height=2,

        bg=BUTTON_COLOR,

        fg="white",

        font=("Arial", 12, "bold"),

        command=lambda:
        show_recommendations("Action")

    )

    action_btn.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    comedy_btn = tk.Button(

        button_frame,

        text="Comedy",

        width=15,

        height=2,

        bg=BUTTON_COLOR,

        fg="white",

        font=("Arial", 12, "bold"),

        command=lambda:
        show_recommendations("Comedy")

    )

    comedy_btn.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    scifi_btn = tk.Button(

        button_frame,

        text="Sci-Fi",

        width=15,

        height=2,

        bg=BUTTON_COLOR,

        fg="white",

        font=("Arial", 12, "bold"),

        command=lambda:
        show_recommendations("Sci-Fi")

    )

    scifi_btn.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    horror_btn = tk.Button(

        button_frame,

        text="Horror",

        width=15,

        height=2,

        bg=BUTTON_COLOR,

        fg="white",

        font=("Arial", 12, "bold"),

        command=lambda:
        show_recommendations("Horror")

    )

    horror_btn.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    romance_btn = tk.Button(

        button_frame,

        text="Romance",

        width=15,

        height=2,

        bg=BUTTON_COLOR,

        fg="white",

        font=("Arial", 12, "bold"),

        command=lambda:
        show_recommendations("Romance")

    )

    romance_btn.grid(
        row=2,
        column=0,
        padx=10,
        pady=10
    )

    animation_btn = tk.Button(

        button_frame,

        text="Animation",

        width=15,

        height=2,

        bg=BUTTON_COLOR,

        fg="white",

        font=("Arial", 12, "bold"),

        command=lambda:
        show_recommendations("Animation")

    )

    animation_btn.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )



    recommendation_box = tk.Text(

        main_frame,

        width=55,

        height=12,

        bg=BOX_COLOR,

        fg="white",

        font=("Arial", 14),

        bd=2

    )

    recommendation_box.pack(
        pady=25
    )

    recommendation_box.insert(
        "end",
        "Select a genre to get recommendations."
    )

    recommendation_box.config(
        state="disabled"
    )
   #recommendation function

def show_recommendations(genre):

    recommendation_box.config(
        state="normal"
    )

    recommendation_box.delete(
        "1.0",
        "end"
    )

    recommendation_box.insert(
        "end",
        f"\nRecommended {genre} Movies\n\n"
    )

    for movie in movies[genre]:

        recommendation_box.insert(
            "end",
            f"🎬 {movie}\n"
        )

    recommendation_box.config(
        state="disabled"
    )

#reset

def reset_recommendations():

    recommendation_box.config(
        state="normal"
    )

    recommendation_box.delete(
        "1.0",
        "end"
    )

    recommendation_box.insert(
        "end",
        "Select a genre to get recommendations."
    )

    recommendation_box.config(
        state="disabled"
    )


#project small info in about section


def about_project():

    messagebox.showinfo(

        "About",

        "Movie Recommendation System\n\n"
        "Uses content-based filtering.\n"
        "Movies are recommended based on "
        "the genre selected by the user."

    )

#controls

control_frame = tk.Frame(

    bg=BG_COLOR
)

control_frame.pack(
    pady=10
)

reset_button = tk.Button(

    control_frame,

    text="RESET",

    width=12,

    height=2,

    bg=BUTTON_COLOR,

    fg="white",

    font=("Arial", 12, "bold"),

    command=reset_recommendations

)

reset_button.grid(
    row=0,
    column=0,
    padx=10
)

about_button = tk.Button(

    control_frame,

    text="ABOUT",

    width=12,

    height=2,

    bg=BUTTON_COLOR,

    fg="white",

    font=("Arial", 12, "bold"),

    command=about_project

)

about_button.grid(
    row=0,
    column=1,
    padx=10
)



root.mainloop()