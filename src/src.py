import pygame



class Projectile():

    def __init__(self, pos=(0,0), size =20, life=1000):

    def update(self, dt):

    def update_surface(self):
    
    def draw(self, surface):
    

class ProjectileTrail():

    def __init__(self, pos, size, life):
    
class ProjectilePattern():

    def __init__(self, screen_res):

class PlayerObject():

    def __init(self):

def main():
    pygame.init()
    pygame.display.set_caption("Bullet Hell")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False

        # Add update function here later for projectiles

        screen.fill('Black')
        # Call on draw function here later
        pygame.display.flip()
        dt = clock.tick(64)
    pygame.quit()


if __name__ == "__main__":
    main()