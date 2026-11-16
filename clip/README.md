# Flux de versions Zeus Clip

Le site Zeus Clip lit `latest.json` et affiche le téléchargement uniquement quand `available` vaut `true` et que `download_url` contient l’URL de l’archive publiée.

## Publier une version

1. Préparer `ZeusClip-<version>-Windows-x64.zip`. L’archive inclut le dossier compilé, `setup/Installer-Zeus-Clip.ps1`, `setup/Desinstaller-Zeus-Clip.ps1` et `Installer Zeus Clip.bat`.
2. Créer une release GitHub dans `hackgaming82/zeus-updates` avec le tag `zeus-clip-v<version>` et joindre l’archive.
3. Le workflow `zeus-clip-release-feed.yml` met à jour ce flux. La page de téléchargement affiche alors automatiquement la nouvelle version, le poids et le hash si GitHub le fournit.

Le flux Zeus Clip est indépendant des clés et des versions des autres logiciels Zeus, même s’il réside dans le dépôt public commun des mises à jour.

