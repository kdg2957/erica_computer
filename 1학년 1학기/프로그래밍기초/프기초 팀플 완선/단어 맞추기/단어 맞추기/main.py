import pygame
import ctypes
import time
from copy import deepcopy

from game import *
from gui_class import *


pygame.init()
pygame.display.set_caption('단어 맞추기')
pygame.mouse.set_visible(False)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)

FPS = 60
u32 = ctypes.windll.user32
WIDTH, HEIGHT = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg_color = list(BLACK)
txt_color = list(WHITE)

GUESSALPHABET = 0
GUESSWORD = 1

WON = 0
LOST = 1
ONPLAYING = 2

AUTOCONFIRMTIME = 3


@cache
def font(size):
    return pygame.font.Font('./font/NotoSansKR-Medium.otf', size)


# 화면에 글씨 나타내는 함수
def write(txt, font_size, color, pos, criterion='center', bg_color=()):
    if not bool(bg_color):
        text = font(font_size).render(txt, True, color)
    else:
        text = font(font_size).render(txt, True, color, bg_color)
    text_pos = text.get_rect()
    setattr(text_pos, criterion, pos)
    screen.blit(text, text_pos)


def main():
    # 화면에 마우스 커서 그리는 함수
    def draw_cursor():
        nonlocal cursor_pos, clickable_form

        radius = 5 if clickable_form else 2
        pygame.draw.circle(screen, txt_color, cursor_pos, radius, 2)


    # 정답을 입출력 하는 버튼 초기화
    def init_answers():
        nonlocal game_manager
        nonlocal answers, answer_board

        QuizButton.guessing_word = False

        answers = []
        word_len = len(game_manager.answer)

        for i in range(word_len):
            if i < word_len:
                total_width = WIDTH * 7 // 9
                x_len = WIDTH * 3 / 65
                y_len = x_len * 3 / 2

                x_pos = WIDTH / 9 + total_width * (i + 1) / (word_len + 1)
                y_pos = HEIGHT / 4

                button = QuizButton((x_len, y_len), (x_pos, y_pos), game_manager.quiz[i] == '_', BLUE, bg_color)
                button.init_txt(game_manager.answer[i], y_len // 2, txt_color)
                
                answers.append(button)

        answer_board = AlphabetButton((WIDTH * 7 // 9, y_len * 5 // 3), (WIDTH / 2, HEIGHT / 4), bg_color)
        answer_board.init_txt('', 0, txt_color)


    # 알파벳 카드(버튼) 초기화
    def init_alphabets():
        nonlocal alphabets

        alphabets = []

        for i in range(26):
            x_len = WIDTH * 3 / 65
            y_len = x_len * 3 / 2
            y_interval = x_len / 4

            x_pos = answer_board.rect.x + answer_board.rect.width * (i % 13 + 1) / 14
            y_pos = HEIGHT * 3 / 4 - y_interval / 2 - y_len / 2 + (y_len + y_interval) * (i // 13)

            button = AlphabetButton((x_len, y_len), (x_pos, y_pos), bg_color)
            button.init_txt(chr(97 + i), y_len // 2, txt_color)

            alphabets.append(button)


    # 맞춘 알파벳 드러내는 함수
    def uncover_answer(alphabet):
        nonlocal game_manager, answers

        if game_manager.guess_letter(alphabet):
            for button in answers:
                if button.txt == alphabet:
                    button.covered = False


    # 새로운 게임 시작하기 (관련 변수 초기화)
    def reset():
        nonlocal guess, game_progress, progress_txt
        nonlocal timer_working, confirm_timer

        game_manager.get_new_quiz()
        game_manager.attempt_count = game_manager.max_attempt

        init_answers()
        init_alphabets()

        guess = GUESSALPHABET
        game_progress = ONPLAYING
        progress_txt = f"{game_manager.max_attempt} / {game_manager.max_attempt}"

        timer_working = False
        confirm_timer = [0, 0]


    # 난이도 변경
    def change_difficulty(difficulty):
        nonlocal difficulty_buttons

        radius = alphabets[0].rect.height // 6
        difficulty_buttons = []

        for i in range(1, 4):
            icon = txt_icon(int(radius * 1.5), str(i), WHITE, BLACK)
            pos = (answer_board.rect.topright[0] - radius * ((3 - i) * 3 + 1), answer_board.rect.y * 3 / 4)
            difficulty_buttons.append(FuncButton(icon, radius, pos, txt_color, bg_color))
        
        icon = txt_icon(int(radius * 1.5), str(difficulty + 1), BLACK, WHITE)
        pos = (answer_board.rect.topright[0] - radius * ((2 - difficulty) * 3 + 1), answer_board.rect.y * 3 / 4)
        difficulty_buttons[difficulty] = FuncButton(icon, radius, pos, txt_color, bg_color)
        difficulty_buttons[difficulty].selected = True

        game_manager.difficulty = difficulty

    
    # 자동 채점 타이머의 길이 반환
    def get_timer_length(runtime):
        nonlocal confirm_timer

        rest = runtime - (confirm_timer[1] - confirm_timer[0])

        return 0 if rest <= 0 else answer_board.rect.width * (rest / runtime)


    # 1. 변수 선언 및 초기화 ----------------------------------------------------------------------
    game_manager = GameManager(5)
    alphabets = [AlphabetButton((0, 0), (0, 0), ())]
    answers = [QuizButton((0, 0), (0, 0), False, (0, 0, 0), ())]
    answer_board = AlphabetButton((0, 0), (0, 0), ())

    drag_button = AlphabetButton((0, 0), (0, 0), bg_color)
    drag_button.init_txt('', 0, WHITE)

    game_manager.load_words("./words_sample.txt")
    game_manager.difficulty = 0

    reset()

    radius = alphabets[0].rect.height // 6
    pos = (answer_board.rect.x + radius, answer_board.rect.y * 3 / 4)
    reset_button = FuncButton(reset_icon(radius * 3 // 2, txt_color, bg_color), radius, pos, txt_color, bg_color)

    difficulty_buttons:list[FuncButton] = []
    change_difficulty(0)


    clickable_form = False
    guess = GUESSALPHABET
    game_progress = ONPLAYING
    progress_txt = f"{game_manager.max_attempt} / {game_manager.max_attempt}"

    timer_working = False
    confirm_timer = [0, 0]
    timer_length = get_timer_length(AUTOCONFIRMTIME)


    while True:
        screen.fill(bg_color)
        dt = clock.tick(FPS) / 1000

        # 2. 이벤트에 따른 제어 -------------------------------------------------------------------------
        # 2.1 이벤트 가져오기
        events = pygame.event.get()
        cursor_pos = pygame.mouse.get_pos()

        # 2.2 모든 GUI 객체에 이벤트 전달
        Button.events = events
        FuncButton.events = events

        # 2.3 각 이벤트에 따른 제어
        for event in events:
            # 2.3.1 창을 닫았을 때, 프로그램 종료
            if event.type == pygame.QUIT:
                return None
            
            # 2.3.2 ESC 눌렀을 때, 프로그램 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                
            # 2.3.3 알파벳 카드(버튼)를 내려놨을 때, 그 위치에 따라서 단어 또는 알파벳 유추
            if event.type == pygame.MOUSEBUTTONUP:
                for button in answers:
                    # 단어 유추
                    if drag_button.get_collided_button(button):
                        if not button.covered:
                            continue

                        guess = GUESSWORD
                        QuizButton.guessing_word = True

                        button.input_txt = drag_button.txt
                        break
                
                # 알파벳 유추
                if guess == GUESSALPHABET and drag_button.get_collided_button(answer_board):
                    uncover_answer(drag_button.txt)

                drag_button = AlphabetButton((0, 0), (0, 0), bg_color)
                drag_button.init_txt('', 0, WHITE)

        # 3. 단어 유추 상황에 따른 제어 ----------------------------------------------------
        if guess == GUESSWORD:
            all_guessed=  True
            all_blank = True

            # 3.1 빈칸을 모두 채웠는지(all_guessed), 모두 비웠는지(all_blank)를 판단
            for button in answers:
                if button.is_clicked():
                    button.input_txt = '_'

                if button.covered:
                    if button.input_txt == '_':
                        all_guessed = False
                        timer_working = False
                    else:
                        all_blank = False

            # 3.2 모든 빈칸이 채워졌을 때, 자동 채점 시작
            if all_guessed:
                if not timer_working:
                    timer_working = True
                    confirm_timer[0] = time.perf_counter()

                for button in alphabets:
                    button.dark = True

            # 3.3 모든 빈칸이 비워졌을 때, 단어 유추 상태 해제
            if all_blank:
                guess = GUESSALPHABET
                QuizButton.guessing_word = False
        
        # 3.4 자동 채점 타이머 작동
        if timer_working:
            confirm_timer[1] = time.perf_counter()

            timer_length = get_timer_length(AUTOCONFIRMTIME)

            if timer_length <= 0:
                timer_working = False

                guessed_word = ''
                for button in answers:
                    guessed_word += button.input_txt if button.covered else button.txt

                    button.input_txt = '_'

                game_manager.guess_word(guessed_word)

        # 4. 알파벳 카드(버튼) 드래그 앤 드롭 -------------------------------------------------------------      
        # 4.1 알파벳 카드(버튼) 위에 커서가 올라왔을 때, 사용 가능 여부 표시
        for button in alphabets:
            if bool(drag_button.txt):
                break

            if not button.dark and button.on_cursor():
                clickable_form = True
                button.marked = True
                break
        
        # 4.2 알파벳 카드(버튼)을 클릭했을 때, 복제 및 마우스 위치로 이동
        for button in alphabets:
            if not button.dark and button.is_clicked():
                drag_button = deepcopy(button)
                button.dark = True

        drag_button.follow_cursor()

        # 4.3 알파벳 유추 시, 드래그 앤 드롭의 가능 여부 표시
        if guess == GUESSALPHABET and drag_button.get_collided_button(answer_board):
            answer_board.marked = True

        # 4.4 단어 유추 시, 드래그 앤 드롭의 가능 여부 표시
        for button in answers:
            if not button.covered:
                continue

            if drag_button.get_collided_button(button):
                button.marked = True
                answer_board.marked = False
                break

            if button.on_cursor():
                clickable_form = False if button.input_txt == '_' else True

                button.marked = True
                break

        # 5. 기능 버튼 제어 --------------------------------------------------------------------------
        # 5.1 게임 재시작 버튼 제어
        if reset_button.on_cursor():
            clickable_form = True

        if reset_button.is_clicked():
            reset()

        # 5.2 난이도 조절 버튼 제어
        for i in range(len(difficulty_buttons)):
            if difficulty_buttons[i].on_cursor():
                clickable_form = True

            if difficulty_buttons[i].selected:
                continue

            if difficulty_buttons[i].is_clicked():
                change_difficulty(i)
                reset()

        # 6. 게임 진행 상황에 따른 제어 -----------------------------------------------------------
        # 6.1 게임 오버
        if game_manager.attempt_count <= 0:
            progress_txt = "Game Over"
            guess = GUESSALPHABET

            for button in alphabets:
                button.dark = True
            
            for button in answers:
                button.covered = False
        # 6.2 게임 클리어
        elif len(game_manager.targets) == 0:
            progress_txt = "Game Clear"
            guess = GUESSALPHABET

            for button in alphabets:
                button.dark = True
            
            for button in answers:
                button.covered = False


        # 7. 화면 업데이트 -------------------------------------------------------------------------
        # 7.1 정답 입력 칸 그리기
        for button in answers:
            button.draw(screen)
        answer_board.draw(screen)
        
        # 7.2 알파벳 카드(버튼) 그리기
        for button in alphabets:
            button.draw(screen)
        drag_button.draw(screen)

        # 7.3 자동 제출 타이머 그리기
        timer_color = GREEN if timer_working else txt_color
        start_pos = (answer_board.rect.x, HEIGHT // 2)
        end_pos = (start_pos[0] + get_timer_length(AUTOCONFIRMTIME), HEIGHT // 2)
        pygame.draw.line(screen, timer_color, start_pos, end_pos, 5)

        # 7.4 진행 상황 알림 (시도 횟수 및 클리어 여부 안내)
        font_size = alphabets[0].rect.height // 3
        write(progress_txt, font_size, txt_color, (WIDTH // 2, HEIGHT // 2), bg_color=bg_color)

        # 7.5 리셋 버튼 그리기
        reset_button.draw(screen)

        # 7.6 난이도 설정 버튼 그리기
        for button in difficulty_buttons:
            button.draw(screen)

        # 7.7 마우스 커서 그리기
        draw_cursor()

        # 7.8 화면 업데이트
        pygame.display.update()


        # 8. 루프별 변수 초기화 ----------------------------------------------------------------------------
        # 8.1 게임의 종료 여부와는 관계없이 초기화
        clickable_form = False

        if not timer_working:
            confirm_timer = [0, 0]
        
        if game_manager.attempt_count <= 0:
            game_progress = LOST
        elif len(game_manager.targets) == 0:
            game_progress = WON

        if game_progress != ONPLAYING:
            continue
        
        # 게임 종료 (승리 또는 패배) 시 초기화 되지 않음
        progress_txt = f"{game_manager.attempt_count} / {game_manager.max_attempt}"

        answer_board.marked = False
        for button in answers:
            button.marked = False

        for button in alphabets:
            button.marked = False
            button.dark = False

            if button.txt in game_manager.used_alphabets or button.txt == drag_button.txt:
                button.dark = True


main()
pygame.quit()