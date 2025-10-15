from os import listdir, makedirs, system
from pyautogui import moveTo, click, write
from time import sleep
import re

BASE_PATH = "instructions/"

def getInstructionFiles():
  makedirs(BASE_PATH, exist_ok = True)
  return [_ for _ in listdir(BASE_PATH) if _[-4:] == ".ins"]

def deleteInstructionFile(file):
  try:
    import os
    os.remove(f"{BASE_PATH}{file}")
    return True
  except Exception as e:
    print(f"Error deleting file: {e}")
    return False

def runInstructions(file: str):
  if file == "None":
    raise ValueError("No instruction file provided")

  with open(f"{BASE_PATH}{file}", "r") as file:
    instructions = file.readlines()

    for instruction in instructions:
      if re.match("(^#.*$|^$)", instruction):
        continue

      match instruction.split("="):
        case ["start", params]:
          system(f"start {params.strip()}")

        case ["shutdown", params]:
          system(f"shutdown {params.strip()}")

        case ["await", params]:
          sleep(float(params))

        case ["click", params]:
          click(*map(int, params.split(",")))

        case ["write", params]:
          write(params.strip())

        case ["moveTo", params]:
          moveTo(*map(int, params.split(",")))

        case _:
          print(f"Unknown instruction {instruction}")

  return True

def saveInstructions(file: str, text: str):
  print(file.find(".ins"))
  file = file if file.find(".ins") != -1 else f"{file}.ins"

  with open(f"{BASE_PATH}{file}", "w+") as f:
    f.write(text)