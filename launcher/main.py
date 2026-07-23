import customtkinter as ctk
import sys
import os


# Allow importing runtime module
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

from runtime.runtime_manager import RuntimeManager


# App settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Main window
app = ctk.CTk()

app.title("LiteDroid One")
app.geometry("900x600")


# Function for runtime button
def start_runtime():

    runtime = RuntimeManager()

    status = runtime.get_status()

    status_label.configure(
        text=status
    )


# Title
title = ctk.CTkLabel(
    app,
    text="🚀 LiteDroid One",
    font=("Arial", 32, "bold")
)

title.pack(pady=40)


# Subtitle
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


# Button
button = ctk.CTkButton(
    app,
    text="Start Android Runtime",
    width=250,
    height=45,
    command=start_runtime
)

button.pack(pady=40)


# Run application
app.mainloop()