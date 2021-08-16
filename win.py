# -*- coding: utf-8 -*-
from pywinauto.application import Application

def start_app(path):
    app = Application(backend="win32").start(path)
return app

def connect_app(path):
    app = Application().connect(path=path)
return app


def start_uia_app(path):
    app = Application(backend="uia").start(path)
return app
