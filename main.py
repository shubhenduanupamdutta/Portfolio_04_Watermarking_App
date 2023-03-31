from tkinter import *
from tkinter import filedialog
from PIL import Image

# ------------------- CONSTANTS ------------------------------------#
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


def get_watermark_size(image_size, watermark_size, scale):
    img_width, img_height = image_size
    wm_width, wm_height = watermark_size
    wm_aspect = wm_width / wm_height

    width = int(img_width * scale)
    height = int(img_height * scale)

    # TODO: There is some problems in logic here I will correct later, to get good aspect ration of watermark
    # if img_width < img_height:
    #     width = int(img_width * scale)
    #     height = int(width/wm_aspect)
    # else:
    #     height = int(img_height * scale)
    #     width = int(height * wm_aspect)
    return width, height


def watermark(*args):
    watermark_size = size_value.get()
    watermark_position = value_placement.get()
    watermark_file = f"watermark.png"
    image_file = image_entry.get()
    filename = image_file.rsplit("/", 1)[1].rsplit(".", 1)[0]
    filename = filename + "_watermarked.png"

    if watermark_size == "Small":
        watermark_scale = 0.1
    elif watermark_size == "Medium":
        watermark_scale = 0.25
    else:
        watermark_scale = 0.5

    if image_file:
        original_image = Image.open(image_file).convert("RGBA")
        watermark_image = Image.open(watermark_file)

        # Setting the opacity of watermark (0-1)
        alpha_scale = 0.5

        watermark_size = get_watermark_size(original_image.size, watermark_image.size, watermark_scale)
        watermark_image = watermark_image.resize(watermark_size)

        # Calculating watermark position,
        if watermark_position == "Center":
            watermark_position = (int((original_image.width - watermark_size[0])/2),
                                  int((original_image.height - watermark_size[1])/2))
        elif watermark_position == "Bottom Right":
            watermark_position = (original_image.width - watermark_size[0], original_image.height - watermark_size[1])
        else:
            watermark_position = (0, 0)

        mask = watermark_image.split()[3]
        original_image.paste(watermark_image, watermark_position, mask=mask)
        original_image.save(f"../{filename}")

        # Informing user that watermarking is done.
        user_choice.config(text=f"Watermarking Done!!\nFile saved as {filename}", font=("Times New Roman", 20, "bold"), background="green")

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

icon_img = PhotoImage(file="file_icon.png")
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

user_choice = Label(text=f"Watermark will be placed at {value_placement.get()}\n And Size will be {size_value.get()}",
                    font=FONT)
user_choice.grid(row=5, column=0, columnspan=3, pady=10)

submit = Button(text="WaterMark", font=("Times New Roman", 14, "bold"), command=watermark, background="lightgreen")
submit.grid(row=6, column=0, columnspan=3, pady=15)

window.mainloop()
