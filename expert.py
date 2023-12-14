import tkinter as tk
from tkinter import ttk

def submit():
    name = entry_name.get()
    sex = combo.get()
    age = entry_age.get()
    cholestero = entry_cholestero.get()
    sugar = entry_sugar.get()
    temperature = entry_temperature.get()
    print(f"Name: {name}")
    print(f"Sex: {sex}")
    print(f"Age: {age}")
    print(f"TauxCholestero: {cholestero}")
    print(f"TauxSucreSang: {sugar}")
    print(f"TempératureAmbiante: {temperature}")



# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Define the color fading theme
start_color = "#F3F4F6"
end_color = "#60A5FA"

# Create a gradient background
for i in range(400):
    intensity = int(255 - i * (255 / 400))
    color = '#%02x%02x%02x' % (
        int((1 - i / 400) * int(start_color[1:3], 16) + (i / 400) * int(end_color[1:3], 16)),
        int((1 - i / 400) * int(start_color[3:5], 16) + (i / 400) * int(end_color[3:5], 16)),
        int((1 - i / 400) * int(start_color[5:7], 16) + (i / 400) * int(end_color[5:7], 16))
    )
    window.configure(bg=color)
    

    
label_title = tk.Label(window, text="Système expert de conseil en nutrition personnalisée", font=("Arial", 14, "bold"), fg="#EC4899")
label_title.pack(pady=(20, 10))

# Create a label and pack it into the window
label_name = tk.Label(window, text="Name:", bg=start_color, fg="#374151", font=("Arial", 12, "bold"))
label_name.pack(pady=(20, 5))

# Create an entry widget (text box) for name and pack it into the window
entry_name = tk.Entry(window, font=("Arial", 12))
entry_name.pack(pady=(0, 10))

# Create a label for the sex selection
label_sex = tk.Label(window, text="Sex:", bg=start_color, fg="#374151", font=("Arial", 12, "bold"))
label_sex.pack()

# Create a combo box (dropdown menu) for sex selection
sex_values = ["Male", "Female"]
combo = ttk.Combobox(window, values=sex_values, font=("Arial", 12))
combo.pack(pady=(0, 10))

# Set the default selection to the first value in the list
combo.current(0)

# Create a label and pack it into the window
label_age = tk.Label(window, text="Age:", bg=start_color, fg="#374151", font=("Arial", 12, "bold"))
label_age.pack()

# Create an entry widget (text box) for age and pack it into the window
entry_age = tk.Entry(window, font=("Arial", 12))
entry_age.pack(pady=(0, 10))

# Create a label and pack it into the window
label_cholestero = tk.Label(window, text="TauxCholestero:", bg=start_color, fg="#374151", font=("Arial", 12, "bold"))
label_cholestero.pack()

# Create an entry widget (text box) for TauxCholestero and pack it into the window
entry_cholestero = tk.Entry(window, font=("Arial", 12))
entry_cholestero.pack(pady=(0, 10))

# Create a label and pack it into the window
label_sugar = tk.Label(window, text="TauxSucreSang:", bg=start_color, fg="#374151", font=("Arial", 12, "bold"))
label_sugar.pack()

# Create an entry widget (text box) for TauxSucreSang and pack it into the window
entry_sugar = tk.Entry(window, font=("Arial", 12))
entry_sugar.pack(pady=(0, 10))

# Create a label and pack it into the window
label_temperature = tk.Label(window, text="TempératureAmbiante:", bg=start_color, fg="#374151", font=("Arial", 12, "bold"))
label_temperature.pack()

# Create an entry widget (text box) for TempératureAmbiante and pack it into the window
entry_temperature = tk.Entry(window, font=("Arial", 12))
entry_temperature.pack(pady=(0, 10))

# Create a button and pack it into the window
button = tk.Button(window, text="Submit", command=submit, bg="#60A5FA", fg="#FFFFFF", font=("Arial", 12, "bold"))
button.pack(pady=(10, 20))

# Create a label to display the result
result_label = tk.Label(window, text=f"Result: ", font=("Arial", 12), bg=start_color, fg="#374151")
result_label.pack(pady=(10, 20))

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

# # Définition des prédicats
# def Masculin(x):
#     # Implémentation de Masculin(x)
#     pass
    
# def Féminin(x):
#     # Implémentation de Féminin(x)
#     pass

# def Age(x, y):
#     # Implémentation de Age(x, y)
#     pass

# def BesoinsCaloriques(x, z):
#     # Implémentation de BesoinsCaloriques(x, z)
#     pass

# def Objectif(x, y):
#     # Implémentation de Objectif(x, y)
#     pass

# def ActivitéPhysique(x, y):
#     # Implémentation de ActivitéPhysique(x, y)
#     pass

# def TauxCholesterol(x, y):
#     # Implémentation de TauxCholesterol(x, y)
#     pass

# def TauxSucreSang(x, y):
#     # Implémentation de TauxSucreSang(x, y)
#     pass

# def TempératureAmbiante(x, y):
#     # Implémentation de TempératureAmbiante(x, y)
#     pass

# def RégimeAlimentaire(x, y):
#     # Implémentation de RégimeAlimentaire(x, y)
#     pass

# def SuiviNonAtteint(x):
#     # Implémentation de SuiviNonAtteint(x)
#     pass

# # Règles

# # Règle de Calcul des Besoins Caloriques
# def calculer_besoins_caloriques(x, y):
#     if Masculin(x) and 18 <= y <= 30:
#         BesoinsCaloriques(x, "Formule X")
#     elif Féminin(x) and 18 <= y <= 30:
#         BesoinsCaloriques(x, "Formule Y")

# # Règle de Composition des Repas
# def recommander_composition_repas(x, y):
#     if Objectif(x, "Perte de poids") and ActivitéPhysique(x, "Faible"):
#         RecommandationMacronutriments(x, "Répartition spécifique")
#     elif Objectif(x, "Prise de masse musculaire") and ActivitéPhysique(x, "Élevée"):
#         RecommandationMacronutriments(x, "Autre répartition")

# # Règle de Recommandation Alimentaire
# def recommander_alimentation(x, y):
#     if TauxCholesterol(x, "Élevé"):
#         RecommandationAliments(x, "Riches en fibres et en acides gras insaturés")
#     elif TauxSucreSang(x, "Instable"):
#         RecommandationAliments(x, "À faible indice glycémique")

# # Règle de Recommandation de Portions
# def recommander_portions(x, y):
#     if Objectif(x, "Maintien du poids") and ActivitéPhysique(x, "Modérée"):
#         RecommandationPortions(x, "Spécifiques pour chaque groupe alimentaire")

# # Règle de Recommandation d'Hydratation
# def recommander_hydratation(x, y):
#     if TempératureAmbiante(y, "Élevée") and ActivitéPhysique(x, "Intense"):
#         RecommandationHydratation(x, "Augmentation de la consommation d'eau")

# # Règle de Recommandation de Suppléments
# def recommander_suppléments(x):
#     if RégimeAlimentaire(x, "Manque de certaines vitamines"):
#         RecommandationSuppléments(x, "Spécifiques en fonction des besoins individuels")

# # Règle de Suivi et d'Ajustement
# def suivi_et_ajustement(x):
#     if SuiviNonAtteint(x):
#         RévisionRecommandations(x)

# # Exemple d'utilisation
# patient1 = "John"
# age1 = 25
# sexe1 = "Masculin"
# activité1 = "Modérée"
# objectif1 = "Maintien du poids"

# # Appel des règles
# calculer_besoins_caloriques(patient1, age1)
# recommander_portions(patient1, activité1)
# suivi_et_ajustement(patient1)


