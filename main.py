import pygame

from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    _ = pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = pygame.Surface.fill(screen,"black")
        dt = clock.tick(60) / 1000
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
