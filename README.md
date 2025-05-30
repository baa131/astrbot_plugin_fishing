# AstrBot钓鱼插件

一个功能齐全的钓鱼系统插件，支持钓鱼、鱼塘管理、鱼类交易等功能。

## 功能特点

- 完整的钓鱼系统，支持不同稀有度的鱼类
- 用户鱼塘管理，查看自己钓到的鱼
- 鱼类交易系统，出售鱼获得金币
- 自动钓鱼功能
- 鱼类稀有度分级系统
- 多样化的鱼类资源

## 安装方法

### 通过插件市场安装

1. 在AstrBot管理面板中选择"插件市场"
2. 搜索"钓鱼"或"fishing"
3. 点击安装本插件

### 手动安装

```bash
cd {AstrBot目录}/data/plugins
git clone https://github.com/yourusername/astrbot_plugin_fishing
```

## 使用方法

插件提供以下命令：

- `/钓鱼` - 开始钓鱼
- `/鱼塘` - 查看自己的鱼塘
- `/卖鱼 [鱼名] [数量]` - 卖出指定数量的鱼获得金币
- `/全部卖出` - 卖出鱼塘中所有可卖出的鱼
- `/钓鱼帮助` - 显示帮助信息
- `/自动钓鱼` - 开启/关闭自动钓鱼功能

## 配置说明

插件首次运行时会在插件数据目录创建配置文件，你可以根据需要修改以下配置：

- `auto_fishing_enabled`: 是否启用自动钓鱼功能
- `auto_fishing_interval`: 自动钓鱼的时间间隔(秒)
- `fishing_cost`: 每次钓鱼的成本(金币)

## 常见问题

**Q: 为什么我无法开启自动钓鱼？**  
A: 请确保你有足够的金币，并且自动钓鱼功能在配置中已启用。

**Q: 如何增加稀有鱼的出现概率？**  
A: 使用特级鱼饵可以提高稀有鱼类的出现概率。

## 贡献

欢迎提交Issue和Pull Request来完善本插件。

## 许可证

本项目采用MIT许可证。
