import tkinter

from canvas import *
from helpers import clean_screen


def render_entry():
    register_btn = tkinter.Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )

    loging_btn = tkinter.Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 200, window=register_btn)
    frame.create_window(350, 260, window=loging_btn)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = tkinter.Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        command=registration
    )

    frame.create_window(300, 250, window=registration_btn)


def login():
    clean_screen()


def registration():
    pass


first_name_box = tkinter.Entry(root, bd=0)
last_name_box = tkinter.Entry(root, bd=0)
username_box = tkinter.Entry(root, bd=0)
password_box = tkinter.Entry(root, bd=0)
