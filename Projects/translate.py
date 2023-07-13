import tkinter as tk
from tkinter.ttk import Notebook

class Translate(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Translate")
        self.notebook = Notebook(self)
        self.notebook.pack(fill = tk.BOTH, expand= 1)
        
        english_tab = tk.Frame(self.notebook)
        self.english_entry = tk.Text(english_tab)
        self.english_entry.pack(side = tk.TOP, expand= 1)
        self.notebook.add(english_tab, text = "English")


        self.translate_button = tk.Button(english_tab, text="Translate",
                                          command = self.translate)
        
        self.translate_button.pack(side = tk.BOTTOM, fill= tk.X)
        


        spanish_tab = tk.Frame(self.notebook)
        self.notebook.add(spanish_tab,text="Spanish")
        self.spanish_entry = tk.Text(spanish_tab)
        
    def translate(self):
        print("MOTHERFUCKING TRANSLATING")





if __name__ == "__main__":
    translate = Translate()
    translate.mainloop()