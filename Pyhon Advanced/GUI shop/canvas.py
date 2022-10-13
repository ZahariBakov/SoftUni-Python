import tkinter


def create_app():
    root = tkinter.Tk()

    root.geometry("700x600")
    root.title("GUI Product shop")

    return root


def create_frame():
    frame = tkinter.Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_app()
frame = create_frame()
