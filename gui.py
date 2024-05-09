import tkinter as tk
import autoaccept

# Function to create the main GUI layout
def create_main_gui(start_background_change, start_riot_id_change, start_practice_tool, start_dodge_lobby, toggle_auto_accept):
    # Create the main window
    root = tk.Tk()
    root.title("")

    # Create a frame within the main window
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Button to change the background
    btn_background = tk.Button(frame, text="Change Background", command=start_background_change)
    btn_background.pack(fill=tk.X, padx=10, pady=5)

    # Button to change the Riot ID
    btn_riot_id = tk.Button(frame, text="Change Riot ID", command=start_riot_id_change)
    btn_riot_id.pack(fill=tk.X, padx=10, pady=5)

    # Button to start the 5v5 Practice Tool
    btn_practice_tool = tk.Button(frame, text="Start 5v5 Practice Tool", command=start_practice_tool)
    btn_practice_tool.pack(fill=tk.X, padx=10, pady=5)

    # Button to dodge the lobby
    btn_dodge = tk.Button(frame, text="Dodge Lobby", command=start_dodge_lobby)
    btn_dodge.pack(fill=tk.X, padx=10, pady=5)

    # Button to toggle auto-accept feature
    auto_accept_button = tk.Button(frame, text=f"Auto Accept: {'ON' if autoaccept.is_auto_accept_enabled() else 'OFF'}",
                                    command=toggle_auto_accept)
    auto_accept_button.pack(fill=tk.X, padx=10, pady=5)

    # Button to exit the application
    btn_exit = tk.Button(frame, text="Exit", command=root.quit)
    btn_exit.pack(fill=tk.X, padx=10, pady=5)

    # Start the GUI event loop
    root.mainloop()
