#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def 主程序(参数):
    错 = "没法比色：请给出两种颜色，每种是红、绿、蓝三个零到二百五十五的整数\n"
    if len(参数) != 6:
        sys.stderr.write(错)
        return 2
    盒子 = []
    for 段 in 参数:
        if 段[:1] == "+":
            sys.stderr.write(错)
            return 2
        身 = 段[1:] if 段[:1] == "-" else 段
        if 身 == "" or any(字 not in "0123456789" for 字 in 身):
            sys.stderr.write(错)
            return 2
        值 = int(段)
        if 值 < 0 or 值 > 255:
            sys.stderr.write(错)
            return 2
        盒子.append(值)
    甲 = 盒子[0] * 30 + 盒子[1] * 59 + 盒子[2] * 11
    乙 = 盒子[3] * 30 + 盒子[4] * 59 + 盒子[5] * 11
    if 甲 < 乙:
        临时 = 甲
        甲 = 乙
        乙 = 临时
    if 甲 + 1 >= (乙 + 1) * 3:
        sys.stdout.write("够\n")
    else:
        sys.stdout.write("不够\n")
    return 0


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
