# -*- coding:utf-8 -*-

import os
import subprocess
import time
import datetime

class AndroidTools():

    def run_cmd(self, str):
        '''启动cmd'''
        self.str = str
        self.run = os.popen(self.str)
        return self.run.read()

    def get_status(self):
        '''获取设备状态'''
        self.status = self.run_cmd("adb devices").strip()
        if self.status == "List of devices attached":
            self.status = "当前无设备连接"
        elif "offline" in self.status:
            subprocess.Popen('adb kill-server')
            subprocess.Popen('adb devices')
        else:
            self.status = self.status.replace("List of devices attached", "").strip()
        return self.status

    def install_package(self, file_path):
        '''装包'''
        # self.file_path = file_path
        pagkageName = "com.huobionchainwallet"
        if pagkageName in self.installed_package_list():
            self.run_cmd("adb install -r " + file_path)
        else:
            self.run_cmd("adb install " + file_path)

    def installed_package_list(self):
        '''查看已安装的应用'''
        self.packageList = self.run_cmd("adb shell pm list packages -3")
        

    def record_screen(self):
        '''录屏'''
        # self.screenrecord = self.run_cmd("adb shell screenrecord ")
        pass

    def screenshot(self):
        '''截图'''
        pass

    def get_log(self):
        '''拉日志'''
        pass

if __name__ == '__main__':
    AndroidTools().install_package()
    # AndroidTools().installed_package_list()