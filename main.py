import numpy as np
import matplotlib.pyplot as plt

# 1. DONNÉES RÉELLES (Observées par les télescopes)
r_obs = np.array([1, 2, 5, 10, 15, 20, 25, 30])
v_obs = np.array([95, 120, 145, 155, 155, 150, 152, 155])

# 2. MODÉLISATION MATHÉMATIQUE
r_model = np.linspace(1, 30, 100)
G = 43007  # Constante gravitationnelle ajustée aux unités (kpc, km/s, Masse solaire)
M_visible = 1e9  # Masse de la galaxie (bulbe + disque)

# Modèle A : Gravité Newtonienne pure (Masse visible uniquement)
v_newton = np.sqrt((G * M_visible) / r_model)

# Modèle B : Matière Noire (Halo de masse supplémentaire)
M_dark_halo = M_visible + (1.5e9 * r_model) # La masse augmente linéairement
v_dark_matter = np.sqrt((G * M_dark_halo) / r_model)

# Modèle C : MOND (Modified Newtonian Dynamics) - On modifie la loi, pas la masse
v_mond = np.sqrt(np.sqrt(G * M_visible * 1.2e-10)) * np.ones_like(r_model) # Simplification MOND

# 3. VISUALISATION PROFESSIONNELLE
plt.figure(figsize=(10, 6))
plt.scatter(r_obs, v_obs, color='black', label="Observations Réelles (NGC 3198)", zorder=5)
plt.plot(r_model, v_newton, '--', label="Théorie Newton (Échec)", color='red')
plt.plot(r_model, v_dark_matter, label="Modèle Matière Noire", color='blue')
plt.plot(r_model, v_mond, ':', label="Modèle MOND (Gravité Modifiée)", color='green')

plt.title("Le duel des modèles : Qui explique la rotation de NGC 3198 ?", fontsize=14)
plt.xlabel("Distance du centre (kilo-parsecs)")
plt.ylabel("Vitesse de rotation (km/s)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
