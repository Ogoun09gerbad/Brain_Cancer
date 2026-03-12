import pandas as pd
import re
import os

def update_readme():
    csv_path = 'leaderboard/leaderboard.csv'
    if not os.path.exists(csv_path):
        print("Erreur : Fichier CSV introuvable")
        return

    # Lire les scores réels
    df = pd.read_csv(csv_path)
    
    # Trier par le premier score (Accuracy)
    df = df.sort_values(by=df.columns[1], ascending=False)
    
    # Générer le tableau Markdown
    markdown_table = df.to_markdown(index=False)
    
    # Lire le README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacer la section Leaderboard
    # On cherche entre le titre Leaderboard et la suite
    pattern = r"(## 🏆 Leaderboard\n\n)(.*?)(?=\n\n> 📣)"
    if re.search(pattern, content, flags=re.DOTALL):
        new_content = re.sub(pattern, r"\1" + markdown_table, content, flags=re.DOTALL)
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README mis à jour avec succès !")
    else:
        print("⚠️ Balise Leaderboard non trouvée dans le README")

if __name__ == "__main__":
    update_readme()
