#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

from settings import *


def login(url):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_css_selector("div.qrcode-signin-cut-button > span.signin-switch-password").click()
    browser.find_element_by_name("account").send_keys(EMAIL)
    browser.find_element_by_name("password").send_keys(PASSWORD)
    # input capcha
    time.sleep(7)

    browser.find_element_by_css_selector("div.button-wrapper > button.sign-button").click()


if __name__ == '__main__':
    url = 'http://www.zhihu.com/#signin'
    login(url)
