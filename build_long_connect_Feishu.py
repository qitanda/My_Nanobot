import lark_oapi as lark
from lark_oapi.api.im.v1 import P2ImMessageReceiveV1

# 1. 定义事件处理函数
def do_p2_im_message_receive_v1(data: P2ImMessageReceiveV1) -> None:
    print(f'[收到消息] content: {lark.JSON.marshal(data.event.message.content)}')

# 2. 初始化客户端并启动
def main():
    # 1. 创建事件分发器 (这部分保持不变)
    event_handler = lark.EventDispatcherHandler.builder("", "") \
        .register_p2_im_message_receive_v1(do_p2_im_message_receive_v1) \
        .build()

    # 2. 创建长连接客户端 (修改这里！直接实例化)
    # 旧写法 (报错): client = lark.ws.Client.builder(...).build()
    # 新写法 (正确):
    client = lark.ws.Client(
        "cli_a91b36ea0a385bd2",          # 你的 App ID
        "iEBiLk9F5AMuHqxLPzvapcVMisEEkjwV",            # 你的 App Secret
        event_handler=event_handler,  # 注入事件处理器
        log_level=lark.LogLevel.DEBUG # 可选: 开启调试日志
    )

    # 3. 启动连接
    client.start()

if __name__ == "__main__":
    main()