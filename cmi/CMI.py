from tkinter import filedialog

from cipher import Cipher


def encrypt_file():
    input("entrer pour chiffrer un fichier")
    file = filedialog.askopenfilename(filetypes=[("Fichier PBM", "pbm")], title="séléctionner *.pbm")
    password = input("mot de passe:")
    destination = filedialog.asksaveasfilename(filetypes=[("Fichier PBM", "pbm")], title="séléctionner *.pbm")
    stream = open(file, "r")

    content = stream.read().split("\n")
    head = "\n".join(content[0:2])
    content = "".join(content[2:]).split(" ")
    content = [int(b) for b in content if b != '']
    print("chiffrage en cours, cela va prendre un moment...")
    encrypted = Cipher.encrypt(content, password)
    print("chiffrage terminé !")
    s = open(destination, "w")
    fileContent = head + "\n" + " ".join([str(x) for x in encrypted])
    s.write(fileContent)
    s.close()
    stream.close()
    print("le fichier chiffré a bien été sauvegardé dans", destination)

print("Bienvenue dans mon super programme de la mort qui tue")
while True:
    try:
        encrypt_file()
    except Exception as e:
        print()
        print("Erreur ! " + str(e))
