import tkinter
from tkinter import *
import tkinter.filedialog
import yaml
import requests
import os
import sys


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def write_config():
    with open("config.yaml", "w+") as f:
        yaml.dump(config, f, default_flow_style=False)


config = load_config()

mods = yaml.load(requests.get(config.get("sources")).text, Loader=yaml.FullLoader)

mods_fetched = {}

for k, v in mods.items():
    mods_fetched[k] = requests.get(v).json()

os.chdir(os.path.dirname(__file__))
os.makedirs("cache", exist_ok=True)

def install():
    print("installing", mod.get(), "to", goldsrc_path.get())
    # make dir in mods_fetched[mod.get()]["dir"]
    # os.makedirs(os.path.join(goldsrc_path.get(), mods_fetched[mod.get()]["dir"]), exist_ok=True)
    # https://github.com/HLSourceHub/goldsrc-wizardwars_beta/archive/refs/heads/master.zip
    # https://raw.githubusercontent.com/HLSourceHub/goldsrc-wizardwars_beta/master/wizardwars_beta.sourcehub.json


import tkinter as tk
import pygubu
from SourceHubModManui import asdUI


def entry_set(entry, value):
    entry.delete(0, tk.END)
    entry.insert(0, value)


def prompt_goldsrc_dir(initialdir):
    goldsrc_dir = tkinter.filedialog.askdirectory(initialdir=initialdir)
    if not goldsrc_dir.strip():
        return initialdir
    config["goldsrc_path"] = goldsrc_dir
    write_config()
    return goldsrc_dir


class asd(asdUI):
    def __init__(self, master=None):
        super().__init__(master)

        install_button = self.builder.get_object("installbutton")
        install_button.config(command=lambda: print("INSTALL"))
        

        goldsrc_path = self.builder.get_object("goldsrc_path")
        entry_set(goldsrc_path, config.get("goldsrc_path"))

        goldsrc_path_button = self.builder.get_object("gamepathbutton")
        goldsrc_path_button.config(command=lambda: entry_set(goldsrc_path, prompt_goldsrc_dir(goldsrc_path.get())))

        # mod = tkinter.StringVar()
        # mod.set(list(mods_fetched.keys())[0])
        # mod_label = tkinter.Label(root, text="Mod")
        # mod_label.pack()
        # mod_dropdown = tkinter.OptionMenu(root, mod, *mods_fetched.keys())
        # mod_dropdown.pack()


if __name__ == "__main__":
    app = asd()
    app.run()
