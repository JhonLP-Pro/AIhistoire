# Générateur de Texte en Français avec GPT-2

Un générateur de texte simple utilisant un modèle GPT-2 pré-entraîné en français. Pour être précis, il utilise le modèle "asi/gpt-fr-cased-small" et ce programme génère des histoires de 200 caractères maximum.

## Prérequis

1. **Python** : Version 3.8-3.11
   - Téléchargez sur [python.org](https://www.python.org/downloads/)
   - ⚠️ Cochez "Add Python to PATH" pendant l'installation

2. **Bibliothèques Python** :
   ```bash
   # Pour CPU uniquement
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
   pip install transformers

   # Pour GPU (NVIDIA)
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install transformers
   ```

3. **Pour utiliser le GPU** (optionnel) :
   - Carte graphique NVIDIA
   - [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

## Installation

1. Téléchargez tous les fichiers dans un même dossier
2. Vérifiez l'installation :
   ```bash
   python verify_install.py
   ```

## Utilisation

1. Lancez le programme :
   ```bash
   python exemple_utilisation.py
   ```
2. Entrez votre texte de départ quand demandé (si jamais un chargement a lieu avant que vous puissiez entrer votre texte, c'est que le modèle est en train de charger. Vous pouvez écrire votre texte après que le processus de chargement soit terminé)
3. Le programme générera 3 versions différentes de votre histoire
4. Choisissez si vous voulez générer une nouvelle histoire

## Fichiers

- `text_generator.py` : Classe principale du générateur
- `exemple_utilisation.py` : Interface utilisateur
- `verify_install.py` : Vérification de l'installation 