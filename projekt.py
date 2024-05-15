import qrcode
from PIL import Image, ImageTk
import tkinter as tk

# Värvide sõnastik, mis seob värvinimed RGB väärtustega
color_dict = {
    'punane': (255, 0, 0),
    'roheline': (0, 255, 0),
    'sinine': (0, 0, 255),
    'must': (0, 0, 0),
    'valge': (255, 255, 255),
    'roosa' : (255, 192, 203),
    'kollane' : (255, 255, 0),
    'oranž' : (255, 165, 0),
    'lilla' : (128, 0, 128),
    'pruun' : (165, 42, 42),
    'hall' : (128, 128, 128),
    # Lisa siia veel värve
}

def generate_qr_code(data, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,  # Ei ole piiri QR koodi ümber
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='must', back='valge')
    colored_img = Image.new('RGB', img.size, back_color)
    data = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if data[x, y] == 0:
                colored_img.putpixel((x, y), fill_color)

    return colored_img

def next_question():
    if question_label['text'] == "Sisesta oma andmed siia":
        data_entry.pack_forget()
        next_button.config(command=lambda: next_question())
        question_label.config(text="Vali QR koodi värv")
        for color in color_dict.keys():
            tk.Radiobutton(window, text=color, variable=fill_color_var, value=color).pack()
        fill_color_var.set('must')
    elif question_label['text'] == "Vali QR koodi värv":
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()
        next_button.config(command=lambda: next_question())
        question_label.config(text="Vali taustavärv")
        for color in color_dict.keys():
            tk.Radiobutton(window, text=color, variable=back_color_var, value=color).pack()
        back_color_var.set('valge')
    else:
        next_button.pack_forget()
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()
        display_qr_code()

def display_qr_code():
    question_label.config(text=" ")
    data = data_entry.get()
    fill_color = color_dict[fill_color_var.get()]
    back_color = color_dict[back_color_var.get()]
    img = generate_qr_code(data, fill_color, back_color)
    
    max_size = (500, 500) # Pildi maksimaalsed mõõtmed
    img.thumbnail(max_size) 

    tk_img = ImageTk.PhotoImage(img) 
    label.config(image=tk_img)
    label.image = tk_img
    caption_label = tk.Label(window, text="Siin on sinu QR kood")
    caption_label.pack()
    input_label = tk.Entry(window)
    save_button = tk.Button(window, text="Salvesta", command=lambda: save())
    def save():
        if input_label.get() == "":
            img.save("qrcode.png")
        else:
            img.save(input_label.get()+".png")
        print("QR kood on salvestatud")
        window.quit()

    save_button.pack()
    input_label.pack()

window = tk.Tk()
window.title("QR Koodi Genereerija")
window.geometry("600x600")

question_label = tk.Label(window, text="Sisesta oma andmed siia")
question_label.pack()

data_entry = tk.Entry(window)
data_entry.pack()

next_button = tk.Button(window, text="Next", command=next_question)
next_button.pack()

fill_color_var = tk.StringVar()
back_color_var = tk.StringVar()

label = tk.Label(window)
label.pack()

window.mainloop()