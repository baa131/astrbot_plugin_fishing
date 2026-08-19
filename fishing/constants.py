# 天气类型
WEATHER_TYPES = ['晴天', '阴天', '雨天', '暴雨', '极光', '潮汐']

# 天气效果
WEATHER_EFFECTS = {
    '晴天': {'success_rate': 0.7, 'cost_modifier': 1.0},
    '阴天': {'success_rate': 0.6, 'cost_modifier': 1.0},
    '雨天': {'success_rate': 0.5, 'cost_modifier': 1.05},
    '暴雨': {'success_rate': 0.3, 'cost_modifier': 1.1},
    '极光': {'success_rate': 0.6, 'cost_modifier': 1.1},
    '潮汐': {'success_rate': 0.8, 'cost_modifier': 0.9}
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