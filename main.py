from tkinter import simpledialog, messagebox
import tkinter as tk
import background
import riotid
import practice
import gui
import dodge
import autoaccept
import threading
import time

# Define global variable for the auto-accept button
auto_accept_button = None

# Function to start the 5v5 practice tool
def start_practice_tool():
    practice.start_practice_tool()

# Function to change the background of the League of Legends client
def change_background():
    champ_skins = background.get_all_champion_skins()
    if champ_skins is None:
        messagebox.showerror("Error", "Failed to fetch champion skins.")
        return

    champion_name = simpledialog.askstring("Change Background", "Enter the champion name:")
    if champion_name is None:
        return

    champion_name_lower = champion_name.lower()
    matching_champions = [champ for champ in champ_skins.keys() if champ.lower() == champion_name_lower]
    if not matching_champions:
        messagebox.showerror("Error", f"No skins found for {champion_name}.")
        return
    elif len(matching_champions) > 1:
        messagebox.showerror("Error", f"Multiple champions found for {champion_name}. Please be more specific.")
        return

    champion_name = matching_champions[0]

    skin_window = tk.Toplevel()
    skin_window.title(f"Skins for {champion_name}")

    max_button_width = max(len(skin["name"]) for skin in champ_skins[champion_name])

    for i, skin in enumerate(champ_skins[champion_name]):
        skin_name = skin["name"]
        skin_button = tk.Button(skin_window, text=skin_name, width=max_button_width, command=lambda s=skin: set_background(champion_name, s))
        skin_button.grid(row=i, column=0, padx=5, pady=5)

# Function to set the background using the selected skin
def set_background(champion_name, selected_skin):
    background.change_background_skin(selected_skin["id"])

# Function to change the Riot ID (nickname)
def change_riot_id():
    riot_id = simpledialog.askstring("Change Riot ID", "Enter the new Riot ID (nickname):")
    if riot_id is None:
        return

    tag_line = simpledialog.askstring("Change Riot ID", "Enter the tag line:")
    if tag_line is None:
        return

    response = riotid.change_riot_id(riot_id, tag_line)
    if response.get("isSuccess", False):
        messagebox.showinfo("Riot ID Change", "Riot ID changed successfully")
    else:
        error_code = response.get("errorCode", "Unknown")
        error_message = response.get("errorMessage", "Unknown")
        messagebox.showerror("Riot ID Change", f"Error: {error_code}\nReason: {error_message}")

# Function to dodge the lobby
def start_dodge_lobby():
    response = dodge.dodge_lobby()
    if response.get("error"):
        # Remove the line below that triggers the message box
        # messagebox.showerror("Error", response["error"])
        pass  # Do nothing

# Function to toggle auto-accept feature
def toggle_auto_accept():
    if autoaccept.is_auto_accept_enabled():
        autoaccept.disable_auto_accept()
    else:
        autoaccept.enable_auto_accept()
    # Update the text of the auto-accept button if it's initialized
    if auto_accept_button:
        auto_accept_button.config(text=f"Auto Accept: {'ON' if autoaccept.is_auto_accept_enabled() else 'OFF'}")

# Function to continuously check and auto-accept queue
def check_auto_accept():
    while True:
        if autoaccept.is_auto_accept_enabled():
            autoaccept.enable_auto_accept()
        time.sleep(1)  # Check every second

# Main function to handle the application logic
def main():
    # Define functions to pass to the GUI
    start_background_change = change_background
    start_riot_id_change = change_riot_id

    # Call function to create the main GUI
    global auto_accept_button
    auto_accept_button = gui.create_main_gui(start_background_change, start_riot_id_change, start_practice_tool, start_dodge_lobby, toggle_auto_accept)

    # Start the thread to continuously check auto-accept
    threading.Thread(target=check_auto_accept, daemon=True).start()

if __name__ == "__main__":
    main()
