import customtkinter
from tkinter import *
from tkinter import ttk
import pandas as pd
import webbrowser as wb


class InventoryPage(customtkinter.CTkToplevel):
    def __init__(self, selection):
        super().__init__()
        self.geometry("1510x800")
        self.title("Database")
        self.resizable(0, 0)
        self.selection = selection

        # Button to add item
        self.btn_add = customtkinter.CTkButton(self, text="Add", command=self.open_add_item)
        self.btn_add.grid(column=1, row=0, sticky=E, pady=10, padx=40)

        # Button to remove item
        self.btn_remove = customtkinter.CTkButton(self, text="Remove", command=self.open_remove_item)
        self.btn_remove.grid(column=1, row=1, sticky=E, pady=10, padx=40)

        # Label for title
        self.label = customtkinter.CTkLabel(self, text="Inventory", font=("Roboto", 24))
        self.label.grid(column=0, row=1, sticky=W, pady=10, padx=15)

        # Create Treeview frame
        self.tree_frame = Frame(self)
        self.tree_frame.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        # Create Treeview scrollbar
        self.tree_scroll = Scrollbar(self.tree_frame, orient="vertical")
        self.tree_scroll.grid(column=1, row=0, sticky='ns')

        # Create Treeview
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, height=25,
                                    selectmode="extended")
        self.create_tree()

        self.toplevel_window = None

    def get_tree(self):
        """return Treeview object"""
        return self.my_tree

    def open_add_item(self):
        """Open add item window, code cited: GitHub @TomSchimansky/CustomTkinter"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AddItemWindow(self.my_tree, self.tree_scroll)
        else:
            self.toplevel_window.focus()

    def open_remove_item(self):
        """Open remove item window, code cited: GitHub @TomSchimansky/CustomTkinter"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = RemoveItemWindow(self.my_tree, self.tree_scroll)
        else:
            self.toplevel_window.focus()

    def create_tree(self):
        """Create new Treeview"""
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(".", font=('Roboto', 10), foreground="white")
        self.style.configure("Treeview.Heading", background="#3d3d3d", padding=8)
        self.style.configure("Treeview", background="#2e2e2e", foreground="white", rowheight=25,
                             fieldbackground="#2e2e2e", padding=10)

        if self.selection == "basic":
            df = pd.read_csv('microservice/basic_result.csv')
        elif self.selection == "advanced":
            df = pd.read_csv('microservice/advanced_result.csv')
        elif self.selection == "dining":
            df = pd.read_csv('microservice/home_inventory.csv')
            df = df.loc[(df["Location"] == "Dining Room")]
            df.to_csv("database/dining_room.csv", index=False)
        elif self.selection == "living":
            df = pd.read_csv('microservice/home_inventory.csv')
            df = df.loc[(df["Location"] == "Living Room")]
            df.to_csv("database/living_room.csv", index=False)
        elif self.selection == "bedroom":
            df = pd.read_csv('microservice/home_inventory.csv')
            df = df.loc[(df["Location"] == "Bedroom")]
            df.to_csv("database/bedroom.csv", index=False)
        elif self.selection == "all":
            df = pd.read_csv('microservice/home_inventory.csv')
        else:
            df = pd.read_csv('microservice/home_inventory.csv')

        # Set up new treeview
        self.my_tree["column"] = list(df.columns)
        self.my_tree["show"] = "headings"
        # Loop through column list for headings
        for column in self.my_tree["column"]:
            self.my_tree.heading(column, text=column)

        self.my_tree.column("Name", anchor=W, width=300, minwidth=80)
        self.my_tree.column("Brand", anchor=W, width=200, minwidth=80)
        self.my_tree.column("Category", anchor=W, width=100, minwidth=80)
        self.my_tree.column("Color", anchor=W, width=100, minwidth=80)
        self.my_tree.column("Location", anchor=W, width=100, minwidth=80)
        self.my_tree.column("Width", anchor=W, width=50, minwidth=50)
        self.my_tree.column("Depth", anchor=W, width=50, minwidth=50)
        self.my_tree.column("Height", anchor=W, width=50, minwidth=50)
        self.my_tree.column("Price", anchor=W, width=50, minwidth=60)
        self.my_tree.column("Link", anchor=W, width=450, minwidth=80)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.my_tree.insert("", "end", values=row)

        self.my_tree.grid(column=0, row=0)

        # Configure scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Bind double click to tree
        self.my_tree.bind("<Double-1>", click_url)

    def refresh_tree(self):
        """Refresh Treeview after modifying data"""
        for row in self.my_tree.get_children():
            self.my_tree.delete(row)
        self.selection = "All"
        InventoryPage.create_tree(self)


class AddItemWindow(customtkinter.CTkToplevel):
    def __init__(self, my_tree, tree_scroll):
        super().__init__()
        self.geometry("510x650")
        self.title("Add Item")
        self.resizable(0, 0)
        self.my_tree = my_tree
        self.tree_scroll = tree_scroll

        self.label = customtkinter.CTkLabel(self, text="Add Item", font=("Roboto", 20))
        self.label.grid(column=0, row=0, columnspan=2, sticky=NSEW, pady=20)

        # Name label and entry
        self.label_name = customtkinter.CTkLabel(self, text="Name", font=("Roboto", 14))
        self.label_name.grid(column=0, row=1, pady=10, padx=10)
        self.entry_name = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_name.grid(column=1, row=1, pady=10, padx=10)

        # Brand label and entry
        self.label_brand = customtkinter.CTkLabel(self, text="Brand", font=("Roboto", 14))
        self.label_brand.grid(column=0, row=2, pady=10, padx=10)
        self.entry_brand = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_brand.grid(column=1, row=2, pady=10, padx=10)

        # Category label and entry
        self.label_category = customtkinter.CTkLabel(self, text="Category", font=("Roboto", 14))
        self.label_category.grid(column=0, row=3, pady=10, padx=10)
        self.entry_category = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_category.grid(column=1, row=3, pady=10, padx=10)

        # Color label and entry
        self.label_color = customtkinter.CTkLabel(self, text="Color", font=("Roboto", 14))
        self.label_color.grid(column=0, row=4, pady=10, padx=10)
        self.entry_color = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_color.grid(column=1, row=4, pady=10, padx=10)

        # Location label and entry
        self.label_location = customtkinter.CTkLabel(self, text="Location", font=("Roboto", 14))
        self.label_location.grid(column=0, row=5, pady=10, padx=10)
        self.entry_location = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_location.grid(column=1, row=5, pady=10, padx=10)

        # Width label and entry
        self.label_width = customtkinter.CTkLabel(self, text="Width", font=("Roboto", 14))
        self.label_width.grid(column=0, row=6, pady=10, padx=10)
        self.entry_width = customtkinter.CTkEntry(self, width=200, height=30)
        self.entry_width.grid(column=1, row=6, sticky=W, pady=10, padx=10)

        # Depth label and entry
        self.label_depth = customtkinter.CTkLabel(self, text="Depth", font=("Roboto", 14))
        self.label_depth.grid(column=0, row=7, pady=10, padx=10)
        self.entry_depth = customtkinter.CTkEntry(self, width=200, height=30)
        self.entry_depth.grid(column=1, row=7, sticky=W, pady=10, padx=10)

        # Height label and entry
        self.label_height = customtkinter.CTkLabel(self, text="Height", font=("Roboto", 14))
        self.label_height.grid(column=0, row=8, pady=10, padx=10)
        self.entry_height = customtkinter.CTkEntry(self, width=200, height=30)
        self.entry_height.grid(column=1, row=8, sticky=W, pady=10, padx=10)

        # Price label and entry
        self.label_price = customtkinter.CTkLabel(self, text="Price", font=("Roboto", 14))
        self.label_price.grid(column=0, row=9, pady=10, padx=10)
        self.entry_price = customtkinter.CTkEntry(self, width=200, height=30)
        self.entry_price.grid(column=1, row=9, sticky=W, pady=10, padx=10)

        # Link label and entry
        self.label_link = customtkinter.CTkLabel(self, text="Link", font=("Roboto", 14))
        self.label_link.grid(column=0, row=10, pady=10, padx=10)
        self.entry_link = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_link.grid(column=1, row=10, sticky=W, pady=10, padx=10)

        # Button to submit item
        self.button_go = customtkinter.CTkButton(self, text="Go", command=lambda: self.add_to_csv())
        self.button_go.grid(column=0, row=11, columnspan=2, pady=10, padx=10)

        # Placeholder area for error message
        self.error = customtkinter.CTkLabel(self, text="")
        self.error.grid(column=0, row=12, columnspan=2, sticky=NSEW, padx=20)

    def add_to_csv(self):
        """Validate and add an item to the inventory database"""
        item_list = [self.entry_name, self.entry_brand, self.entry_category, self.entry_color, self.entry_location,
                     self.entry_width, self.entry_depth, self.entry_height, self.entry_price, self.entry_link]

        # If an element in the list is empty, print error message and return False
        for item in item_list:
            if len(item.get()) == 0:
                self.error.configure(text="One or more field is empty", text_color="orange")
                return False

        # If width/depth/height/price is not numeric, print error message and return False
        if not self.entry_width.get().isnumeric():
            self.error.configure(text="Width must be numeric", text_color="orange")
            return False
        if not self.entry_depth.get().isnumeric():
            self.error.configure(text="Depth must be numeric", text_color="orange")
            return False
        if not self.entry_height.get().isnumeric():
            self.error.configure(text="Height must be numeric", text_color="orange")
            return False
        if not self.entry_price.get().isnumeric():
            self.error.configure(text="Price must be numeric", text_color="orange")
            return False

        # Else add item
        item = f"{self.entry_name.get()},{self.entry_brand.get()},{self.entry_category.get()}," \
               f"{self.entry_color.get()},{self.entry_location.get()},{self.entry_width.get()}," \
               f"{self.entry_depth.get()},{self.entry_height.get()},{self.entry_price.get()},{self.entry_link.get()}\n"
        # Append new item to home_inventory.csv
        with open("microservice/home_inventory.csv", "a") as file:
            file.write(item)

        InventoryPage.refresh_tree(self)
        self.destroy()


class RemoveItemWindow(customtkinter.CTkToplevel):
    def __init__(self, my_tree, tree_scroll):
        super().__init__()
        self.geometry("480x200")
        self.title("Remove Item")
        self.resizable(0, 0)
        self.my_tree = my_tree
        self.tree_scroll = tree_scroll

        self.label_title = customtkinter.CTkLabel(self, text="Remove Item", font=("Roboto", 20))
        self.label_title.grid(column=0, row=0, columnspan=2, sticky=NSEW, pady=20)

        # Name label and entry
        self.label_name = customtkinter.CTkLabel(self, text="Name", font=("Roboto", 14))
        self.label_name.grid(column=0, row=1, pady=10, padx=10)
        self.entry_name = customtkinter.CTkEntry(self, width=400, height=30)
        self.entry_name.grid(column=1, row=1, sticky=W, pady=10, padx=10)

        # Button to submit item
        self.button_go = customtkinter.CTkButton(self, text="Go", command=self.open_remove_warning)
        self.button_go.grid(column=0, row=2, columnspan=2, pady=10, padx=10)

        # Placeholder area for error message
        self.error = customtkinter.CTkLabel(self, text="")
        self.error.grid(column=0, row=3, columnspan=2, sticky=NSEW, padx=20)

    def open_remove_warning(self):
        """Open remove warning window"""
        self.top = customtkinter.CTkToplevel()
        self.top.geometry("450x180")
        self.top.title("Warning")
        self.top.resizable(0, 0)

        label_warning = customtkinter.CTkLabel(self.top, text="Are you sure you want to delete this item?",
                                               font=("Roboto", 14))
        label_warning.pack(pady=8, padx=10)

        button_yes = customtkinter.CTkButton(self.top, text="Yes", command=lambda: [self.remove_from_csv(), self.top.destroy()])
        button_yes.pack(pady=12, padx=10)

        button_no = customtkinter.CTkButton(self.top, text="No", command=self.top.destroy)
        button_no.pack(pady=12, padx=10)

    def remove_from_csv(self):
        """Validate and remove an item from the inventory database"""
        if len(self.entry_name.get()) == 0:
            self.error.configure(text="Field is empty", text_color="orange")
        # Else remove item
        else:
            df = pd.read_csv("microservice/home_inventory.csv")  # read csv
            row_index = df[(df.Name == self.entry_name.get())].index  # get row index of item to be removed
            df.drop(row_index, axis=0, inplace=True)  # drop item
            df.to_csv("microservice/home_inventory.csv", index=False)  # write csv

            InventoryPage.refresh_tree(self)
            self.top.destroy()
            self.destroy()


def click_url(event):
    """Configure double click for URL"""
    tree = event.widget  # get the treeview widget
    item = tree.item(tree.focus())  # get treeview selection
    link = item['values'][9]  # get value from link column of the selected row
    wb.open_new_tab(link)  # open link in a browser tab
