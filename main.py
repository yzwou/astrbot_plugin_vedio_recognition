from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.core.message.message_event_result import MessageChain
from astrbot.core.platform.sources.aiocqhttp.aiocqhttp_message_event import AiocqhttpMessageEvent


@register(
    "astrbot_plugin_video_recognition",
    "Yuwai",
    "AstrBot 识别视频文件",
    "0.0.3"
)
class MyPlugin(Star):

    def __init__(self, context: Context):
        super().__init__(context)

    @filter.platform_adapter_type(filter.PlatformAdapterType.AIOCQHTTP)
    async def on_aiocqhttp(self, event: AstrMessageEvent):
        msg_chain = event.message_obj.message

        # for seg in msg_chain:
        #     try:
        #         await event.send(MessageChain().message(seg.url))
        #     except AttributeError:
        #         await event.send(MessageChain().message(str(seg)))