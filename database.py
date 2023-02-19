import customtkinter
from tkinter import *
from tkinter import ttk
from tktooltip import ToolTip
import pandas as pd
import webbrowser as wb


def open_database(selection):
    """Open database window"""
    frame = customtkinter.CTkToplevel()
    frame.geometry("1510x800")
    frame.title("Database")
    frame.resizable(0, 0)

    # Button to add item
    button_add = customtkinter.CTkButton(master=frame, text="Add", command=lambda: open_add_item(my_tree, tree_scroll))
    button_add.grid(column=1, row=0, sticky=E, pady=10, padx=40)

    # Button to remove item
    button_remove = customtkinter.CTkButton(master=frame, text="Remove", command=lambda: open_remove_item(my_tree, tree_scroll))
    button_remove.grid(column=1, row=1, sticky=E, pady=10, padx=40)

    # Label for title
    label = customtkinter.CTkLabel(master=frame, text="Inventory", font=("Roboto", 24))
    label.grid(column=0, row=1, sticky=W, pady=10, padx=15)

    # Create Treeview frame
    tree_frame = Frame(frame)
    tree_frame.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    # Create Treeview scrollbar
    tree_scroll = Scrollbar(tree_frame, orient="vertical")
    tree_scroll.grid(column=1, row=0, sticky='ns')

    # Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=25, selectmode="extended")
    create_tree(selection, my_tree, tree_scroll)


def refresh_tree(tree, tree_scroll):
    """Refresh Treeview after modifying data"""
    for row in tree.get_children():
        tree.delete(row)
    create_tree("All", tree, tree_scroll)


def create_tree(selection, tree, tree_scroll):
    """Create new Treeview"""
    style = ttk.Style()
    style.theme_use("default")
    style.configure(".", font=('Roboto', 10), foreground="white")
    style.configure("Treeview.Heading", background="#3d3d3d", padding=8)
    style.configure("Treeview", background="#2e2e2e", foreground="white", rowheight=25, fieldbackground="#2e2e2e", padding=10)


    if selection == "basic":
        df = pd.read_csv('microservice/basic_result.csv')
    elif selection == "advanced":
        df = pd.read_csv('microservice/advanced_result.csv')
    elif selection == "dining":
        df = pd.read_csv('microservice/home_inventory.csv')
        df = df.loc[(df["Location"] == "Dining Room")]
        df.to_csv("database/dining_room.csv", index=False)
    elif selection == "living":
        df = pd.read_csv('microservice/home_inventory.csv')
        df = df.loc[(df["Location"] == "Living Room")]
        df.to_csv("database/living_room.csv", index=False)
    elif selection == "bedroom":
        df = pd.read_csv('microservice/home_inventory.csv')
        df = df.loc[(df["Location"] == "Bedroom")]
        df.to_csv("database/bedroom.csv", index=False)
    elif selection == "all":
        df = pd.read_csv('microservice/home_inventory.csv')
    else:
        df = pd.read_csv('microservice/home_inventory.csv')

    # Set up new treeview
    tree["column"] = list(df.columns)
    tree["show"] = "headings"
    # Loop through column list for headings
    for column in tree["column"]:
        tree.heading(column, text=column)

    tree.column("Name", anchor=W, width=300, minwidth=80)
    tree.column("Brand", anchor=W, width=200, minwidth=80)
    tree.column("Category", anchor=W, width=100, minwidth=80)
    tree.column("Color", anchor=W, width=100, minwidth=80)
    tree.column("Location", anchor=W, width=100, minwidth=80)
    tree.column("Width", anchor=W, width=50, minwidth=50)
    tree.column("Depth", anchor=W, width=50, minwidth=50)
    tree.column("Height", anchor=W, width=50, minwidth=50)
    tree.column("Price", anchor=W, width=50, minwidth=60)
    tree.column("Link", anchor=W, width=450, minwidth=80)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

    tree.grid(column=0, row=0)

    # Configure scrollbar
    tree_scroll.config(command=tree.yview)

    # Bind double click to tree
    tree.bind("<Double-1>", click_url)


def click_url(event):
    """Configure double click for URL"""
    tree = event.widget             # get the treeview widget
    item = tree.item(tree.focus())  # get treeview selection
    link = item['values'][9]        # get link from the selected row
    wb.open_new_tab(link)           # open link in a browser tab


def open_add_item(tree, tree_scroll):
    """Open the Add item window"""
    top = customtkinter.CTkToplevel()
    top.geometry("510x650")
    top.title("Add Item")
    top.resizable(0, 0)

    # Title label
    label_title = customtkinter.CTkLabel(master=top, text="Add Item", font=("Roboto", 20))
    label_title.grid(column=0, row=0, columnspan=2, sticky=NSEW, pady=20)

    # Name label and entry
    label_name = customtkinter.CTkLabel(master=top, text="Name", font=("Roboto", 14))
    label_name.grid(column=0, row=1, pady=10, padx=10)
    entry_name = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_name.grid(column=1, row=1, pady=10, padx=10)

    # Brand label and entry
    label_brand = customtkinter.CTkLabel(master=top, text="Brand", font=("Roboto", 14))
    label_brand.grid(column=0, row=2, pady=10, padx=10)
    entry_brand = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_brand.grid(column=1, row=2, pady=10, padx=10)

    # Category label and entry
    label_category = customtkinter.CTkLabel(master=top, text="Category", font=("Roboto", 14))
    label_category.grid(column=0, row=3, pady=10, padx=10)
    entry_category = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_category.grid(column=1, row=3, pady=10, padx=10)

    # Color label and entry
    label_color = customtkinter.CTkLabel(master=top, text="Color", font=("Roboto", 14))
    label_color.grid(column=0, row=4, pady=10, padx=10)
    entry_color = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_color.grid(column=1, row=4, pady=10, padx=10)

    # Location label and entry
    label_location = customtkinter.CTkLabel(master=top, text="Location", font=("Roboto", 14))
    label_location.grid(column=0, row=5, pady=10, padx=10)
    entry_location = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_location.grid(column=1, row=5, pady=10, padx=10)

    # Width label and entry
    label_width = customtkinter.CTkLabel(master=top, text="Width", font=("Roboto", 14))
    label_width.grid(column=0, row=6, pady=10, padx=10)
    entry_width = customtkinter.CTkEntry(master=top, width=200, height=30)
    entry_width.grid(column=1, row=6, sticky=W, pady=10, padx=10)

    # Depth label and entry
    label_depth = customtkinter.CTkLabel(master=top, text="Depth", font=("Roboto", 14))
    label_depth.grid(column=0, row=7, pady=10, padx=10)
    entry_depth = customtkinter.CTkEntry(master=top, width=200, height=30)
    entry_depth.grid(column=1, row=7, sticky=W, pady=10, padx=10)

    # Height label and entry
    label_height = customtkinter.CTkLabel(master=top, text="Height", font=("Roboto", 14))
    label_height.grid(column=0, row=8, pady=10, padx=10)
    entry_height = customtkinter.CTkEntry(master=top, width=200, height=30)
    entry_height.grid(column=1, row=8, sticky=W, pady=10, padx=10)

    # Price label and entry
    label_price = customtkinter.CTkLabel(master=top, text="Price", font=("Roboto", 14))
    label_price.grid(column=0, row=9, pady=10, padx=10)
    entry_price = customtkinter.CTkEntry(master=top, width=200, height=30)
    entry_price.grid(column=1, row=9, sticky=W, pady=10, padx=10)

    # Link label and entry
    label_link = customtkinter.CTkLabel(master=top, text="Link", font=("Roboto", 14))
    label_link.grid(column=0, row=10, pady=10, padx=10)
    entry_link = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_link.grid(column=1, row=10, sticky=W, pady=10, padx=10)

    # Button to submit item
    button_go = customtkinter.CTkButton(master=top, text="Go", command=lambda: add_to_csv(entry_name, entry_brand,
                                                                                          entry_category, entry_color,
                                                                                          entry_location, entry_width,
                                                                                          entry_depth, entry_height,
                                                                                          entry_price, entry_link,
                                                                                          error, top, tree, tree_scroll))
    button_go.grid(column=0, row=11, columnspan=2, pady=10, padx=10)

    # Placeholder area for error message
    error = customtkinter.CTkLabel(master=top, text="")
    error.grid(column=0, row=12, columnspan=2, sticky=NSEW, padx=20)


def add_to_csv(name, brand, category, color, location, width, depth, height, price, link, err, top, tree, tree_scroll):
    """Validate and add an item to the inventory database"""
    item_list = [name, brand, category, color, location, width, depth, height, price, link]

    # If an element in the list is empty, print error message and return False
    for item in item_list:
        if len(item.get()) == 0:
            err.configure(text="One or more field is empty", text_color="orange")
            return False

    # If width/depth/height/price is not numeric, print error message and return False
    if not width.get().isnumeric():
        err.configure(text="Width must be numeric", text_color="orange")
        return False
    if not depth.get().isnumeric():
        err.configure(text="Depth must be numeric", text_color="orange")
        return False
    if not height.get().isnumeric():
        err.configure(text="Height must be numeric", text_color="orange")
        return False
    if not price.get().isnumeric():
        err.configure(text="Price must be numeric", text_color="orange")
        return False

    # Else add item
    item = f"{name.get()},{brand.get()},{category.get()},{color.get()},{location.get()},{width.get()},{depth.get()}," \
           f"{height.get()},{price.get()},{link.get()}\n"
    # Append new item to home_inventory.csv
    with open("microservice/home_inventory.csv", "a") as file:
        file.write(item)

    refresh_tree(tree, tree_scroll)
    top.destroy()


def open_remove_item(tree, tree_scroll):
    """Open remove item window"""
    top = customtkinter.CTkToplevel()
    top.geometry("480x200")
    top.title("Remove Item")
    top.resizable(0, 0)

    # Title label
    label_title = customtkinter.CTkLabel(master=top, text="Remove Item", font=("Roboto", 20))
    label_title.grid(column=0, row=0, columnspan=2, sticky=NSEW, pady=20)

    # Name label and entry
    label_name = customtkinter.CTkLabel(master=top, text="Name", font=("Roboto", 14))
    label_name.grid(column=0, row=1, pady=10, padx=10)
    entry_name = customtkinter.CTkEntry(master=top, width=400, height=30)
    entry_name.grid(column=1, row=1, sticky=W, pady=10, padx=10)

    # Button to submit item
    button_go = customtkinter.CTkButton(master=top, text="Go",
                                        command=lambda: open_remove_warning(entry_name, error, top, tree, tree_scroll))
    button_go.grid(column=0, row=2, columnspan=2, pady=10, padx=10)

    # Placeholder area for error message
    error = customtkinter.CTkLabel(master=top, text="")
    error.grid(column=0, row=3, columnspan=2, sticky=NSEW, padx=20)


def open_remove_warning(item, err, tp, tree, tree_scroll):
    """Open warning window for remove confirmation"""
    top = customtkinter.CTkToplevel()
    top.geometry("450x180")
    top.title("Warning")
    top.resizable(0, 0)

    label_warning = customtkinter.CTkLabel(master=top, text="Are you sure you want to delete this item?",
                                           font=("Roboto", 14))
    label_warning.pack(pady=8, padx=10)

    button_yes = customtkinter.CTkButton(master=top, text="Yes",
                                         command=lambda: [remove_from_csv(item, err, tp, tree, tree_scroll), top.destroy()])
    button_yes.pack(pady=12, padx=10)

    button_no = customtkinter.CTkButton(master=top, text="No", command=top.destroy)
    button_no.pack(pady=12, padx=10)


def remove_from_csv(item, err, top, tree, tree_scroll):
    """Validate and remove an item from the inventory database"""
    if len(item.get()) == 0:
        err.configure(text="Field is empty", text_color="orange")
    # Else remove item
    else:
        df = pd.read_csv("microservice/home_inventory.csv")  # read csv
        row_index = df[(df.Name == item.get())].index  # get row index of item to be removed
        df.drop(row_index, axis=0, inplace=True)  # drop item
        df.to_csv("microservice/home_inventory.csv", index=False)  # write csv

        refresh_tree(tree, tree_scroll)
        top.destroy()
