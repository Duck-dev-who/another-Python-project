import tkinter as tk

root = tk.Tk()
root.title("Note Keeper")
root.geometry("400x300")

notes = []

def save_note():
    note = entry.get()
    if note.strip() != "":
        notes.append(note)
        listbox.insert(tk.END, note)
        entry.delete(0, tk.END)
        status_label.config(text="Note saved!")
    else:
        status_label.config(text="Can't save empty note.")

def delete_note():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        del notes[index]
        status_label.config(text="Note deleted.")
    else:
        status_label.config(text="No note selected.")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

save_button = tk.Button(root, text="save note", command=save_note)
save_button.pack()

delete_button = tk.Button(root, text="delete note", command=delete_note)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()


root.mainloop()