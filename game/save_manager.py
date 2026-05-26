"""存档系统"""

import json
import os
from game.player import Player

SAVE_DIR = "save"


def save_game(player):
    """保存游戏"""
    os.makedirs(SAVE_DIR, exist_ok=True)
    data = player.to_dict()
    filepath = os.path.join(SAVE_DIR, f"{player.name}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n存档成功！({filepath})")


def load_game():
    """读取存档"""
    if not os.path.exists(SAVE_DIR):
        print("没有找到存档。")
        return None

    saves = [f[:-5] for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    if not saves:
        print("没有找到存档。")
        return None

    print("\n可用存档:")
    for i, name in enumerate(saves, 1):
        print(f"  {i}. {name}")

    while True:
        try:
            idx = int(input("\n选择存档（0取消）: ").strip()) - 1
            if idx == -1:
                return None
            if 0 <= idx < len(saves):
                break
            print("无效选择。")
        except ValueError:
            print("请输入数字。")

    filepath = os.path.join(SAVE_DIR, f"{saves[idx]}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    player = Player.from_dict(data)
    print(f"\n读取存档成功！欢迎回来，{player.name}。")
    return player
