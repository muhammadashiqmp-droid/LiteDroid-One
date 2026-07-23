import customtkinter as ctk


# App settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Main window
app = ctk.CTk()

app.title("LiteDroid One")
app.geometry("900x600")


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


# Button
button = ctk.CTkButton(
    app,
    text="Start Android Runtime",
    width=250,
    height=45
)

button.pack(pady=40)


# Run
app.mainloop()