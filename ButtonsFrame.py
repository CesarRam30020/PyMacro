from tkinter import Frame, Button

class ButtonsFrame(Frame):
  def __init__(self, root, buttons = []):
    super().__init__(root)

    for i, button in enumerate(buttons):
      btn = Button(
        self,
        text=button["text"],
        command=button["command"]
      )
      btn.grid(row=i, column=0)