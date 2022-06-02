from typing import List
import os
import tkinter as tk


# def open_file():
#     # items = dl_list_box.curselection()
#     for item in dl_list_box.curselection():
#         file = dl_list_box.get(item)
#         file_type = file[-4:]
#         # print(f"{file_type=}")
#         if file_type != '.exe':
#             file_path = f'D:\Downloads\\"{file}"'
#             print("start " + file_path)
#             # subprocess.Popen([file_path])
#             os.system("start " + file_path)


def move_file(from_box, to_box):
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


def main():
    ### Main Window ###
    window = tk.Tk()
    window.geometry('700x350')

    ### Downloads ### 
    # DL LabelFrame
    dl_frame = tk.LabelFrame(window, text="Downloads")
    # dl_frame.pack(padx=20, pady=20)
    dl_frame.grid(row=0, column=2, padx=20, pady=20)

    # DL Listbox
    dl_list = os.listdir('D:\Downloads')
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
    destination_list_box = tk.Listbox(destination_frame)
    destination_list_box.pack(padx=10, pady=10)

    ### Main Loop ### 
    window.mainloop()


if __name__ == "__main__":
    main()