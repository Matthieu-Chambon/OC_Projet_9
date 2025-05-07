# 📚 Projet 9 - Développez une application Web en utilisant Django

## 📝 Description

**LITRevu** est une application web communautaire dédiée à la critique littéraire. Développée avec **Django**, elle permet à ses utilisateurs de **partager**, **lire** et **solliciter** des critiques de livres ou d’articles.

Chaque utilisateur peut :

- 🧾 Créer un **billet** pour demander une critique
- ✍️ Publier une **critique**, soit en réponse à un billet existant, soit spontanément
- 👥 **Suivre d'autres utilisateurs** pour accéder à leurs publications dans un **flux personnalisé**

🔧 Le projet respecte les bonnes pratiques du framework **Django** et les recommandations **PEP8** pour garantir une qualité de code professionnelle.

---

## 🖥️ Fonctionnalités

### 🔓 Utilisateur non connecté

- 📝 **Inscription** à la plateforme
- 🔐 **Connexion** à un compte existant

### 🔐 Utilisateur connecté
 
- 📰 Un flux personnalisé affiche

    - 🔁 Ses propres **billets** et **critiques**
    - 👤 Les billets et critiques des **utilisateurs suivis**
    - 💬 Les critiques des autres utilisateurs en **réponse à ses billets**

- ✏️ Création

    - 🧾 **Billet** (demande de critique)
    - 🗣️ **Critique** liée à un billet existant
    - 🚀 **Billet + critique** en une seule étape

- ⚙️ Gestion de contenu

    - 🗃️ **Modifier et supprimer** ses propres billets et critiques

- 👥 Gestion des abonnements

    - 🔍 **Suivre** un utilisateur via son nom d'utilisateur
    - 📋 **Lister** les utilisateurs suivis
    - ❌ **Se désabonner** d’un utilisateur

---

## 📥 Installation et exécution

### 1️⃣ Cloner le projet

```sh
cd "chemin/vers/dossier/souhaité/"
git clone https://github.com/Matthieu-Chambon/OC_Projet_9
```

### 2️⃣ Installer le projet

```sh
cd OC_Projet_9
python -m venv env
env\Scripts\activate  # Sous Windows
source env/bin/activate  # Sous Mac ou Linux
pip install -r requirements.txt
python manage.py migrate
```

### 3️⃣ Lancer le serveur

```sh
python manage.py runserver
```

### 4️⃣ Accéder à l’application

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠️ Technologies utilisées

* 🐍 **Python 3**
* 🌐 **Django**
* 🗃️ **SQLite** (base de données locale)
* 💻 **HTML / CSS**
* ⚙️ **JavaScript**

---

## ✅ Conformité

* ✅ Respect des bonnes pratiques **Django**
* ✅ Respect des normes **PEP8**
* ✅ Respect bonnes pratiques référentiel **WCAG**
* ✅ Base de données livrée (**db.sqlite3**)
