import customtkinter as ctk
import sys
import os
from tkinter import filedialog


# Allow importing project modules
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


from runtime.runtime_manager import RuntimeManager
from modules.apk_manager import APKManager


# App settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Main window
app = ctk.CTk()

app.title("LiteDroid One")
app.geometry("900x600")


# -----------------------------
# Functions
# -----------------------------

def get_apps_manager():

    apps_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "apps"
    )

    return APKManager(apps_path)



def start_runtime():

    runtime = RuntimeManager()

    status = runtime.get_status()

    status_label.configure(
        text="Runtime Status: " + status
    )



def scan_apps():

    manager = get_apps_manager()

    apps = manager.scan_apks()


    if apps:

        apps_text = "\n".join(apps)

    else:

        apps_text = "No apps found"


    apps_label.configure(
        text=apps_text
    )



def import_apk():

    apk_file = filedialog.askopenfilename(
        filetypes=[
            ("Android APK", "*.apk")
        ]
    )


    if apk_file:

        manager = get_apps_manager()

        success = manager.import_apk(
            apk_file
        )


        if success:

            scan_apps()



# -----------------------------
# UI
# -----------------------------

title = ctk.CTkLabel(
    app,
    text="🚀 LiteDroid One",
    font=("Arial", 32, "bold")
)

title.pack(pady=30)



subtitle = ctk.CTkLabel(
    app,
    text="Lightweight Android App Runner",
    font=("Arial", 18)
)

subtitle.pack()



status_label = ctk.CTkLabel(
    app,
    text="Runtime Status: Unknown",
    font=("Arial", 16)
)

status_label.pack(pady=20)



apps_title = ctk.CTkLabel(
    app,
    text="Installed Apps:",
    font=("Arial", 18, "bold")
)

apps_title.pack(pady=10)



apps_label = ctk.CTkLabel(
    app,
    text="No apps scanned",
    font=("Arial", 16)
)

apps_label.pack()



runtime_button = ctk.CTkButton(
    app,
    text="Start Android Runtime",
    width=250,
    height=45,
    command=start_runtime
)

runtime_button.pack(pady=20)



scan_button = ctk.CTkButton(
    app,
    text="Scan Apps",
    width=250,
    height=45,
    command=scan_apps
)

scan_button.pack(pady=10)



import_button = ctk.CTkButton(
    app,
    text="Import APK",
    width=250,
    height=45,
    command=import_apk
)

import_button.pack(pady=10)



# Start application

app.mainloop()