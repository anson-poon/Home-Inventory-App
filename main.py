from database import *
import time
import customtkinter
from tkinter import *
from tkinter import ttk
from tktooltip import ToolTip
import pandas as pd

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")


def main():
    root = customtkinter.CTk()
    root.title("Home Inventory System")
    root.geometry("920x470")
    root.resizable(0, 0)

    root.columnconfigure((0, 1, 2), weight=1)
    root.rowconfigure(0, weight=3)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    # Main Bubble
    frame = customtkinter.CTkFrame(master=root, corner_radius=20)
    frame.columnconfigure((0, 1, 2, 3), weight=1)
    frame.grid(column=0, row=0, columnspan=3, sticky=NSEW, pady=20, padx=40)

    # Title
    label = customtkinter.CTkLabel(master=frame, text="Home Inventory System", font=("Roboto", 24))
    label.grid(column=0, row=0, columnspan=5, sticky=N, pady=20, padx=30)

    # Search entry field
    entry = customtkinter.CTkEntry(master=frame, width=480, height=30, placeholder_text="Search an item")
    entry.grid(column=0, row=1, columnspan=2, pady=10, padx=10)

    # Button - Search
    button_search = customtkinter.CTkButton(master=frame, text="Search",
                                            command=lambda: basic_search(entry, error))
    button_search.grid(column=3, row=1, pady=10, padx=10)

    # Button - Advanced Search
    button_advanced_search = customtkinter.CTkButton(master=frame, text="Advanced Search",
                                                     command=open_advanced_search)
    button_advanced_search.grid(column=4, row=1, pady=10, padx=10)

    # Tooltip message for Advanced Search
    tip = ToolTip(button_advanced_search, msg="Search item by dimensions", delay=0, follow=True,
                  parent_kwargs={"bg": "#1c1c1c", "padx": 5, "pady": 5},
                  fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)

    # Error message for invalid search
    error = customtkinter.CTkLabel(master=frame, text="")
    error.grid(column=0, row=2, sticky=W, padx=20)

    # Subframe 1 - About
    subframe1 = customtkinter.CTkFrame(master=root, corner_radius=20)
    subframe1.grid(column=0, row=1, sticky=NSEW, pady=20, padx=40)

    label_subframe1 = customtkinter.CTkLabel(master=subframe1, text="What is a home inventory?",
                                             font=("Roboto", 15))
    label_subframe1.pack(pady=20, padx=30)

    text_subframe1 = customtkinter.CTkLabel(master=subframe1,
                                            text="A home inventory keeps track\n"
                                                 "of all of the physical belongings\n"
                                                 "in your house.The system\n"
                                                 "makes it easy for you to\n"
                                                 "record, organize, and search\n"
                                                 "item all within a few clicks.\n\n"
                                                 "NEW FEATURE: Advanced Search",
                                            font=("Roboto", 12))
    text_subframe1.pack(pady=0, padx=30)

    # Subframe 2 - Categories
    subframe2 = customtkinter.CTkFrame(master=root, corner_radius=20)
    subframe2.grid(column=1, row=1, sticky=NSEW, pady=20, padx=40)

    label_subframe2 = customtkinter.CTkLabel(master=subframe2, text="Locations", font=("Roboto", 15))
    label_subframe2.pack(pady=20, padx=40)

    button1 = customtkinter.CTkButton(master=subframe2, text="Dining Room", command=lambda: open_database("dining"))
    button1.pack(pady=10, padx=40)

    button2 = customtkinter.CTkButton(master=subframe2, text="Living Room", command=lambda: open_database("living"))
    button2.pack(pady=10, padx=40)

    button3 = customtkinter.CTkButton(master=subframe2, text="Bedroom", command=lambda: open_database("bedroom"))
    button3.pack(pady=10, padx=40)

    # Subframe 3 - View All
    subframe3 = customtkinter.CTkFrame(master=root, corner_radius=20)
    subframe3.grid(column=2, row=1, sticky=NSEW, pady=20, padx=40)

    label_subframe3 = customtkinter.CTkLabel(master=subframe3, text="View all \ninventory",
                                             font=("Roboto", 18))
    label_subframe3.pack(pady=40, padx=40)
    button_view_all = customtkinter.CTkButton(master=subframe3, text="Go", command=lambda: open_database("all"))
    button_view_all.pack(pady=10, padx=40)

    root.mainloop()


def basic_search(t, err):
    """Initiate communication with basic_search microservice"""
    search_item = t.get()

    # if search field is not empty, write search_item into basic_search.txt
    if len(search_item) != 0:
        f = open('microservice/basic_search.txt', 'w')
        f.write(search_item)
        f.close()
        time.sleep(0.5)

        open_database("basic")
    else:
        err.configure(text="This field is required", text_color="orange")


def open_advanced_search():
    """Open advanced search window"""
    top = customtkinter.CTkToplevel()
    top.geometry("270x350")
    top.title("Advanced Search")
    top.resizable(0, 0)

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
                                        command=lambda: advanced_search(length, width, height, error))
    button_go.pack(pady=12, padx=10)

    # Placeholder area for error message
    error = customtkinter.CTkLabel(master=top, text="")
    error.pack(pady=20)


def advanced_search(l, w, h, err):
    """Initiate communication with advanced_search microservice"""

    # Validate dimension (length, width, height) to be non-empty positive float values
    try:
        l_num = float(l.get())
        w_num = float(w.get())
        h_num = float(h.get())

        if l_num > 0 and w_num > 0 and h_num > 0:
            f = open('microservice/advanced_search.txt', 'w')
            f.write(str(l_num) + "\n" + str(l_num) + "\n" + str(l_num) + "\n")
            f.close()
            time.sleep(0.5)

            open_database("advanced")

    except ValueError:
        err.configure(text="Please enter valid numbers for all sides", text_color="orange")


if __name__ == "__main__":
    main()
