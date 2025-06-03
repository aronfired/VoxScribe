# moduli_feedback.py
import tkinter as tk
from tkinter import messagebox
import json

def feedback_interface(trascrizione_iniziale, on_feedback_callback):
    """
    Crea una finestra Tkinter che mostra la trascrizione iniziale e permette di correggerla.
    Quando l'utente preme "Salva feedback", viene invocata la callback on_feedback_callback.
    """
    def salva_feedback():
        testo_corretta = text_area.get("1.0", tk.END).strip()
        if testo_corretta:
            on_feedback_callback(trascrizione_iniziale, testo_corretta)
            root.destroy()
        else:
            messagebox.showwarning("Attenzione", "Inserisci la trascrizione corretta.")

    root = tk.Tk()
    root.title("Verifica e Correggi Trascrizione")
    
    label = tk.Label(root, text="Verifica la trascrizione e correggila se necessario:")
    label.pack(pady=5)
    
    text_area = tk.Text(root, height=10, width=60)
    text_area.insert(tk.END, trascrizione_iniziale)
    text_area.pack(padx=10, pady=5)
    
    button_salva = tk.Button(root, text="Salva feedback", command=salva_feedback)
    button_salva.pack(pady=10)
    
    root.mainloop()

def salva_feedback_file(trascrizione_iniziale, trascrizione_corretta, filename="feedback.json"):
    """
    Salva il feedback (coppia trascrizione iniziale e quella corretta) in un file JSON.
    """
    feedback = {
        "trascrizione_iniziale": trascrizione_iniziale,
        "trascrizione_corretta": trascrizione_corretta
    }
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(feedback)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("Feedback salvato.")
