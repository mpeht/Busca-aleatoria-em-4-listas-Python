import random

poesia01 = ["um", "uma", "o", "a", "ele", "ela", "eu", "você", "nós"];
poesia02 = ["rapaz", "garota", "gato", "cachorro", "idoso", "idosa", "cavalo", "borboleta"];
poesia03 = ["andar", "subir", "descer", "bater", "cozinhar", "trabalhar", "cheirar", "dirigir"];
poesia04 = ["carro", "escada", "avião", "panela", "martelo", "uvas", "caminhão", "berço"];
lista = [poesia01, poesia02, poesia03, poesia04]
i = 0
elemento01 = ""
elemrento02 = ""
elemento03 = ""
elemento04 = ""
for i in range(0, 5):
    
    elemento01 = random.choice(poesia01)
    elemento02 = random.choice(poesia02)
    elemento03 = random.choice(poesia03)
    elemento04 = random.choice(poesia04)
    print(elemento01, elemento02, elemento03, elemento04)    
    