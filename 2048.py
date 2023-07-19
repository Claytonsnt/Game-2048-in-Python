#A proposta do projeto é criar o jogo 2048
import random
import os


def main():
     global tabuleiro, mov, posicoes
     tabuleiro = [0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]    
     
     mov = ["w", "s", "d", "a"]    
     posicoes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
     tabRand()
     tabRand()
     jogo()

def imprimir():
    count = 0    
    for i in tabuleiro:         
         print("|"," "*1,i,end=" "*2)
         count +=1
         if count == 4:
              print("|\n")
              count = 0

def numRand():
     rand = [2, 4]
     num = random.choice(rand)
     return num

def tabRand():
     rand = random.randint(0, 15)
     while tabuleiro[rand] != 0:
          rand = random.randint(0, 15)                 
     
     tabuleiro[rand] = numRand()


def movimentos(m):     
     paredew = [0, 1, 2, 3]
     paredes = [12, 13, 14, 15]
     paredea = [0, 4, 8, 12]
     pareded = [3, 7, 11, 15]
     casasw = [4, 8, 12, 5, 9, 13, 6, 10, 14, 7, 11, 15]
     casass = [8, 4, 0, 9, 5, 1, 10, 6, 2, 11, 7, 3]
     casasa = [13, 14, 15, 9, 10, 11, 5, 6, 7, 1, 2, 3]
     casasd = [14, 13, 12, 10, 9, 8, 6, 5, 4, 2, 1, 0]
     if m == 'w':
          movs(casasw, paredew, -4)
     if m == 's':
          movs(casass, paredes, 4)
     if m == 'a':
          movs(casasa, paredea, -1)
     if m == 'd':
          movs(casasd, pareded, 1)

def movs(casas, parede, move):     
     for i in casas:
          while True:
               if tabuleiro[i] != 0:
                    if not((i+move) in posicoes):                         
                         break

                    if (tabuleiro[i+move] != 0 and tabuleiro[i+move] != tabuleiro[i]) or (i in parede):
                         break
                    
                    if tabuleiro[i+move] == tabuleiro[i]:                         
                         tabuleiro[i+move] = tabuleiro[i+move]*2                              
                         tabuleiro[i] = 0                         
                         break                         

                    if tabuleiro[i+move] == 0:                         
                         tabuleiro[i+move] = tabuleiro[i]
                         tabuleiro[i] = 0
                         i+=move                         
               else:
                    break

     for i in posicoes:
          if tabuleiro[i] == 2048:
                    print("--------Você ganhou!--------")
                    imprimir()
                    #g = input("Se Deseja continuar o jogo pressione [s]: ").lower()
                    #if g == 's':
                    #     break
                    #else:
                    #     return
     tabRand()
     jogo()

def jogo():       
     
     while not gameover():
          os.system('cls')          
          imprimir()
          m = input("\nDigite o comando: ").lower()
          while m not in mov:
               os.system('cls')
               imprimir()
               m = input("\nDigite um movimento válido: ").lower()
          movimentos(m)
     if gameover() == True:
          print("NÃO HÁ MAIS MOVIMENTOS POSSÍVEIS! =[")
          

def menu():
     print("JOGO 2048")
     print("MOVIMENTOS DO JOGO: \n'W' ou 'w': Mover para cima \n'S' ou 's': Mover para baixo \n'A' ou 'a': Mover para esquerda \n'D' ou 'd': Mover para direita \n")
     r = input("\nAperte [i] caso deseje inicar o jogo ou [s] caso deseje fechar o programa! ").lower()
     if r == 'i':
          print("JOGO INICIADO!")
          main()
     else:
          exit()

def gameover():
     for i in posicoes:
          if tabuleiro[i] == 0:
               return False
          if tabuleiro[i] == tabuleiro[i+1]:
               return False
          if tabuleiro[i] == tabuleiro[i-1]:
               return False
          if tabuleiro[i] == tabuleiro[i+4]:
               return False
          if tabuleiro[i] == tabuleiro[i-4]:
               return False
     return True

menu()