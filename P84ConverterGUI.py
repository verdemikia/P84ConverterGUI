import tkinter as tk
from tkinter import ttk, filedialog
import subprocess

def run_blasters_to_normal_battle():
    folder_path = filedialog.askdirectory()
    if folder_path:
        subprocess.run(["python", "BlastersToNormalBattle.py", folder_path])

def run_normal_battle_to_blasters():
    folder_path = filedialog.askdirectory()
    if folder_path:
        subprocess.run(["python", "NormalBattleToBlasters.py", folder_path])

# Title
root = tk.Tk()
root.title("P84ConverterGUI")

initial_width = 150  
initial_height = 100 

# responsive shit
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Windows 10/11 button style
style = ttk.Style()
style.configure('TButton', padding=6, relief='raised')

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Blasters to normal battle code
btn_blasters_to_normal_battle = ttk.Button(main_frame, text="Blasters to Normal Battle", command=run_blasters_to_normal_battle, width=40)
btn_blasters_to_normal_battle.grid(row=0, column=0, padx=10, pady=10)

# Normal battle to blasters code
btn_normal_battle_to_blasters = ttk.Button(main_frame, text="Normal Battle to Blasters", command=run_normal_battle_to_blasters, width=40)
btn_normal_battle_to_blasters.grid(row=1, column=0, padx=10, pady=10)

# Credits
credits_label = ttk.Label(root, text="Credit:\Mikki (GUI)\nMath_kk (OG script)")
credits_label.grid(row=1, column=0, sticky="se", padx=10, pady=10)

root.update()
root.geometry('{}x{}'.format(initial_width * 3, initial_height * 3))

root.mainloop()

