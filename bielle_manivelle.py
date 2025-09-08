import numpy as np
import matplotlib.pyplot as plt

class BielleManivelle:
    def __init__(self, L_manivelle, L_bielle, omega):
        """
        L_manivelle: longueur de la manivelle (m)
        L_bielle: longueur de la bielle (m)
        omega: vitesse angulaire de la manivelle (rad/s)
        """
        self.r = L_manivelle
        self.L = L_bielle
        self.omega = omega
        
    def position(self, theta):
        """Position du piston en fonction de l'angle theta"""
        return self.r * np.cos(theta) + np.sqrt(self.L**2 - (self.r * np.sin(theta))**2)
    
    def vitesse(self, theta):
        """Vitesse du piston"""
        num = -self.r * self.omega * (self.r * np.sin(2*theta))
        den = 2 * np.sqrt(self.L**2 - (self.r * np.sin(theta))**2)
        return -self.r * self.omega * np.sin(theta) + num/den
    
    def acceleration(self, theta):
        """Accélération du piston"""
        return -self.r * self.omega**2 * (
            np.cos(theta) + 
            (self.r/self.L) * np.cos(2*theta) / 
            (1 - (self.r/self.L)**2 * np.sin(theta)**2)**0.5
        )
    
    def plot_cinematique(self):
        theta = np.linspace(0, 4*np.pi, 1000)
        pos = [self.position(t) for t in theta]
        vit = [self.vitesse(t) for t in theta]
        acc = [self.acceleration(t) for t in theta]
        
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        ax1.plot(theta, pos)
        ax1.set_title('Position du piston')
        ax1.set_ylabel('Position (m)')
        ax1.grid(True)
        
        ax2.plot(theta, vit)
        ax2.set_title('Vitesse du piston')
        ax2.set_ylabel('Vitesse (m/s)')
        ax2.grid(True)
        
        ax3.plot(theta, acc)
        ax3.set_title('Accélération du piston')
        ax3.set_ylabel('Accélération (m/s²)')
        ax3.set_xlabel('Angle (rad)')
        ax3.grid(True)
        
        plt.tight_layout()
        plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    mecanisme = BielleManivelle(L_manivelle=0.05, L_bielle=0.2, omega=50)
    mecanisme.plot_cinematique()
