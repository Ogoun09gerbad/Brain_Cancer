# 🧠 Brain Tumor MRI Classification Challenge

<div align="center">

![Brain MRI](https://img.shields.io/badge/Task-Multi--Class%20Classification-blue)
![Classes](https://img.shields.io/badge/Classes-4-green)
![Images](https://img.shields.io/badge/MRI%20Images-7023-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Pouvez-vous détecter les tumeurs cérébrales à partir d'IRM ?**

[📊 Leaderboard](#-leaderboard) • [📁 Dataset](#-dataset) • [🚀 Quick Start](#-quick-start) • [📤 How to Submit](#-submission-process) • [🔒 Security](#-security-system)

</div>

---

## 🏆 Leaderboard

| User | Score1 (Accuracy) | Score2 (F1) |
|:---|:---|:---|
| 🥇 **Binta** | **0.88** | **0.91** |
| 🥈 — | — | — |
| 🥉 — | — | — |

> 📣 Le classement est mis à jour automatiquement via **GitHub Actions** après chaque soumission valide.
> Historique complet : [`leaderboard/leaderboard.csv`](leaderboard/leaderboard.csv)

---

## 📋 Présentation du Projet

### La Mission
Classifier des images IRM cérébrales en **4 catégories** :

| Label | Type de Tumeur | Description |
|-------|-------|-------------|
| `0` | `glioma` | Gliome — se développe dans les cellules gliales |
| `1` | `meningioma` | Méningiome — se développe dans les méninges |
| `2` | `no_tumor` | Cerveau Sain — aucune tumeur détectée |
| `3` | `pituitary` | Adénome hypophysaire — dans l'hypophyse |

---

## 📁 Dataset

**Source**: [Brain Tumor MRI Dataset — Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

- **Total** : 7 023 images IRM
- **Format** : JPEG, tailles variables

---

## 🚀 Guide de démarrage rapide

### 1. Installation
```bash
git clone https://github.com/Ogoun09gerbad/Brain_Cancer.git
cd Brain_Cancer
pip install pandas cryptography tabulate scikit-learn
```

### 2. Chiffrer votre résultat
```bash
python3 simple_encrypt.py
```

### 3. Soumettre
```bash
git add submissions/baseline.enc
git commit -m "Nouvelle soumission"
git push origin main
```

---

## 🔒 Système de Sécurité (RSA)

Ce challenge utilise un pipeline de chiffrement **bout-en-bout** pour protéger les résultats.

---

<div align="center">
<sub>Challenge propulsé par <b>GitHub Actions</b> • Créé par <b>Binta</b></sub>
</div>
