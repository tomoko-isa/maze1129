import random
import math
from js import setTimeout, document

# 定数の宣言 --- (*1)
INTERVAL = 150  # プレイヤーの描画間隔（ミリ秒）
MAP_ROWS = 30  # 迷路の行数
MAP_COLS = 30  # 迷路の列数
BLOCK_SIZE = 20  # ブロックのサイズ（ピクセル）

# ゲーム内で利用するグローバル変数 --- (*2)
player = {"x": 1, "y": 1, "anime": 0}  # プレイヤーの位置
info = document.getElementById("info")  # 情報表示用の要素を取得
canvas = document.getElementById("canvas")  # キャンバスを取得
context = canvas.getContext("2d")  # 2D描画コンテキストを取得
maze = []  # ブロックの配置を保持する2次元配列

def init_game():
    """ゲームの初期化"""  # --- (*3)
    init_maze_data()  # 迷路データを初期化
    player["x"], player["y"] = 1, 1  # プレイヤーの初期位置
    game_loop()  # ゲームループを開始

def game_loop():
    """ゲームのメインループ"""  # --- (*4)
    draw_screen()  # 画面を更新
    # 次の描画を予約
    setTimeout(game_loop, INTERVAL)

def draw_screen():
    """画面を描画する関数"""  # --- (*5)
    map_colors = ["white", "brown"]
    # 迷路を描画
    for y in range(MAP_ROWS):
        for x in range(MAP_COLS):
            context.fillStyle = map_colors[maze[y][x]]
            context.fillRect(
                x * BLOCK_SIZE, y * BLOCK_SIZE,
                BLOCK_SIZE, BLOCK_SIZE)
    # プレイヤーを光らせて描画 --- (*6)
    player["anime"] = (player["anime"] + 1) % 2
    pcolor = ["red", "blue"]
    context.fillStyle = pcolor[player["anime"]]
    context.fillRect(
        player["x"] * BLOCK_SIZE + 3,
        player["y"] * BLOCK_SIZE + 3,
        BLOCK_SIZE - 6, BLOCK_SIZE - 6)

init_game()  # ゲームを初期化 --- (*7)