import pygame
from .player import Player
from .obstacle import Obstacle

# Game Engine

WHITE = (255, 255, 255)
BROWN = (120, 80, 40)
DARK_GREEN = (30, 100, 30)
BLACK = (0, 0, 0)


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_y = height - 40

        # ---------------------------------------------------------
        # TASK 4: Sound initialization
        # ---------------------------------------------------------
        self.jump_sound = pygame.mixer.Sound("sounds/jump.wav")
        self.score_sound = pygame.mixer.Sound("sounds/score.mp3")
        self.game_over_sound = pygame.mixer.Sound(
            "sounds/game_over.mp3"
        )

        # Player
        self.player = Player(80, self.ground_y)

        # ---------------------------------------------------------
        # TASK 1: Speed control
        # ---------------------------------------------------------
        self.speed = 6
        self.max_speed = 12
        self.speed_increase_per_frame = 0.003

        # ---------------------------------------------------------
        # TASK 3: Difficulty settings
        # ---------------------------------------------------------
        self.difficulties = {
            "Easy": {
                "speed": 4,
                "spawn_interval": 85
            },
            "Medium": {
                "speed": 6,
                "spawn_interval": 70
            },
            "Hard": {
                "speed": 8,
                "spawn_interval": 55
            }
        }

        self.current_difficulty = "Medium"

        self.spawn_interval = 70
        self._spawn_timer = 0

        self.obstacles = []

        self.distance = 0
        self.score = 0

        # Fonts
        self.font = pygame.font.SysFont("Arial", 30)

        self.game_over_font = pygame.font.SysFont(
            "Arial", 60, bold=True
        )

        self.final_score_font = pygame.font.SysFont(
            "Arial", 35
        )

        self.instruction_font = pygame.font.SysFont(
            "Arial", 25
        )

        self.difficulty_font = pygame.font.SysFont(
            "Arial", 40, bold=True
        )

        # Game states
        self.game_over = False
        self.difficulty_select = False

    # -------------------------------------------------------------
    # EVENT HANDLING
    # -------------------------------------------------------------
    def handle_event(self, event):

        if event.type != pygame.KEYDOWN:
            return

        # PLAYING STATE
        if not self.game_over and not self.difficulty_select:

            if event.key in (
                pygame.K_SPACE,
                pygame.K_UP,
                pygame.K_w
            ):
                self.player.jump()

                # TASK 4: Jump sound
                if not self.player.on_ground:
                    self.jump_sound.play()

        # GAME OVER STATE
        elif self.game_over:

            # R = Play Again
            if event.key == pygame.K_r:
                self.game_over = False
                self.difficulty_select = True

            # ESC = Exit
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(
                    pygame.event.Event(pygame.QUIT)
                )

        # DIFFICULTY SELECTION STATE
        elif self.difficulty_select:

            if event.key == pygame.K_1:
                self.start_new_game("Easy")

            elif event.key == pygame.K_2:
                self.start_new_game("Medium")

            elif event.key == pygame.K_3:
                self.start_new_game("Hard")

            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(
                    pygame.event.Event(pygame.QUIT)
                )

    # -------------------------------------------------------------
    # INPUT
    # -------------------------------------------------------------
    def handle_input(self):
        pass

    # -------------------------------------------------------------
    # START NEW GAME
    # -------------------------------------------------------------
    def start_new_game(self, difficulty):

        self.current_difficulty = difficulty

        settings = self.difficulties[difficulty]

        # Reset player
        self.player = Player(
            80,
            self.ground_y
        )

        # Reset obstacles
        self.obstacles = []

        # Reset score
        self.score = 0

        # Reset distance
        self.distance = 0

        # Reset spawn timer
        self._spawn_timer = 0

        # Set starting speed
        self.speed = settings["speed"]

        # Set spawn interval
        self.spawn_interval = settings["spawn_interval"]

        # Reset game states
        self.game_over = False
        self.difficulty_select = False

    # -------------------------------------------------------------
    # GAME UPDATE
    # -------------------------------------------------------------
    def update(self):

        if self.game_over or self.difficulty_select:
            return

        # TASK 1: Speed limit
        self.speed = min(
            self.speed + self.speed_increase_per_frame,
            self.max_speed
        )

        self.player.update()

        self._spawn_timer += 1

        if self._spawn_timer >= self.spawn_interval:

            self._spawn_timer = 0

            self.obstacles.append(
                Obstacle(
                    self.width,
                    self.ground_y,
                    self.speed
                )
            )

        # Move obstacles and check collisions
        for obstacle in self.obstacles:

            # TASK 1: Save previous position
            previous_x = obstacle.x

            obstacle.move()

            obstacle.speed = self.speed

            # Normal collision
            if obstacle.rect().colliderect(
                self.player.rect()
            ):
                self.game_over = True

                # TASK 4: Game-over sound
                self.game_over_sound.play()

                return

            # TASK 1: High-speed crossing detection
            player_rect = self.player.rect()

            previous_right = (
                previous_x + obstacle.width
            )

            current_right = (
                obstacle.x + obstacle.width
            )

            crossed_player = (
                previous_right >= player_rect.left
                and current_right <= player_rect.right
                and obstacle.y < player_rect.bottom
                and obstacle.y + obstacle.height > player_rect.top
            )

            if crossed_player:
                self.game_over = True

                # TASK 4: Game-over sound
                self.game_over_sound.play()

                return

        # Score obstacles that passed the player
        for obstacle in self.obstacles:

            if (
                not obstacle.scored
                and obstacle.x + obstacle.width < self.player.x
            ):
                obstacle.scored = True
                self.score += 1

                # TASK 4: Score sound
                self.score_sound.play()

        # Remove off-screen obstacles
        self.obstacles = [
            obstacle
            for obstacle in self.obstacles
            if not obstacle.off_screen()
        ]

        self.distance += self.speed

    # -------------------------------------------------------------
    # RENDER
    # -------------------------------------------------------------
    def render(self, screen):

        pygame.draw.line(
            screen,
            BROWN,
            (0, self.ground_y),
            (self.width, self.ground_y),
            4
        )

        pygame.draw.rect(
            screen,
            WHITE,
            self.player.rect()
        )

        for obstacle in self.obstacles:

            pygame.draw.rect(
                screen,
                DARK_GREEN,
                obstacle.rect()
            )

        # Score
        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            BLACK
        )

        screen.blit(
            score_text,
            (10, 10)
        )

        # ---------------------------------------------------------
        # TASK 2 + TASK 3: GAME OVER SCREEN
        # ---------------------------------------------------------
        if self.game_over:

            overlay = pygame.Surface(
                (self.width, self.height),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 170)
            )

            screen.blit(
                overlay,
                (0, 0)
            )

            # GAME OVER
            game_over_text = self.game_over_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            game_over_rect = game_over_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2 - 80
                )
            )

            screen.blit(
                game_over_text,
                game_over_rect
            )

            # Final score
            final_score_text = self.final_score_font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            final_score_rect = final_score_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2 - 20
                )
            )

            screen.blit(
                final_score_text,
                final_score_rect
            )

            # Replay
            replay_text = self.instruction_font.render(
                "Press R to Play Again",
                True,
                WHITE
            )

            replay_rect = replay_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2 + 30
                )
            )

            screen.blit(
                replay_text,
                replay_rect
            )

            # Exit
            exit_text = self.instruction_font.render(
                "Press ESC to Exit",
                True,
                WHITE
            )

            exit_rect = exit_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2 + 70
                )
            )

            screen.blit(
                exit_text,
                exit_rect
            )

        # ---------------------------------------------------------
        # TASK 3: DIFFICULTY SELECTION
        # ---------------------------------------------------------
        elif self.difficulty_select:

            overlay = pygame.Surface(
                (self.width, self.height),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 190)
            )

            screen.blit(
                overlay,
                (0, 0)
            )

            # Title
            title_text = self.difficulty_font.render(
                "SELECT DIFFICULTY",
                True,
                WHITE
            )

            title_rect = title_text.get_rect(
                center=(
                    self.width // 2,
                    80
                )
            )

            screen.blit(
                title_text,
                title_rect
            )

            # Easy
            easy_text = self.instruction_font.render(
                "1 - EASY",
                True,
                WHITE
            )

            easy_rect = easy_text.get_rect(
                center=(
                    self.width // 2,
                    160
                )
            )

            screen.blit(
                easy_text,
                easy_rect
            )

            # Medium
            medium_text = self.instruction_font.render(
                "2 - MEDIUM",
                True,
                WHITE
            )

            medium_rect = medium_text.get_rect(
                center=(
                    self.width // 2,
                    210
                )
            )

            screen.blit(
                medium_text,
                medium_rect
            )

            # Hard
            hard_text = self.instruction_font.render(
                "3 - HARD",
                True,
                WHITE
            )

            hard_rect = hard_text.get_rect(
                center=(
                    self.width // 2,
                    260
                )
            )

            screen.blit(
                hard_text,
                hard_rect
            )

            # Exit
            exit_text = self.instruction_font.render(
                "ESC - Exit",
                True,
                WHITE
            )

            exit_rect = exit_text.get_rect(
                center=(
                    self.width // 2,
                    320
                )
            )

            screen.blit(
                exit_text,
                exit_rect
            )