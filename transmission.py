import numpy as np
import matplotlib.pyplot as plt

class Transmission:
    def __init__(self, D1, D2, type_transmission="courroie"):
        """
        D1: Diamètre de la poulie/roue menante (mm)
        D2: Diamètre de la poulie/roue menée (mm)
        type_transmission: "courroie" ou "chaine"
        """
        self.D1 = D1
        self.D2 = D2
        self.type = type_transmission
        
    def rapport_transmission(self):
        """Calcul du rapport de transmission"""
        return self.D2 / self.D1
    
    def vitesse_sortie(self, N1):
        """
        Calcul de la vitesse de sortie
        N1: Vitesse d'entrée (tr/min)
        """
        i = self.rapport_transmission()
        return N1 / i
    
    def couple_sortie(self, C1, rendement=0.95):
        """
        Calcul du couple de sortie
        C1: Couple d'entrée (N.m)
        rendement: Rendement de la transmission
        """
        i = self.rapport_transmission()
        return C1 * i * rendement
    
    def puissance_transmise(self, N1, C1, rendement=0.95):
        """
        Calcul de la puissance transmise
        N1: Vitesse d'entrée (tr/min)
        C1: Couple d'entrée (N.m)
        """
        omega = N1 * 2 * np.pi / 60  # conversion en rad/s
        return C1 * omega * rendement
    
    def plot_caracteristiques(self, N1_range):
        """
        Affiche les caractéristiques de la transmission
        N1_range: plage de vitesses d'entrée à étudier
        """
        N2_range = [self.vitesse_sortie(N1) for N1 in N1_range]
        
        plt.figure(figsize=(12, 6))
        plt.plot(N1_range, N2_range)
        plt.title(f'Caractéristique de la transmission par {self.type}')
        plt.xlabel('Vitesse d\'entrée (tr/min)')
        plt.ylabel('Vitesse de sortie (tr/min)')
        plt.grid(True)
        plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple avec une transmission par courroie
    D1 = 100  # mm
    D2 = 200  # mm
    N1 = 1500  # tr/min
    C1 = 50  # N.m
    
    trans = Transmission(D1, D2, "courroie")
    
    # Calculs
    i = trans.rapport_transmission()
    N2 = trans.vitesse_sortie(N1)
    C2 = trans.couple_sortie(C1)
    P = trans.puissance_transmise(N1, C1)
    
    print(f"Rapport de transmission: {i:.2f}")
    print(f"Vitesse de sortie: {N2:.1f} tr/min")
    print(f"Couple de sortie: {C2:.1f} N.m")
    print(f"Puissance transmise: {P/1000:.2f} kW")
    
    # Affichage de la caractéristique
    N1_range = np.linspace(500, 3000, 100)
    trans.plot_caracteristiques(N1_range)
