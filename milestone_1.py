import customtkinter
from tkinter import *
from tkinter import ttk
from tktooltip import ToolTip

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")


def main():
    root = customtkinter.CTk()
    window = Home(root, "Home Inventory System", "920x470")

    return None


def open_database():
    top = customtkinter.CTkToplevel()
    top.geometry("920x470")
    top.title("Database")

    # Button to add item
    button_add = customtkinter.CTkButton(master=top, text="Add", command=open_add_item)
    button_add.pack(side=TOP, anchor="e", pady=12, padx=10)

    # Button to remove item
    button_remove = customtkinter.CTkButton(master=top, text="Remove", command=open_remove_item)
    button_remove.pack(side=TOP, anchor="e", pady=12, padx=10)

    # Create tree
    my_tree = ttk.Treeview(top)
    my_tree["column"] = ("Name", "Brand", "Category", "Color", "Location", "Dimensions", "Price", "Link")

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("Name", text="Name", anchor=W)
    my_tree.heading("Brand", text="Brand", anchor=W)
    my_tree.heading("Category", text="Category", anchor=W)
    my_tree.heading("Color", text="Color", anchor=W)
    my_tree.heading("Location", text="Location", anchor=W)
    my_tree.heading("Dimensions", text="Dimensions", anchor=W)
    my_tree.heading("Price", text="Price", anchor=W)
    my_tree.heading("Link", text="Link", anchor=W)

    my_tree.column("#0", width=40, minwidth=40)
    my_tree.column("Name", anchor=W, width=180, minwidth=80)
    my_tree.column("Brand", anchor=W, width=140, minwidth=80)
    my_tree.column("Category", anchor=W, width=100, minwidth=80)
    my_tree.column("Color", anchor=W, width=100, minwidth=80)
    my_tree.column("Location", anchor=W, width=100, minwidth=80)
    my_tree.column("Dimensions", anchor=W, width=120, minwidth=80)
    my_tree.column("Price", anchor=W, width=60, minwidth=60)
    my_tree.column("Link", anchor=W, width=180, minwidth=80)

    # Insert items
    my_tree.insert(parent='', index='end', iid=0, text="", values=("Hamilton Leather",
                                                                   "West Elm",
                                                                   "Sofa",
                                                                   "Brown",
                                                                   "Living Room",
                                                                   "70 x 35.8 x 31.5",
                                                                   "2499",
                                                                   "https://www.westelm.com/products/hamilton-sofa-h848/"))
    my_tree.insert(parent='', index='end', iid=1, text="", values=("LOMMARP",
                                                                   "Ikea",
                                                                   "Bookcase",
                                                                   "Black",
                                                                   "Living Room",
                                                                   "25 x 13 x 78",
                                                                   "179"))
    my_tree.insert(parent='', index='end', iid=2, text="", values=("Morgan Barrelback Slope Arm",
                                                                   "Restoration Hardware",
                                                                   "Dining Chair",
                                                                   "White",
                                                                   "Dining Room",
                                                                   "22.5 x 23 x 31.5",
                                                                   "970"))
    my_tree.insert(parent='', index='end', iid=3, text="", values=("T-Brace Rectangular Extension",
                                                                   "Restoration Hardware",
                                                                   "Dining Table",
                                                                   "Grey Oak",
                                                                   "Dining Room",
                                                                   "108 x 38 x 30",
                                                                   "6675"))
    my_tree.insert(parent='', index='end', iid=4, text="", values=("Blackstone Upholstered Square Stitched",
                                                                   "Zinus",
                                                                   "Bed Frame",
                                                                   "Black",
                                                                   "Bedroom",
                                                                   "76.2 x 80.5 x 38.4",
                                                                   "319"))
    my_tree.insert(parent='', index='end', iid=5, text="", values=("Norah",
                                                                   "Springhill Designs",
                                                                   "Drawer",
                                                                   "White",
                                                                   "Bedroom",
                                                                   "49 x 19 x 54",
                                                                   "1599"))
    my_tree.insert(parent='', index='end', iid=6, text="", values=("Urban Park",
                                                                   "Northridge Home",
                                                                   "Nightstand",
                                                                   "Brown",
                                                                   "Bedroom",
                                                                   "18 x 28 x 29",
                                                                   "499"))

    my_tree.pack(pady=20)


def open_add_item():
    top = customtkinter.CTkToplevel()
    top.geometry("570x320")
    top.title("Add Item")

    label_name = customtkinter.CTkLabel(master=top, text="Name", font=("Roboto", 14))
    label_name.pack(pady=8, padx=10)

    entry_name = customtkinter.CTkEntry(master=top, width=500, height=30)
    entry_name.pack(pady=8, padx=10)

    label_brand = customtkinter.CTkLabel(master=top, text="Brand", font=("Roboto", 14))
    label_brand.pack(pady=8, padx=10)

    entry_brand = customtkinter.CTkEntry(master=top, width=500, height=30)
    entry_brand.pack(pady=8, padx=10)

    label_dimensions = customtkinter.CTkLabel(master=top, text="Dimensions", font=("Roboto", 14))
    label_dimensions.pack(pady=8, padx=10)

    entry_brand = customtkinter.CTkEntry(master=top, width=500, height=30)
    entry_brand.pack(pady=8, padx=10)

    button_go = customtkinter.CTkButton(master=top, text="Go", command=open_database)
    button_go.pack(pady=12, padx=10)


def open_remove_item():
    top = customtkinter.CTkToplevel()
    top.geometry("520x180")
    top.title("Remove Item")

    label_name = customtkinter.CTkLabel(master=top, text="Name", font=("Roboto", 14))
    label_name.pack(pady=8, padx=10)

    entry_name = customtkinter.CTkEntry(master=top, width=500, height=30)
    entry_name.pack(pady=8, padx=10)

    button_go = customtkinter.CTkButton(master=top, text="Go", command=open_warning)
    button_go.pack(pady=12, padx=10)


def open_warning():
    top = customtkinter.CTkToplevel()
    top.geometry("450x180")
    top.title("Warning")

    label_warning = customtkinter.CTkLabel(master=top, text="Are you sure you want to delete this item?",
                                           font=("Roboto", 14))
    label_warning.pack(pady=8, padx=10)

    button_yes = customtkinter.CTkButton(master=top, text="Yes", command=top.destroy)
    button_yes.pack(pady=12, padx=10)

    button_no = customtkinter.CTkButton(master=top, text="No", command=top.destroy)
    button_no.pack(pady=12, padx=10)


def open_advanced_search():
    top = customtkinter.CTkToplevel()
    top.geometry("270x350")
    top.title("Advanced Search")

    # Search entry fields for the dimensions
    label2 = customtkinter.CTkLabel(master=top, text="Dimensions", font=("Roboto", 20))
    label2.pack(pady=20, padx=10)
    length = customtkinter.CTkEntry(master=top, width=70, height=30, placeholder_text="Length")
    length.pack(pady=12, padx=10)
    width = customtkinter.CTkEntry(master=top, width=70, height=30, placeholder_text="Width")
    width.pack(pady=12, padx=10)
    height = customtkinter.CTkEntry(master=top, width=70, height=30, placeholder_text="Height")
    height.pack(pady=12, padx=10)

    # Button that go to the database, with input validation for the search entries
    button_go = customtkinter.CTkButton(master=top, text="Go",
                                        command=lambda: dim_search_validation(length, width, height, error))
    button_go.pack(pady=12, padx=10)

    # Placeholder area for error message
    error = customtkinter.CTkLabel(master=top, text="")
    error.pack(pady=20)


def text_search_validation(t, err):
    """Validate text entry to be non-empty string value"""
    if len(t.get()) != 0:
        open_database()
    else:
        err.configure(text="This field is required", text_color="orange")


def dim_search_validation(l, w, h, err):
    """Validate dimension (length, width, height) to be non-empty positive float values"""
    try:
        l_int = float(l.get())
        w_int = float(w.get())
        h_int = float(h.get())

        if l_int > 0 and w_int > 0 and h_int > 0:
            open_database()

    except ValueError:
        err.configure(text="Please enter valid numbers\n"
                           "for all sides", text_color="orange")


class Home:
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        # self.root.resizable(0, 0)

        self.root.columnconfigure((0, 1, 2), weight=1)
        self.root.rowconfigure(0, weight=3)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Main Bubble
        self.frame = customtkinter.CTkFrame(master=self.root, corner_radius=20)
        self.frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.frame.grid(column=0, row=0, columnspan=3, sticky=NSEW, pady=20, padx=40)

        # Title
        self.label = customtkinter.CTkLabel(master=self.frame, text=title, font=("Roboto", 24))
        self.label.grid(column=0, row=0, columnspan=5, sticky=N, pady=20, padx=30)

        # Search entry field
        self.entry = customtkinter.CTkEntry(master=self.frame, width=480, height=30, placeholder_text="Search an item")
        self.entry.grid(column=0, row=1, columnspan=2, pady=10, padx=10)

        # Button - Search
        self.button_search = customtkinter.CTkButton(master=self.frame, text="Search",
                                                     command=lambda: text_search_validation(self.entry, self.error))
        self.button_search.grid(column=3, row=1, pady=10, padx=10)

        # Button - Advanced Search
        self.button_advanced_search = customtkinter.CTkButton(master=self.frame, text="Advanced Search",
                                                              command=open_advanced_search)
        self.button_advanced_search.grid(column=4, row=1, pady=10, padx=10)

        # Tooltip message for Advanced Search
        self.tip = ToolTip(self.button_advanced_search, msg="Search item by dimensions", delay=0, follow=True,
                           parent_kwargs={"bg": "#1c1c1c", "padx": 5, "pady": 5},
                           fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)

        self.error = customtkinter.CTkLabel(master=self.frame, text="")  # Error message for invalid search
        self.error.grid(column=0, row=2, sticky=W, padx=20)

        # Subframe 1 - About
        self.subframe1 = customtkinter.CTkFrame(master=self.root, corner_radius=20)
        self.subframe1.grid(column=0, row=1, sticky=NSEW, pady=20, padx=40)

        self.label_subframe1 = customtkinter.CTkLabel(master=self.subframe1, text="What is a home inventory?",
                                                      font=("Roboto", 15))
        self.label_subframe1.pack(pady=20, padx=30)

        self.text_subframe1 = customtkinter.CTkLabel(master=self.subframe1,
                                                     text="A home inventory keeps track\n"
                                                          "of all of the physical belongings\n"
                                                          "in your house.The system\n"
                                                          "makes it easy for you to\n"
                                                          "record, organize, and search\n"
                                                          "item all within a few clicks.\n\n"
                                                          "NEW FEATURE: Advanced Search",
                                                     font=("Roboto", 12))
        self.text_subframe1.pack(pady=0, padx=30)

        # Subframe 2 - Categories
        self.subframe2 = customtkinter.CTkFrame(master=self.root, corner_radius=20)
        self.subframe2.grid(column=1, row=1, sticky=NSEW, pady=20, padx=40)

        self.label_subframe2 = customtkinter.CTkLabel(master=self.subframe2, text="Categories", font=("Roboto", 15))
        self.label_subframe2.pack(pady=20, padx=40)

        self.button1 = customtkinter.CTkButton(master=self.subframe2, text="Dining Room", command=open_database)
        self.button1.pack(pady=10, padx=40)

        self.button2 = customtkinter.CTkButton(master=self.subframe2, text="Living Room", command=open_database)
        self.button2.pack(pady=10, padx=40)

        self.button3 = customtkinter.CTkButton(master=self.subframe2, text="Bedroom", command=open_database)
        self.button3.pack(pady=10, padx=40)

        # Subframe 3 - View All
        self.subframe3 = customtkinter.CTkFrame(master=self.root, corner_radius=20)
        self.subframe3.grid(column=2, row=1, sticky=NSEW, pady=20, padx=40)

        self.label_subframe3 = customtkinter.CTkLabel(master=self.subframe3, text="View all \ninventory",
                                                      font=("Roboto", 18))
        self.label_subframe3.pack(pady=40, padx=40)
        self.button_view_all = customtkinter.CTkButton(master=self.subframe3, text="Go", command=open_database)
        self.button_view_all.pack(pady=10, padx=40)

        self.root.mainloop()


if __name__ == "__main__":
    main()
