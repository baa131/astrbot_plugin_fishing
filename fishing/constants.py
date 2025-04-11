# 天气类型
WEATHER_TYPES = ['晴天', '阴天', '雨天', '暴雨', '极光', '潮汐']

# 鱼类等级
FISH_GRADES = ['S', 'A', 'B', 'C', 'D']

# 鱼类数据
FISH_DATA = {
    'S': {
        '金龙鱼': 2000,
        '霓虹鲤': 1800,
        '星辰鲈': 1500
    },
    'A': {
        '银鲫鱼': 800,
        '彩虹鱼': 700,
        '月光鱼': 600
    },
    'B': {
        '草鱼': 400,
        '鲤鱼': 300,
        '鲈鱼': 250
    },
    'C': {
        '小鲫鱼': 150,
        '泥鳅': 100,
        '河虾': 80
    },
    'D': {
        '蝌蚪': 30,
        '小虾米': 20,
        '水藻': 10
    }
}

# 鱼类品质显示
GRADE_DISPLAY = {
    'S': '【SSR】⭐⭐⭐⭐⭐',
    'A': '【SR】⭐⭐⭐⭐',
    'B': '【R】⭐⭐⭐',
    'C': '【N】⭐⭐',
    'D': '【C】⭐'
}

# 鱼类重量范围(kg)
FISH_WEIGHT_RANGE = {
    'S': (15.0, 30.0),
    'A': (8.0, 15.0),
    'B': (3.0, 8.0),
    'C': (1.0, 3.0),
    'D': (0.1, 1.0)
}

# 称号数据
TITLES = {
    'fisher_newbie': {
        'id': 1,
        'name': '初出茅庐',
        'condition': {'total_fishing': 10},
        'description': '累计钓鱼10次'
    },
    'fisher_amateur': {
        'id': 2,
        'name': '渔场新星',
        'condition': {'total_fishing': 50},
        'description': '累计钓鱼50次'
    },
    'fisher_master': {
        'id': 3,
        'name': '渔场大师',
        'condition': {'total_fishing': 100},
        'description': '累计钓鱼100次'
    },
    'rich_fisher': {
        'id': 4,
        'name': '富甲一方',
        'condition': {'total_coins': 10000},
        'description': '累计获得10000金币'
    },
    'rare_collector': {
        'id': 5,
        'name': '稀有收藏家',
        'condition': {'s_grade_fish': 5},
        'description': '获得5条S级鱼类'
    }
}

# 每日任务数据
DAILY_TASKS = {
    'daily_fishing': {
        'id': 1,
        'name': '勤劳渔夫',
        'condition': {'daily_fishing': 10},
        'description': '每日钓鱼10次',
        'reward': 200  # 金币奖励
    },
    'daily_s_fish': {
        'id': 2,
        'name': '寻找珍稀',
        'condition': {'daily_s_fish': 1},
        'description': '每日钓到1条S级鱼',
        'reward': 500
    },
    'daily_sell': {
        'id': 3,
        'name': '渔场商人',
        'condition': {'daily_sell': 1000},
        'description': '每日出售鱼获得1000金币',
        'reward': 300
    },
    'daily_bait': {
        'id': 4,
        'name': '饵料专家',
        'condition': {'daily_bait_use': 3},
        'description': '每日使用3次鱼饵',
        'reward': 150
    }
}

# 成就数据
ACHIEVEMENTS = {
    'first_fish': {
        'id': 1,
        'name': '初次捕获',
        'condition': {'total_fishing': 1},
        'description': '完成第一次钓鱼',
        'reward': 100
    },
    'millionaire': {
        'id': 2,
        'name': '百万富翁',
        'condition': {'total_coins': 1000000},
        'description': '累计获得100万金币',
        'reward': 10000
    },
    'fish_collector': {
        'id': 3,
        'name': '鱼类收藏家',
        'condition': {'unique_fish': 20},
        'description': '收集20种不同的鱼类',
        'reward': 5000
    }
}

# 特殊事件数据
SPECIAL_EVENTS = {
    'golden_hour': {
        'name': '黄金时刻',
        'description': '接下来1小时内钓鱼成功率提升50%',
        'effect': {'success_rate': 1.5},
        'duration': 3600  # 持续时间(秒)
    },
    'fish_frenzy': {
        'name': '鱼群狂潮',
        'description': '接下来30分钟内必定钓到鱼',
        'effect': {'success_rate': 1.0},
        'duration': 1800
    },
    'lucky_coins': {
        'name': '幸运金币',
        'description': '接下来1小时内出售鱼获得双倍金币',
        'effect': {'coin_multiplier': 2.0},
        'duration': 3600
    }
}

# 鱼饵数据
BAIT_DATA = {
    '普通鱼饵': {
        'price': 100,
        'effect': 0.1,
        'duration': 600,  # 10分钟
        'description': '略微提升钓鱼成功率，持续10分钟'
    },
    '高级鱼饵': {
        'price': 300,
        'effect': 0.2,
        'duration': 1200,  # 20分钟
        'description': '显著提升钓鱼成功率，持续20分钟'
    },
    '特级鱼饵': {
        'price': 500,
        'effect': 0.3,
        'duration': 3600,  # 1小时
        'description': '大幅提升钓鱼成功率和稀有鱼类出现概率，持续1小时'
    }
} 