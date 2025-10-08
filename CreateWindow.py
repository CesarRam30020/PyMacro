from tkinter import Toplevel

class CreateWindow(Toplevel):
  def __init__(self, title = "Title"):
    super().__init__()
    self.title(title)

    # self.wm_attributes("-alpha", 0.7)
    # self.wm_attributes("-fullscreen", True)

  #   self.bind("<Button>", self.on_click)

  # def on_click(self, event):
  #   print(f"({event.x}, {event.y})")