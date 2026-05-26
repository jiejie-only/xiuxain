"""全局配置"""

# 境界体系
REALMS = [
    {"name": "淬体",   "min_level": 1,  "exp_mult": 1.0,   "hp_bonus": 0,   "atk_bonus": 0},
    {"name": "聚气",   "min_level": 10, "exp_mult": 1.5,   "hp_bonus": 50,  "atk_bonus": 10},
    {"name": "筑基",   "min_level": 20, "exp_mult": 2.0,   "hp_bonus": 150, "atk_bonus": 25},
    {"name": "金丹",   "min_level": 35, "exp_mult": 3.0,   "hp_bonus": 300, "atk_bonus": 50},
    {"name": "元婴",   "min_level": 50, "exp_mult": 4.0,   "hp_bonus": 600, "atk_bonus": 100},
    {"name": "化神",   "min_level": 65, "exp_mult": 6.0,   "hp_bonus": 1000,"atk_bonus": 180},
    {"name": "炼虚",   "min_level": 80, "exp_mult": 8.0,   "hp_bonus": 1800,"atk_bonus": 300},
    {"name": "合道",   "min_level": 90, "exp_mult": 12.0,  "hp_bonus": 3000,"atk_bonus": 500},
    {"name": "渡劫",   "min_level": 100,"exp_mult": 20.0,  "hp_bonus": 5000,"atk_bonus": 800},
]

# 灵根品质加成
SPIRIT_ROOTS = {
    "废灵根":   {"exp_mult": 0.5, "luck": -5},
    "下品灵根": {"exp_mult": 1.0, "luck": 0},
    "中品灵根": {"exp_mult": 1.3, "luck": 3},
    "上品灵根": {"exp_mult": 1.6, "luck": 5},
    "天灵根":   {"exp_mult": 2.0, "luck": 10},
    "圣灵根":   {"exp_mult": 3.0, "luck": 15},
}

# 功法数据
TECHNIQUES = {
    # 正道功法
    "太虚吐纳诀": {"type": "正道", "rarity": "人阶", "atk_bonus": 10, "def_bonus": 5,  "mp_regen": 5,  "realm": "淬体"},
    "青元剑诀":   {"type": "正道", "rarity": "地阶", "atk_bonus": 25, "def_bonus": 10, "crit_rate": 15, "realm": "筑基"},
    "九霄雷法":   {"type": "正道", "rarity": "天阶", "atk_bonus": 60, "def_bonus": 20, "crit_rate": 25, "realm": "金丹"},
    # 魔道功法
    "血海吞天功": {"type": "魔道", "rarity": "地阶", "atk_bonus": 35, "def_bonus": 0,  "lifesteal": 10, "realm": "聚气"},
    "白骨观":     {"type": "魔道", "rarity": "地阶", "atk_bonus": 20, "def_bonus": 30, "realm": "筑基"},
    "噬魂诀":     {"type": "魔道", "rarity": "天阶", "atk_bonus": 50, "def_bonus": 10, "mp_steal": 15, "realm": "金丹"},
}

# 丹药数据
ITEMS = {
    "回气丹":   {"type": "消耗", "desc": "恢复30灵力", "price": 10},
    "疗伤丹":   {"type": "消耗", "desc": "恢复50生命", "price": 15},
    "破境丹":   {"type": "消耗", "desc": "突破成功率+20%", "price": 100},
    "延寿丹":   {"type": "消耗", "desc": "增加20年寿元", "price": 200},
    "洗髓丹":   {"type": "消耗", "desc": "重置灵根品质", "price": 500},
    "筑基丹":   {"type": "消耗", "desc": "筑基成功率+30%", "price": 80},
}

# 敌人数据
ENEMIES = {
    # 凡境
    "野狼":       {"hp": 30,  "attack": 5,  "exp": 10,  "level": 1,  "drops": {"疗伤丹": 0.3}},
    "山匪":       {"hp": 50,  "attack": 8,  "exp": 20,  "level": 3,  "drops": {"回气丹": 0.4}},
    "妖狐":       {"hp": 80,  "attack": 12, "exp": 35,  "level": 5,  "drops": {"疗伤丹": 0.5}},
    "黑山妖兽":   {"hp": 150, "attack": 18, "exp": 60,  "level": 8,  "drops": {"破境丹": 0.2}},
    # 灵境
    "血蝠":       {"hp": 200, "attack": 25, "exp": 80,  "level": 12, "drops": {"疗伤丹": 0.5}},
    "魔修":       {"hp": 350, "attack": 40, "exp": 150, "level": 18, "drops": {"回气丹": 0.6}},
    "妖将":       {"hp": 500, "attack": 55, "exp": 250, "level": 25, "drops": {"破境丹": 0.3}},
    "血河分身":   {"hp": 800, "attack": 80, "exp": 500, "level": 35, "drops": {"延寿丹": 0.2}},
    # 天境
    "天机傀儡":   {"hp": 1500,"attack": 120,"exp": 1000,"level": 50, "drops": {"洗髓丹": 0.15}},
    "血河老祖":   {"hp": 3000,"attack": 200,"exp": 3000,"level": 70, "drops": {"延寿丹": 0.5}},
}

# 宗门数据
SECTS = {
    "青云宗": {"type": "正道", "bonus": {"defense": 10}, "ranks": ["外门弟子","内门弟子","真传","长老","宗主"]},
    "万毒门": {"type": "魔道", "bonus": {"attack": 15}, "ranks": ["外门弟子","内门弟子","真传","长老","宗主"]},
    "天机阁": {"type": "中立", "bonus": {"luck": 5},    "ranks": ["外门弟子","内门弟子","真传","长老","宗主"]},
}
