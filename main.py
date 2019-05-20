import pygame #importamos librería pygame
import sys #importamos librería system

#pendiente de hacer class runner(): con la imagen, atributos, métodos propios, etc

class Game():#clase llamada Game()
    corredores=[]#lista para guardar corredores
    
    def __init__(self):#función constructora de objetos
        self.__screen = pygame.display.set_mode((640,480))#iniciamos pantalla dando tamaño
        pygame.display.set_caption("Carrera de bichos")#nombre para la pantalla
        self.background = pygame.image.load("images/desert.png")#imagen de fondo de pantalla
        
        self.runner = pygame.image.load("images/runner.png")#cargo imagen para un corredor
    
    def competir(self):
        x=0
        hayGanador = False
        while not hayGanador:
            #comprobación de eventos
            for event in pygame.event.get():#para cada evento en la obtencion de eventos para pygame
                if event.type == pygame.QUIT:#si el tipo de evento es igual a quitar pygame
                    pygame.quit()#quitar pygame
                    sys.exit()#salida de sistema (opcion muy bestia, no es bueno usarla)
            
            self.__screen.blit(self.background, (0,0))#pintamos el fondo y damos coordenadas que empiezan arriba a la izquierda
            self.__screen.blit(self.runner, (x,240))#colocamos a corredor en las coordenadas dadas respecto de arriba a la izquierda
            pygame.display.flip()# función refrescar/renderizar pantalla, cogida directamente de la librería pygame
            
            x += 3#aumentamos x de pantalla de 3 en 3
            if x >= 400:#si x es igual a 250, hayGanador pasará a true y saldremos del bucle while
                hayGanador = True#asignamos variable a booleano true
                        
        print("Tenemos un ganador.")#imprimimos 
        pygame.quit()#quitar pygame
        sys.exit()#salida de sistema (opcion muy bestia, no es bueno usarla)
    

if __name__== "__main__":#compruebo si es fichero principal main.py
    pygame.init()#inicializo librería pygame
    game = Game()#asigno objeto a variable
    game.competir()#invocamos a función competir
        
        
        
