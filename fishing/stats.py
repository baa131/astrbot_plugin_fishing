from dataclasses import dataclass
from typing import List, Optional

@dataclass
class FisherStats:
    user_id: str
    nickname: str
    catch_count: int
    total_value: int
    avg_value: float
    trash_rate: float  # 垃圾鱼占比

@dataclass
class BestCatch:
    fisher: str
    fish_name: str
    value: int
    rarity: int
    catch_time: float 