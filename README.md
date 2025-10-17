# Willy Wandji — Cloud & Data Portfolio

Bienvenue sur mon portfolio **Cloud & Data** : Data Wrangling (Python/Pandas), **SAP Analytics Cloud**, **Power BI**, et premiers pas **Azure**.

## 🧭 Contenu
- `data/` — Jeux de données synthétiques (LaundryFlow & Ayoka)
- `notebooks/` — Analyses et KPI (Matplotlib sans styles personnalisés)
- `dashboards/` — Guides SAP SAC & Power BI (ajoutez vos captures)
- `src/` — Scripts utilitaires + exemple d'upload Azure
- CI GitHub Actions — exécute le notebook principal à chaque push

## 🔥 Démarrer
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## 🧩 Projets inclus
- **LaundryFlow Analytics** : KPI (CA, panier moyen, délai de livraison), courbes hebdo
- **Ayoka Kitchen Analytics** : ventes par plat, par ville, satisfaction

## ☁️ Azure (optionnel)
Voir `src/azure_upload.py` (ne mettez jamais vos secrets dans Git).