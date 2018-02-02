# File: proto_test.py
# Author: Ben Heil
# Since: 2/2/18

from Level import Level
import pygame


def test_Level_init():
    lvl = Level()
    assert lvl.walking == False
    assert lvl.kick == False

def test_Level_run():
    lvl = Level()
    assert lvl.run() == 0

