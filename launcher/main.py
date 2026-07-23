import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import shutil
import subprocess


# -----------------------------
# Appearance
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# -----------------------------
# Paths
# -----------------------------

PROJECT_FOLDER = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

APPS_FOLDER = os.path.join(
    PROJECT_FOLDER,
    "apps"
)

os.makedirs(
    APPS_FOLDER,
    exist_ok=True
)


# -----------------------------
# Window
# -----------------------------

app = ctk.CTk()

app.title(
    "LiteDroid One v0.4"
)

app.geometry(
    "900x600"
)


# -----------------------------
# Functions
# -----------------------------

def get_apps():

    apps = []

    for file in os.listdir(APPS_FOLDER):

        if file.lower().endswith(
            (
                ".exe",
                ".lnk",
                ".apk",
                ".msix"
            )
        ):
            apps.append(file)

    return apps



def launch_file(path):

    try:

        extension = os.path.splitext(path)[1].lower()


        if extension == ".exe":

            subprocess.Popen(
                path
            )


        elif extension == ".lnk":

            os.startfile(
                path
            )


        elif extension == ".apk":

            messagebox.showinfo(
                "APK",
                "Android runtime is not connected yet."
            )


        elif extension == ".msix":

            os.startfile(
                path
            )


    except Exception as e:

        messagebox.showerror(
            "Launch Error",
            str(e)
        )



def refresh_apps():

    for widget in app_frame.winfo_children():

        widget.destroy()


    apps = get_apps()


    if not apps:

        empty = ctk.CTkLabel(
            app_frame,
            text="No apps installed"
        )

        empty.pack(
            pady=20
        )

        return



    for item in apps:


        row = ctk.CTkFrame(
            app_frame
        )

        row.pack(
            fill="x",
            padx=20,
            pady=8
        )


        name = ctk.CTkLabel(
            row,
            text="📱 " + item,
            font=(
                "Arial",
                16
            )
        )

        name.pack(
            side="left",
            padx=20
        )


        location = os.path.join(
            APPS_FOLDER,
            item
        )


        launch = ctk.CTkButton(
            row,
            text="▶ Launch",
            width=120,
            command=lambda p=location:
            launch_file(p)
        )

        launch.pack(
            side="right",
            padx=20
        )



def install_app():

    file = filedialog.askopenfilename(
        title="Select Application",
        filetypes=[
            (
                "Applications",
                "*.exe *.lnk *.apk *.msix"
            ),
            (
                "All Files",
                "*.*"
            )
        ]
    )


    if not file:

        return


    try:

        destination = os.path.join(
            APPS_FOLDER,
            os.path.basename(file)
        )


        shutil.copy2(
            file,
            destination
        )


        messagebox.showinfo(
            "LiteDroid One",
            "App added successfully!"
        )


        refresh_apps()


    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )



# -----------------------------
# UI
# -----------------------------


title = ctk.CTkLabel(
    app,
    text="🚀 LiteDroid One",
    font=(
        "Arial",
        32,
        "bold"
    )
)

title.pack(
    pady=20
)



install_btn = ctk.CTkButton(
    app,
    text="📦 Install App",
    width=250,
    height=45,
    command=install_app
)

install_btn.pack(
    pady=10
)



refresh_btn = ctk.CTkButton(
    app,
    text="🔄 Refresh Apps",
    width=250,
    height=45,
    command=refresh_apps
)

refresh_btn.pack(
    pady=10
)



app_frame = ctk.CTkScrollableFrame(
    app,
    width=700,
    height=300
)

app_frame.pack(
    pady=20
)



refresh_apps()


app.mainloop()