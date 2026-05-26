"""《长生劫》文字修仙游戏 - 入口"""

import sys
import io

# Windows 控制台 UTF-8 支持
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')

from game.player import create_player
from game.ui import menu
from game.save_manager import load_game


def main():
    print("=" * 50)
    print("        《长 生 劫》")
    print("      文字修仙 RPG")
    print("=" * 50)
    print()
    print("那一年，大雪封山。")
    print("你跪在尸堆里，第一次见到了仙人。")
    print()
    print("他低头看着你。")
    print()
    print('"想活吗？"')
    print()
    print("你点了点头。")
    print()
    print("自此，凡尘尽断。")
    print()

    while True:
        print("1. 新的旅程")
        print("2. 读取存档")
        print("3. 退出游戏")
        choice = input("\n请选择: ").strip()

        if choice == "1":
            player = create_player()
            menu.main_loop(player)
            break
        elif choice == "2":
            player = load_game()
            if player:
                menu.main_loop(player)
            break
        elif choice == "3":
            print("后会有期，道友。")
            break
        else:
            print("无效选择，请重新输入。\n")


if __name__ == "__main__":
    main()
