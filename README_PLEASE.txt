Pour tout les script marche sans probleme on a besion des bibiotheques suivant
- PYTHON 3.6
les bibiotheque : numpy, pickle, tensorflow 12, keras, pyqt5
pour les installer
par cmd
- pip -m pip install --upgrade pip
- pip install numpy
- pip install pickle
- pip install tensorflow
- pip install keras
- pip install pyqt5

l'executable marche sans l'installation de python et sans l'installation d'aucun bibiotheque.

dossier models : contient tout les models tester. 

dossier dataset : contient le dataset et les donnees apres preprocessing

dossier gui : contient le code source de l'application 'l'executable'

dossier logs : contient les graphs des reseaux de neuron pour determiner le meilleur reseau
	       pour visualiser les graph on doit tapez cette commande sur cmd
		tensorboard --logdir=path/to/log-directory

dossier netlog : comme logs mais contient les graphs de meilleur reseaux avec dropout et sans dropout
		 tensorboard --logdir=path/to/log-directory

100_leaves-layersize128-layercount2 : c'est le meilleur model apres l'apprentissage avec dropout avec apprentissage de 500 epochs

bestnet.py : le script qui lance beaucoup de reseau de neurons

net.py : le script d'apprentissage final

testnet.py : le script qui test le reseau de neuron avec les donnees de test calcule accuracy

preprocessing : le script qui fait preprocessing a le dataset	



Etudiant : Hadjerci Med Allaeddine