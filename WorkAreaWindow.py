from Window import *

# def main_menu_creating(_menu):


class WorkAreaWindow(Window):
    """Класс, отвечающий за окно с рабочей областью"""
    def __init__(self, title):
        super().__init__(title)
        self.image_btn = None
        self.curve_btn = None
        self.draw_btn = None
        self.text_btn = None
        self.tune_btn = None
        self.effects_btn = None
        self.crop_btn = None
        self.option_add("*tearOff", FALSE)
        self.main_menu = Menu(master=self)
        self.main_menu_creating()
        self.config(menu=self.main_menu)
        self.tools_buttons_creating()
    def main_menu_creating(self):
        """Создание главного меню"""
        file_menu = Menu(master=self.main_menu)
        file_menu.add_command(label="Create new project...")
        file_menu.add_command(label="Create new canvas...")
        file_menu.add_command(label="Open project...")
        file_menu.add_command(label="Open image...")
        file_menu.add_separator()
        file_menu.add_command(label="Save...")
        file_menu.add_command(label="Save as...")
        file_menu.add_command(label="Save copy...")
        file_menu.add_command(label="Revert")
        file_menu.add_separator()
        file_menu.add_command(label="Export...")
        file_menu.add_command(label="Export as...")
        file_menu.add_separator()
        file_menu.add_command(label="Print...")
        file_menu.add_separator()
        file_menu.add_command(label="Close all")
        file_menu.add_command(label="Exit")

        self.main_menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(master=self.main_menu)
        edit_menu.add_command(label="Undo") # добавить ЧТО undo....
        edit_menu.add_command(label="Redo") # the same
        edit_menu.add_command(label="Undo history")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")

        edit_menu_paste_as = Menu(master=edit_menu)
        edit_menu_paste_as.add_command(label="New layer")
        edit_menu_paste_as.add_command(label="New image")

        edit_menu.add_cascade(label="Paste as", menu=edit_menu_paste_as)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear")

        edit_menu_fill = Menu(master=edit_menu)
        edit_menu_fill.add_command(label="Selection outline...")
        edit_menu_fill.add_command(label="Path...")

        edit_menu.add_cascade(label="Fill", menu=edit_menu_fill)

        edit_menu_stroke = Menu(master=edit_menu)
        edit_menu_stroke.add_command(label="Selection...")
        edit_menu_stroke.add_command(label="Path...")

        edit_menu.add_cascade(label="Stroke", menu=edit_menu_stroke)
        edit_menu.add_separator()
        edit_menu.add_command(label="Settings")

        self.main_menu.add_cascade(label="Edit", menu=edit_menu)

        image_menu = Menu(master=self.main_menu)
        image_menu.add_command(label="Duplicate")
        image_menu.add_separator()

        image_menu_mode = Menu(master=image_menu)
        image_menu_mode.add_radiobutton(label="RGB")
        image_menu_mode.add_radiobutton(label="CMYK")
        image_menu_mode.add_radiobutton(label="Grayscale")
        """здесь добвить возможно что-то еще.... и сделать что сначала выбран какой-то формат!!!!"""
        image_menu.add_cascade(label="Mode", menu=image_menu_mode)
        image_menu.add_separator()
        image_menu.add_command(label="Rotate...")
        image_menu.add_command(label="Resize...")
        image_menu.add_command(label="Scale image...")

        image_menu_crop = Menu(master=image_menu)
        image_menu_crop.add_command(label="To selection")
        image_menu_crop.add_command(label="To content")

        image_menu.add_cascade(label="Crop...", menu=image_menu_crop)
        image_menu.add_separator()
        image_menu.add_command(label="Merge visible layers")
        image_menu.add_separator()
        image_menu.add_command(label="Image info")

        self.main_menu.add_cascade(label="Image", menu=image_menu)

        layer_menu = Menu(master=self.main_menu)
        layer_menu.add_command(label="New layer...")
        layer_menu.add_command(label="New from visible")
        layer_menu.add_command(label="New layer group")
        layer_menu.add_command(label="Merge with the previous layer")
        layer_menu.add_command(label="Merge all visible")
        layer_menu.add_command(label="Duplicate")
        layer_menu.add_command(label="Delete layer")
        layer_menu.add_separator()

        layer_menu_moving_across = Menu(master=layer_menu)
        layer_menu_moving_across.add_command(label="Go to the layer above")
        layer_menu_moving_across.add_command(label="Go to the layer below")

        layer_menu.add_cascade(label="Moving through layers", menu=layer_menu_moving_across)

        layer_menu_layer_moving = Menu(master=layer_menu)
        layer_menu_layer_moving.add_command(label="Raise the layer")
        layer_menu_layer_moving.add_command(label="Lower the layer")
        layer_menu_layer_moving.add_command(label="Make the layer top")
        layer_menu_layer_moving.add_command(label="Make the layer the lowest")
        layer_menu_layer_moving.add_separator()
        layer_menu_layer_moving.add_command(label="Reverse layer order")

        layer_menu.add_cascade(label="Layer moving", menu=layer_menu_layer_moving)

        layer_menu_mask = Menu(master=layer_menu)
        layer_menu_mask.add_command(label="Add layer mask...")
        layer_menu_mask.add_command(label="Apply layer mask")
        layer_menu_mask.add_command(label="Delete layer mask")

        layer_menu.add_cascade(label="Mask", menu=layer_menu_mask)
        layer_menu.add_command(label="Transparency...")
        layer_menu.add_command(label="Rotate...")
        layer_menu.add_command(label="Resize...")
        layer_menu.add_command(label="Scale...")

        self.main_menu.add_cascade(label="Layer", menu=layer_menu)

        select_menu = Menu(master=self.main_menu)
        select_menu.add_command(label="All")
        select_menu.add_command(label="None")
        select_menu.add_command(label="Invert")
        select_menu.add_command(label="By color")
        select_menu.add_separator()
        select_menu.add_command(label="Into the outline")

        self.main_menu.add_cascade(label="Select", menu=select_menu)

        filter_menu = Menu(master=self.main_menu)

        filter_menu_blur = Menu(master=filter_menu)
        filter_menu_blur.add_command(label="Box blur")
        filter_menu_blur.add_command(label="Gaussian blur")
        filter_menu.add_cascade(label="Blur", menu=filter_menu_blur)

        filter_menu.add_command(label="Sharpness...")

        filter_menu_color = Menu(master=filter_menu)
        filter_menu_color.add_command(label="Saturation") #image.color
        filter_menu_color.add_command(label="Contrast")
        filter_menu_color.add_command(label="Brightness")

        filter_menu.add_cascade(label="Color", menu=filter_menu_color)
        filter_menu.add_separator()
        filter_menu.add_command(label="Grayscale") #imageops
        filter_menu.add_command(label="Invert")
        filter_menu.add_command(label="Posterize...")
        filter_menu.add_command(label="Solarize...")
        filter_menu.add_separator()
        filter_menu.add_command(label="Perspective transform...") #imagetransform
        filter_menu.add_command(label="Quad transform...")

        self.main_menu.add_cascade(label="Filter", menu=filter_menu)

        help_menu = Menu(master=self.main_menu)
        help_menu.add_command(label="Manual")
        help_menu.add_command(label="About")

        self.main_menu.add_cascade(label="Help", menu=help_menu)

        print(dt.now().time(), "Created main menu")
    def tools_buttons_creating(self):
        Label(master=self, text="Tools:").pack()
        self.crop_btn = Button(master=self, text="Crop", command=self.crop_button_clicked)
        self.crop_btn.pack()
        self.effects_btn = Button(master=self, text="Effects", command=self.effects_btn_clicked)
        self.effects_btn.pack()
        self.tune_btn = Button(master=self, text="Tune", command=self.tune_btn_clicked)
        self.tune_btn.pack()
        self.text_btn = Button(master=self, text="Text", command=self.text_btn_clicked)
        self.text_btn.pack()
        self.draw_btn = Button(master=self, text="Draw", command=self.draw_btn_clicked)
        self.draw_btn.pack()
        self.curve_btn = Button(master=self, text="Curve", command=self.curve_btn_clicked)
        self.curve_btn.pack()
        self.image_btn = Button(master=self, text="Image", command=self.image_btn_clicked)
    def crop_button_clicked(self):
        self.crop_btn["state"] = "disabled"
        """actions"""
        self.crop_btn["state"] = "normal"
    def effects_btn_clicked(self):
        self.effects_btn["state"] = "disabled"
        """action"""
        self.effects_btn["state"] = "normal"
    def tune_btn_clicked(self):
        self.tune_btn["state"] = "disabled"
        """action"""
        self.tune_btn["state"] = "normal"
    def text_btn_clicked(self):
        self.text_btn["state"] = "disabled"
        """action"""
        self.text_btn["state"] = "normal"
    def draw_btn_clicked(self):
        self.draw_btn["state"] = "disabled"
        """action"""
        self.draw_btn["state"] = "normal"
    def curve_btn_clicked(self):
        self.curve_btn["state"] = "disabled"
        """action"""
        self.curve_btn["state"] = "normal"
    def image_btn_clicked(self):
        self.image_btn["state"] = "disabled"
        """action"""
        self.image_btn["state"] = "normal"