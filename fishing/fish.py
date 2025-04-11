from dataclasses import dataclass
from typing import Optional

@dataclass
class Fish:
    id: int
    name: str
    rarity: int  # 1-5 表示稀有度
    weight: int  # 重量(克)
    value: int   # 价值(积分)
    owner_id: Optional[str] = None   # 当前拥有者ID
    catch_time: Optional[float] = None  # 捕获时间
    no_sell_until: Optional[float] = None  # 禁售期截止时间
    
    @property
    def rarity_stars(self) -> str:
        return "⭐" * self.rarity
        
    @property
    def rarity_text(self) -> str:
        texts = {
            1: "垃圾",
            2: "普通", 
            3: "稀有",
            4: "史诗",
            5: "传说"
        }
        return texts.get(self.rarity, "未知") 