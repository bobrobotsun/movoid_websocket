#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : test_listener
# Author        : Sun YiFan-Movoid
# Time          : 2024/8/4 21:27
# Description   : 
"""
from movoid_websocket import WebSocketListener, OneListener


class TestListener:
    def test_import(self):
        wsl = WebSocketListener()
        ol = OneListener('')
        print(wsl)
        print(ol)
