import tkinter as tk
import time
import random

# 게임 창 설정
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 40
cols, rows = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

root = tk.Tk()
root.title("크레이지 아케이드 - 2인용")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

# 물풍선, 아이템, 벽 데이터
bombs = []
items = []
walls = []
breakable_walls = []

# 플레이어 리스트
players = []

# 게임 상태 관리
game_started = False
game_over = False
start_button = None


# 플레이어 생성
def create_player(start_x, start_y, color, keys, occupied):
    """플레이어를 겹치지 않는 위치에 생성"""
    while True:
        start_x, start_y = random.randint(0, cols - 1), random.randint(0, rows - 1)
        if (start_x, start_y) not in occupied:  # 벽이나 다른 플레이어가 없는 위치
            occupied.add((start_x, start_y))  # 위치를 점유 처리
            break
    
    return {
        "x": start_x,
        "y": start_y,
        "color": color,
        "key_left": keys["left"],
        "key_right": keys["right"],
        "key_up": keys["up"],
        "key_down": keys["down"],
        "key_bomb": keys["bomb"],
        "health": 5,
        "range": 1,
        "max_bombs": 1,
        "current_bombs": 0,
    }



# 맵 생성
def generate_map():
    """랜덤한 벽과 부술 수 있는 벽 생성"""
    global walls, breakable_walls
    walls = []
    breakable_walls = []
    
    occupied = set()  # 이미 생성된 위치 추적 (벽과 플레이어 모두 포함)

    for x in range(cols):
        for y in range(rows):
            if random.random() < 0.1:  # 고정된 벽
                if (x, y) not in occupied:
                    walls.append((x, y))
                    occupied.add((x, y))
            elif random.random() < 0.15:  # 부술 수 있는 벽
                if (x, y) not in occupied:
                    breakable_walls.append((x, y))
                    occupied.add((x, y))
    
    return occupied  # occupied를 반환하여 플레이어 생성에 사용

# 맵을 격자로 표시
def draw_grid():
    for i in range(0, WIDTH, CELL_SIZE):
        canvas.create_line(i, 0, i, HEIGHT, fill="white")
    for i in range(0, HEIGHT, CELL_SIZE):
        canvas.create_line(0, i, WIDTH, i, fill="white")

def draw_walls():
    """벽 그리기"""
    for x, y in walls:
        canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill="gray"
        )
    for x, y in breakable_walls:
        canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill="brown"
        )

def draw_players():
    for player in players:
        x, y = player["x"], player["y"]
        canvas.create_oval(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill=player["color"]
        )
        canvas.create_text(
            (x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE,
            text=f"{player['health']} HP", fill="white", font=("Arial", 10, "bold")
        )

def draw_bombs():
    """물풍선 및 폭발 그리기"""
    current_time = time.time()
    exploded = []

    for bomb in bombs:
        x, y, placed_time, owner, range_ = bomb
        if current_time - placed_time < 2:  # 2초 후 폭발
            canvas.create_oval(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill="yellow"
            )
        else:
            exploded.append(bomb)
            draw_explosion(x, y, range_, owner)

    for bomb in exploded:
        bombs.remove(bomb)
        bomb[3]["current_bombs"] -= 1  # 폭발 후 물풍선 설치 가능 개수 복구
        
def spawn_item(x, y):
    """아이템 생성"""
    if random.random() < 0.5:  # 50% 확률로 아이템 생성
        item_type = random.choice(["range", "max_bombs", "heal"])  # 회복 아이템 추가
        items.append({"x": x, "y": y, "type": item_type, "protected": True})




def draw_items():
    """아이템 그리기"""
    for item in items:
        # 보호 상태 해제 (한 프레임 이후부터 폭발 영향을 받게 함)
        if item["protected"]:
            item["protected"] = False

        x, y, item_type = item["x"], item["y"], item["type"]
        color = "green" if item_type == "range" else "blue"
        canvas.create_oval(
            x * CELL_SIZE + 10, y * CELL_SIZE + 10,
            (x + 1) * CELL_SIZE - 10, (y + 1) * CELL_SIZE - 10,
            fill=color
        )



def draw_explosion(x, y, range_, owner):
    """폭발 처리 (벽 관통 방지 및 물풍선 연쇄 폭발 구현)"""
    queue = [(x, y, range_)]  # 폭발할 물풍선의 위치와 범위 저장
    processed = set()  # 이미 처리한 물풍선을 저장

    while queue:
        cx, cy, crange = queue.pop(0)  # 큐에서 하나씩 꺼내 처리
        if (cx, cy) in processed:
            continue  # 이미 처리한 위치는 건너뜀
        processed.add((cx, cy))  # 처리 기록

        explosion_coords = [(cx, cy)]
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 상, 하, 좌, 우
            for i in range(1, crange + 1):
                nx, ny = cx + direction[0] * i, cy + direction[1] * i
                if (nx, ny) in walls:
                    break  # 고정된 벽에서 멈춤
                explosion_coords.append((nx, ny))
                if (nx, ny) in breakable_walls:
                    breakable_walls.remove((nx, ny))
                    spawn_item(nx, ny)  # 부술 수 있는 벽에서 아이템 생성
                    break  # 부술 수 있는 벽에서 멈춤
                # 다른 물풍선 연쇄 폭발
                for bomb in bombs[:]:  # 리스트 복사 후 순회
                    if bomb[0] == nx and bomb[1] == ny and (nx, ny) not in processed:
                        queue.append((bomb[0], bomb[1], bomb[4]))  # 큐에 추가
                        if bomb in bombs:  # 리스트에 남아 있는지 확인
                            bombs.remove(bomb)  # 폭발된 물풍선 제거
                            bomb[3]["current_bombs"] -= 1  # 설치 가능 개수 복구
                        break

        # 폭발 표시
        for ex, ey in explosion_coords:
            canvas.create_rectangle(
                ex * CELL_SIZE, ey * CELL_SIZE,
                (ex + 1) * CELL_SIZE, (ey + 1) * CELL_SIZE,
                fill="orange"
            )
            # 아이템 제거
            items[:] = [item for item in items if (item["x"], item["y"]) != (ex, ey) or item["protected"]]
            # 플레이어 체력 감소
            for player in players:
                if player["x"] == ex and player["y"] == ey and player["health"] > 0:
                    player["health"] -= 1




def move_player(player, dx, dy):
    """플레이어 이동"""
    new_x = player["x"] + dx
    new_y = player["y"] + dy
    if (
        0 <= new_x < cols and 0 <= new_y < rows
        and (new_x, new_y) not in walls
        and (new_x, new_y) not in breakable_walls
        and (new_x, new_y) not in [(b[0], b[1]) for b in bombs]  # 물풍선 위로 이동 불가
        and not any(p["x"] == new_x and p["y"] == new_y for p in players)
    ):
        player["x"], player["y"] = new_x, new_y

        # 아이템 획득
        for item in items[:]:
            if (new_x, new_y) == (item["x"], item["y"]):
                if item["type"] == "range":
                    player["range"] += 1
                elif item["type"] == "max_bombs":
                    player["max_bombs"] += 1
                elif item["type"] == "heal":
                    if player["health"] < 5:  # 최대 체력 5
                        player["health"] += 1
                items.remove(item)  # 아이템 제거



def place_bomb(player):
    """물풍선 설치"""
    if player["current_bombs"] < player["max_bombs"]:
        x, y = player["x"], player["y"]
        if not any(b[0] == x and b[1] == y for b in bombs):
            bombs.append((x, y, time.time(), player, player["range"]))
            player["current_bombs"] += 1

def spawn_item(x, y):
    """아이템 생성"""
    if random.random() < 0.5:  # 50% 확률로 아이템 생성
        item_type = "range" if random.random() < 0.5 else "max_bombs"
        items.append({"x": x, "y": y, "type": item_type, "protected": True})


def game_loop():
    global game_started, game_over
    if not game_started:
        return

    # 게임 종료 조건: 두 플레이어 중 하나라도 체력이 0 이하가 되면 게임 종료
    if ( any(player["health"] <= 0 for player in players) ):
        game_over = True 
        show_game_over()
        return
    
        
    
    canvas.delete("all")
    draw_grid()
    draw_walls()
    draw_players()
    draw_bombs()
    draw_items()
    root.after(50, game_loop)


def key_press(event):
    for player in players:
        if event.keysym == player["key_left"]:
            move_player(player, -1, 0)
        elif event.keysym == player["key_right"]:
            move_player(player, 1, 0)
        elif event.keysym == player["key_up"]:
            move_player(player, 0, -1)
        elif event.keysym == player["key_down"]:
            move_player(player, 0, 1)
        elif event.keysym == player["key_bomb"]:
            place_bomb(player)
            
# 게임 시간 변수
start_time = None

def start_game():
    global game_started, players, start_button, start_time
    game_started = True
    start_time = time.time()  # 게임 시작 시간 기록

    # 버튼 삭제
    if start_button:
        start_button.destroy()
        
    

    # 맵 생성 및 점유 위치 반환
    occupied = generate_map()

    # 플레이어 초기화
    players.clear()
    player1 = create_player(1, 1, "red", {"left": "a", "right": "d", "up": "w", "down": "s", "bomb": "q"}, occupied)
    player2 = create_player(13, 8, "blue", {"left": "Left", "right": "Right", "up": "Up", "down": "Down", "bomb": "space"}, occupied)
    players.extend([player1, player2])

    game_loop()


def show_start_screen():
    global start_button
    canvas.delete("all")
    canvas.create_text(WIDTH // 2, HEIGHT // 2 - 50, text="크레이지 아케이드", font=("Arial", 24, "bold"), fill="black")
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="시작하려면 아래 버튼을 누르세요", font=("Arial", 14), fill="black")
    start_button = tk.Button(root, text="시작하기", font=("Arial", 14), command=start_game)
    start_button.pack()
    
    

def restart_game():
    global game_started, game_over, bombs, items, walls, breakable_walls, players, start_time
    game_started = False
    game_over = False
    bombs = []
    items = []
    walls = []
    breakable_walls = []
    players = []
    start_time = time.time()  # 새로운 게임 시작 시간 설정
    start_game()  # 게임 재시작

def show_game_over():
    global restart_button
    canvas.delete("all")

    # 플레이 시간 계산
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    time_text = f"플레이 시간: {minutes}분 {seconds}초"
    
   
        
    
    # 게임 오버 메시지
    canvas.create_text(WIDTH // 2, HEIGHT // 2 - 120, text="게임 오버", font=("Arial", 24, "bold"), fill="red")
    canvas.create_text(WIDTH // 2, HEIGHT // 2 - 80, text=time_text, font=("Arial", 14), fill="black")
    
    # 승리 조건 확인
    alive_players = [player for player in players if player["health"] > 0]
    if len(alive_players) == 1:
        winner = alive_players[0]
        victory_message = f"플레이어 ({winner['color']}) 승리!"
    elif elapsed_time > 10:
        victory_message = "무승부!"
    

    # 승리 메시지 표시
    canvas.create_text(WIDTH // 2, HEIGHT // 2 - 40, text=victory_message, font=("Arial", 18, "bold"), fill="green")
    
    # 각 플레이어의 상태 표시
    for i, player in enumerate(players, start=1):
        canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + (i * 30),
            text=f"플레이어 {i} ({player['color']}): 남은 목숨 {player['health']}개",
            font=("Arial", 14),
            fill="black"
        )

    # 재시작 버튼 생성
    restart_button = tk.Button(root, text="다시 하기", font=("Arial", 14), command=lambda: [restart_game(), restart_button.destroy()])
    restart_button.pack()



root.bind("<KeyPress>", key_press)
show_start_screen()
root.mainloop()


