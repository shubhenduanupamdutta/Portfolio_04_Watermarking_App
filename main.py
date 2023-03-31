from tkinter import *
from tkinter import filedialog

# ------------------- SOME CONSTANTS ------------------------------------#
WIDTH = 700
HEIGHT = 500
FONT = ("Times New Roman", 16, "normal")


# ------------------------ UI FUNCTIONALITY ---------------------------------#
def update_choice(*args):
    watermark_position = value_placement.get()
    watermark_size = size_value.get()
    user_choice.config(text=f"Watermark will be placed at {watermark_position}\n And Size will be {watermark_size}")


def select_file(*args):
    file_path = filedialog.askopenfilename()
    image_entry.insert(0, file_path)

# ------------------- USER INTERFACE SETUP ------------------------------#
window = Tk()
window.title("WaterMarker")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=25, pady=50)
window.resizable(False, False)

canvas = Canvas(width=(WIDTH - 10), height=200)
# canvas.config(highlightthickness=0)
logo_img = PhotoImage(file="title_compressed.png")
canvas.create_image((WIDTH - 10) / 2, 74, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

image_label = Label(text="Image File", font=FONT)
image_label.grid(row=1, column=0, columnspan=3, pady=5)

image_entry = Entry(font=FONT, width=60)
image_entry.grid(row=2, column=0, columnspan=2, pady=5)

icon_img = PhotoImage(file="file_icon_compressed.png")
file_button = Button(width=25, image=icon_img, command=select_file)
file_button.grid(row=2, column=2, pady=5)

position = Label(text="Watermark position?", font=FONT)
position.grid(row=3, column=0)

value_placement = StringVar(window)
value_placement.set("Bottom Right")
placement_options = ["Bottom Right", "Top Left", "Center"]
placement = OptionMenu(window, value_placement, *placement_options, command=update_choice)
placement.grid(row=3, column=1, columnspan=2, pady=5)

size = Label(text="Watermark Size?", font=FONT)
size.grid(row=4, column=0)

size_value = StringVar(window)
size_value.set("Small")
size_options = ["Small", "Medium", "Large"]
size = OptionMenu(window, size_value, *size_options, command=update_choice)
size.grid(row=4, column=1, columnspan=2, pady=5)

user_choice = Label(text=f"Watermark will be placed at {value_placement.get()}\n And Size will be {size_value.get()}", font=FONT)
user_choice.grid(row=5, column=0, columnspan=3, pady=15)

window.mainloop()
