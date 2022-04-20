"""
    练习1：定义函数，根据年月日，返回星期数。
    “星期一“
    “星期二”
    “星期三”
    。。。

    思路：年月日 --》 时间元祖 --》星期 --》 格式
"""
import time


def get_week(year, month, day):
    """
        获取星期数
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 星期几的字符串
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    dic_weeks = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
    return dic_weeks[tuple_time[6]]


# print(get_week(2022, 4, 15))


"""
    练习2：根据生日，计算活了多少天。
    思路： 当前时间 - 出生时间。
          差值换算成天
"""


def life_days(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_in_sec = time.time() - time.mktime(tuple_time)
    return life_in_sec / 60 / 60 // 24


print(life_days(1998, 5, 19))

