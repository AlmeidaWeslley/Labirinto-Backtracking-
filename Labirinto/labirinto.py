import random
import time


class MazeGenerator:
    #cria o objeto da classe ja com uma matriz com o tamanho passado,
    #  e completamente preenchida com paredes('#')
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['#' for _ in range(width)] for _ in range(height)]
        self.player_x = None
        self.player_y = None

    # cria os caminhos do labirinto
    def generate_maze(self):
        walls = [(1, 1)]
        self.maze[1][1] = '.'

        while walls:
            x, y = walls.pop(random.randint(0, len(walls) - 1))
            # Chama o metodo para criar os caminhos
            self._carve_path(x, y, walls)

        # Chama o metodo que cria a saida do labirinto
        self._add_exit()

        # Colocando o jogador na posição (1,1) do labirinto
        self.player_x = 1
        self.player_y = 1
        self.maze[self.player_x][self.player_y] = 'P'

    def _carve_path(self, x, y, walls):
        # Escolhe aleatoriamente uma das tuplas que está dentro de 'directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        # Realiza um calculo com a tupla escolhida para colocar os caminhos
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2

            # Confere se o calculo realizado na tupla pode ser utilizado,
            # se for valido, coloca o caminho, se não, realiza outro sorteio e calculos
            if self._is_valid_position(nx, ny):
                self.maze[nx][ny] = '.'
                self.maze[x + dx][y + dy] = '.'
                walls.append((nx, ny))

    # Confere se os dados passado são validos
    def _is_valid_position(self, x, y):
        return x >= 0 and x < self.height and y >= 0 and y < self.width and self.maze[x][y] == '#'

    # def _is_valid_position_move(self, x, y):
    #     return x >= 0 and x < self.height and y >= 0 and y < self.width and (self.maze[x][y] == '.' or self.maze[x][y] == 'S' or self.maze[x][y] == '-')
    

    # def move_player(self):
        
    #     new_x = self.player_x
    #     new_y = self.player_y

    #     if (self.maze[new_x + 1][new_y] == '.') or (self.maze[new_x + 1][new_y]  == 'S'):
    #         new_x += 1
    #     elif (self.maze[new_x][new_y + 1] == '.') or (self.maze[new_x][new_y + 1] == 'S'):
    #         new_y += 1
    #     elif (self.maze[new_x][new_y - 1] == '.') or (self.maze[new_x][new_y - 1] == 'S'):
    #         new_y -= 1
    #     elif (self.maze[new_x - 1][new_y] == '.') or (self.maze[new_x - 1][new_y] == 'S'):
    #         new_x -= 1
        

    #     if (self.maze[new_x - 1][new_y] == '-') or (self.maze[new_x - 1][new_y] == 'S'):
    #         new_x -= 1
    #     elif (self.maze[new_x][new_y - 1] == '-') or (self.maze[new_x][new_y - 1] == 'S'):
    #         new_y -= 1
    #     elif (self.maze[new_x][new_y + 1] == '-') or (self.maze[new_x][new_y + 1] == 'S'):
    #         new_y += 1
    #     elif (self.maze[new_x + 1][new_y] == '-') or (self.maze[new_x + 1][new_y]  == 'S'):
    #         new_x += 1
        


    #     if direction == 'w':
    #         new_x -= 1
    #     elif direction == 's':
    #         new_x += 1
    #     elif direction == 'a':
    #         new_y -= 1
    #     elif direction == 'd':
    #         new_y += 1


    #     if self._is_valid_position_move(new_x, new_y):
    #         if self.maze[new_x][new_y] == 'S':
    #             self.maze[self.player_x][self.player_y] = '-'
    #             self.player_x = new_x
    #             self.player_y = new_y
    #             self.maze[self.player_x][self.player_y] = 'P'
    #             return True
    #         else:
    #             self.maze[self.player_x][self.player_y] = '-'
    #             self.player_x = new_x
    #             self.player_y = new_y
    #             self.maze[self.player_x][self.player_y] = 'P'
    #     else:
    #         pass
            

    # Metodo que cria a saida do labirinto em uma posição aleatoria, no final inferior do labirinto
    def _add_exit(self):
        exit_x = random.choice(range(1, self.width, 2))
        self.maze[self.height - 1][exit_x] = 'S'

    # Mostra na tela o labirinto
    def print_maze(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        for row in self.maze:
            print(' '.join(row))
    
    # Metodo recursivo para mover o player utilizando backtracking
    def move_player(self, new_x, new_y):
        # Confere se a nova posição esta fora do tamanho do labirinto
        if new_x < 0 or new_x >= self.width or new_y < 0 and new_y >= self.height:
            return False
        
        # Confere se a nova posição é uma parede ou um caminho já percorrido
        if self.maze[new_x][new_y] == '#' or self.maze[new_x][new_y] == '-':
            return False

        # Confere se a nova posição é a saída do labirinto
        if self.maze[new_x][new_y] == 'S':
            time.sleep(0.2)
            print('')
            self.print_maze()
            
            self.maze[self.player_x][self.player_y] = '-'
            self.player_x = new_x
            self.player_y = new_y
            self.maze[self.player_x][self.player_y] = 'P'
            return True
        
        time.sleep(0.2)
        print('')
        self.print_maze()

        # Movimenta o jogador para a nova posição encontrada
        self.maze[self.player_x][self.player_y] = '-'
        self.player_x = new_x
        self.player_y = new_y
        self.maze[self.player_x][self.player_y] = 'P'

        # Condições para saber se o jogador pode mover para determinada posição
        if self.move_player(new_x - 1, new_y):  # Up
            return True
        if self.move_player(new_x + 1, new_y):  # Down
            return True
        if self.move_player(new_x, new_y - 1):  # Left
            return True
        if self.move_player(new_x, new_y + 1):  # Right
            return True
        
        
        # self.maze[new_x][new_y] = '-'
        # time.sleep(0.2)
        # print('')
        return False
    
    # Metodo para a inicialização da movimentação do personagem
    def play(self):
        self.move_player(self.player_x, self.player_y)
        self.print_maze()

        print("Voce ganhou!")


# Exemplo de uso
width = 11
height = 11

# Cria o objeto da classe MazeGenerator
generator = MazeGenerator(width, height)

# Chama o Metodo para criação dos caminhos do labirinto
generator.generate_maze()

# Chama o metodo de mostrar o labirinto na tela
generator.print_maze()

# Chama a função de começar a movimentação do personagem
generator.play()

# while True:
#     aux = generator.move_player()
#     generator.print_maze()
#     if aux:
#         print("Você ganhou!")
#         break

# while True:
#     direction = input("Digite a direção para mover o jogador (u-up/d-down/l-left/r-right) ou 'q' para sair: ")
#     if direction == 'q':
#         break
#     aux = generator.move_player()
#     generator.print_maze()
#     if aux:
#         print("Você ganhou!")
#         break

