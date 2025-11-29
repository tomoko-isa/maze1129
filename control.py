# プレイヤーの移動を制御するコード
def move_player(dx, dy):
    """プレイヤーを移動する関数"""  # --- (*1)
    new_x = player["x"] + dx
    new_y = player["y"] + dy
    if 0 <= new_x < MAP_COLS and 0 <= new_y < MAP_ROWS:
        # 移動先が通路なら移動
        if maze[new_y][new_x] == 0:
            player["x"] = new_x
            player["y"] = new_y
    # 情報表示を更新
    info.innerText = f"Player: ({player['x']}, {player['y']})"
    if player["x"] == MAP_COLS - 2 and player["y"] == MAP_ROWS - 2:
        info.innerText += " ゴールに到達！！お疲れさまでした！"

def keydown(event):
    """キーが押されたときの処理"""
    # デフォルトのキー操作を無効化 --- (*2)
    event.preventDefault()
    # 押されたキーに応じてプレイヤーを移動 --- (*3)
    key = event.key
    if key == "ArrowLeft":
        move_player(-1, 0)
    elif key == "ArrowRight":
        move_player(1, 0)
    elif key == "ArrowUp":
        move_player(0, -1)
    elif key == "ArrowDown":
        move_player(0, 1)

# キー入力イベントの登録 --- (*4)
document.addEventListener("keydown", keydown)

def canvas_on_click(event):
    """キャンバスがクリックされたときの処理"""  # --- (*5)
    rect = canvas.getBoundingClientRect()
    cx = event.clientX - rect.left
    cy = event.clientY - rect.top
    px = player["x"] * BLOCK_SIZE + BLOCK_SIZE // 2
    py = player["y"] * BLOCK_SIZE + BLOCK_SIZE // 2
    dx, dy = 0, 0
    if abs(cx - px) > abs(cy - py):
        dx = 1 if cx > px else -1
    else:
        dy = 1 if cy > py else -1    
    move_player(dx, dy)