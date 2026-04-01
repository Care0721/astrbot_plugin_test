from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star
from astrbot.api import register, logger, AstrBotConfig
import time

@register("bot_online_test", "Care", "用于用户测试自己的bot是否在线", "1.3.0")
class BotOnlineTestPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        
        # 网页配置读取模板
        self.reply_template = self.config.get(
            "reply_template",
            "Bot 在线状态确认\n当前时间：{time}\nBot 运行正常，未检测到掉线。\n如需进一步测试或确认状态，请随时发送指令。"
        )

    @filter.command("测试")
    async def test_online(self, event: AstrMessageEvent):
        # 记录日志
        logger.info(f"[在线测试] 被触发 | 用户: {event.get_sender_name()}({event.get_sender_id()}) | 时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        # 获取精确时间
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        # 安全格式化
        try:
            reply_text = self.reply_template.format(time=current_time)
        except Exception:
            # 回退到默认回复
            reply_text = (
                f"Bot 在线状态确认\n"
                f"当前时间：{current_time}\n"
                f"Bot 运行正常，未检测到掉线。\n"
                f"[提示：回复模板格式异常，已使用默认模板]"
            )
        
        yield event.plain_result(reply_text)