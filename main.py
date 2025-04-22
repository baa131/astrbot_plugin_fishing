import os
import logging
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from .fishing.fishing import FishingSystem
from .fishing.db import FishingDB

@register("fishing", "Your Name", "一个功能齐全的钓鱼系统插件", "1.0.0", "https://github.com/yourusername/astrbot_plugin_fishing")
class FishingPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        # 初始化日志记录器
        self.logger = logging.getLogger("FishingPlugin")
        
        # 初始化数据目录
        self.data_dir = "data/"
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 初始化数据库和钓鱼系统
        db_path = os.path.join(self.data_dir, "fishing.db")
        self.config = {
            'database': db_path,
            'auto_fishing_enabled': True,
            'base_cost': 50,
            'weather_update_interval': 3600,
            'initialize_fish_types': True,
            'baits': [
                {
                    'name': '普通鱼饵',
                    'price': 100,
                    'effect': 0.1,
                    'description': '略微提升钓鱼成功率'
                },
                {
                    'name': '高级鱼饵',
                    'price': 300,
                    'effect': 0.2,
                    'description': '显著提升钓鱼成功率'
                },
                {
                    'name': '特级鱼饵',
                    'price': 500,
                    'effect': 0.3,
                    'description': '大幅提升钓鱼成功率和稀有鱼类出现概率'
                }
            ]
        }
        self.db = FishingDB(db_path)
        self.fishing_system = FishingSystem(self.config, self.get_user_nickname)
        
        self.logger.info("钓鱼插件初始化完成")
    
    def get_user_nickname(self, user_id: str) -> str:
        """获取用户昵称"""
        # 可以通过AstrBot API获取用户昵称
        try:
            # 尝试从AstrBot获取用户信息
            # 这里仅作示例，实际实现需要根据AstrBot的API
            return user_id  # 如果无法获取，则返回用户ID
        except Exception as e:
            self.logger.error(f"获取用户昵称出错: {e}")
            return user_id
    
    @filter.command("钓鱼")
    async def fishing(self, event: AstrMessageEvent):
        '''开始钓鱼'''
        user_id = event.get_sender_id()
        result = self.fishing_system.fish(user_id)
        yield event.plain_result(result)
    
    @filter.command("鱼塘")
    async def fish_pond(self, event: AstrMessageEvent):
        '''查看自己的鱼塘'''
        user_id = event.get_sender_id()
        result = self.fishing_system.get_user_fish_pond(user_id)
        yield event.plain_result(result)
    
    @filter.command("卖鱼")
    async def sell_fish(self, event: AstrMessageEvent):
        '''卖出鱼获得金币'''
        user_id = event.get_sender_id()
        message = event.message_str
        # 解析参数，提取鱼名和数量
        parts = message.split()
        if len(parts) >= 3:
            fish_name = parts[1]
            try:
                amount = int(parts[2])
                result = self.fishing_system.sell_fish(user_id, fish_name, amount)
                yield event.plain_result(result)
            except ValueError:
                yield event.plain_result("❌ 请输入正确的数量")
        else:
            yield event.plain_result("格式: /卖鱼 [鱼名] [数量]")
    
    @filter.command("全部卖出")
    async def sell_all_fish(self, event: AstrMessageEvent):
        '''卖出所有鱼获得金币'''
        user_id = event.get_sender_id()
        result = self.fishing_system.sell_all_fish(user_id)
        yield event.plain_result(result)
    
    @filter.command("自动钓鱼")
    async def auto_fishing(self, event: AstrMessageEvent):
        '''开启/关闭自动钓鱼'''
        user_id = event.get_sender_id()
        result = self.fishing_system.toggle_auto_fishing(user_id)
        yield event.plain_result(result)
    
    @filter.command("钓鱼帮助")
    async def fishing_help(self, event: AstrMessageEvent):
        '''显示钓鱼帮助信息'''
        result = self.fishing_system.show_help()
        yield event.plain_result(result)
    
    @filter.command("鱼类图鉴")
    async def fish_guide(self, event: AstrMessageEvent):
        '''查看鱼类图鉴'''
        result = self.db.get_all_fish_types()
        yield event.plain_result(result)
    
    @filter.command("钓鱼签到")
    async def daily_check_in(self, event: AstrMessageEvent):
        '''每日钓鱼签到'''
        user_id = event.get_sender_id()
        result = self.fishing_system.daily_check_in(user_id)
        yield event.plain_result(result)
    
    @filter.command("鱼饵商城")
    async def bait_shop(self, event: AstrMessageEvent):
        '''查看鱼饵商城'''
        result = self.fishing_system.show_bait_shop()
        yield event.plain_result(result)
    
    @filter.command("购买鱼饵")
    async def buy_bait(self, event: AstrMessageEvent):
        '''购买鱼饵'''
        user_id = event.get_sender_id()
        message = event.message_str
        # 解析参数，提取鱼饵名称
        parts = message.split()
        if len(parts) >= 2:
            bait_name = parts[1]
            result = self.fishing_system.buy_bait(user_id, bait_name)
            yield event.plain_result(result)
        else:
            yield event.plain_result("格式: /购买鱼饵 [鱼饵名称]")
    
    @filter.command("使用鱼饵")
    async def use_bait(self, event: AstrMessageEvent):
        '''使用鱼饵'''
        user_id = event.get_sender_id()
        message = event.message_str
        # 解析参数，提取鱼饵名称
        parts = message.split()
        if len(parts) >= 2:
            bait_name = parts[1]
            result = self.fishing_system.use_bait(user_id, bait_name)
            yield event.plain_result(result)
        else:
            yield event.plain_result("格式: /使用鱼饵 [鱼饵名称]")
    
    @filter.command("我的鱼饵")
    async def my_baits(self, event: AstrMessageEvent):
        '''查看我的鱼饵'''
        user_id = event.get_sender_id()
        result = self.fishing_system.show_my_baits(user_id)
        yield event.plain_result(result)
    
    @filter.command("天气")
    async def weather(self, event: AstrMessageEvent):
        '''查看钓鱼天气'''
        result = self.fishing_system.get_weather_info()
        yield event.plain_result(result)
    
    async def terminate(self):
        '''插件被卸载/停用时调用'''
        self.logger.info("钓鱼插件正在终止...")
        # 结束自动钓鱼线程等清理工作
        # 关闭数据库连接等
