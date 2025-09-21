import matplotlib.pyplot as plt

def analyser_adn(sequence):
    """
    Analyser une séquence ADN pour compter les dinucléotides CG/GC et AT/TA
    SANS chevauchement (CGC = 1 seule paire, pas 2)
    """
    sequence = sequence.upper().strip()
    total_positions = len(sequence) - 1  # Nombre de paires possibles
    
    if total_positions <= 0:
        return 0.0, 0.0, 0, 0, 0, 0
    
    # Compter sans chevauchement
    cg_count = 0
    gc_count = 0
    at_count = 0
    ta_count = 0
    
    i = 0
    while i < len(sequence) - 1:
        paire = sequence[i:i+2]
        
        if paire == 'CG':
            cg_count += 1
            i += 2  # Sauter la prochaine position pour éviter le chevauchement
        elif paire == 'GC':
            gc_count += 1
            i += 2  # Sauter la prochaine position pour éviter le chevauchement
        elif paire == 'AT':
            at_count += 1
            i += 2  # Sauter la prochaine position pour éviter le chevauchement
        elif paire == 'TA':
            ta_count += 1
            i += 2  # Sauter la prochaine position pour éviter le chevauchement
        else:
            i += 1  # Position suivante normale
    
    # Total des paires GC et AT (sans chevauchement)
    total_gc_pairs = cg_count + gc_count
    total_at_pairs = at_count + ta_count
    
    # Calculer les pourcentages
    gc_pourcent = (total_gc_pairs / total_positions) * 100
    at_pourcent = (total_at_pairs / total_positions) * 100
    
    return gc_pourcent, at_pourcent, cg_count, gc_count, at_count, ta_count

def lire_fichier_adn(nom_fichier):
    """Lire les séquences depuis un fichier"""
    sequences = []
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                sequences.append(ligne)
    return sequences

def visualiser_adn(sequences):
    """Créer des graphiques pour visualiser l'analyse des dinucléotides ADN"""
    # Analyser toutes les séquences
    resultats = []
    for i, seq in enumerate(sequences):
        gc_pct, at_pct, cg, gc, at, ta = analyser_adn(seq)
        resultats.append({
            'nom': f'Séq {i+1}',
            'sequence': seq,
            'longueur': len(seq),
            'gc_pourcent': gc_pct,
            'at_pourcent': at_pct,
            'cg': cg, 'gc': gc, 'at': at, 'ta': ta
        })
    
    # Créer les graphiques
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Analyse des Dinucléotides ADN (CG/GC et AT/TA)', fontsize=16)
    
    # Graphique 1: Pourcentages de dinucléotides GC et AT
    noms = [f'DNA {i+1}' for i in range(len(resultats))]
    gc_values = [r['gc_pourcent'] for r in resultats]
    at_values = [r['at_pourcent'] for r in resultats]
    autres_values = [100 - r['gc_pourcent'] - r['at_pourcent'] for r in resultats]
    
    x = range(len(noms))
    ax1.bar(x, gc_values, label='Paires GC (CG+GC)', color='blue', alpha=0.8)
    ax1.bar(x, at_values, bottom=gc_values, label='Paires AT (AT+TA)', color='red', alpha=0.8)
    ax1.bar(x, autres_values, bottom=[gc_values[i] + at_values[i] for i in range(len(gc_values))], 
            label='Autres paires', color='gray', alpha=0.5)
    
    ax1.set_title('Pourcentage de Dinucléotides par Séquence')
    ax1.set_xlabel('Séquences')
    ax1.set_ylabel('Pourcentage (%)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(noms, rotation=45)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Graphique 2: Nombre de paires par séquence
    cg_gc_counts = [r['cg'] + r['gc'] for r in resultats]
    at_ta_counts = [r['at'] + r['ta'] for r in resultats]
    
    x_pos = range(len(noms))
    ax2.bar([x - 0.2 for x in x_pos], cg_gc_counts, 
            width=0.4, label='CG/GC', color='blue', alpha=0.8)
    ax2.bar([x + 0.2 for x in x_pos], at_ta_counts, 
            width=0.4, label='AT/TA', color='orange', alpha=0.8)
    
    ax2.set_title('Pair counts in DNA sequences')
    ax2.set_xlabel('DNA Sequences')
    ax2.set_ylabel('Counts')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(noms)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Graphique 3: Comparaison GC vs AT seulement
    ax3.bar([x - 0.2 for x in range(len(noms))], gc_values, 
            width=0.4, label='Paires GC', color='green', alpha=0.8)
    ax3.bar([x + 0.2 for x in range(len(noms))], at_values, 
            width=0.4, label='Paires AT', color='orange', alpha=0.8)
    
    ax3.set_title('Comparaison Paires GC vs AT')
    ax3.set_xlabel('Séquences')
    ax3.set_ylabel('Pourcentage (%)')
    ax3.set_xticks(range(len(noms)))
    ax3.set_xticklabels(noms, rotation=45)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Ajouter les valeurs sur les barres
    for i, (gc, at) in enumerate(zip(gc_values, at_values)):
        ax3.text(i - 0.2, gc + 1, f'{gc:.1f}%', ha='center', fontsize=9)
        ax3.text(i + 0.2, at + 1, f'{at:.1f}%', ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.show()

def afficher_tableau_paires(sequences):
    """Afficher un tableau formaté des paires de dinucléotides par séquence"""
    print("\n=== Tableau des Paires de Dinucléotides par Séquence ADN ===")
    print()
    
    # En-tête du tableau
    print("+" + "-" * 78 + "+")
    print("| {:^10} | {:^8} | {:^10} | {:^10} | {:^10} | {:^8} | {:^8} |".format(
        "Séquence", "Longueur", "Paires AT", "Paires GC", "Total", "%AT", "%GC"))
    print("+" + "-" * 78 + "+")
    
    # Données du tableau
    for i, seq in enumerate(sequences):
        gc_pct, at_pct, cg, gc, at, ta = analyser_adn(seq)
        
        nom_seq = f"Séq {i+1}"
        longueur = len(seq)
        paires_at = at + ta
        paires_gc = cg + gc
        total_paires = paires_at + paires_gc
        
        print("| {:^10} | {:^8} | {:^10} | {:^10} | {:^10} | {:^8.2f} | {:^8.2f} |".format(
            nom_seq, longueur, paires_at, paires_gc, total_paires, at_pct, gc_pct))
    
    print("+" + "-" * 78 + "+")
    print()

def afficher_details_analyse(sequences):
    """Afficher les détails de l'analyse pour chaque séquence"""
    print("=== Analyse des Dinucléotides ADN ===")
    print()
    
    for i, seq in enumerate(sequences):
        gc_pct, at_pct, cg, gc, at, ta = analyser_adn(seq)
        
        print(f"Séquence {i+1}: {seq}")
        print(f"Longueur: {len(seq)} nucléotides")
        print(f"Dinucléotides (sans chevauchement):")
        print(f"  CG: {cg}, GC: {gc} → Total paires GC: {cg + gc}")
        print(f"  AT: {at}, TA: {ta} → Total paires AT: {at + ta}")
        print(f"Pourcentages:")
        print(f"  Paires GC (CG+GC): {gc_pct:.2f}%")
        print(f"  Paires AT (AT+TA): {at_pct:.2f}%")
        print("-" * 50)

# Programme principal
if __name__ == "__main__":
    try:
        # Lire le fichier DNAFile.txt
        sequences = lire_fichier_adn('DNAFile.txt')
        
        if sequences:
            print(f"Fichier DNAFile.txt lu avec succès. {len(sequences)} séquences trouvées.")
            
            # Afficher l'analyse détaillée
            afficher_details_analyse(sequences)
            
            # Afficher le tableau des paires
            afficher_tableau_paires(sequences)
            
            # Créer les graphiques
            print("Création des graphiques...")
            visualiser_adn(sequences)
        else:
            print("Aucune séquence trouvée dans DNAFile.txt")
            
    except FileNotFoundError:
        print("Erreur: Le fichier DNAFile.txt n'a pas été trouvé dans le dossier courant.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")