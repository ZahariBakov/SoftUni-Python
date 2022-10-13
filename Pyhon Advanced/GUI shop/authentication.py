from canvas import *


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
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 200, window=register_btn)
    frame.create_window(350, 260, window=loging_btn)


def register():
    pass


def login():
    pass
