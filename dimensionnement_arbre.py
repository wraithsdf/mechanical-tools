import math

class DimensionnementArbre:
    def __init__(self, couple, limite_elastique, coef_securite=2):
        """
        couple: couple appliqué (N.m)
        limite_elastique: limite élastique du matériau (Pa)
        coef_securite: coefficient de sécurité
        """
        self.couple = couple
        self.Re = limite_elastique
        self.cs = coef_securite
        
    def diametre_minimal(self):
        """Calcul du diamètre minimal de l'arbre"""
        tau_adm = self.Re / (2 * self.cs)  # Contrainte admissible en cisaillement
        
        # Formule du diamètre minimal
        d = ((16 * self.couple) / (math.pi * tau_adm)) ** (1/3)
        return d
    
    def contrainte_cisaillement(self, diametre):
        """Calcul de la contrainte de cisaillement pour un diamètre donné"""
        return (16 * self.couple) / (math.pi * diametre**3)

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple avec un arbre en acier
    couple = 1000  # N.m
    Re = 400e6  # Pa (limite élastique de l'acier)
    
    arbre = DimensionnementArbre(couple, Re)
    d_min = arbre.diametre_minimal()
    
    print(f"Diamètre minimal requis: {d_min*1000:.2f} mm")
    print(f"Contrainte de cisaillement: {arbre.contrainte_cisaillement(d_min)/1e6:.2f} MPa")
