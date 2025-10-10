from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()

setup(
  name="PyMacro",
  version="1.0.0",
  author="César Ramírez",
  author_email="cesar.ram.30020@gmail.com",
  description="Aplicación para crear y ejecutar macros de teclado y mouse para automatizar tareas repetitivas.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/CesarRam30020/PyMacro",
  packages=find_packages(include=["scripts", "scripts.*"]),
  include_package_data=True,
  package_data={
    "": ["*.ins"],  # incluye archivos .ins en cualquier subcarpeta
  },
  install_requires=[
    "MouseInfo>=0.1.3 ",
    "pip>=4.3.1",
    "PyAutoGUI>=0.9.54",
    "PyGetWindow>=0.0.9 ",
    "PyMsgBox>=2.0.1 ",
    "pyperclip>=1.11.0",
    "PyRect>=0.2.0 ",
    "PyScreeze>=1.0.1 ",
    "pytweening>=1.2.0 ",
    "tk>=0.1.0",
    "pyinstaller>=6.16.0",
    "pyinstaller-hooks-contrib>=2025.9",
    # agrega dependencias si usas tkinter, customtkinter, etc.
  ],
  python_requires=">=3.9",
  entry_points={
    "console_scripts": [
      # permite ejecutar 'pymacro' desde la terminal
      "pymacro=scripts.main:main",
    ],
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Utilities",
    "Intended Audience :: End Users/Desktop",
    "Development Status :: 4 - Beta",
  ],
  keywords="automation macros keyboard mouse tkinter gui",
)
