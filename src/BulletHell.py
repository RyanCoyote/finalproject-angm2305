import pygame



class Projectile():

    def __init__(self, pos=(0,0), size =20, life=1000, shape='rectangle'):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('Orange')
        self.age = 0.0
        self.alpha = 255
        self.surface = self.update_surface()
        self.dead = False
        self.shape = shape


    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - self.age / self.life)
    

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        if self.dead == True:
            return
        self.surface.set_alpha(self.alpha)
        if self.shape == 'rectangle':
            pygame.draw.rect(self.surface, self.color, (200, 150, 100, 50))
        else:
            pygame.draw.circle(self.surface, self.color, self.pos, self.size)
    
'''
class ProjectileTrail():

    def __init__(self, pos, size, life):
    
class ProjectilePattern():

    def __init__(self, screen_res):

class PlayerObject():

    def __init(self):
'''

def main():
    pygame.init()
    pygame.display.set_caption("Bullet Hell")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (1280, 720)
    screen = pygame.display.set_mode(resolution)
    projectile = Projectile()
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False

        # Add update function here later for projectiles

        screen.fill('Black')
        # Call on draw function here later
        projectile.draw(screen)
        pygame.display.flip()
        dt = clock.tick(64)
    pygame.quit()


if __name__ == "__main__":
    main()