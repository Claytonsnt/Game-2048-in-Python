#A proposta do projeto é criar o jogo 2048 usando POO

import random
import os

class Game2048:
    def __init__(self):
        self.tabuleiro = [0,0,0,0,
                          0,0,0,0,
                          0,0,0,0,
                          0,0,0,0]  
        self.posicoes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.mov = ["w", "s", "d", "a"]
        self.tabrand()
        self.tabrand()
    

    def tabrand(self):
        numrand = [2, 4]
        rand = random.randint(0, 15)
        while self.tabuleiro[rand] != 0:
            rand = random.randint(0, 15)   

        self.tabuleiro[rand] = random.choice(numrand) 

    def imprimir(self):
        count = 0    
        for i in self.tabuleiro:         
            print("|"," "*1,i,end=" "*2)
            count +=1
            if count == 4:
                print("|\n")
                count = 0   

    def movs(self, m):

        paredew = [0, 1, 2, 3]
        paredes = [12, 13, 14, 15]
        paredea = [0, 4, 8, 12]
        pareded = [3, 7, 11, 15]
        casasw = [4, 8, 12, 5, 9, 13, 6, 10, 14, 7, 11, 15]
        casass = [8, 4, 0, 9, 5, 1, 10, 6, 2, 11, 7, 3]
        casasa = [13, 14, 15, 9, 10, 11, 5, 6, 7, 1, 2, 3]
        casasd = [14, 13, 12, 10, 9, 8, 6, 5, 4, 2, 1, 0]

        if m == 'w':            
            casas = casasw
            parede = paredew
            move = -4
        if m == 's':            
            casas = casass
            parede = paredes
            move = 4
        if m == 'a':            
            casas = casasa
            parede = paredea
            move = -1
        if m == 'd':            
            casas = casasd
            parede = pareded
            move = 1

        for i in casas:
            while True:
                if self.tabuleiro[i] !=0:
                    if not((i+move) in self.posicoes):                         
                            break
                    if not((i+move) in self.posicoes):                         
                            break

                    if (self.tabuleiro[i+move] != 0 and self.tabuleiro[i+move] != self.tabuleiro[i]) or (i in parede):
                            break
                        
                    if self.tabuleiro[i+move] == self.tabuleiro[i]:                         
                            self.tabuleiro[i+move] = self.tabuleiro[i+move]*2                              
                            self.tabuleiro[i] = 0                         
                            break                         

                    if self.tabuleiro[i+move] == 0:                         
                            self.tabuleiro[i+move] = self.tabuleiro[i]
                            self.tabuleiro[i] = 0
                            i+=move                         
                else:
                        break
        for i in self.posicoes:
          if self.tabuleiro[i] == 2048:
                    print("--------Você ganhou!--------")
                    #imprimir()


    def gameover(self):
     for i in self.posicoes:
          if self.tabuleiro[i] == 0:
               return False
          if self.tabuleiro[i] == self.tabuleiro[i+1]:
               return False
          if self.tabuleiro[i] == self.tabuleiro[i-1]:
               return False
          if self.tabuleiro[i] == self.tabuleiro[i+4]:
               return False
          if self.tabuleiro[i] == self.tabuleiro[i-4]:
               return False
     return True

def inicial():
     print("JOGO 2048")
     print("MOVIMENTOS DO JOGO: \n'W' ou 'w': Mover para cima \n'S' ou 's': Mover para baixo \n'A' ou 'a': Mover para esquerda \n'D' ou 'd': Mover para direita \n")
     r = input("\nAperte [i] caso deseje inicar o jogo ou [s] caso deseje fechar o programa! ").lower()
     if r == 'i':
          print("JOGO INICIADO!")
          main()
     else:
          exit()

def main():
    game = Game2048()    

    while not game.gameover():
        os.system('cls')          
        game.imprimir()
        m = input("\nDigite o comando: ").lower()    
        while m not in game.mov:
            #os.system('cls')
            game.imprimir()
            m = input("\nDigite um movimento válido: ").lower()
        game.movs(m)
        game.tabrand()               
    if game.gameover() == True:
        print("NÃO HÁ MAIS MOVIMENTOS POSSÍVEIS! =[")

inicial()


