from tkinter import Toplevel

class CreateWindow(Toplevel):
  def __init__(self, title = "Title"):
    super().__init__()
    self.title(title)

    