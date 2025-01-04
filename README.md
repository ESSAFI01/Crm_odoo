# Module Personnalisé CRM Odoo

## Aperçu
Ce module étend les fonctionnalités du CRM d'Odoo en automatisant des processus clés et en améliorant la gestion des relations clients. Il offre les fonctionnalités suivantes :
- **Archivage automatique des opportunités** après 30 jours.
- **Envoi automatique de rappels par e-mail** aux clients et aux commerciaux.
- **Collecte de feedback client** via un questionnaire après la finalisation des activités.

---

## Fonctionnalités
1. **Archivage automatique des opportunités** :
   - Archive automatiquement les opportunités 30 jours après leur création.
   - Paramétrable depuis les paramètres du module.

2. **Rappels automatiques par e-mail** :
   - Envoie des rappels aux jours 7, 15 et 30.
   - E-mails personnalisables avec des champs dynamiques.

3. **Questionnaire de feedback** :
   - Génère un formulaire de feedback pour les clients après la finalisation d'une activité.
   - Enregistre les réponses pour analyse et reporting.

---

## Installation
1. Clonez le dépôt ou copiez le module dans le répertoire `addons` de votre instance Odoo :
   ```bash
   git clone <url-du-depot> /chemin/vers/odoo/addons/odoo_crm_custom_module
