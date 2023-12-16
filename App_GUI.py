import tkinter as tk
from tkinter import ttk


def start_GUI():

    def submit():
        Nom = entry_name.get()
        sex = sex_combo.get()
        age = entry_age.get()
        cholesterol = chol_combo.get()
        sugar = sugar_combo.get()
        temperature = temp_combo.get()
        activity = activity_combo.get()
        missing_vitamins = vitamins_combo.get()
        height = entry_taille.get()
        weight = entry_poids.get()
        print(f"Nom: {Nom}")
        print(f"Sex: {sex}")
        print(f"Age: {age}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Cholesterol Level: {cholesterol}")
        print(f"Blood Sugar Level: {sugar}")
        print(f"Ambient Temperature: {temperature}")
        print(f"Activity Level: {activity}")
        print(f"Missing Vitamins: {missing_vitamins}")
        # Create a label inside the frame
        label_tkinter = tk.Label(
            window,
            text="**** Que ton aliment soit ta seule médecine ****:",
            bg='#d5e6e6',
            fg="#374151",
            font=("Arial", 12, "bold")
        )
        label_tkinter.grid(row=12, column=0, sticky="nsew", padx=(0, 5))

        return True


        # # Create an entry widget (text box) inside the poids_frame
        # entry_response = tk.Entry(window, font=("Arial", 12))
        # entry_response.grid(row=12, columnspan=5, rowspan=5, sticky="nsew", padx=100)


    # Create the main window
    window = tk.Tk()
    window.title("Système expert de conseil en nutrition personnalisée")


    # Create a gradient background
    window.configure(bg='#d5e6e6')

    label_title = tk.Label(
        window,
        text="Bienvenue dans le système expert de conseil en nutrition personnalisée",
        font=("Arial", 24, "bold"),
        bg='#d5e6e6',
        fg="#cd8282"
    )
    label_title.grid(row=0, column=1, padx=10, pady=10)

    # Create a frame to hold the label and entry
    name_frame = tk.Frame(window)
    name_frame.grid(row=1, column=0, padx=30, pady=10)

    # Create a label inside the frame
    label_name = tk.Label(
        name_frame,
        text="Nom:",
        bg='#d5e6e6',
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_name.grid(row=1, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the name_frame
    entry_name = tk.Entry(name_frame, font=("Arial", 12))
    entry_name.grid(row=1, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    sex_frame = tk.Frame(window)
    sex_frame.grid(row=2, column=0, padx=30, pady=10)

    # Create a label inside the frame
    label_sex = tk.Label(
        sex_frame,
        text="Sex:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_sex.grid(row=2, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the sex_frame
    sex_values = ["Male", "Female"]
    sex_combo = ttk.Combobox(window, values=sex_values, font=("Arial", 12))
    sex_combo.grid(row=2, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    taille_frame = tk.Frame(window)
    taille_frame.grid(row=3, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_taille = tk.Label(
        taille_frame,
        text="Taille:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_taille.grid(row=3, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the taille_frame
    entry_taille = tk.Entry(window, font=("Arial", 12))
    entry_taille.insert(0, "Taille en cm.")
    entry_taille.configure(fg='gray')
    entry_taille.grid(row=3, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    age_frame = tk.Frame(window)
    age_frame.grid(row=4, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_age = tk.Label(
        age_frame,
        text="Age:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_age.grid(row=4, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the age_frame
    entry_age = tk.Entry(window, font=("Arial", 12))
    entry_age.grid(row=4, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    poids_frame = tk.Frame(window)
    poids_frame.grid(row=5, column=0, padx=10, pady=10)

    # Create a label inside theframe
    label_poids = tk.Label(
        poids_frame,
        text="Poids:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_poids.grid(row=5, column=0, sticky="nsew", padx=(0, 5))

    # Create an entry widget (text box) inside the poids_frame
    entry_poids = tk.Entry(window, font=("Arial", 12))
    entry_poids.insert(0, "Poids en kg.")
    entry_poids.configure(fg='gray')
    entry_poids.grid(row=5, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    chol_frame = tk.Frame(window)
    chol_frame.grid(row=6, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_chol = tk.Label(
        chol_frame,
        text="Taux de cholestérol:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_chol.grid(row=6, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the chol_frame
    chol_values = ["Normale", "Élevé"]
    chol_combo = ttk.Combobox(window, values=chol_values, font=("Arial", 12))
    chol_combo.grid(row=6, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    sugar_frame = tk.Frame(window)
    sugar_frame.grid(row=7, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_sugar = tk.Label(
        sugar_frame,
        text="Taux de sucre dans le sang:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_sugar.grid(row=7, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the sugar_frame
    sugar_values = ["Stable", "Instable"]
    sugar_combo = ttk.Combobox(window, values=sugar_values, font=("Arial", 12))
    sugar_combo.grid(row=7, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    temp_frame = tk.Frame(window)
    temp_frame.grid(row=8, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_temp = tk.Label(
        temp_frame,
        text="Température ambiante:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_temp.grid(row=8, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the temp_frame
    temp_values = ["Normale", "Élevée"]
    temp_combo = ttk.Combobox(window, values=temp_values, font=("Arial", 12))
    temp_combo.grid(row=8, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    activity_frame = tk.Frame(window)
    activity_frame.grid(row=9, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_activity = tk.Label(
        activity_frame,
        text="Niveau d'activité:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_activity.grid(row=9, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the activity_frame
    activity_values = ["Faible", "Modéré", "Intense"]
    activity_combo = ttk.Combobox(window, values=activity_values, font=("Arial", 12))
    activity_combo.grid(row=9, column=1, sticky="nsew")

    # Create a frame to hold the label and entry
    vitamins_frame = tk.Frame(window)
    vitamins_frame.grid(row=10, column=0, padx=10, pady=10)

    # Create a label inside the frame
    label_vitamins = tk.Label(
        vitamins_frame,
        text="Vitamines manquantes:",
        fg="#374151",
        font=("Arial", 12, "bold")
    )
    label_vitamins.grid(row=10, column=0, sticky="nsew", padx=(0, 5))

    # Create a combo box inside the vitamins_frame
    vitamins_values = ["Vitamine A", "Vitamine C", "Vitamine D", "Vitamine B12", "Fer", "Aucun"]
    vitamins_combo = ttk.Combobox(window, values=vitamins_values, font=("Arial", 12))
    vitamins_combo.grid(row=10, column=1, sticky="nsew")

    # Create a button to submit the form
    submit_button = tk.Button(
        window,
        text="Envoyer",
        fg="#cd8282",
        font=("Arial", 12, "bold"),
        command=submit
    )
    submit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)




    # Set the window size and center it on the screen
    window_width = 1600
    window_height = 1600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Start the main event loop
    window.mainloop()
    print("hello")




