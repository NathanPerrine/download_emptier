from tkinter.messagebox import YES
from typing import List
from tkinter import filedialog
import tkinter as tk
import os
import json


def load_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data


def create_json_file():
    # TODO: Create json
    #   

    tk.messagebox.showinfo(title="Select Downloads", message="Select your download folder from the explorer.")
    dl_path = tk.filedialog.askdirectory()
    if dl_path:
        print(dl_path)
        with open("./folders.json", "w", encoding="utf-8") as f:
            data = {
                "download": dl_path,
                "destinations" : [] 
            }
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        create_json_file()


def move_file(from_box, to_box, file):
    # TODO: move_file
    #   Move file to new directory
    #   Reset downloads list
    #   Display what moved to where
    # selected_files = dl_list_box.curselection()
    pass


def fill_list_box(box, info: List) -> None:
    # TODO: fill_list_box
    #   
    for i, v in enumerate(info):
        box.insert(i, v)


def add_destination(box):
    print("hello world")
    new_dest = filedialog.askdirectory()

    if new_dest:
        with open('./folders.json', 'r+') as f:
            data = json.load(f)
            data['destinations'].append(new_dest)
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    fill_list_box(box, data['destinations'])

def main():
    ### Main Window ###
    window = tk.Tk()
    window.geometry('700x350')


    ### Load / Create Information ### 
    if os.path.exists("./folders.json"):
        info = load_from_json("./folders.json")
    else: 
        create_json_file()
        info = load_from_json("./folders.json")

    # print(info)

    ### Downloads ### 
    # DL LabelFrame
    dl_frame = tk.LabelFrame(window, text="Downloads")
    # dl_frame.pack(padx=20, pady=20)
    dl_frame.grid(row=0, column=2, padx=20, pady=20)

    # DL Listbox
    dl_list = os.listdir(info['download'])
    dl_list_box = tk.Listbox(dl_frame, selectmode="multiple")
    dl_list_box.pack(padx=10, pady=10)
    fill_list_box(dl_list_box, dl_list)


    ### Arrow Button ### 
    # Arrow Frame
    arrow_frame = tk.Frame(window, highlightbackground='black', highlightthickness=1)
    # arrow_frame.pack(side=tk.LEFT)
    arrow_frame.grid(row=0, column=3, padx=5)

    # Arrow Button
    arrow_button = tk.Button(arrow_frame, text="->")
    arrow_button.pack()


    ### Destinations ### 
    # Dest. frame 
    destination_frame = tk.LabelFrame(window, text="Destination")
    destination_frame.grid(row=0, column=4, padx=20, pady=20)

    # Dest. Listbox 
    destination_list_box = tk.Listbox(destination_frame, width=25)
    destination_list_box.grid(row=0, column=0, padx=10, pady=10)
    fill_list_box(destination_list_box, info['destinations'])
    
    # Dest. button frame 
    dest_button_frame = tk.Frame(destination_frame)
    dest_button_frame.grid(row=0, column=1, padx=(0,10))
    # Add destination button
    add_button = tk.Button(dest_button_frame, text="+", command= lambda: add_destination(destination_list_box))
    add_button.pack()

    ### Main Loop ### 
    window.mainloop()


if __name__ == "__main__":
    main()


# TODO: Main
#   Add destination button
#   Save destination folders
#   Transfer Log   
#   