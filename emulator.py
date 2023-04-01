import os
import tkinter as tk
from pyboy import PyBoy

class GameBoy:
    def __init__(self):
        self.rom_folder = "ROMS"
        self.window = tk.Tk()
        self.window.title("Game Boy")
        self.window.configure(background='gray')
        self.create_ui()

    def create_ui(self):
        # Create a label to prompt the user to choose a game
        prompt_label = tk.Label(self.window, text="Choose a Game", background='gray')
        prompt_label.pack(padx=10, pady=10)
        # Create a listbox to display the ROM files
        rom_listbox = tk.Listbox(self.window, height=20, width=50)
        rom_listbox.pack(padx=10, pady=10)
        # Add all ROM files to the listbox
        for file in os.listdir(self.rom_folder):
            if file.endswith(".gb") or file.endswith(".gbc"):
                rom_listbox.insert(tk.END, file)
        # Bind double-click on a game to start the game
        rom_listbox.bind("<Double-Button-1>", lambda event: self.start_game(rom_listbox.get(tk.ACTIVE)))
        # Add a button to add more games
        add_button = tk.Button(self.window, text="Add Games", command=self.add_games)
        add_button.pack(pady=10)

    def start_game(self, rom_name):
        pyboy = PyBoy('ROMS/'+rom_name)
        while not pyboy.tick():
            pass
        pyboy.stop()

    def add_games(self):
        # TODO: add games from https://roms-telecharger.com/roms/gameboy
        pass

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    library = GameBoy()
    library.run()
