import pandas as pd
import os

def update():
    try:
        # 1. Lire le résultat qui vient d'être décrypté
        with open("leaderboard/last_result.csv", "r") as f:
            data = f.read().strip().split(',')
        
        user = data[0]
        score1 = float(data[1])
        score2 = float(data[2])

        # 2. Charger ou créer le leaderboard
        lb_path = "leaderboard/leaderboard.csv"
        if os.path.exists(lb_path):
            df = pd.read_csv(lb_path)
        else:
            df = pd.DataFrame(columns=["User", "Score1", "Score2"])

        # 3. Ajouter le nouveau score et trier
        new_row = pd.DataFrame([{"User": user, "Score1": score1, "Score2": score2}])
        df = pd.concat([df, new_row], ignore_index=True)
        df = df.sort_values(by="Score1", ascending=False).drop_duplicates(subset=["User"], keep='first')
        
        # 4. Sauvegarder
        df.to_csv(lb_path, index=False)
        
        # 5. Mettre à jour le README
        with open("README.md", "w") as f:
            f.write("# 🏆 Brain Tumor Challenge Leaderboard\n\n")
            f.write(df.to_markdown(index=False))
        
        print("✅ Leaderboard et README mis à jour !")
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        exit(1)

if __name__ == "__main__":
    update()
