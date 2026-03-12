# 🧠 Brain Tumor MRI Classification Challenge

<div align="center">

![Brain MRI](https://img.shields.io/badge/Task-Multi--Class%20Classification-blue)
![Classes](https://img.shields.io/badge/Classes-4-green)
![Images](https://img.shields.io/badge/MRI%20Images-7023-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Can you detect brain tumors from MRI scans?**

[📊 Leaderboard](#-leaderboard) • [📁 Dataset](#-dataset) • [🚀 Quick Start](#-quick-start) • [📤 How to Submit](#-submission-process) • [🔒 Security](#-security-system)

</div>

---

## 🏆 Leaderboard

| User              |   Score1 (Accuracy) |   Score2 (F1) |
|:------------------|--------------------:|--------------:|
| 🥇 Binta & Badele |                0.88 |          0.91 |
| 🥈 Gedeon & James |                0.85 |          0.89 |

> 📣 The leaderboard is automatically updated via **GitHub Actions** after each valid submission.
> Full history: [`leaderboard/leaderboard.csv`](leaderboard/leaderboard.csv)

---

## 📋 Project Overview

### The Mission
Classify brain MRI images into **4 categories**:

| Label | Tumor Type | Description |
|-------|-------|-------------|
| `0` | `glioma` | Glioma — arises from glial cells |
| `1` | `meningioma` | Meningioma — arises from the meninges |
| `2` | `no_tumor` | Healthy Brain — no tumor detected |
| `3` | `pituitary` | Pituitary Adenoma — in the pituitary gland |

---

## 📁 Dataset

**Source**: [Brain Tumor MRI Dataset — Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

- **Total**: 7,023 MRI images
- **Format**: JPEG, variable sizes

---

## 🚀 Quick Start Guide

### 1. Installation
```bash
git clone https://github.com/Ogoun09gerbad/Brain_Cancer.git
cd Brain_Cancer
pip install pandas cryptography tabulate scikit-learn
```

### 2. Encrypt your result
Use the official encryption script with the public key:
```bash
python3 encryption/encrypt.py your_predictions.csv public_key.pem submissions/your_team_name.enc
```

### 3. Submit
```bash
git add submissions/your_team_name.enc
git commit -m "New submission"
git push origin main
```

---

## 🔒 Security System (RSA)

This challenge uses an **end-to-end** encryption pipeline to protect results and ensure fair competition.

---

<div align="center">
<sub>Challenge powered by <b>GitHub Actions</b> • Created by <b>Binta & Badélé</b></sub>
</div>
