import numpy as np
import matplotlib.pyplot as plt

class PoutreEulerBernoulli:
    def __init__(self, L, E, I, q):
        """
        L: longueur de la poutre (m)
        E: module de Young (Pa)
        I: moment quadratique (m^4)
        q: charge répartie (N/m)
        """
        self.L = L
        self.E = E
        self.I = I
        self.q = q
        
    def fleche(self, x):
        """Calcul de la flèche en tout point x"""
        return (self.q * x * (self.L**3 - 2*self.L*x**2 + x**3)) / (24 * self.E * self.I)
    
    def contrainte_max(self, h):
        """
        Calcul de la contrainte maximale
        h: hauteur de la section (m)
        """
        M_max = (self.q * self.L**2) / 8  # Moment fléchissant maximal
        return (M_max * h/2) / self.I
    
    def plot_fleche(self):
        x = np.linspace(0, self.L, 100)
        y = [self.fleche(xi) for xi in x]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y)
        plt.title('Flèche de la poutre')
        plt.xlabel('Position (m)')
        plt.ylabel('Flèche (m)')
        plt.grid(True)
        plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    L = 2.0  # Longueur de la poutre en m
    E = 210e9  # Module de Young de l'acier en Pa
    b = 0.05  # Largeur de la section en m
    h = 0.1  # Hauteur de la section en m
    I = (b * h**3) / 12  # Moment quadratique
    q = 1000  # Charge répartie en N/m
    
    poutre = PoutreEulerBernoulli(L, E, I, q)
    poutre.plot_fleche()
    print(f"Contrainte maximale: {poutre.contrainte_max(h)/1e6:.2f} MPa")
