Smart Agence: Application de Gestion de Clients pour une Agence
Description du Projet Smart Agence est une application web complète
conçue pour aider les agences à gérer efficacement leurs agents, les
tickets clients et le suivi des activités associées. Le projet est
divisé en deux parties principales : une API robuste développée avec
FastAPI pour la gestion des données, et une interface utilisateur
intuitive construite avec React et TypeScript, stylisée avec Tailwind
CSS. La base de données utilisée pour le stockage des informations est
MongoDB. Fonctionnalités Clés \* Gestion des Agents : Permet d\'ajouter,
de modifier et de supprimer les profils des agents de l\'agence. \*
Gestion des Tickets Clients : Création, suivi et mise à jour des tickets
soumis par les clients. \* Suivi des Activités : Enregistrement et
visualisation des actions et des progrès liés au traitement des tickets.
\* API RESTful : Une interface backend puissante pour toutes les
opérations de données. \* Interface Utilisateur Réactive : Une
expérience utilisateur fluide et moderne pour la gestion quotidienne.
Technologies Utilisées Backend \* FastAPI (Python) : Framework web pour
la création d\'APIs rapides et robustes. \* Prisma : ORM nouvelle
génération (bien que pour MongoDB, une autre librairie Python sera
utilisée en parallèle ou à la place de Prisma si Prisma ne supporte pas
MongoDB directement). \* MongoDB : Base de données NoSQL pour le
stockage des données. Frontend \* React (TypeScript) : Bibliothèque
JavaScript pour la construction d\'interfaces utilisateur. \* TypeScript
: Sur-ensemble de JavaScript qui ajoute le typage statique. \* Tailwind
CSS : Framework CSS utilitaire pour un stylisme rapide et
personnalisable. Prérequis Assurez-vous d\'avoir les éléments suivants
installés sur votre machine : \* Node.js (version 18 ou supérieure) \*
Python 3 (version 3.x) \* Un environnement virtuel Python (recommandé)
Installation Le projet est divisé en deux dépôts distincts pour le
backend et le frontend. 1. Cloner les Dépôts Clonez les deux dépôts Git
sur votre machine locale : \* Backend (API FastAPI) : git clone
https://github.com/ibracciano/smart_agence.git cd smart_agence

\* Frontend (Interface Utilisateur React) : git clone
https://github.com/ibracciano/smart_agence_frontend.git cd
smart_agence_frontend

2\. Configuration du Backend  1. Naviguez vers le dossier du backend :
cd smart_agence

2. Créez et activez un environnement virtuel Python : python3 -m venv
venv source venv/bin/activate \# Sur Linux/macOS \# ou \#
venv\\Scripts\\activate \# Sur Windows

3. Installez les dépendances Python : pip install -r requirements.txt

4. Générez le client Prisma : npx prisma generate

Note : Assurez-vous d\'avoir npm ou yarn installé pour npx. 5.
Configurez votre base de données MongoDB : Créez un fichier .env à la
racine de votre dossier smart_agence et ajoutez votre URL de connexion
MongoDB : MONGODB_URL=\"mongodb://localhost:27017/smart_agence_db\" \#
Ou votre URL de connexion à un service MongoDB cloud (ex: MongoDB Atlas)

3\. Configuration du Frontend  1. Naviguez vers le dossier du frontend :
cd smart_agence_frontend

2. Installez les dépendances Node.js : npm install npm i
\@tanstack/react-query \@tanstack/react-query-devtools lucide-react
react-hot-toast react-router-dom recharts \# ou \# yarn install \# yarn
add \@tanstack/react-query \@tanstack/react-query-devtools lucide-react
react-hot-toast react-router-dom recharts

3. Configurez l\'URL de l\'API Backend : Créez un fichier .env (ou
.env.local) à la racine de votre dossier smart_agence_frontend et
définissez l\'URL de votre backend FastAPI :
VITE_API_BASE_URL=http://localhost:8000 \# Ajustez le port si votre
backend s\'exécute sur un autre port

Utilisation 1. Lancer le Backend Depuis le dossier smart_agence (avec
l\'environnement virtuel activé) : uvicorn main:app \--reload

L\'API sera accessible à l\'adresse http://localhost:8000 (ou le port
spécifié). La documentation Swagger UI sera disponible à
http://localhost:8000/docs. 2. Lancer le Frontend Depuis le dossier
smart_agence_frontend : npm run dev \# ou \# yarn dev

L\'interface utilisateur sera accessible à l\'adresse
http://localhost:5173 (ou le port indiqué par votre terminal). Liens des
Dépôts \* Backend : https://github.com/ibracciano/smart_agence.git \*
Frontend : https://github.com/ibracciano/smart_agence_frontend.git
Contribution Les contributions sont les bienvenues ! Veuillez suivre les
étapes suivantes :  1. Forker le dépôt. 2. Créer une nouvelle branche
(git checkout -b feature/nouvelle-fonctionnalite). 3. Effectuer vos
modifications. 4. Commiter vos changements (git commit -m \'Ajout d\'une
nouvelle fonctionnalité\'). 5. Pousser vers la branche (git push origin
feature/nouvelle-fonctionnalite). 6. Ouvrir une Pull Request. Licence Ce
projet est sous licence \[Spécifiez votre licence ici, par exemple MIT,
Apache 2.0, etc.\].
