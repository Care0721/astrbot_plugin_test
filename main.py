from astrbot.api.all import *
from astrbot.api import AstrBotConfig
import time

@register("bot_online_test", "Care", "在线测试：发送“测试”证明Bot在线", "1.3.0")
class BotOnlineTestPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        
        # 从网页配置读取回复模板
        self.reply_template = self.config.get(
            "reply_template",
            "Bot 在线状态确认\n当前时间：{time}\nBot 运行正常，未检测到掉线。\n如需进一步测试或确认状态，请随时发送指令。"
        )

    @command("测试")
    async def test_online(self, event: AstrMessageEvent):
        # 获取当前时间
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        # 模版配置（支持 {time} 占位符）
        reply_text = self.reply_template.format(time=current_time)
        
        yield event.plain_result(reply_text)