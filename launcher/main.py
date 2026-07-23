import customtkinter as ctk
import sys
import os


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

def start_runtime():

    runtime = RuntimeManager()

    status = runtime.get_status()

    status_label.configure(
        text="Runtime Status: " + status
    )


def scan_apps():

    apps_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "apps"
    )


    manager = APKManager(
        apps_path
    )


    apps = manager.scan_apks()


    if apps:

        apps_text = "\n".join(apps)

    else:

        apps_text = "No apps found"


    apps_label.configure(
        text=apps_text
    )


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


# Runtime status

status_label = ctk.CTkLabel(
    app,
    text="Runtime Status: Unknown",
    font=("Arial", 16)
)

status_label.pack(pady=20)


# Installed apps title

apps_title = ctk.CTkLabel(
    app,
    text="Installed Apps:",
    font=("Arial", 18, "bold")
)

apps_title.pack(pady=10)


# Apps list

apps_label = ctk.CTkLabel(
    app,
    text="No apps scanned",
    font=("Arial", 16)
)

apps_label.pack()


# Runtime button

runtime_button = ctk.CTkButton(
    app,
    text="Start Android Runtime",
    width=250,
    height=45,
    command=start_runtime
)

runtime_button.pack(pady=25)


# Scan apps button

scan_button = ctk.CTkButton(
    app,
    text="Scan Apps",
    width=250,
    height=45,
    command=scan_apps
)

scan_button.pack()


# Start application

app.mainloop()