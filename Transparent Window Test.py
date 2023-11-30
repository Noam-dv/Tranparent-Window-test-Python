import ctypes, pygame
class CPPVersion:
    def __init__(self):
        self.user32 = ctypes.windll.user32

    def window(self):
        hWnd = self.user32.CreateWindowExW(
            0x00000020, "STATIC", "transparent window!!!!!!!!", 0x80000000 | 0x10000000,
            100, 100, 160, 20,
            0, 0, 0, 0
        )
        self.user32.SetLayeredWindowAttributes(hWnd, 0, 200, 2)
        return hWnd

class PygameVersion:
    def __init__(self, image_path, window_title='pygame transparent window test'):
        pygame.init()
        self.window_title = window_title
        self.image = pygame.image.load(image_path)
        self.screen = pygame.display.set_mode((620, 625), pygame.NOFRAME)
        self.screen.set_alpha(200)
        self.clock = pygame.time.Clock()

    def display_image(self):
        self.screen.blit(self.image, (0, 0))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: running = False
            self.display_image()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    cpp = CPPVersion()
    cpp.window()
    pg =PygameVersion(r"./p.png")
    pg.run()