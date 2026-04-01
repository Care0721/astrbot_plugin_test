from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Star, register
from astrbot.api import logger, AstrBotConfig
from astrbot.api.star import Context    Context
import time

@register("bot_online_test", "Care", "在线测试：发送“测试”证明Bot在线", "1.0.5")
class BotOnlineTestPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        
        # 从网页配置读取回
        self.reply_template = self.config.get(
            "reply_template",
            "Bot 在线状态确认\n当前时间：{time}\nBot 运行正常，未检测到掉线。\n如需进一步测试或确认状态，请随时发送指令。"
        )

    @filter.command("测试")
    async def test_online(self, event: AstrMessageEvent):
        # 记录日志
        logger.info(f"[在线测试] 被触发 | 用户: {event.get_sender_name()}({event.get_sender_id()})")

        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        try:
            reply_text = self.reply_template.format(time=current_time)
        except Exception:
            reply_text = (
                f"Bot 在线状态确认\n"
                f"当前时间：{current_time}\n"
                f"Bot 运行正常，未检测到掉线。"
            )
        
        yield event.plain_result(reply_text)