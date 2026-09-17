# -*- coding: utf-8 -*-
"""G06 复核公共 Playwright 工具：file:// 直开、每页新建 page、双监听 pageerror+console.error"""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = '/Users/bailey/Desktop/xiaohei-workplace/FundFlow'

def page_uri(rel):
    return pathlib.Path(ROOT, rel).as_uri()

class Harness:
    def __init__(self):
        self._pw = sync_playwright().start()
        self.browser = self._pw.chromium.launch()
        self.results = []   # (page_label, js_errors)

    def open(self, rel, wait_ms=600, label=None):
        """打开一个页面：新建 context+page，双监听，goto 后 wait"""
        errors = []
        ctx = self.browser.new_context()
        page = ctx.new_page()
        page.on('pageerror', lambda e: errors.append('pageerror: %s' % e))
        page.on('console', lambda m: errors.append('console.error: %s' % m.text) if m.type == 'error' else None)
        page.goto(page_uri(rel), wait_until='load')
        page.wait_for_timeout(wait_ms)
        label = label or rel
        return ctx, page, errors

    def close(self):
        self.browser.close()
        self._pw.stop()
