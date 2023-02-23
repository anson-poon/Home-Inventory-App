from database import *
import time
import customtkinter
from tkinter import *
from tktooltip import ToolTip


class MainPage(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.title("Home Inventory System")
        self.geometry("920x470")
        self.resizable(0, 0)

        self.main_widget()
        self.about_widget()
        self.category_widget()
        self.view_all_widget()

        self.toplevel_window = None

    def main_widget(self):
        """Display basic and advanced search field"""
        self.frame = customtkinter.CTkFrame(self.master, corner_radius=20)
        self.frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.frame.grid(column=0, row=0, columnspan=3, sticky=NSEW, pady=20, padx=40)

        self.label = customtkinter.CTkLabel(self.frame, text="Home Inventory System", font=("Roboto", 24))
        self.label.grid(column=0, row=0, columnspan=5, sticky=N, pady=20, padx=30)

        # Search entry field
        self.entry = customtkinter.CTkEntry(self.frame, width=480, height=30, placeholder_text="Search an item")
        self.entry.grid(column=0, row=1, columnspan=2, pady=10, padx=10)

        # Button - Search
        self.btn_search = customtkinter.CTkButton(self.frame, text="Search", command=self.basic_search)
        self.btn_search.grid(column=3, row=1, pady=10, padx=10)

        # Button - Advanced Search
        self.btn_advanced_search = customtkinter.CTkButton(self.frame, text="Advanced Search",
                                                           command=self.open_advanced_search)
        self.btn_advanced_search.grid(column=4, row=1, pady=10, padx=10)

        # Tooltip message for Advanced Search
        tip = ToolTip(self.btn_advanced_search, msg="Search item by dimensions", delay=0, follow=True,
                      parent_kwargs={"bg": "#1c1c1c", "padx": 5, "pady": 5},
                      fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)

        self.error = customtkinter.CTkLabel(master=self.frame, text="")  # Placeholder for error message
        self.error.grid(column=0, row=2, sticky=W, padx=20)

    def basic_search(self):
        """Initiate communication with basic_search microservice"""
        # if search field is not empty, write search_item into basic_search.txt
        if len(self.entry.get()) != 0:
            f = open('microservice/basic_search.txt', 'w')
            f.write(self.entry.get())
            f.close()
            time.sleep(0.5)

            open_database("basic")
        else:
            self.error.configure(text="This field is required", text_color="orange")

    def open_advanced_search(self):
        """Open advanced search window"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AdvancedSearchWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def about_widget(self):
        """"""
        frame = customtkinter.CTkFrame(self.master, corner_radius=20)
        frame.grid(column=0, row=1, sticky=NSEW, pady=20, padx=40)

        label = customtkinter.CTkLabel(frame, text="What is a home inventory?", font=("Roboto", 15))
        label.grid(column=0, row=0, sticky=NSEW, pady=20, padx=30)

        self.text = customtkinter.CTkLabel(frame, text="A home inventory keeps track\n"
                                                       "of all of the physical belongings\n"
                                                       "in your house.The system\n"
                                                       "makes it easy for you to\n"
                                                       "record, organize, and search\n"
                                                       "item all within a few clicks.\n\n"
                                                       "NEW FEATURE: Advanced Search",
                                           font=("Roboto", 12))
        self.text.grid(column=0, row=1, sticky=NSEW, pady=0, padx=30)

    def category_widget(self):
        """"""
        frame = customtkinter.CTkFrame(self.master, corner_radius=20)
        frame.grid(column=1, row=1, sticky=NSEW, pady=20, padx=40)

        label = customtkinter.CTkLabel(frame, text="Locations", font=("Roboto", 15))
        label.pack(pady=20, padx=40)

        button1 = customtkinter.CTkButton(frame, text="Dining Room", command=lambda: open_database("dining"))
        button1.pack(pady=10, padx=40)

        button2 = customtkinter.CTkButton(frame, text="Living Room", command=lambda: open_database("living"))
        button2.pack(pady=10, padx=40)

        button3 = customtkinter.CTkButton(frame, text="Bedroom", command=lambda: open_database("bedroom"))
        button3.pack(pady=10, padx=40)

    def view_all_widget(self):
        """Subframe 3 - View All"""
        frame = customtkinter.CTkFrame(self.master, corner_radius=20)
        frame.grid(column=2, row=1, sticky=NSEW, pady=20, padx=40)

        label_subframe3 = customtkinter.CTkLabel(frame, text="View all \ninventory",
                                                 font=("Roboto", 18))
        label_subframe3.pack(pady=40, padx=40)
        button_view_all = customtkinter.CTkButton(frame, text="Go", command=lambda: open_database("all"))
        button_view_all.pack(pady=10, padx=40)


class AdvancedSearchWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("270x350")
        self.title("Advanced Search")
        self.resizable(0, 0)

        self.label = customtkinter.CTkLabel(self, text="Dimensions", font=("Roboto", 20))
        self.label.pack(pady=20, padx=10)
        self.width = customtkinter.CTkEntry(self, width=70, height=30, placeholder_text="Width")
        self.width.pack(pady=12, padx=10)
        self.depth = customtkinter.CTkEntry(self, width=70, height=30, placeholder_text="Depth")
        self.depth.pack(pady=12, padx=10)
        self.height = customtkinter.CTkEntry(self, width=70, height=30, placeholder_text="Height")
        self.height.pack(pady=12, padx=10)
        self.btn_go = customtkinter.CTkButton(self, text="Go", command=lambda: self.advanced_search())
        self.btn_go.pack(pady=12, padx=10)

        self.error = customtkinter.CTkLabel(self, text="")  # Placeholder for error message
        self.error.pack(pady=20)

    def advanced_search(self):
        """Initiate communication with advanced_search microservice"""
        try:  # Validate dimension (length, width, height) to be non-empty positive float values
            w_num = float(self.width.get())
            d_num = float(self.depth.get())
            h_num = float(self.height.get())

            if w_num > 0 and d_num > 0 and h_num > 0:
                with open('microservice/advanced_search.txt', 'w') as f:
                    f.write(str(w_num) + "\n" + str(d_num) + "\n" + str(h_num) + "\n")
                time.sleep(0.5)
                open_database("advanced")
        except ValueError:
            self.error.configure(text="Please enter valid numbers for all sides", text_color="orange")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")
    root = MainPage()
    root.mainloop()
