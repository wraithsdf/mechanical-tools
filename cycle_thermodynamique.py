import numpy as np
import matplotlib.pyplot as plt

class CycleThermodynamique:
    def __init__(self, type_cycle="otto"):
        """
        type_cycle: "otto", "diesel" ou "rankine"
        """
        self.type = type_cycle
        self.R = 287.1  # Constante des gaz parfaits pour l'air (J/kg.K)
        self.gamma = 1.4  # Rapport des chaleurs spécifiques pour l'air
        
    def cycle_otto(self, V1, T1, P1, taux_compression, Q_combustion):
        """
        Calcul d'un cycle Otto
        V1: Volume initial (m³)
        T1: Température initiale (K)
        P1: Pression initiale (Pa)
        taux_compression: rapport volumétrique
        Q_combustion: Chaleur apportée par la combustion (J/kg)
        """
        # Point 1 (début compression)
        self.V1, self.T1, self.P1 = V1, T1, P1
        
        # Point 2 (fin compression)
        self.V2 = V1 / taux_compression
        self.T2 = T1 * taux_compression**(self.gamma-1)
        self.P2 = P1 * taux_compression**self.gamma
        
        # Point 3 (fin combustion)
        self.V3 = self.V2
        self.T3 = self.T2 + Q_combustion / (self.R * (self.gamma-1))
        self.P3 = self.P2 * (self.T3/self.T2)
        
        # Point 4 (fin détente)
        self.V4 = self.V1
        self.T4 = self.T3 * (1/taux_compression)**(self.gamma-1)
        self.P4 = self.P3 * (1/taux_compression)**self.gamma
        
        # Calcul du rendement
        self.rendement = 1 - 1/taux_compression**(self.gamma-1)
        
    def cycle_diesel(self, V1, T1, P1, taux_compression, taux_cutoff):
        """
        Calcul d'un cycle Diesel
        taux_cutoff: rapport des volumes après/avant combustion
        """
        # Point 1 (début compression)
        self.V1, self.T1, self.P1 = V1, T1, P1
        
        # Point 2 (fin compression)
        self.V2 = V1 / taux_compression
        self.T2 = T1 * taux_compression**(self.gamma-1)
        self.P2 = P1 * taux_compression**self.gamma
        
        # Point 3 (fin combustion)
        self.V3 = self.V2 * taux_cutoff
        self.T3 = self.T2 * taux_cutoff
        self.P3 = self.P2
        
        # Point 4 (fin détente)
        self.V4 = self.V1
        self.T4 = self.T3 * (self.V3/self.V4)**(self.gamma-1)
        self.P4 = self.P3 * (self.V3/self.V4)**self.gamma
        
        # Calcul du rendement
        self.rendement = 1 - (1/taux_compression**(self.gamma-1)) * \
                        ((taux_cutoff**self.gamma - 1)/(self.gamma*(taux_cutoff-1)))
    
    def plot_cycle(self):
        """Affiche le diagramme PV du cycle"""
        # Création des points pour les courbes
        V_compression = np.linspace(self.V2, self.V1, 100)
        P_compression = self.P1 * (self.V1/V_compression)**self.gamma
        
        V_detente = np.linspace(self.V3, self.V4, 100)
        P_detente = self.P3 * (self.V3/V_detente)**self.gamma
        
        plt.figure(figsize=(10, 6))
        
        # Tracé des transformations
        plt.plot(V_compression, P_compression, 'b-', label='Compression')
        plt.plot([self.V2, self.V3], [self.P2, self.P3], 'r-', label='Combustion')
        plt.plot(V_detente, P_detente, 'g-', label='Détente')
        plt.plot([self.V4, self.V1], [self.P4, self.P1], 'k-', label='Échappement')
        
        plt.title(f'Diagramme PV - Cycle {self.type.capitalize()}')
        plt.xlabel('Volume (m³)')
        plt.ylabel('Pression (Pa)')
        plt.grid(True)
        plt.legend()
        plt.yscale('log')
        plt.xscale('log')
        plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple avec un cycle Otto
    V1 = 0.0005  # m³
    T1 = 300  # K
    P1 = 101325  # Pa
    taux_compression = 8
    Q_combustion = 1000  # J/kg
    
    cycle = CycleThermodynamique("otto")
    cycle.cycle_otto(V1, T1, P1, taux_compression, Q_combustion)
    print(f"Rendement du cycle Otto: {cycle.rendement*100:.1f}%")
    cycle.plot_cycle()
    
    # Exemple avec un cycle Diesel
    cycle_diesel = CycleThermodynamique("diesel")
    taux_cutoff = 2
    cycle_diesel.cycle_diesel(V1, T1, P1, taux_compression, taux_cutoff)
    print(f"Rendement du cycle Diesel: {cycle_diesel.rendement*100:.1f}%")
    cycle_diesel.plot_cycle()
