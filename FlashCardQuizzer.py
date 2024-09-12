"""This is a FlashCard Quizzer made by https://github.com/JoaoRm42"""

import pygame
import random

questions_data = {
    "What is the capital city of France?": {
        "correct": "Paris",
        "wrong": ["Berlin", "Madrid", "Rome"]
    },
    "Which planet is known as the Red Planet?": {
        "correct": "Mars",
        "wrong": ["Venus", "Jupiter", "Saturn"]
    },
    "What is the largest ocean on Earth?": {
        "correct": "Pacific Ocean",
        "wrong": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
    },
    "Who wrote the play \"Romeo and Juliet\"?": {
        "correct": "William Shakespeare",
        "wrong": ["Charles Dickens", "Jane Austen", "Mark Twain"]
    },
    "What is the chemical symbol for gold?": {
        "correct": "Au",
        "wrong": ["Ag", "Fe", "Pb"]
    },
    "What is the hardest natural substance on Earth?": {
        "correct": "Diamond",
        "wrong": ["Gold", "Iron", "Platinum"]
    },
    "Who painted the Mona Lisa?": {
        "correct": "Leonardo da Vinci",
        "wrong": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet"]
    },
    "What is the smallest prime number?": {
        "correct": "2",
        "wrong": ["1", "3", "4"]
    },
    "In what year did the Titanic sink?": {
        "correct": "1912",
        "wrong": ["1905", "1915", "1920"]
    },
    "Which element has the atomic number 1?": {
        "correct": "Hydrogen",
        "wrong": ["Helium", "Oxygen", "Nitrogen"]
    },
    "What is the capital city of Japan?":{
        "correct": "Tokyo",
        "wrong": ["Osaka", "Kyoto", "Hiroshima"]
    }
}

# Shuffle questions
temp_questions_data = questions_data.copy()
questions = list(questions_data.keys())
random.shuffle(questions)

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Recs
rects = [
    pygame.Rect(130, 250, 250, 100),
    pygame.Rect(420, 250, 250, 100),
    pygame.Rect(130, 380, 250, 100),
    pygame.Rect(420, 380, 250, 100)
]

next_rect = pygame.Rect(350, 525, 100, 50)
tryagain_Rect = pygame.Rect(200, 150, 200, 100)
exit_Rect = pygame.Rect(500, 150, 100, 100)
# Global Variables
ingame = 0
home = 0
tmp_total_questions = len(questions)
quest_num = 1
score = 0
screen = None
clock = None
flag = 0
correct = 0
correct_answer_rect_idx = None
global_question = questions[0]

def end_game():
    """Function to display End of the game"""
    global screen, questions, temp_questions_data, questions_data, home, quest_num, global_question, correct_answer_rect_idx, correct, flag, score, tmp_total_questions
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 800, 600), 100)

    if score <= tmp_total_questions / 4 and tmp_total_questions >= 0:
        font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
        bad = font.render('You are completly terrible', True, BLACK, WHITE)
        badRect = bad.get_rect()
        badRect.center = (400, 400)
        screen.blit(bad, badRect)
    elif score >= tmp_total_questions / 4 and score <= tmp_total_questions / 2:
        font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
        bad = font.render('You need to study', True, BLACK, WHITE)
        badRect = bad.get_rect()
        badRect.center = (400, 400)
        screen.blit(bad, badRect)
    elif score >= tmp_total_questions / 2 and score < tmp_total_questions - 1:
        font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
        bad = font.render('You are so smart but not perfect', True, BLACK, WHITE)
        badRect = bad.get_rect()
        badRect.center = (400, 400)
        screen.blit(bad, badRect)
    else:
        font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
        bad = font.render('You need to go touch some grass', True, BLACK, WHITE)
        badRect = bad.get_rect()
        badRect.center = (400, 400)
        screen.blit(bad, badRect)

    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    text = font.render(f'Score: {score}/{tmp_total_questions}', True, BLACK, WHITE)
    textRect = text.get_rect()
    textRect.center = (400, 300)
    screen.blit(text, textRect)

    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    try_text = font.render('Try Again', True, BLACK, WHITE)
    try_textRect = try_text.get_rect()
    try_textRect.center = (300, 200)
    screen.blit(try_text, try_textRect)

    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    exit_text = font.render('EXIT', True, BLACK, WHITE)
    exit_textRect = exit_text.get_rect()
    exit_textRect.center = (550, 200)
    screen.blit(exit_text, exit_textRect)



def wrong_scren(idx):
    """Screen after correct answer"""
    global correct_answer_rect_idx, screen, rects, flag
    pygame.draw.rect(screen, RED, rects[idx - 1], 5)
    flag = 1

    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    text = font.render('Next', True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (400, 550)
    screen.blit(text, textRect)

def correct_screen():
    """Screen after correct answer"""
    global correct_answer_rect_idx, screen, rects, flag, score, correct
    pygame.draw.rect(screen, GREEN, rects[correct_answer_rect_idx - 1], 5)
    score += 1
    flag = 1

    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    next_text = font.render('Next', True, WHITE, BLACK)
    nexttextRect = next_text.get_rect()
    nexttextRect.center = (400, 550)
    screen.blit(next_text, nexttextRect)



def game():
    """Game logic for the Question and answers"""
    global screen, questions, temp_questions_data, correct_answer, correct_answer_rect_idx, flag
    correct_answer_rect_idx = None
    correct_answer = None
    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 20)
    text = font.render(questions[0], True, BLACK, WHITE)
    textRect = text.get_rect()
    textRect.center = (370, 150)
    screen.blit(text, textRect)

    flag = 0
    for question in questions:
    # Get correct and wrong answers
        correct_answer = temp_questions_data[question]["correct"]
        wrong_answers = temp_questions_data[question]["wrong"]


        # Combine correct answer with wrong answers and shuffle
        all_answers = wrong_answers + [correct_answer]
        random.shuffle(all_answers)

        counter = 1
        for id in all_answers:
            if (id == correct_answer):
                correct_answer_rect_idx = counter
                break
            counter += 1

        for idx, answer in enumerate(all_answers, start=1):
            # Render the answer text
            text1 = font.render(answer, True, BLACK, WHITE)

            # Get the text rectangle
            textRect1 = text1.get_rect()

            # Set the center of the text rectangle to the center of the corresponding rectangle
            textRect1.center = rects[idx - 1].center

            # Draw the text on the screen
            screen.blit(text1, textRect1)

        del questions[0]
        del temp_questions_data[question]
        break

def game_screen():
    """This function will handle the game screen"""
    global screen, events, quest_num, score, home, ingame
    # fill the screen with a color
    ingame = 1
    screen.fill(WHITE)
    # Draw rectangle outer borders
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 800, 600), 100)

    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    text = font.render(f'Score: {score}/{tmp_total_questions}', True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (200, 50)
    screen.blit(text, textRect)

    text2 = font.render(f'Questions: {quest_num}/{tmp_total_questions}', True, WHITE, BLACK)
    textRect2 = text.get_rect()
    textRect2.center = (400, 50)
    screen.blit(text2, textRect2)
    # Draw line
    pygame.draw.line(screen, BLACK, (0, 200), (800, 200), 5)

    pygame.draw.rect(screen, BLACK, pygame.Rect(130, 250, 250, 100), 5)
    pygame.draw.rect(screen, BLACK, pygame.Rect(420, 250, 250, 100), 5)
    pygame.draw.rect(screen, BLACK, pygame.Rect(130, 380, 250, 100), 5)
    pygame.draw.rect(screen, BLACK, pygame.Rect(420, 380, 250, 100), 5)
    game()
    quest_num += 1
    home = 1


def main_screen_text():
    """This function will just draw the text for the main screen"""
    global screen
    image_enter = pygame.image.load('enter.png')
    image_rect = image_enter.get_rect()
    image_rect.center = (385, 400)
    # Get the font for the text and the size
    font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
    # Render the font to text and colors
    text = font.render('Welcome to Flash Card Quizzer', True, BLACK, WHITE)
    text2 = font.render('Made By: JoaoRm42', True, BLACK, WHITE)
    text3 = font.render('Press          to play', True, BLACK, WHITE)
    # Get the object size
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    # Position of the object
    textRect.center = (400, 150)
    textRect2.center = (400, 200)
    textRect3.center = (395, 400)
    # Screen text draw
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(image_enter, image_rect)


def main_screen():
    """This function will handle the main screen"""
    global screen
    # fill the screen with a color
    screen.fill(WHITE)
    # Draw rectangle outer borders
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 800, 600), 100)
    # Draw text on screen
    main_screen_text()

def game_init():
    global screen, clock

    # Display Settings
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    pygame.display.set_caption("FlashCard Quizzer by JoaoRM42")
    pygame.display.set_icon(pygame.image.load('card.png'))

    # Music
    # pygame.mixer.music.load('track.mp3')
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.1)

def main():
    global rects, correct_answer_rect_idx, flag, next_rect, home, ingame, screen, questions, temp_questions_data, questions_data, home, quest_num, global_question, correct_answer_rect_idx, correct, flag, score, tmp_total_questions

    pygame.init()
    #pygame.mixer.init()
    game_init()
    main_screen()
    ingame = 0
    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
                elif event.key == 13 and home != 1:
                    game_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(rects, start=1):
                    if rect.collidepoint(mouse_pos):
                        if idx == correct_answer_rect_idx and flag != 1 and ingame == 1:
                            correct_screen()
                            font = pygame.font.Font('C:\Windows\Fonts\segoescb.ttf', 26)
                            text = font.render(f'Score: {score}/10', True, WHITE, BLACK)
                            textRect = text.get_rect()
                            textRect.center = (200, 50)
                            screen.blit(text, textRect)
                        else:
                            if flag != 1 and ingame == 1:
                                wrong_scren(idx)

                if flag == 1 and next_rect.collidepoint(mouse_pos):
                    if len(questions) != 0:
                        game_screen()
                    else:
                        end_game()
                if tryagain_Rect.collidepoint(mouse_pos) and len(temp_questions_data) == 0:
                    ingame = 0
                    temp_questions_data = questions_data
                    questions = list(questions_data.keys())
                    random.shuffle(questions)
                    home = 0
                    tmp_total_questions = len(questions)
                    quest_num = 1
                    score = 0
                    flag = 0
                    correct = 0
                    correct_answer_rect_idx = None
                    global_question = questions[0]
                    main_screen()
                if exit_Rect.collidepoint(mouse_pos) and len(temp_questions_data) == 0:
                    running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
