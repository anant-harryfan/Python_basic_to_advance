import pygame
from sys import exit
from random import randint
from random import choice

# sprites is used to make all code for player and obstacle in one class and help to organizes our code
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("Resources/graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("Resources/graphics/Player/player_walk_2.png").convert_alpha()
        # importing images with slightly different
        self.player_walk = [player_walk_1, player_walk_2]
        self.playerIndex = 0
        self.player_jump = pygame.image.load("Resources/graphics/Player/jump.png").convert_alpha()
        self.image = self.player_walk[self.playerIndex]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        # to add volume we need pygame.mixer.Sound(path)
        self.jump_sound = pygame.mixer.Sound("Resources/audio/audio_jump.mp3")
        # to set vol arg: vol 0<your number<1 where 1 is full sound and 0 is mute
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        """Help to get player input"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        """Help to apply gravity in game"""
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        """Help to create animation for player"""
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.playerIndex += 0.1
            if self.playerIndex >= len(self.player_walk):
                self.playerIndex = 0
            self.image = self.player_walk[int(self.playerIndex)]

    def update(self):
        """Now we do not want to mes up by calling all func one by in in game loop so we use update which call all func of the class"""
        self.player_input()
        self.apply_gravity()
        self.animation_state()
# defining obstacle class to detect collide with them
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fly":
            fly_frame1 = pygame.image.load('Resources/graphics/fly/fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('Resources/graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('Resources/graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('Resources/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))


    def animation_state(self):
        """Help to animate obstacle"""
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        """Destroy the not useful self.rect.x value which is gone form the screen"""
        if self.rect.x <= -100:
            self.kill()
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time
def collision_sprite():
    # help to get a list that where are sprites collide (very useful)
    # 1st arg: sprite, 2nd ard: group, 3rd arg: bool(use for if sprites collide so we want to destroy it or not)
    # when we initialize player it didn't become sprite so we now make it a sprite by pygame func
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PygameAwesome")
game_active = False
clock = pygame.time.Clock()
bg_music = pygame.mixer.Sound("Resources/audio/music.wav")
bg_music.play(loops=-1)  # there is a agrs loop, we can use it to tell pygame that till how many times we have to play this music, -1 means forever

sky_surface = pygame.image.load("Resources/graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("Resources/graphics/ground.png").convert_alpha()

test_font = pygame.font.Font("Resources/font/Pixeltype.ttf", 50)

scoreEndSurf = test_font.render("Keshav", False, (111, 195, 169))
scoreEmdRect = scoreEndSurf.get_rect(midbottom=(400, 100))
infoEndSurf = test_font.render("Press space to run", False, (111, 195, 169))
infoEmdRect = infoEndSurf.get_rect(midbottom=(400, 350))

# group
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

player_stand = pygame.image.load("Resources/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # collisions
        game_active = collision_sprite()
    elif not game_active:
        start_time = int(pygame.time.get_ticks() / 1000)
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        player_gravity = 0
        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(scoreEndSurf, scoreEmdRect)
        if score == 0:
            start_time = int(pygame.time.get_ticks() / 1000)
            screen.blit(infoEndSurf, infoEmdRect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)