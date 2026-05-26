"""随机奇遇系统"""

import random

# 奇遇事件列表: (名称, 描述, 选项列表, 权重)
# 选项: (文字, 效果函数名)
ADVENTURES = [
    {
        "name": "破庙奇遇",
        "desc": '你避雨进入破庙，神像后方传来低语：\n> “少年，你想长生吗？”',
        "choices": [
            {"text": "掀开神像", "effect": "find_secrets"},
            {"text": "转身离开", "effect": "leave_safe"},
            {"text": "点香祭拜", "effect": "worship"},
            {"text": "一剑斩碎神像", "effect": "destroy_statue"},
        ],
        "weight": 10,
        "min_level": 1,
    },
    {
        "name": "山洞老爷爷",
        "desc": "你在山洞中发现一位奄奄一息的老人，他似乎在守护着什么。",
        "choices": [
            {"text": "救下老人", "effect": "save_old_man"},
            {"text": "搜寻宝物", "effect": "loot_cave"},
            {"text": "转身离开", "effect": "leave_safe"},
        ],
        "weight": 8,
        "min_level": 3,
    },
    {
        "name": "上古残魂",
        "desc": "一道残魂漂浮在你面前，似乎想要说什么。",
        "choices": [
            {"text": "倾听残魂", "effect": "listen_soul"},
            {"text": "吞噬残魂", "effect": "devour_soul"},
            {"text": "无视离开", "effect": "leave_safe"},
        ],
        "weight": 5,
        "min_level": 10,
    },
    {
        "name": "妖女求救",
        "desc": '一位白衣女子慌张跑来，身后有数名修士追赶。\n"求求你，救救我！"',
        "choices": [
            {"text": "出手相救", "effect": "save_girl"},
            {"text": "加入追兵", "effect": "join_hunters"},
            {"text": "袖手旁观", "effect": "leave_safe"},
        ],
        "weight": 8,
        "min_level": 5,
    },
    {
        "name": "神秘黑棺",
        "desc": "你在悬崖下发现一口漆黑的棺材，散发着阴冷的气息。",
        "choices": [
            {"text": "打开棺材", "effect": "open_coffin"},
            {"text": "在旁修炼", "effect": "cultivate_near"},
            {"text": "封印棺材", "effect": "seal_coffin"},
            {"text": "远离此地", "effect": "leave_safe"},
        ],
        "weight": 5,
        "min_level": 15,
    },
    {
        "name": "灵脉暴动",
        "desc": "地面震动，灵气喷涌而出，一处隐藏灵脉暴露了！",
        "choices": [
            {"text": "吸收灵气", "effect": "absorb_spirit"},
            {"text": "标记位置", "effect": "mark_location"},
        ],
        "weight": 10,
        "min_level": 1,
    },
    {
        "name": "落难修士",
        "desc": "一位修士倒在路边，储物袋半开着，隐约可见几颗灵石。",
        "choices": [
            {"text": "救助修士", "effect": "save_cultivator"},
            {"text": "拿走灵石", "effect": "steal_stones"},
            {"text": "无视离开", "effect": "leave_safe"},
        ],
        "weight": 10,
        "min_level": 1,
    },
    {
        "name": "秘境入口",
        "desc": "一道空间裂缝出现在你面前，对面似乎是一处上古秘境。",
        "choices": [
            {"text": "进入秘境", "effect": "enter_secret"},
            {"text": "在外探索", "effect": "explore_outside"},
            {"text": "标记位置离开", "effect": "leave_safe"},
        ],
        "weight": 3,
        "min_level": 20,
    },
]


def trigger_random_event(player):
    """触发随机奇遇"""
    suitable = [e for e in ADVENTURES if e["min_level"] <= player.level]
    if not suitable:
        return

    weights = [e["weight"] for e in suitable]
    event = random.choices(suitable, weights=weights, k=1)[0]

    print(f"\n{'~'*40}")
    print(f"  奇遇: {event['name']}")
    print(f"{'~'*40}")
    print(event["desc"])
    print()

    for i, choice in enumerate(event["choices"], 1):
        print(f"  {i}. {choice['text']}")

    while True:
        try:
            idx = int(input("\n你的选择: ").strip()) - 1
            if 0 <= idx < len(event["choices"]):
                break
            print("无效选择。")
        except ValueError:
            print("请输入数字。")

    chosen = event["choices"][idx]
    apply_effect(player, chosen["effect"], event["name"])


def apply_effect(player, effect, event_name):
    """应用奇遇效果"""
    if effect == "find_secrets":
        print("你掀开神像，发现一本残破古卷和三块灵石。")
        player.add_item("疗伤丹", 2)
        player.spirit_stones += 3
        player.luck += 2
        player.gain_exp(50)
        player.karma += 1

    elif effect == "leave_safe":
        print("你离开了此地，平安无事。")

    elif effect == "worship":
        print("你虔诚祭拜，感到一阵暖流涌入体内。")
        player.heal(30)
        player.luck += 3
        player.karma += 2

    elif effect == "destroy_statue":
        print("你一剑斩碎神像，里面掉出一本魔功秘籍！")
        if "血海吞天功" not in player.skills:
            player.skills.append("血海吞天功")
            print("学会了「血海吞天功」！")
        player.attack += 10
        player.karma -= 3

    elif effect == "save_old_man":
        print("老人感激道：年轻人，老夫传你一门功法。")
        if "太虚吐纳诀" not in player.skills:
            player.skills.append("太虚吐纳诀")
            print("学会了「太虚吐纳诀」！")
        player.luck += 5
        player.karma += 3

    elif effect == "loot_cave":
        print("你在山洞中搜到了一些宝物。")
        player.add_item("破境丹", 1)
        player.spirit_stones += 10
        player.karma -= 2

    elif effect == "listen_soul":
        print("残魂将毕生领悟传给了你……")
        player.gain_exp(200)
        player.luck += 3

    elif effect == "devour_soul":
        print("你吞噬了残魂的力量，但神识受损。")
        player.gain_exp(500)
        player.max_mp -= 10
        player.karma -= 5

    elif effect == "save_girl":
        print("你击退追兵，救下了女子。")
        print('她微微欠身："多谢恩公，小女子苏璃，来日必报此恩。"')
        player.luck += 5
        player.karma += 5
        player.gain_exp(80)

    elif effect == "join_hunters":
        print("你加入追兵，抢到了女子的储物袋。")
        player.add_item("回气丹", 5)
        player.spirit_stones += 8
        player.karma -= 5

    elif effect == "open_coffin":
        roll = random.randint(1, 100)
        if roll <= 30:
            print("棺中沉睡的古尸苏醒了！")
            from game.combat import battle
            battle(player, "血蝠")
        else:
            print("棺中有一具上古修士的遗骸，旁边放着几颗丹药。")
            player.add_item("延寿丹", 1)
            player.spirit_stones += 15

    elif effect == "cultivate_near":
        print("你利用棺材散发的阴气修炼，修为大增！")
        player.gain_exp(150)
        player.karma -= 1

    elif effect == "seal_coffin":
        print("你布下阵法封印了棺材，天道有感，降下福泽。")
        player.luck += 5
        player.karma += 5
        player.gain_exp(100)

    elif effect == "absorb_spirit":
        print("你贪婪地吸收灵气，修为猛涨！")
        player.gain_exp(100 + player.level * 10)
        player.restore_mp(player.max_mp)

    elif effect == "mark_location":
        print("你标记了灵脉位置，可随时回来修炼。")
        player.luck += 2
        print("（灵脉已记录，日后修炼效率提升）")

    elif effect == "save_cultivator":
        print("修士醒来，感激地给了你一些丹药。")
        player.add_item("回气丹", 3)
        player.karma += 3
        player.gain_exp(30)

    elif effect == "steal_stones":
        print("你拿走了灵石，但心中有些不安。")
        player.spirit_stones += 8
        player.karma -= 3

    elif effect == "enter_secret":
        print("你进入秘境，遭遇了强大的守护兽！")
        from game.combat import battle
        result = battle(player)
        if result:
            print("你在秘境中获得了大量宝物！")
            player.spirit_stones += 30
            player.add_item("洗髓丹", 1)
            player.gain_exp(500)

    elif effect == "explore_outside":
        print("你在秘境外围探索，找到了一些灵草。")
        player.add_item("疗伤丹", 5)
        player.gain_exp(80)

    else:
        print("你平安无事。")
