import os
import discord as dc
import json
from discord.ext import commands
import random as rd

debug = 2 # Définit le niveau de messages sur le terminal (jusqu'à 2 pour un max d'infos)
logs = 1 # Aucune influence (flemme)

initPath = os.getcwd()
print(initPath)
#initPath = "/home/nod2/Desktop/VTTFounwet"
os.chdir(initPath)

with open("data.json", "r") as f :
	data = json.load(f)

TOKEN = data["TOKEN"] # Token du bot
CHANNELID = data["CHANNEL_ID"] # Salon de messages d'up du bot
CHANNLOGID = data["CHANNLOG_ID"] # Salon de logs
SUPPORTLINK = data["SUPPORT_LINK"] # Lien d'aide pour bot
DEVID = data["DEV_ID"]
prefix = data["PREFIX"]
prefix = data["TESTS_PREFIX"]

ver = "V1.6"

V = f'''
**{ver}**\n
Version opérationnelle pour la plupart des commandes.\n
Refonte et ajout de fonctions pour la commande `{prefix}r`
'''

bot = commands.Bot(command_prefix=prefix, intents=dc.Intents.all())
bot.remove_command('help')
print(initPath)


@bot.command(pass_context = True)
async def help(ctx, command = ''):
	
	if command == '' :
		message = f"""Bonjour, jeune brebis en quête de réponses ! :sheep:
Si tu as essayé cette commande, c'est que tu dois probablement être perdu.
Voici donc une petite liste des différentes informations que je peux te proposer :

`{prefix}help bot`
Te donne des informations générales sur le bot :robot:

`{prefix}help commands`
Affiche la liste des commandes possibles

`{prefix}help attributs`
Explique le fonctionnement des différents types d'attributs (normaux, 'DEG' et 'JAU')

`{prefix}help support`
Te donne un lien pour aller me poser directement tes questions (je te mangerai pas :eyes:)
"""
	
	elif command == 'bot' :
		message = f"""Tu veux des infos sur moi ? :face_with_peeking_eye:
Alors voilà :
Je suis un petit bot tout mignon créé par <@{DEVID}> à des fins de gestion de personnages et stats pour du TTRPG.
Fatigué des VTT style Foundry ou Roll20 qui sont peu/pas adaptés à mon support de prédilection (iPad), il (le dev) a décidé de coder un petit programme en python pour simplifier la vie de certains joueurs sur Discord.

Je ne conviendrai certainement pas à tous ; j'ai encore de nombreux défauts, que le dev essaie (ou pas) de régler, update après update. Je suis donc une proposition alternative aux incroyables bots comme Avrae ou DiceParser, pour ceux qui veulent essayer  :D
"""
	
	elif command == 'attributs' :
		message = f"""## Types d'attributs
Plusieurs commandes de ce bot  (comme '{prefix}charsave' ou '{prefix}rm') manipulent plusieurs types d'attributs différents, tels que 'DEG' et 'JAU'.
Mais qu'est-ce qui les différencie des attributs classiques ?
Peu de choses, en fait.

Ils sont simplement traités différemment par les commandes d'appel.

Les attributs "normaux" sont des attributs qui sont liés à une valeur numérique ainsi qu'à un "type de dé" (comme du d6, d20, d100 etc).
En voici un exemple :
`Attribut 65 100`
Quand tu demanderas au programme de faire un jet de dé avec cet attribut, il lancera un dé à 100 faces et comparera la valeur obtenue avec la valeur de la stat.
C'est un attribut "simple", qui sert à dire si ton jet de dé est réussi ou non.

Les attributs de type 'DEG' ('DEG' pour 'dégâts') n'ont pas le même genre de valeurs que les attributs normaux :
Là où les attributs normaux ont une valeur et un type de dé, les attributs 'DEG' ont un type et un NOMBRE de dés, ainsi qu'une valeur optionnelle qui permet de leur donner un bonus ou un malus.
Exemple :
`DEGAttribut 6 3 2`
Cet attribut se nommera 'Attribut' (le 'DEG' n'est là que pour définir le type, même s'il est obligatoire de l'écrire lors de la création ou modification du personnage).
En écrivant ainsi, on donne à l'attribut 'Attribut' une valeur de **3**d**6** +**2** (lance trois dés à six faces et ajoute 2. Note que le nombre de faces de chaque dé se place avant la quantité de dés, pour les attributs 'DEG').
Cet attribut commence par les caractères `DEG` ; c'est avec ces trois premières lettres qu'il faut les nommer quand tu voudras ajouter un attribut de type 'DEG' à ton personnage. Si tu l'enregistres de cette manière, le programme le stockera comme étant de type 'DEG', et tu pourras ensuite l'appeler avec '{prefix}rm' (par exemple) sans écrire le 'DEG'.
Ces attributs servent à obtenir l'addition de plusieurs jets de dés, sans les comparer à quoi que ce soit.

Les attributs de type 'JAU' (pour 'jauge') sont des attributs que tu pourras modifier à tout moment.
Ils possèdent une "valeur actuelle" et une "valeur maximale":
Exemple :
`JAUpv 10 10 -3`
Cet attribut portera le nom 'pv' et aura une valeur actuelle égale à sa valeur maximale, 10 En revanche, sa valeur minimale sera de -3.
Cela signifie que tu pourras faire varier cet attribut dans une plage allant de -3 à 10, via la commande '{prefix}mod'. Ces stats ne sont PAS destinées à être utilisées avec des commandes de type '{prefix}rm' ou '{prefix}rr', mais cela reste possible. À noter que cela reviendrait à utiliser une stat "normale", car les commandes sus-mentionnées ne font pas la distinction entre les stats 'JAU' et normales.

## Définir un type d'attribut
Il suffit d'enregistrer ton personnage en collant `DEG` ou `JAU` au début de l'attribut en question.
N'oublie pas d'adapter les valeurs que tu donnes à ces attributs !

Une fois définis comme appartenant à un certain type, tes attributs peuvent être appelés en omettant le `DEG` ou `JAU` dans leur nom. Attention tout de même à ne pas empiéter sur un autre attribut qui porterait le même nom.
"""
	
	elif command == 'support' :
		message = f"""Voici le lien qui te permettra d'accéder à mon serveur de test et développement :

{SUPPORTLINK}

C'est pas très bien rangé mais au moins j'y réponds  :)
"""
	
	elif command == 'commands' :
		message = f"""## Liste des commandes disponibles :
**{prefix}selfid**
sans argument
Renvoie ton pseudonyme et ID d'utilisateur Discord.

**{prefix}vers**
sans argument
Donne la version actuelle du bot

**{prefix}merlin**
Recharge le personnage d'exemple dans ton dossier

**{prefix}signup**
sans argument
Te crée un dossier de sauvegarde afin d'enregistrer tes prochains personnages.

**{prefix}charsave**
<nom>  <déParDéfaut>  
<stat1>  <valeurStat1>  <(déSpécifique)>
<stat2>  <valeurStat2>  <(déSpécifique)>
...
<DEGstat12>  <typeDé12>  <(nbDé12)> <(bonus/malus)>
...
<('OVW')>
Enregistre ton personnage ainsi que ses stats. Aucune limite de stat n'est imposée, mais essaye de rester raisonnable  :D

**{prefix}charlist**
sans argument
Affiche la liste de tes personnages

**{prefix}charsel**
<nom>
Sélectionne le personnage que tu souhaites jouer

**{prefix}charsee**
<(nom)>
Affiche les informations du personnage indiqué (ou du personnage sélectionné si aucun personnage n'a été indiqué)

**{prefix}charedit**
<(nom)>
Te permet de modifier le personnage indiqué (ou ton personnage sélectionné si aucun personnage n'a été indiqué)

**{prefix}chardelete**
<nom>
Supprime le personnage indiqué :warning:**ATTENTION**:warning: aucune confirmation de suppression n'est demandée !!

**{prefix}rm**
**{prefix}rr**
<stat>  <(bonus/malus)>
Lance un dé d'attribut et te dit si le jet est réussi ou échoué. '{prefix}rm' te dira l'écart de réussite ou d'échec, et '{prefix}rr' te dira le résultat du dé

**{prefix}r**
<dés> <(bonus/malus)>
Lance un ou plusieurs dés et renvoie le résultat

**{prefix}mod**
<stat>  <('y')>
Modifie un attribut de type 'JAU', comme par exemple les PVs d'un personnage
(Réfère-toi à `{prefix}help attributs` pour comprendre le type 'JAU')

> Tape `{prefix}help <commande>` pour une explication plus complète !
"""
	
	elif command == "vers" or command == f"{prefix}vers" :
		message = f"""## {prefix}vers
Te dit quelle version du bot est en ligne et quelles sont ses améliorations depuis la version précédentes

syntaxe :

`{prefix}vers`
"""
	
	elif command == "selfid" or command == f"{prefix}selfid" :
		message = f"""## {prefix}selfid
La commande '{prefix}selfid' te permet d'afficher ton nom d'utilisateur ainsi que ton ID dans le salon où tu appelleras la commande.
C'est honnêtement pas très utile, mais on sait jamais...

syntaxe :

`{prefix}selfid`
"""
	
	elif command == "signup" or command == f"{prefix}signup" :
		message = f"""## {prefix}signup
'{prefix}signup' crée un dossier à ton nom dans les fichiers du bot. Ce dossier ne peut être ouvert que par :
- toi
- moi (le dev)
- le bot (mais il ne l'ouvrira que pour toi)
- le vilain magicien chanteur qui hante chaque dossier
Ce dossier te permettra de stocker des fichiers de type '.json' afin d'enregistrer tes personnages.
Quand tu feras 'signup' pour la première fois, deux fichiers seront également créés (.json également) :

Le premier sera utilisé pour enregistrer le nom du personnage que tu as sélectionné afin de pouvoir le retrouver rapidement.

Le deuxième est un fichier de personnage que tu pourras utiliser pour faire des tests.


(Le nom peut porter à confusion, mais cette commadne est gratuite !)

syntaxe :

`{prefix}signup`
"""

	elif command == "merlin" or command == f"{prefix}merlin" :
		message = f"""## {prefix}merlin
Recharge ton personnage "Merlin le chanteur" et le met à jour.
Attention : si tu as déjà un personnage portant ce nom, il sera écrasé.

syntaxe :

`{prefix}merlin`
"""

	elif command == "charsave" or command == f"{prefix}charsave" :
		message = f"""## {prefix}charsave
La commande '{prefix}charsave' est la commande centrale du programme.
Via une syntaxe assez précise, elle permet de créer un fichier .json qui stockera les valeurs données sous forme de personnage.

syntaxe :

```{prefix}charsave "Merlin le Chanteur" 20
URL=https://<URL>
For 8
Amour 13 
Magie 78 100
DEGSortilège 6 3 4
DEGLance 10 2 -1
JAUPV 23 25
OVW```

Cette commande enregistrera le personnage nommé Merlin le Chanteur, qui jouera avec un d20.
L'URL de son illustration est ajouté à la deuxième ligne
Son premier attribut est la For et sa valeur est 8.
Son deuxième attribut est l'Amour, avec une valeur de 13.
Son troisième attribut est la Magie, dont la valeur est de 78 ; mais cet attribut se joue au d100 au lieu du d20 réglé par défaut.
Il possède deux attributs de type DEG (= dégâts) :
L'attribut Sortilège, dont le dé est de 3d6+4, et l'attribut Lance avec une valeur de 2d10-1.
Il a également un attribut de type JAU (= jauge) :
L'attribut PV, qu'il est possible de modifier avec '{prefix}mod'.
(Les attributs de type DEG sont enregistrés en écrivant DEG<attribut> et peuvent être appelés soit via DEG<attribut> soit par <attribut>. Tape '{prefix}help rm' pour plus d'informations sur les appels d'attributs)
L'argument OVW est facultatif ; il permet de forcer l'enregistrement et d'écraser une potentielle ancienne sauvegarde du même personnage.
(Des guillemets sont nécessaires si le nom ou un attribut de ton personnage comporte des espaces)
"""
	
	elif command == "docs" or command == f"{prefix}docs" :
		message = f"""Voici l'URL de Merlin le Chanteur :
https://media.discordapp.net/attachments/1210647216155525130/1216171097393856673/IMG_2886.jpg?ex=65ff6a98&is=65ecf598&hm=cbcc9870a6cb9991f00bfcd3d17e3ff89f2616ffb73e3e666e63bc46b6f974ca&=&format=webp&width=442&height=425
"""

	elif command == "charlist" or command == f"{prefix}charlist" :
		message = f"""## {prefix}charlist
En écrivant '{prefix}charlist', tu demandes au bot de t'afficher la liste de tes personnages. Il ne te dira que leur nom, pas leur attributs

syntaxe :

`{prefix}charlist`
"""
		
	elif command == "charsel" or command == f"{prefix}charsel" :
		message = f"""## {prefix}charsel
La commande '{prefix}charsel' te permet de sélectionner le personnage avec lequel tu veux jouer. Le programme enregistrera ton choix et s'en souviendra jusqu'à ce que tu le changes manuellement

syntaxe :

`{prefix}charsel "Merlin le Chanteur"`

Cette commande définira Merlin le Chanteur en tant que ton personnage actif.
(Les guillemets sont nécessaires si le nom de ton personnage comporte un ou plusieurs espaces)
"""
	
	elif command == "charsee" or command == f"{prefix}charsee" :
		message = f"""## {prefix}charsee
'{prefix}charsee' est une commande assez utile :
Elle permet de voir la liste d'attributs de votre personnage.

Si tu as déjà sélectionné un personnage, la commande '{prefix}charsee' n'a pas besoin d'argument. Par défaut, elle t'affichera le personnage que tu as sélectionné.
Si tu veux voir un autre de tes personnages ou que tu n'as pas encore sélectionné un personnage par défaut, tu vas devoir écrire le nom exact du personnage à afficher.

syntaxe :

`{prefix}charsee "Merlin le Chanteur"`

Cette commande affichera le personnage nommé Merlin le Chanteur ainsi que ses attributs.
(Les guillemets sont nécessaires si le nom de ton personnage comporte des espaces)
"""
	
	elif command == "charedit" or command == f"{prefix}charedit" :
		message = f"""## {prefix}charedit
Avec '{prefix}charedit', tu peux modifier ton personnage, ajouter ou supprimer des attributs ou créer une copie de ton personnage avec un autre nom.
Elle te renverra un message sous format texte commençant par '{prefix}charsave' ; tu n'auras qu'à copier, modifier puis renvoyer le message ua bot, et il enregistrera ton nouveau personnage.
Si tu laisses le même nom, l'ancien personnage sera écrasé. Sinon, il créera un nouveau fichier portant le nom que tu auras choisi.

Si tu as déjà sélectionné un personnage, la commande '{prefix}charedit' n'a pas besoin d'argument. Par défaut, elle te donnera le personnage que tu as sélectionné.
Si tu veux éditerr un autre de tes personnages ou que tu n'as pas encore sélectionné un personnage par défaut, tu vas devoir écrire le nom exact du personnage à modifier.

syntaxe :

`{prefix}charedit "Merlin le Chanteur"`

Cette commande t'enverra le message d'enregistrement de Merlin le Chanteur.
(Les guillemets sont nécessaires si le nom de ton personnage comporte des espaces)
"""
		
	elif command == "chardelete" or command == f"{prefix}chardelete" :
		message = f"""## {prefix}charedit
Fais TRES ATTENTION avec cette commande !!
'{prefix}chardelete' supprime définitivement ton personnage, sans avertissement ou confirmation de suppression.
Elle te renverra tout de même quelques attributs de ton personnage, afin que tu puisses le réenregistrer si besoin, mais ça n'est pas optimal. Je te conseille plutôt de charger le message d'enregistrement de ton personnage avec '{prefix}charedit' si tu veux le garder quelque part.

syntaxe :

`{prefix}chardelete "Merlin le Chanteur"`

Cette commande SUPPRIMERA Merlin le Chanteur.
(Les guillemets sont nécessaires si le nom de ton personnage comporte des espaces)
"""

	elif command == "rm" or command == f"{prefix}rm" :
		message = f"""## {prefix}rm
Cette commande est l'une des deux manières de lancer un dé (la seule différence avec '{prefix}rr' apparaît au moment de l'affichage du résultat)
Elle nécessite d'avoir enregistré ET sélectionné un personnage avec '{prefix}charsave' et '{prefix}charsel', et a besoin du nom exact d'un des attributs du personnage en tant qu'argument, donc faites attention aux fautes de frappe.

Si l'attribut donné est un attribut "normal" (comme 'For' ou 'Amour'), le jet se passe de la manière suivante :
1) lance un dé du type indiqué lors de la création du personnage (ou du dé par défaut si aucun dé particulier n'a été spécifié)
2) compare la valeur de l'attribut et le résultat du dé
3) si le résultat du dé est INFÉRIEUR à la valeur d'attribut, envoie un message de réussite et spécifie __le degré de réussite__ (pareil pour l'échec si le résultat est supérieur à la valeur d'attribut)

Si l'attribut est un attribut de type 'DEG' :
1) lance XdY+Z, oÙ X, Y et Z sont les valeurs de l'attribut indiquées lors de l'enregistrement du personnage (voir '{prefix}charsave')
2) affiche le détail de chaque dé et la somme totale

Cette commande autorise un argument supplémentaire : le <bonus/malus>, qui viendra modifier le jet de dé.

syntaxes :
(Les exemples ci-dessous sont montrés se référant à la fiche de personnage "Merlin le Chanteur". Sa fiche d'enregistrement est trouvable en tapant `{prefix}help charsave`)

`{prefix}rm For 5`
Cette commande lancera un d20 et la comparera à la valeur de l'atribut For. Un bonus de 5 a été implémenté au jet

`{prefix}rm Sortilège -2`
Cette commande lancera un jet de type DEG : 3d6+4 , puis appliquera le malus de -2 et affichera le résultat
"""

	elif command == "rr" or command == f"{prefix}rr" :
		message = f"""## {prefix}rm
Cette commande est l'une des deux manières de lancer un dé (la seule différence avec '{prefix}rm' apparaît au moment de l'affichage du résultat)
Elle nécessite d'avoir enregistré ET sélectionné un personnage avec '{prefix}charsave' et '{prefix}charsel', et a besoin du nom exact d'un des attributs du personnage en tant qu'argument, donc faites attention aux fautes de frappe.

Si l'attribut donné est un attribut "normal" (comme 'For' ou 'Amour'), le jet se passe de la manière suivante :
1) lance un dé du type indiqué lors de la création du personnage (ou du dé par défaut si aucun dé particulier n'a été spécifié)
2) compare la valeur de l'attribut et le résultat du dé
3) si le résultat du dé est INFÉRIEUR à la valeur d'attribut, envoie un message de réussite et spécifie __le résultat final du dé__ (pareil pour l'échec si le résultat est supérieur à la valeur d'attribut)

Si l'attribut est un attribut de type 'DEG' :
1) lance XdY+Z, oÙ X, Y et Z sont les valeurs de l'attribut indiquées lors de l'enregistrement du personnage (voir '{prefix}charsave')
2) affiche le détail de chaque dé et la somme totale

Cette commande autorise un argument supplémentaire : le <bonus/malus>, qui viendra modifier le jet de dé.

syntaxes :
(Les exemples ci-dessous sont montrés se référant à la fiche de personnage "Merlin le Chanteur". Sa fiche d'enregistrement est trouvable en tapant `{prefix}help charsave`)

`{prefix}rm For 5`
Cette commande lancera un d20 et la comparera à la valeur de l'atribut For. Un bonus de 5 a été implémenté au jet

`{prefix}rm Sortilège -2`
Cette commande lancera un jet de type DEG : 3d6+4 , puis appliquera le malus de -2 et affichera le résultat
"""
	
	elif command == "mod" or command == f"{prefix}mod" :
		message = f"""## {prefix}mod
Tu peux facilement modifier tes attributs de type 'JAU' avec '{prefix}mod'.
Cette commande comprend un argument obligatoire et deux optionnels :
Si tu ne donnes que l'argument obligatoire, le bot te montrera uniquement l'état actuel de ton attribut, et ne le modifiera pas. Le premier argument optionnel sert à donner la valeur de la modification. Le dernier argument sert à savoir si tu veux que la valeur de ton attribut puisse dépasser sa "valeur maximale" ou non. (Si tu ne mets rien, elle sera bloquée.)

syntaxe :

`{prefix}mod PV -3`

Cette commande réduira la valeur actuelle de la jauge PV de trois points.
Attention à ne PAS mettre d'espace entre le signe "-" et la valeur à soustraire !

`{prefix}mod PV 6 y`
Cette commande additionnera 6 points à la valeur actuelle de la jauge PV, et autorise le dépassement de sa valeur maximale (supérieure comme inférieure).
"""

	elif command == "r" or command == f"{prefix}r" :
		message = f"""## {prefix}r
Avec '{prefix}r', tu pourras lancer un ou plusieurs dés simples.
Tu peux __additionner__ plusieurs dés en les séparant par le symbole '+', et ajouter un bonus ou un malus précédé du signe '+' (pour ajouter au résultat) ou '-' (pour soustraire au résultat).

Il est possible d'ajouter autant de paramètres que souhaité

syntaxe :

`{prefix}r 2d6 + d20 -10`

Cette commande contient plusieurs paramètres :
`2d6` génèrera deux fois un chiffre aléatoire compris entre 1 et 6
`d20` (équivalent à `1d20`) génèrera un nombre compris entre 1 et 20
`-10` enlèvera 10 points sur la somme des résultats
La commande renverra l'addition de tout ceci
"""
	
	else :
		message =f"""Aucune commande '{command}' n'a été trouvée :sweat_smile:
Essaye de vérifier ton typage ?
Et, si tu vois qu'une commande existe vraiment mais n'est pas disponible ici, merci d'en informer le dev ! (Son serveur est disponible via '{prefix}help support')
"""
	
	print (f"Longueur du message : {len(message)}")
	while len(message) > 2000 :
		for i in range (1700, len(message)) :
			print(message[i], end = "")
			if message[i] == "\n" or (i >= 1950 and message[i] == " ") or i == 1999 :
				break
		await ctx.send(message[:i])
		print("\n")
		message = message[i:]
	
	await ctx.send(message)

@bot.event
async def on_ready():
	print("BotIsReady")
	channel = bot.get_channel(CHANNELID)
	await channel.send(f"Bot is awake ({ver})")

@bot.command()
async def vers(ctx):
	await ctx.send(V)
	
@bot.command()
async def selfid(ctx):
	" - Obtiens ton id d'utilisateur"
	await ctx.send(f"Bonjour {ctx.author.name} !\nVoici ton ID d'utilisateur :")
	await ctx.send(f"{ctx.author.id}")

@bot.command()
async def signup(ctx):
	" - T'ouvre un emplacement de sauvegarde de personnages"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userName = str(ctx.author.name)
	await ctx.send(f"Bonjour {userName} !")
	userID = str(ctx.author.id)
	os.chdir(initPath)
	if not os.path.exists(userID) :
		os.mkdir(userID) # Crée un dossier portant le nom de l'ID de l'utilisateur
		os.chdir(userID) # Accède au dossier
		
		data = {}
		data["UserName"] = userName
		data["CharSelected"] = "None"
		
		with open(userID + '.json', 'w') as f : # Crée un fichier .json portant le nom de l'ID de l'utilisateur
			json.dump(data, f, indent = 4)
		
		data = {}
		data["Name"] = "Merlin le Chanteur"
		data["Die"] = 20
		data["Image"] = "https://media.discordapp.net/attachments/1210647216155525130/1216171097393856673/IMG_2886.jpg?ex=65ff6a98&is=65ecf598&hm=cbcc9870a6cb9991f00bfcd3d17e3ff89f2616ffb73e3e666e63bc46b6f974ca&=&format=webp&width=442&height=425"
		data["Stats"] = [["For", 8, "20", 0], ["Amour", 13, "20", 0], ["Magie", 78, "100", 0], ["DEGSortilège", 6, 3, 4], ["DEGLance", 10, 2, -1], ["JAUPV", 23, 25, 0]]
		
		with open(data["Name"] + '.json', 'w') as f : # Crée un fichier .json du personnage "Merlin le Chanteur" afin de servir d'exemple
			json.dump(data, f, indent = 4)

		await ctx.send("Ton compte a été associé à un nouveau dossier de stockage.")
		await CHANNLOG.send(f"LOG MESSAGE - signup - succeed\nL'utilisateur **{ctx.author.name}** (ID : {userID}) a crée un dossier avec son ID")
	else :
		await ctx.send("Tu possèdes déjà un dossier à ton nom.")
		await CHANNLOG.send(f"LOG MESSAGE - signup - fail\nL'utilisateur **{ctx.author.name}** (ID : {userID}) a échoué à créer un dossier")
	os.chdir(initPath)

@bot.command()
async def merlin(ctx):
	" - T'ouvre un emplacement de sauvegarde de personnages"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userName = str(ctx.author.name)
	await ctx.send(f"Bonjour {userName} !")
	userID = str(ctx.author.id)
	os.chdir(initPath)
	if os.path.exists(userID) :
		os.chdir(userID)
		
		data = {}
		data["Name"] = "Merlin le Chanteur"
		data["Die"] = "20"
		data["Image"] = "https://media.discordapp.net/attachments/1210647216155525130/1216171097393856673/IMG_2886.jpg?ex=65ff6a98&is=65ecf598&hm=cbcc9870a6cb9991f00bfcd3d17e3ff89f2616ffb73e3e666e63bc46b6f974ca&=&format=webp&width=442&height=425"
		data["Stats"] = [["For", 8, "20", 0], ["Amour", 13, "20", 0], ["Magie", 78, "100", 0], ["DEGSortilège", 6, 3, 4], ["DEGLance", 10, 2, -1], ["JAUPV", 23, 25, 0]]
		
		with open(data["Name"] + '.json', 'w') as f : # Crée un fichier .json du personnage "Merlin le Chanteur" afin de servir d'exemple
			json.dump(data, f, indent = 4)

		await ctx.send("""Merlin le Chanteur est dans la place !\n("la place" = ton dossier de stockage)""")
		await CHANNLOG.send(f"LOG MESSAGE - merlin - succeed\nL'utilisateur **{ctx.author.name}** (ID : {userID}) a soigné Merlin")
	else :
		await ctx.send(f"Aucun emplacement de sauvegarde n'a été trouvé.\nCrée-en un via la commande `{prefix}signup` !")
		await CHANNLOG.send(f"LOG MESSAGE - merlin - fail\nL'utilisateur **{userName}** (ID : {userID}) a échoué à soigner Merlin\nRaison : 'signup' non-effectué")
	os.chdir(initPath)

@bot.command()
async def charlist(ctx):
	" - Te donne la liste de tes personnages sauvegardés"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	os.chdir(initPath)
	message = ''
	if os.path.exists(userID) :
		charfiles = os.listdir(userID)
		if len(charfiles) == 0 :
			await ctx.send("Aucun personnage n'a été trouvé.\nPour en créer un, utilise la commande 'charsave'.")
		else :
			await CHANNLOG.send(f"LOG MESSAGE - charlist - succeed\nL'utilisateur **{ctx.author.name}** (ID : {userID}) a affiché sa liste de personnages")
			for i in charfiles : # Affiche la liste des fichiers dans le dossier portant le nom de l'ID de l'utilisateur
				filename = i[:-5] # Efface le '.json' à la fin du nom des dossiers, afin de ne garder que le nom du personnage
				try :
					print(filename[:9])
				except :
					pass
				if filename != str(userID) : # Ignore le fichier de 'charsel' (*le fichier qui garde en mémoire le personnage sélectionné)
					message += f"{filename}\n"
	await ctx.send(message)
	

@bot.command()
async def vwlist(ctx):
	" - Te donne la liste de tes personnages sauvegardés"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userfile = userID + ".json"
	userName = str(ctx.author.name)
	os.chdir(initPath)
	message = ''
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(userfile) :
			with open(userfile, "r") as f :
				userData = json.load(f)
				try :
					gmList = userData["AccessiblesViewerMode"]
					print (gmList)
					for i in gmList :
						message += f"__{str(i[0])}__\nappartient à <@{str(i[1])}>\n"
				except :
					message += f"Aucun personnage n'a été trouvé dans la liste des personnages consultables. Ajoutes-en avec `{prefix}vwadd` !"
	await ctx.send(message)
	os.chdir(initPath)
	
@bot.command()
async def vwadd(ctx, name, owner):
	" - Ajoute un personnage en lecture seule"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	userFile = userID + ".json"
	os.chdir(initPath)
	message = ''
	try :
		if len(owner) == len(userID) :
			owner = int(owner)
			ajoutValide = 1
		if os.path.exists(userID) :
			os.chdir(userID)
			if os.path.exists(userFile) :
				with open(userFile, "r+") as f :
					userData = json.load(f)
					
					
				try :
					
					vwList = userData["AccessiblesViewerMode"]
					for i in vwList :
						if i[0] == name : #and i[0] == owner :
							ajoutValide = 0
				except :
					vwList = []
				
				
				if ajoutValide == 1 :
					vwList.append([name, owner])
					userData["AccessiblesViewerMode"] = vwList
					with open(userFile, "w") as f :
						json.dump(userData, f, indent = 4)
					print(userData)
					message += f"Le personnage **{name}** a été ajouté à votre liste d'accès (demandez à l'utilisateur <@{owner}> de vous en autoriser l'accès)"
				else :
					message += f"Le personnage {name} existe déjà."
						
		else :
			message += f"Aucun dossier de sauvegarde n'a été trouvé."
	except :
		message += f"L'ID entré ({owner}) n'est pas correct."
	await ctx.send(message)

@bot.command()
async def charsave(ctx, name, die, *arr):
	" - Sauvegarde ton personnage"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	channel = bot.get_channel(CHANNELID)
	filename = name + '.json'
	inventory = name + '-Inventory.json'
	stats = list(arr)
	imgUrl = ""
	finish = 0
	aut = ''
	os.chdir(initPath)
	tupleOvw = ("OVW", "'OVW'")
	tupleUrl = ("URL", "Url", "url")
	tupleAut = ("AUT", "Aut", "aut")
	if os.path.exists(userID) :
		os.chdir(userID)
		OverWrite = 0
		if debug >= 1 :
			print("PP : Commande 'charsave' | start")
		for i in arr : 
			try :
				if i in tupleOvw : # Vérifie que la variable 'OVW' est présente dans les arguments. Si elle l'est, écrase tout ancien personnage du même nom.
					OverWrite = 1
				
				elif i[:3] in tupleUrl : # Variable qui permet d'enregistrer l'URL d'une image
					if imgUrl != '' :
						imgUrl += "\n"
					if i[3] == "=" :
						imgUrl += i[4:]
					else :
						imgUrl += i[3:]
					print(imgUrl)
					
				elif i[:3] in tupleAut : # Variable qui permet de donner un accès de lecture à un ou plusieurs membres en ajoutant leur ID
					if (i[3] == "=" and len(i[4:]) == len(userID)) or (i[3] != "=" and len(i[3:]) == len(userID)) : 
						aut = []
						if i[3] == "=" :
							aut.append(i[4:])
						elif i[:3] in tupleAut :
							aut.append(i[3:])
						print(aut) 
					else :
						await ctx.send (f"""L'ID "{i}" n'est pas de la bonne longueur et n'a pas été pris en compte.""")
					
			except :
				pass
		if os.path.exists(filename) and OverWrite == 0 :
			await ctx.send(f"Le personnage {name} existe déjà. Essaie de le supprimer ou de changer le nom de ton nouveau personnage.\n\n!! Pour écraser automatiquement ton ancien personnage, renvoie la commande en rajoutant 'OVW' en dernier argument de la commande (OVW pour OVerWrite) !!")
			await channel.send(f"LOG MESSAGE - charsave - finish = {finish}\nL'utilisateur **{userName}** (ID : {userID}) a échoué à créer le fichier {filename} avec l'argument 'OVW' = {OverWrite}\nRaison : personnage déjà existant")
		else :
			
			"""   # Partie appartenant à la V1.5
			if not os.path.exists(inventory) :
				data = {}
				data["Name"] = name
				data["Inventaire"] = [["Vêtements", 1]]
				with open(inventory, 'w') as f :
					json.dump(data, f, indent = 4)
			else :
				with open(inventory, 'r+') as f :
					data = json.load(f)
					if data["Name"] != name :
						data["Name"] = name
						json.dump(data, f, indent = 4)
			"""		
							
			if debug >= 2 :
				print("PP : OVW analysé, entrée dans le programme d'écriture")
			"""Distribue les valeurs comme suit :
			
			Stats : [
				[
					"NomDeValeur",
					Valeur,
					"Die",
					MalBon
				]
				[
					"NomDeValeur2",
					Valeur,
					"Die"
					MalBon
				]
				[
					"NomDeValDEG",
					Valeur,
					NbDeDie,
					MalBon
				]
			]
			
			"""
			if debug >= 1 :
				print(f"PP : récupération des stats :\n  > stats en input =\t\t{stats}\n  > stats en traitement =\t{list(arr)}")
			statSplit = [] # Liste totale des stats, à ajouter à 'data'
			varGroupe = [] # Groupe de variables en cours de traitement, à transférer dans la liste 'statSplit'
			varAct = 0 # Variable en cours d'analyse à envoyer dans le 'varGroupe' une fois analysée
			finish = 0 # Variable qui permet de sortir du cycle une fois chaque valeur analysée
			x = 0 # 0 = Aucune variable détectée | 1 = Variable textuelle (nom de variable) | 2 = Variable numérique (valeur)
			y = 0 # 0 = Premier cycle, aucune valeur dans 'varGroupe' | 1 = Valeur présente dans 'varGroupe', transfert possible
			DEGstat = 0 # 0 = Stat normale | 1 = Stat de type "DEG" | 2 = Stat de type jauge
			while finish == 0 :
				if debug >= 1 :
					print("PP : début d'un cycle dans la boucle de traitement")
				try :
					while stats[0][:3] in ("URL", "Url", "url", "AUT", "Aut", "aut") or stats[0] in ("OVW", "'OVW'", '"OVW"') :	# Supprime les attributs déjà traités et l'argument OVW
						stats.pop(0)
				except :
					pass
					
				try : # Vérifie qu'il reste au moins une valeur à convertir, puis la récupère et la supprime de la liste des valeurs à traiter
					varAct = stats[0]
					stats.pop(0)
					try : # Essaie de convertir la mémoire actuelle en int afin de déterminer s'il s'agit d'une variable textuelle (donc un nom de variable) ou d'une variable numérique
						varAct = int(varAct)
						x = 2
					except :
						x = 1
					if debug >= 2 :
						print(f"PP : varAct déterminée : {varAct}")
					if x == 1 : # Si la 'valAct' est un nom de variable :
						if y == 1 : # Si la liste 'varGroupe' contient déjà une "stat traitée", la transfère à 'statSplit' et reset 'varGroupe'
							if debug >= 2 :
								if debug >= 2 :
									print(f"PP : longueur de la stat en cours de traitement : {len(varGroupe)}")
							
							while len(varGroupe) < 4 : # Si informations non-précisées, les set à leur valeur par défaut
								if debug >= 1 :
									print(f"PP : début de complétion des données manquantes")
								if len(varGroupe) == 2 :
									
									try :
										if varGroupe[0][:3] == "DEG" :
											DEGstat = 1
										elif varGroupe[0][:3] == "JAU" :
											DEGstat = 2
										else :
											DEGstat = 0
									except :
										pass
										
										
									if DEGstat == 0 :
										if debug >= 1 :
											print(f"Stat {varGroupe[0]} réglée sur du d{die}")
										varGroupe.append(die)
									elif DEGstat == 1 :
										if debug >= 1 :
											print(f"StatDEG {varGroupe[0]} réglée sur du 1d{varGroupe[1]}")
										varGroupe.append(1)
									elif DEGstat == 2 : # Jauge : <nom> <valActuelle> <valMax> <valMin>
										if debug >= 1 :
											print(f"StatJAU {varGroupe[0]} réglée sur du {varGroupe[1]} / {varGroupe[1]}")
										varGroupe.append(varGroupe[1])
										
								if debug >= 1 :
									print(f"{varGroupe[0]} réglée à un BonMal de 0")
								varGroupe.append(0)
								if debug >= 2 :
									print(f"Stat en cours de traitement | Prête : {varGroupe}")
								elif debug >= 1 :
									print(f"PP : stat réglée")
								
								
							statSplit.append(varGroupe)
							varGroupe = []
						varGroupe.append(varAct) # Ajoute le nom de variable à 'varGroupe' en tant que nom de stat
						y = 1
					elif x == 2 : # Si la 'valAct' est une valeur numérique de variable :
						varGroupe.append(varAct)
						if debug >= 2 :
							print(f"PP : varGroupe complété avec varAct : {varGroupe} | {varAct}")
				except : # S'il n'y a pas de valeur à convertir, ajoutes celles en cours et termine le processus
					if x == 0 :
						await ctx.send(f"{name} ne possède pas d'attribut ; merci d'en ajouter au moins un avant d'essayer de l'enregistrer")
						await CHANNLOG.send(f"LOG MESSAGE - charsave - finish = {finish}\nL'utilisateur **{userName}** (ID : {userID}) a échoué à créer le fichier {filename} avec l'argument 'OVW' = {OverWrite}\nRaison : aucun attribut indiqué")
					else :
						while len(varGroupe) < 4 : # Si informations non-précisées, les set à leur valeur par défaut
							if debug >= 1 :
								print(f"PP : début de complétion des données manquantes")
							if len(varGroupe) == 2 :
								try :
									if varGroupe[0][:3] == "DEG" :
										DEGstat = 1
									else :
										DEGstat = 0
								except :
									pass
								if DEGstat == 0 :
									if debug >= 1 :
										print(f"Stat {varGroupe[0]} réglée sur du d{die}")
									varGroupe.append(die)
								elif DEGstat == 1 :
									if debug >= 1 :
										print(f"StatDEG {varGroupe[0]} réglée sur du 1d{varGroupe[1]}")
									varGroupe.append(1)
							if debug >= 1 :
								print(f"{varGroupe[0]} réglée à un BonMal de 0")
							varGroupe.append(0)
							if debug >= 2 :
								print(f"Stat en cours de traitement | Prête : {varGroupe}")
							elif debug >= 1 :
								print(f"PP : stat réglée")
						statSplit.append(varGroupe) # Ajout des variables en cours de traitement
					finish = 1
					if debug >= 1 :
						print(f"PP : finish = 1 ; fin de boucle")
			data = {}
			await ctx.send(f"""Personnage enregistré sous le nom **{name}**.\nPour le consulter, essaie la commande `{prefix}charsee "{name}"` !""")
			data["Name"] = name
			if imgUrl[:8] == "https://" :
				data["Image"] = imgUrl
			else :
				data["Image"] = ""
			data["Viewers"] = aut
			data["Die"] = die
			data["Stats"] = statSplit
			
			with open(filename, 'w') as f :
				json.dump(data, f, indent = 4)

			await CHANNLOG.send(f"LOG MESSAGE - charsave - finish = {finish}\nL'utilisateur **{userName}** (ID : {userID}) a crée le fichier {filename} avec l'argument 'OVW' = {OverWrite}")
				
	else :
		await ctx.send("Aucun emplacement de sauvegarde n'a été trouvé.\nCrée-en un via la commande 'signup' !")
		await CHANNLOG.send(f"LOG MESSAGE - charsave - finish = {finish}\nL'utilisateur **{userName}** (ID : {userID}) a échoué à créer le fichier {filename} avec l'argument 'OVW' = {OverWrite}\nRaison : 'signup' non-effectué")
			
	try :
		os.chdir(initPath)
	except :
		await ctx.send("Échec de retour à l'initPath. Redémarrage requis")

@bot.command(pass_context = True)
async def charsee(ctx, name = ''):
	" - Charge la fiche du personnage indiqué"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	userfile = userID + '.json'
	os.chdir(initPath)
	if name == '' and os.path.exists(userID) :
		os.chdir(userID)
		with open(userfile, 'r') as f :
			charsel = json.load(f)
		filename = charsel["CharSelected"]
		name = filename[:-5]
		os.chdir(initPath)
	else :
		filename = name + '.json'
 
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(filename) :
			with open(filename, 'r') as f :
				data = json.load(f)
			
			Name = data["Name"]
			Die = data["Die"]
			try :
				imgUrl = data["Image"]
			except :
				imgUrl = ""
				
			try :
				viewersID = data["Viewers"]
			except :
				viewersID = ""
				
			message = f"# {Name}\nType de dé utilisé par défaut : d{Die}\n### Stats :"
			for i in data["Stats"] : # i prend chaque valeur de stat
				if i[0][:3] == "DEG" :
					statDegNature = i[0][3:]
					if str(i[3])[0] != "-" :
						message += f"\nDEG : {statDegNature}\t-\t{i[2]}d{i[1]} + {i[3]}"
					else :
						message += f"\nDEG : {statDegNature}\t-\t{i[2]}d{i[1]} - {str(i[3])[1:]}"
				elif i[0][:3] == "JAU" :
					statDegNature = i[0][3:]
					message += f"\nJAU : {statDegNature}\t-\t{i[1]} / {i[2]}"
				else :
					message += f"\n{i[0]}\t-\t{i[1]}"
					if i[2] != Die :
						message += f" (en d{i[2]})"
			
			if imgUrl != "" :
				await ctx.send(imgUrl)
			if viewersID != "" :
				message += f"\n\nUtilisateurs invités :"
				print(viewersID)
				
				
				"""
				while len(viewersID) > len(userID) :
				"""	
				
				idList = []	# Contient chaque caractère des IDs
				idAct = ''	# Contient l'ID en cours de traitement
				for i in viewersID :
					idList.append(i)
				idList.append("\n")
				
				print("Extraction des ID :", idList)
				for i in idList :
					if i != "\n" :
						idAct += i
					else :
						message += f"\n<@{idAct}>"
						idAct = ''
						
			await ctx.send(message)
			await CHANNLOG.send(f"LOG MESSAGE - charsee - succeed\nL'utilisateur **{userName}** (ID : {userID}) a affiché le personnage {name}")
			
		else :
			if name == '' :
				await ctx.send(f"Aucun personnage n'a été sélectionné. Utilise la commande `{prefix}charsel` !")
			else :
				await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
				await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu afficher un personnage inexistant : {name}")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
		await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu afficherle personnage {name} mais ne possède pas de dossier de sauvegarde")
	os.chdir(initPath)

@bot.command(pass_context = True)
async def vwsee(ctx, name = ''):
	" - Charge la fiche du personnage indiqué"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	userFile = userID + '.json'
	os.chdir(initPath)
	message = ''
	if name == '' :
		await ctx.send(f"La commande `{prefix}vwsee` demande un argument")
	else :
		if os.path.exists(userID) :
			os.chdir(userID)
			if os.path.exists(userFile) :
				with open(userFile, 'r') as f :
					data = json.load(f)
				
				try :
					for i in data["AccessiblesViewerMode"] :
						print(f"essai de boucle : {name} - {i}")
						if name == i[0] :
							vwfilename = i[0] + '.json'
							vwuserID = str(i[1])
							print(f"{name} a été trouvé")
							break
					if debug >= 2 :
						print(initPath)
					os.chdir(initPath)
					if debug >= 2 :
						print(vwuserID)
					if os.path.exists(vwuserID) :
						os.chdir(vwuserID)
						if os.path.exists(vwfilename) :
							with open(vwfilename, "r") as f :
								vwdata = json.load(f)
							try :
								for i in vwdata["Viewers"] :
									if i == userID :
										print("Accès autorisé")
									
									
										
										Name = vwdata["Name"]
										Die = vwdata["Die"]
										try :
											imgUrl = vwdata["Image"]
										except :
											imgUrl = ""
											
										try :
											viewersID = vwdata["Viewers"]
										except :
											viewersID = ""
											
										message += f"# {Name}\n**Créé par <@{vwuserID}>**\nType de dé utilisé par défaut : d{Die}\n### Stats :"
										for i in vwdata["Stats"] : # i prend chaque valeur de stat
											if i[0][:3] == "DEG" :
												statDegNature = i[0][3:]
												if str(i[3])[0] != "-" :
													message += f"\nDEG : {statDegNature}\t-\t{i[2]}d{i[1]} + {i[3]}"
												else :
													message += f"\nDEG : {statDegNature}\t-\t{i[2]}d{i[1]} - {str(i[3])[1:]}"
											elif i[0][:3] == "JAU" :
												statDegNature = i[0][3:]
												message += f"\nJAU : {statDegNature}\t-\t{i[1]} / {i[2]}"
											else :
												message += f"\n{i[0]}\t-\t{i[1]}"
												if i[2] != Die :
													message += f" (en d{i[2]})"
										
										if imgUrl != "" :
											await ctx.send(imgUrl)
										
										
									
							except :
								message += f"L'utilisateur n'a autorisé l'accès de {name} à aucun membre"
						
						else :
							message += f"L'utilisateur <@{vwuserID}> ne possède aucun personnage nommé {name}"
					
					else :
						message += f"L'utilisateur propriétaire de {name} <@{vwuserID}> ne possède pas de dossier de personnages"
					
				except :
					message += f"Aucun personnage n'a été détecté dans la liste des personnages consultables"
					
		
		"""
		if os.path.exists(userID) :
			os.chdir(userID)
			if os.path.exists(filename) :
				with open(filename, 'r') as f :
					data = json.load(f)
				
				
				if viewersID != "" :
					message += f"Utilisateurs invités :\n"
					print(viewersID)
					while len(viewersID) > 5 :
						print("Extraction des ID :", viewersID)
						for i in range (len(viewersID)) :
							
							if viewersID[i] == "\n" :
								message += f"<@{viewersID[:i]}>"
								print(f"<@{viewersID[:i]}>")
								viewersID = viewersID[i:]
								break
							
				await ctx.send(message)
				await CHANNLOG.send(f"LOG MESSAGE - charsee - succeed\nL'utilisateur **{userName}** (ID : {userID}) a affiché le personnage {name}")
				
			else :
				if name == '' :
					await ctx.send(f"Aucun personnage n'a été sélectionné. Utilise la commande `{prefix}charsel` !")
				else :
					await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
					await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu afficher un personnage inexistant : {name}")
		else :
			await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
			await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu afficherle personnage {name} mais ne possède pas de dossier de sauvegarde")
		"""
	
	await ctx.send(message)
	os.chdir(initPath)




@bot.command(pass_context = True)
async def img(ctx, name = ''):
	" - Charge l'illustration du personnage indiqué"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	userfile = userID + '.json'
	os.chdir(initPath)
	if name == '' and os.path.exists(userID) :
		os.chdir(userID)
		with open(userfile, 'r') as f :
			charsel = json.load(f)
		filename = charsel["CharSelected"]
		name = filename[:-5]
		os.chdir(initPath)
	else :
		filename = name + '.json'
 
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(filename) :
			with open(filename, 'r') as f :
				data = json.load(f)
			
			Name = data["Name"]
			try :
				imgUrl = data["Image"]
			except :
				imgUrl = ""
				
			message = f"# {Name}"
			if imgUrl != "" :
				await ctx.send(message)
				await ctx.send(imgUrl)
			else :
				await ctx.send(f"Le personnage {name} n'a pas d'image")
			await CHANNLOG.send(f"LOG MESSAGE - charsee - succeed\nL'utilisateur **{userName}** (ID : {userID}) a affiché le personnage {name}")
			
		else :
			if name == '' :
				await ctx.send(f"Aucun personnage n'a été sélectionné. Utilise la commande `{prefix}charsel` !")
			else :
				await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
				await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu afficher un personnage inexistant : {name}")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
		await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu afficherle personnage {name} mais ne possède pas de dossier de sauvegarde")
os.chdir(initPath)



@bot.command()
async def chardelete(ctx, name):
	" - Supprime le personnage indiqué (!! pas de retour possible !!)"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	filename = name + '.json'
	inventory = name + '-Inventory.json'
	os.chdir(initPath)
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(inventory) :
			os.remove(inventory)
			await CHANNLOG.send(f"LOG MESSAGE - chardelete - succeed\nL'utilisateur **{userName}** (ID : {userID}) a supprimmé l'inventaire {inventory}")
		else :
			await CHANNLOG.send(f"LOG MESSAGE - chardelete - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu supprimmer l'inventaire inexistant {inventory}")
		if os.path.exists(filename) :
			with open(filename, 'r') as f :
				data = json.load(f)

			Name = data["Name"]
			Die = data["Die"]
			message = f"{Name} {Die}\n"
			for i in data["Stats"] : # i prend chaque valeur de 'stat'
				message += f"\n{i[0]} {i[1]}"
				if i[2] != Die :
					message += f"{i[2]})"
			message += '\nOVW'
			
			await ctx.send(f"Voici ton personnage supprimé, au cas où tu voudrais le recréer :\n{message}")
			os.remove(filename)
			await CHANNLOG.send(f"LOG MESSAGE - chardelete - succeed\nL'utilisateur **{userName}** (ID : {userID}) a supprimmé le personnage {name}")
		else :
			await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
			await CHANNLOG.send(f"LOG MESSAGE - chardelete - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu supprimmer un personnage inexistant : {name}")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
		await CHANNLOG.send(f"LOG MESSAGE - charsee - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu supprimer le personnage {name} mais ne possède pas de dossier de sauvegarde")
	os.chdir(initPath)

@bot.command(pass_context = True)
async def charedit(ctx, name = ''):
	" - Te permet d'éditer le personnage indiqué"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	userfile = userID + '.json'
	os.chdir(initPath)
	if name == '' and os.path.exists(userID) :
		os.chdir(userID)
		with open(userfile, 'r') as f :
			charsel = json.load(f)
		filename = charsel["CharSelected"]
		name = filename[:-5]
		os.chdir(initPath)
	else :
		filename = name + '.json'
 
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(filename) :
			with open(filename, 'r') as f :
				data = json.load(f)


			Name = data["Name"]
			Die = data["Die"]
			try :
				if data["Image"] == "" :
					raise Exception
				else :
					urlList = str(data["Image"] + "https://")
					imgUrl = '\n'
					finPremUrl = 0
					for i in range (1, len(urlList)) :
						if urlList[i:(i+8)] == "https://" :
							print(urlList)
							imgUrl += ("URL=" + urlList[finPremUrl:i])
							print(imgUrl)
							finPremUrl = i
			except :
				imgUrl = "\nURL=None"
			message = f'{prefix}charsave "{Name}" {Die}{imgUrl}\n'
			for i in data["Stats"] : # i prend chaque valeur de 'stat'
				message += f'\n"{i[0]}" {i[1]}'
				if i[2] != Die or i[0][:3] == "DEG" :
					message += f' {i[2]} {i[3]}'
			message += '\nOVW'
			
			await ctx.send(f"Voici ton personnage.\nCopy-paste, modifie ce que tu veux puis renvoie-le dans un salon auquel j'ai accès. Ton ancien personnage sera écrasé si tu laisses 'OVW' à la fin de ta commande.")
			await ctx.send(message)
			await CHANNLOG.send(f"LOG MESSAGE - charedit - succeed\nL'utilisateur **{userName}** (ID : {userID}) a chargé le message d'édition du personnage {name}")
		else :
			await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
			await CHANNLOG.send(f"LOG MESSAGE - charedit - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu charger le message d'édition d'un personnage inexistant : {name}")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
		await CHANNLOG.send(f"LOG MESSAGE - charedit - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu éditer le personnage {name} mais ne possède pas de dossier de sauvegarde")
	os.chdir(initPath)

@bot.command()
async def charsel(ctx, name):
	" - Te permet de sélectionner un de tes personnages"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	filename = userID + '.json'
	selected = name + ".json"
	os.chdir(initPath)
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(filename) :
			if os.path.exists(selected) :
				data = {}
				data["UserName"] = userName
				data["CharSelected"] = selected
				with open(filename, 'w') as f :
					json.dump(data, f, indent = 4)
				await ctx.send(f"Ton personnage actif est maintenant {name} !\n")
				await CHANNLOG.send(f"LOG MESSAGE - charsel - succeed\nL'utilisateur **{userName}** (ID : {userID}) a sélectionné le personnage {name}")
			else :
				await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande `{prefix}charsave` !")
				await CHANNLOG.send(f"LOG MESSAGE - charsel - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu sélectionner un personnage inexistant : {name}")
		else :
			await ctx.send("Un... Petit problème est survenu.....")
			await ctx.send("Laisse-moi juste essayer un petit truc-")
			os.chdir(initPath)
			if os.path.exists(userID) :
				os.chdir(userID)
				try :
					with open(filename, 'w') as f :
						await ctx.send("**Normalement**, le problème est réglé. Si ça ne marche toujours pas, contacte le dev.")
				except :
					await ctx.send(f"Je n'arrive pas à résoudre ton problème avec mes capacités actuelles.\nPour un support plus efficace, contacte le dev `{prefix}help support`.")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.\n\n!! Si tu as récemment changé d'ID, il est normal que tu ne retrouves pas tes sauvegardes. Repasse à ton ancien ID (si possible) ou demande au dev qu'il te transfère tes fichiers sur ton nouvel ID. (PS.- tu peux voir ton ID actuel avec la commande 'selfid')")
		await CHANNLOG.send(f"LOG MESSAGE - charsel - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu sélectionner le personnage {name} mais ne possède pas de dossier de sauvegarde")
	os.chdir(initPath)

@bot.command()
async def r(ctx, *arr):
	argDie = ''
	for i in arr :
		argDie += i
	print(argDie)
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)	
	os.chdir(initPath)
	operator = "+"								# Conserve l'opérateur précédant la valeur en cours de traitement afin de savoir quoi en faire
	supportedDices = ("d", "D", "r", "R")
	supportedOperators = ("+", "-", "/", "*")	# Liste des opérateurs supportés
	supportedModifiers = ("e", "x")
	valTot = []		# Contient les résultats de chaque monome et leurs signes d'opération
	actualArg = ''	# Contient le monome en cours de traitement
	valAct = 0		# Contient la valeur en cours de traitement
	nbDie = ''		# 1 d10e5
	valDie = ''		# 1d 10 e5
	modDie = ''		# 1d10 e 5
	valModDie = ''	# 1d10e 5
	resArg = 0		# Contient le résultat total du monome en cours de traitement
	resDie = []		# Contient le résultat des dés du monome traité
	dieTot = []		# Contient chaque résultat de dé
	valFinTot = 0	# Valeur finale
	
	
	#try :
	#	await ctx.message.delete()
	#except :
	#	pass
	
	message = f"<@{userID}>\n"
	
	print(argDie)
	
	stop = 0
	monomes = []
	while stop == 0 :
		
		################################################################################
		############################ EXTRACTION DES MONOMES ############################
		################################################################################
		
		for i in range (len(argDie)) :
			try :
				if debug >= 2 :
					print(f"Longueur d'argDie : {len(argDie)} / i : {i}")
				
				if i + 1 == len(argDie) and not argDie in supportedOperators :	# Met fin à "l'absorbtion" du monome si ce dernier est terminé (donc si on voit un opérateur ou si la liste est terminée)
					actualArg += argDie[i]
					stop = 1
					raise Exception
				
				elif argDie[i] in supportedOperators :
					raise Exception
				
				else :
					actualArg += argDie[i]
					
			except :
				monomes.append(str(operator + actualArg))
				operator = argDie[i]
				actualArg = ''
	
	
	################################################################################
	############################ TRAITEMENT DES MONOMES ############################
	################################################################################
	
	if debug >= 1 :
		print(monomes)
		
	for i in monomes :
		
		if i in supportedOperators :
			pass
		else :
			operator = i[0]
			message += f"{i} "
			i = i[1:]
			print(i)
			roll = 0
			for j in range(len(i)) :		# Ordonne les valeurs d'il s'agit d'un dé
				if i[j] in supportedDices :
					roll = 1
					try :
						nbDie = i[:j]
						if nbDie == '' :
							raise Exception
					except :
						nbDie = 1
					try :
						valDie = i[j+1:]
					except :
						valDie = 1
					print(f"{operator}{nbDie}d{valDie} en cours de traitement")
				
				
			if roll == 1 :		# Lance le dé
				#nbDie = int(nbDie)
				if debug >= 1 :
					print(nbDie)
				for j in range(int(nbDie)) :		
					resDie.append(rd.randrange(1, int(valDie) + 1, 1))
					valAct += resDie[j]
				if debug >= 1 :
					print(f"{resDie} => {valAct}")
				
				dieTot.append(resDie)
				
				resDie = []
	
			else :				# Ajoute la valeur à la liste
				try :
					print(i)
					valAct = int(i)
				except :
					print(f"{i} ne peut pas être un int")
					
			valTot.append(operator + str(valAct))
			valAct = 0
		print(valTot, dieTot)
		
	for i in valTot :
		if i[0] == "+" :
			valFinTot += int(i[1:])
		elif i[0] == "-" :
			valFinTot -= int(i[1:])
		elif i[0] == "*" :
			valFinTot = valFinTot * int(i[1:])
		elif i[0] == "/" :
			valFinTot = valFinTot / int(i[1:])
		
		print(valFinTot)




	message += f"\nRésultat : **{valFinTot}**\nDés : {dieTot}"
		
	await ctx.send(message)

@bot.command(pass_context = True)
async def rm(ctx, stat, BonMal = 0):
	" - Lance un dé de la stat indiquée et donne l'écart"
	
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	selFile = userID + '.json'
	os.chdir(initPath)
	message = ''
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(selFile) :
			with open(selFile, 'r') as f :
				data = json.load(f)
				filename = data["CharSelected"]
			if os.path.exists(filename) :
				with open(filename, 'r') as f :
					data = json.load(f)
					name = data["Name"]
					statValue = data["Stats"]
					if debug >= 2 :
						print(statValue)
					
				statDegNature = ''
				DEGmode = 0
				for i in range (len(statValue)) :
					if debug >= 2 :
						print(statValue[i])
						print("\nAnalyse des 3 premiers caractères :", statValue[i][0][:3])
					try :
						if statValue[i][0][:3] == "DEG" : # Vérifie si la stat utilisée est une stat de dégâts ou non
							statDegNature = statValue[i][0][3:]
							DEGmode = 1
							if debug >= 2 :
								print("STATDEGNATURE =", statDegNature)
						else :
							statDegNature = statValue[i][0]
							DEGmode = 0
					except :
						pass
										
						
					# Set le bonus ou malus (naturel et additionnel)
					try :
						BonMalNat = int(statValue[i][3])
					except :
						BonMalNat = 0
					try :
						BonMal = int(BonMal)
					except :
						await ctx.send(f"""Le bonus/malus "{BonMal}" n'a pas pu être pris en compte""")
						BonMal = 0
					BonMalTot = BonMalNat + BonMal
					print (BonMalTot)
							
						
					
					print(stat, statDegNature, f"\nStat de base : {stat} / stat comparée et réduite : {statDegNature[:len(stat)]}")
					
					if stat == statDegNature[:len(stat)] or ((stat == statDegNature) * DEGmode) :
						if debug >= 2 :
							print(f"PP : entrée dans le mode jet avec DEGmode = {DEGmode}")
						
						txtBonMal = ''
						if BonMalNat != 0 :
							if BonMalNat > 0 :
								txt = "Avec bonus naturel"
							elif BonMalNat < 0 :
								txt = "Avec malus naturel"
							txtBonMal = f"{txt} de **{BonMalNat}**"
							if BonMal != 0 :
								txtBonMal += f" et "
						if BonMal != 0 :
							if BonMal > 0 :
								txt = "Bonus"
							elif BonMal < 0 :
								txt = "Malus"
							txtBonMal += f"{txt} de **{BonMal}**"
						
						if DEGmode == 1 : # Roll un jet DEG
							stat = str(statDegNature)
							nbDie = int(statValue[i][2])
							valDie = int(statValue[i][1])
							
							result = 0
							rolls = []
							txt = ''

							message = f"## {name}\n<@{userID}>\nJet de **{statDegNature}** - {nbDie}d{valDie}"
							await CHANNLOG.send(f"LOG MESSAGE - rm - succeed\nL'utilisateur **{userName}** (ID : {userID}) a lancé un dé de dégât {statDegNature} avec le personnage {name}")
							for i in range (nbDie) :
								result = rd.randrange(1, valDie + 1, 1)
								rolls.append(result)
							result = 0
							for i in rolls :
								result += i
							result += BonMalTot
							message += f"\n{rolls} {txtBonMal}\n**Résultat** :\n## {result}\n"
							
						elif DEGmode == 0 : # Roll un jet non-DEG
							if txtBonMal != '' :
								txtBonMal += "\n"
							margeCrit = int(statValue[i][2]) // 20
							critSucc = margeCrit # Sur du d20 : critSucc == 1 | critFail == 20  -  sur du d100 : critSucc == 5 | critFail == 96
							critFail = int(statValue[i][2]) - (margeCrit -1)
							message = f"## {name}\n<@{userID}>\nJet de **{statDegNature}**\n{txtBonMal}"

							await CHANNLOG.send(f"LOG MESSAGE - rm - succeed\nL'utilisateur **{userName}** (ID : {userID}) a lancé un dé de {statDegNature} avec le personnage {name}")
							result = rd.randrange(1, int(statValue[i][2]) + 1, 1)
							if result <= critSucc :
								message += f"## RÉUSSITE CRITIQUE !!\nNat **{result}**"
							elif result >= critFail :
								message += f"## ÉCHEC CRITIQUE !!\nNat **{result}**"
							else :
								result -= BonMalTot
								if result <= int(statValue[i][1]) :
									message += f"C'est un jet **RÉUSSI** de **{int(statValue[i][1]) - result}**"
								elif result > int(statValue[i][1]) :
									message += f"C'est un jet **ÉCHOUÉ** de **{result - int(statValue[i][1])}**"
								else :
									await ctx.send(f"Un problème est survenu : je suis incapable de comparer ta stat avec le dé. Voici ton résultat :\n{result}")
						await ctx.send(message)
						break
			else :
				await ctx.send(f"Un problème est survenu.")
		else :
			await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
			await CHANNLOG.send(f"LOG MESSAGE - rm - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu lancer un dé de dégât {stat} avec un personnage inexistant : {name}")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
		await CHANNLOG.send(f"LOG MESSAGE - rm - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu lancer un dé de dégât {stat} avec le personnage {name} mais ne possède pas de dossier de sauvegarde")
	os.chdir(initPath)

@bot.command(pass_context = True)
async def rr(ctx, stat, BonMal = 0):
	
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	selFile = userID + '.json'
	os.chdir(initPath)
	message = ''
	if os.path.exists(userID) :
		os.chdir(userID)
		if os.path.exists(selFile) :
			with open(selFile, 'r') as f :
				data = json.load(f)
				filename = data["CharSelected"]
			if os.path.exists(filename) :
				with open(filename, 'r') as f :
					data = json.load(f)
					name = data["Name"]
					statValue = data["Stats"]
					if debug >= 2 :
						print(statValue)
					
				statDegNature = ''
				DEGmode = 0
				for i in range (len(statValue)) :
					if debug >= 2 :
						print(statValue[i])
						print("\nAnalyse des 3 premiers caractères :", statValue[i][0][:3])
					try :
						if statValue[i][0][:3] == "DEG" : # Vérifie si la stat utilisée est une stat de dégâts ou non
							statDegNature = statValue[i][0][3:]
							DEGmode = 1
							if debug >= 2 :
								print("STATDEGNATURE =", statDegNature)
						else :
							statDegNature = statValue[i][0]
							DEGmode = 0
					except :
						pass
										
						
					# Set le bonus ou malus (naturel et additionnel)
					try :
						BonMalNat = int(statValue[i][3])
					except :
						BonMalNat = 0
					try :
						BonMal = int(BonMal)
					except :
						await ctx.send(f"""Le bonus/malus "{BonMal}" n'a pas pu être pris en compte""")
						BonMal = 0
					BonMalTot = BonMalNat + BonMal
					print (BonMalTot)
							
						
					
					print(stat, statDegNature, f"\nStat de base : {stat} / stat comparée et réduite : {statDegNature[:len(stat)]}")
					
					if stat == statDegNature[:len(stat)] or ((stat == statDegNature) * DEGmode) :
						if debug >= 2 :
							print(f"PP : entrée dans le mode jet avec DEGmode = {DEGmode}")
						
						txtBonMal = ''
						if BonMalNat != 0 :
							if BonMalNat > 0 :
								txt = "Avec bonus naturel"
							elif BonMalNat < 0 :
								txt = "Avec malus naturel"
							txtBonMal = f"{txt} de **{BonMalNat}**"
							if BonMal != 0 :
								txtBonMal += f" et "
						if BonMal != 0 :
							if BonMal > 0 :
								txt = "Bonus"
							elif BonMal < 0 :
								txt = "Malus"
							txtBonMal += f"{txt} de **{BonMal}**"
						
						if DEGmode == 1 : # Roll un jet DEG
							stat = str(statDegNature)
							nbDie = int(statValue[i][2])
							valDie = int(statValue[i][1])
							
							result = 0
							rolls = []
							txt = ''

							message = f"## {name}\n<@{userID}>\nJet de **{statDegNature}** - {nbDie}d{valDie}"
							await CHANNLOG.send(f"LOG MESSAGE - rm - succeed\nL'utilisateur **{userName}** (ID : {userID}) a lancé un dé de dégât {statDegNature} avec le personnage {name}")
							for i in range (nbDie) :
								result = rd.randrange(1, valDie + 1, 1)
								rolls.append(result)
							result = 0
							for i in rolls :
								result += i
							result += BonMalTot
							message += f"\n{rolls} {txtBonMal}\n**Résultat** :\n## {result}\n"
							
						elif DEGmode == 0 : # Roll un jet non-DEG
							if txtBonMal != '' :
								txtBonMal += "\n"
							margeCrit = int(statValue[i][2]) // 20
							critSucc = margeCrit # Sur du d20 : critSucc == 1 | critFail == 20  -  sur du d100 : critSucc == 5 | critFail == 96
							critFail = int(statValue[i][2]) - (margeCrit -1)
							message = f"## {name}\n<@{userID}>\nJet de **{statDegNature}**\n{txtBonMal}"

							await CHANNLOG.send(f"LOG MESSAGE - rm - succeed\nL'utilisateur **{userName}** (ID : {userID}) a lancé un dé de {statDegNature} avec le personnage {name}")
							resNat = rd.randrange(1, int(statValue[i][2]) + 1, 1)
							if resNat <= critSucc :
								message += f"## RÉUSSITE CRITIQUE !!\nNat **{resNat}**"
							elif resNat >= critFail :
								message += f"## ÉCHEC CRITIQUE !!\nNat **{resNat}**"
							else :
								result = resNat  - BonMalTot
								if result <= int(statValue[i][1]) :
									message += f"C'est un jet **RÉUSSI** ; résultat de **{result}** (Nat {resNat})"
								elif result > int(statValue[i][1]) :
									message += f"C'est un jet **ÉCHOUÉ** ; résultat de **{result}** (Nat {resNat})"
								else :
									await ctx.send(f"Un problème est survenu : je suis incapable de comparer ta stat avec le dé. Voici ton résultat :\n{result}")
						await ctx.send(message)
						break
			else :
				await ctx.send(f"Un problème est survenu.")
		else :
			await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
			await CHANNLOG.send(f"LOG MESSAGE - rr - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu lancer un dé de dégât {statDegNature} avec un personnage inexistant : {name}")
	else :
		await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
		await CHANNLOG.send(f"LOG MESSAGE - rr - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu lancer un dé de dégât {statDegNature} avec le personnage {name} mais ne possède pas de dossier de sauvegarde")
	os.chdir(initPath)

@bot.command(pass_context = True)
async def mod(ctx, stat, modif = '0', dep = 'n'): # 'modif' = valeur de la modification  |  'dep' = dépassement autorisé OU valeur du set de pv
	" - Modifie l'état d'une jauge"
	CHANNLOG = bot.get_channel(CHANNLOGID)
	userID = str(ctx.author.id)
	userName = str(ctx.author.name)
	selFile = userID + '.json'
	os.chdir(initPath)
	
	# Ce passage sert à entrer dans le dossier correspondant et à en sortir la variable à modifier
	try :
		if os.path.exists(userID) :
			os.chdir(userID)
			if debug >= 2 :
				print(f"PP : entrée dans le dossier {userID}")
			if os.path.exists(selFile) :
				with open(selFile, 'r') as f :
					data = json.load(f)
					filename = data["CharSelected"]
				if debug >= 2 :
					print(f"PP : lecture du fichier {userID}.json")
				if os.path.exists(filename) :
					with open(filename, 'r') as f :
						data = json.load(f)
						name = data["Name"]
						statValue = data["Stats"]
						if debug >= 2 :
							print(statValue)
					
					statDegNature = ''
					DEGmode = 0
					if debug >= 2 :
						print(f"PP : lecture du fichier {name}.json")
					for i in range (len(statValue)) :
						if debug >= 2 :
							print(statValue[i])
							print("\nAnalyse des 3 premiers caractères :", statValue[i][0][:3])
						try :
							if statValue[i][0][:3] == "JAU" : # Vérifie si la stat utilisée est une stat de dégâts ou non
								statDegNature = statValue[i][0][3:]
								DEGmode = 2
								if debug >= 2 :
									print("STATDEGNATURE =", statDegNature)
							else :
								DEGmode = 0
						except :
							pass
						
						if stat == statValue[i][0] or stat == statDegNature :
							
							if debug >= 2 :
								print(f"PP : entrée dans le mode jet avec DEGmode = {DEGmode}")

							if DEGmode == 2 : # Affiche et / ou met à jour la jauge
								jauDepart = statValue[i][1] # Garde e mémoire la valeur actuelle AVANT le changement
								if debug >= 1 :
									print(f"Modif = {modif}")
								
								message = ''
								
								# Si le 'try' ne génère pas d'erreur : modifie la jauge avec une addition ou soustraction
								try :
									modif = int(modif)
									if modif == 0 :
										await ctx.send(f"**{name}**\n{statDegNature} :\t{statValue[i][1]}\t/\t{statValue[i][2]}")
										
									elif modif != 0 :
										
										if dep == "y" or dep == "Y" : # Autorise ou interdit le dépassement (négatif ou positif)
											deppos = 1
											depneg = 1
										else :
											deppos = 0
											depneg = 0
										if statValue[i][1] > statValue[i][2] :
											deppos = '1'
										if statValue[i][1] < statValue[i][3] :
											depneg = '1'
											if debug >= 1 :
												print(f"{statDegNature} : Nbre actuel déjà supérieur à Nbre max")
												
										statValue[i][1] = statValue[i][1] + modif
										if debug >= 1 :
											print(f"statValue[i][1] = statValue[i][1] + modif / {statValue[i][1]} = {statValue[i][1] - modif} + {modif}")
										if statValue[i][1] > statValue[i][2] and deppos == 0 :
											stopDep = statValue[i][1] - statValue[i][2]
											statValue[i][1] = statValue[i][2]
											message = f"{stopDep} point(s) positifs ont été effacés pour ne pas dépasser la limite supérieure de {statValue[i][2]}"
											if debug >= 1 :
												print(f"statValue[i][1] = statValue[i][1] + modif / {statValue[i][1]} = {statValue[i][1]} + {modif}")
										elif statValue[i][1] > statValue[i][2] :
											message = f"{statDegNature} dispose de {statValue[i][1] - statValue[i][2]} de dépassement"
										
										if statValue[i][1] < statValue[i][3] and depneg == 0 :
											stopDep = statValue[i][1] - statValue[i][3]
											statValue[i][1] = statValue[i][3]
											message = f"{stopDep} point(s) négatifs ont été effacés pour ne pas dépasser la limite inférieure de {statValue[i][3]}"
											if debug >= 1 :
												print(f"statValue[i][1] = statValue[i][1] + modif / {statValue[i][1]} = {statValue[i][1]} + {modif}")
										elif statValue[i][1] > statValue[i][2] :
											message = f"{statDegNature} dispose de {statValue[i][1] - statValue[i][2]} de dépassement"
											
										await ctx.send(f"**{name}**\n{statDegNature} :\t{statValue[i][1]}\t/\t{statValue[i][2]}\n{message}")
										data["Stats"] = statValue
										with open(filename, 'w') as f :
											json.dump(data, f, indent = 4)
								
								# Si le 'try' a généré une erreur : vérifie la présence d'un argument comme "max", "min" ou "set"
								except :
									if modif == "max" or modif == "Max" or modif == "MAX" : # Set la jauge à sa valeur maximale
										if debug >= 1 :
											print(f"{statValue[i][0]} ({statValue[i][1]}) set à {statValue[i][2]}")
										statValue[i][1] = statValue[i][2]
										message += f"Jauge de {stat} fixée à son maximum\n||{jauDepart} > **{statValue[i][1]}**||"
									elif modif == "min" or modif == "Min" or modif == "MIN" : # Set la jauge à sa valeur maximale
										if debug >= 1 :
											print(f"{statValue[i][0]} ({statValue[i][1]}) set à **{statValue[i][3]}**")
										statValue[i][1] = statValue[i][3]
										message += f"Jauge de {stat} fixée à son minimum \n||{jauDepart} > **{statValue[i][1]}**||"
									elif modif == "set" or modif == "Set" or modif == "SET" : # Set la jauge à la valeur indiquée
										try :
											dep = int(dep)
											if debug >= 1 :
												print(f"{statValue[i][0]} ({statValue[i][1]}) set à {dep}")
											statValue[i][1] = dep
											message += f"Jauge de {stat} fixée à {dep}\n||{jauDepart} > **{statValue[i][1]}**||"
										except :
											await ctx.send(f"Pour la commande '{prefix}mod set', une valeur numérique supplémentaire est attendue.")
											await CHANNLOG.send(f"LOG MESSAGE - mod set - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu set {stat} sans indiquer la valeur du set")
									else :
										await ctx.send(f"Aucune commande '{prefix}mod {modif}', n'est actuellement existante.")
										await CHANNLOG.send(f"LOG MESSAGE - mod - fail\nL'utilisateur **{userName}** (ID : {userID}) a essayé la commande '{prefix}mod {modif}'")
									
									with open(filename, 'w') as f :
											json.dump(data, f, indent = 4)
											
									await ctx.send(f"**{name}**\n{statDegNature} :\t**{statValue[i][1]}**\t/\t**{statValue[i][2]}**\n{message}")
									
								break
							else :
								await ctx.send(f"Un attribut {stat} de type non-jauge a été trouvé")
				else :
					await ctx.send(f"Un problème est survenu : aucun personnage n'a été sélectionné, ou il n'existe pas.")
			else :
				await ctx.send(f"Aucun personnage nommé {name} n'a été trouvé dans ton dossier de sauvegarde.\nPour en créer un, utiliser la commande 'charsave'.")
				await CHANNLOG.send(f"LOG MESSAGE - mod - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu modifier {stat} avec un personnage inexistant : {name}")
		else :
			await ctx.send("Aucun dossier de sauvegarde n'a été trouvé.\nPour en créer un, utiliser la commande 'signup'.")
			await CHANNLOG.send(f"LOG MESSAGE - mod - fail\nL'utilisateur **{userName}** (ID : {userID}) a voulu modifier {stat} avec le personnage {name} mais ne possède pas de dossier de sauvegarde")
	except :
		await ctx.send(f"Problème")
		os.chdir(initPath)


bot.run(TOKEN)
