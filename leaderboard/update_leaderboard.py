import pandas as pd
import re

def update_readme():
    # 1. Lire les scores réels depuis le CSV
    df = pd.read_csv('leaderboard/leaderboard.csv')
    
    # 2. Trier par score (Accuracy) pour avoir le vrai classement
    df = df.sort_values(by=df.columns[1], ascending=False)
    
    # 3. Transformer le tableau en format Markdown
    markdown_table = df.to_markdown(index=False)
    
    # 4. Lire le README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 5. Remplacer l'ancien tableau par le nouveau
    # On cherche ce qui se trouve entre le titre Leaderboard et la suite
    new_content = re.sub(
        r"(## 🏆 Leaderboard\n\n)(.*?)(?=\n\n> 📣)", 
        r"\1" + markdown_table, 
        content, 
        flags=re.DOTALL
    )

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ README mis à jour avec les vrais scores du CSV !")

if __name__ == "__main__":
    update_readme()
