import time
from time import sleep


Prefix = "!!timer"
helpmsg = '''§b----Timer----§r
''' + Prefix + ''' | 显示帮助信息
''' + Prefix + ''' [[整数]h][[整数]m][[整数]s] | 设置倒计时
!!timer 1h3m20s     设置时长为1小时3分钟20秒的倒计时
!!timer 10m         设置时长为10分钟的倒计时
!!timer 11h2s       设置时长为11小时2秒的倒计时'''


def decode_input(input):
    if "h" in input:
        hour = input.split('h')[0]
        input = input.split('h')[1]
    else:
        hour = 0
    if "m" in input:
        minute = input.split('m')[0]
        input = input.split('m')[1]
    else:
        minute = 0
    if "s" in input:
        second = input.split('s')[0]
    else:
        second = 0
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def timer(server, info, time, toall, comment):
    if toall:
        server.say("开始"+str(time)+"秒倒计时 " + comment, encoding=None)
        sleep(time*3/4)
        server.say("倒计时 " + comment +" 剩余" + str(time/4) + "秒", encoding=None)
        sleep(time/4)
        server.say("倒计时 " + comment +" 已结束!", encoding=None)


def on_info(server, info):
    if info.is_player:
        if info.content.startswith(Prefix):
            if len(info.content.split(' ')) == 2:
                timer_time = decode_input(info.content.split(' ')[1])
                timer(server, info, timer_time, True, "")
            if info.content == Prefix:
                server.tell(info.player, helpmsg)


def on_load(server, old_module):
    server.add_help_message(Prefix, '倒计时')
