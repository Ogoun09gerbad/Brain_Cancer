import pandas as pd

def sync_readme():
    # 1. Lire les vrais scores
    df = pd.read_csv('leaderboard/leaderboard.csv')
    
    # 2. Trier par score (Accuracy)
    df = df.sort_values(by='Score1', ascending=False)
    
    # 3. Créer le tableau au format Markdown
    table = df.to_markdown(index=False)
    
    # 4. Lire le README actuel
    with open('README.md', 'r') as f:
        content = f.read()

    # 5. Remplacer la section entre deux balises (si tu en as) 
    # ou simplement reconstruire la section Leaderboard
    # Ici, on va juste s'assurer que le tableau est mis à jour
    print("Mise à jour du README avec les nouveaux scores...")
    # (Logique de remplacement de texte ici)

if __name__ == "__main__":
    sync_readme()
