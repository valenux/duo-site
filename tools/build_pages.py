import os, sys; sys.path.insert(0, os.path.dirname(__file__)); os.chdir(os.path.join(os.path.dirname(__file__), ".."))
from _page import page
page('confidentialite.html','Politique de confidentialité','Comment Duo collecte, utilise et protège vos données.','''
<h1>Politique de confidentialité</h1>
<p class="lead">Dernière mise à jour : 23 novembre 2026</p>

<div class="card">
<h2>En bref</h2>
<ul>
<li>Duo sert uniquement à partager vos dépenses, votre calendrier et votre liste de courses avec votre partenaire.</li>
<li>Vos données ne sont ni vendues, ni louées, ni utilisées pour de la publicité. Duo n'intègre aucun outil de suivi ou d'analyse publicitaire.</li>
<li>Seules les deux personnes d'un même duo voient leurs informations communes.</li>
<li>Vous pouvez supprimer votre compte et vos données à tout moment depuis l'app.</li>
</ul>
</div>

<div class="card">
<h2>Qui est responsable</h2>
<p>Duo est développée par Valentin Guilbert, à Montréal (Québec, Canada). Pour toute question sur vos renseignements personnels : <a href="mailto:info@duo-app.app">info@duo-app.app</a>. Cette personne agit comme responsable de la protection des renseignements personnels.</p>
</div>

<div class="card">
<h2>Les données que nous collectons</h2>
<ul>
<li><strong>Compte :</strong> votre adresse courriel, votre prénom et votre mot de passe (stocké chiffré, jamais lisible).</li>
<li><strong>Contenu que vous créez :</strong> dépenses (titre, montant, catégorie, date, qui a payé et la répartition), événements du calendrier, articles de la liste de courses, budget mensuel et remboursements.</li>
<li><strong>Lien entre partenaires :</strong> le duo auquel vous appartenez et le code d'invitation temporaire.</li>
<li><strong>Notifications :</strong> un identifiant technique d'appareil fourni par Apple pour vous envoyer des notifications, si vous les autorisez, ainsi que l'historique des notifications dans l'app.</li>
</ul>
<p>Duo ne collecte pas votre position, vos contacts, vos photos ni vos données bancaires. Les remboursements entre vous se font en dehors de l'app.</p>
</div>

<div class="card">
<h2>Pourquoi nous les utilisons</h2>
<ul>
<li>Faire fonctionner l'app : afficher et synchroniser vos informations entre vos deux iPhone.</li>
<li>Vous envoyer les courriels nécessaires au compte (confirmation, code de réinitialisation du mot de passe).</li>
<li>Prévenir votre partenaire d'un ajout (dépense, événement, course) et vous rappeler vos événements, selon vos réglages de notifications.</li>
</ul>
</div>

<div class="card">
<h2>Où sont stockées vos données</h2>
<p>Vos données sont hébergées par <strong>Supabase</strong> dans la région <strong>Canada (Centre)</strong>, à Montréal. Elles sont chiffrées pendant leur transfert et protégées par des règles d'accès : chaque compte ne peut lire que ses propres données et celles de son duo.</p>
<p>Prestataires utilisés pour faire fonctionner le service :</p>
<ul>
<li><strong>Supabase</strong> : base de données, authentification et envoi des notifications.</li>
<li><strong>Apple</strong> : distribution de l'app et acheminement des notifications push.</li>
<li><strong>IONOS</strong> : envoi des courriels liés au compte.</li>
<li><strong>GitHub</strong> : stockage des sauvegardes de la base de données, dans un dépôt privé.</li>
</ul>
<p>Ces prestataires traitent les données uniquement pour fournir leur service. Certains peuvent les traiter hors du Québec ; nous choisissons des prestataires qui offrent une protection adéquate.</p>
</div>

<div class="card">
<h2>Conservation et suppression</h2>
<p>Vos données sont conservées tant que votre compte existe. Depuis <em>Profil › Supprimer mon compte</em>, vous supprimez définitivement votre compte et vos données personnelles. Si vous quittez un duo, l'historique commun reste accessible à l'autre personne.</p>
<p>Une sauvegarde chiffrée lors de son transfert est réalisée chaque nuit pour pouvoir restaurer le service en cas de problème. Chaque sauvegarde est conservée 30 jours, puis effacée automatiquement : après la suppression d'un compte, ses données disparaissent donc aussi des sauvegardes au plus tard 30 jours plus tard.</p>
</div>

<div class="card">
<h2>Vos droits</h2>
<p>Conformément à la Loi 25 au Québec et aux lois canadiennes applicables, vous pouvez demander l'accès à vos renseignements, leur rectification, leur suppression ou la portabilité de vos données en écrivant à <a href="mailto:info@duo-app.app">info@duo-app.app</a>. Nous répondons dans un délai de 30 jours. Vous pouvez aussi vous adresser à la Commission d'accès à l'information du Québec.</p>
</div>

<div class="card">
<h2>Enfants</h2>
<p>Duo s'adresse aux adultes et n'est pas destinée aux moins de 14 ans.</p>
</div>

<div class="card">
<h2>Modifications</h2>
<p>Si cette politique change, la date en haut de la page sera mise à jour. En cas de changement important, vous en serez informé dans l'app.</p>
</div>
''')

page('aide.html','Aide et contact',"Questions fréquentes et contact pour l'app Duo.",'''
<h1>Aide et contact</h1>
<p class="lead">Une question, un souci ou une idée pour Duo ? Écris-nous, on répond en général sous 48 heures.</p>

<div class="card">
<h2>Nous écrire</h2>
<p>Courriel : <a href="mailto:info@duo-app.app">info@duo-app.app</a></p>
<a class="btn" href="mailto:info@duo-app.app?subject=Duo%20-%20Aide">Envoyer un courriel</a>
</div>

<div class="card">
<h2>Questions fréquentes</h2>
<details><summary>Comment inviter mon ou ma partenaire ?</summary>
<p>Après avoir créé ton compte, Duo affiche un code d'invitation valable 48 heures. Envoie-le à ton ou ta partenaire : il ou elle crée son compte, choisit « J'ai un code » et le saisit.</p></details>
<details><summary>J'ai oublié mon mot de passe.</summary>
<p>Sur l'écran de connexion, entre ton courriel puis appuie sur « Mot de passe oublié ? ». Tu reçois un code à 6 chiffres à saisir dans l'app, puis tu choisis un nouveau mot de passe. Pense à vérifier tes courriels indésirables.</p></details>
<details><summary>Je ne reçois pas les notifications.</summary>
<p>Vérifie dans Réglages › Notifications › Duo que les notifications sont autorisées, puis dans Duo › Profil › Notifications que les types voulus sont activés. Tu n'es jamais notifié de tes propres ajouts.</p></details>
<details><summary>Duo fait-il les virements entre nous ?</summary>
<p>Non. Duo calcule qui doit combien. Le remboursement se fait comme d'habitude (virement Interac, comptant…), puis tu le marques comme fait avec « Équilibrer ».</p></details>
<details><summary>Comment quitter un duo ou supprimer mon compte ?</summary>
<p>Dans Profil, en bas de l'écran : « Quitter le duo » dissocie vos comptes, « Supprimer mon compte » efface définitivement ton compte et tes données personnelles.</p></details>
<details><summary>Qui peut voir mes données ?</summary>
<p>Uniquement toi et la personne de ton duo. Consulte notre <a href="confidentialite.html">politique de confidentialité</a> pour le détail.</p></details>
</div>
''')
