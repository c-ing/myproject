# -*- encoding=utf8 -*-
__author__ = "asus"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco("android:id/text1").click()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text='钉钉').click()

#poco(text="动品在线").click()
#poco(text="考勤打卡").click()

#poco("com.tencent.mm:id/aa")
#poco("com.tencent.mm:id/kg")
#poco("com.tencent.mm:id/l2")

sleep(1.0)

# 定位到工作
#poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.alibaba.android.rimet:id/home_content").offspring("com.alibaba.android.rimet:id/container").child("android.widget.FrameLayout").offspring("android.webkit.WebView").child("android.view.View").child("android.view.View")[0].child("android.view.View").child("android.view.View")[4].child("android.view.View")[0].child("android.view.View").click()
poco(name="com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()

sleep(5.0)


poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.alibaba.android.rimet:id/home_content").offspring("com.alibaba.android.rimet:id/container").child("android.widget.FrameLayout").offspring("android.webkit.WebView").child("android.view.View").child("android.view.View")[2].swipe([0.0668, -0.6766])

sleep(3.0)


# 定位到考勤打卡
poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.alibaba.android.rimet:id/home_content").offspring("com.alibaba.android.rimet:id/container").child("android.widget.FrameLayout").offspring("android.webkit.WebView").child("android.view.View").child("android.view.View")[0].child("android.view.View").child("android.view.View")[0].child("android.view.View").child("android.view.View").child("android.view.View").click()


# 定位到电话会议
'''poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.alibaba.android.rimet:id/home_content").offspring("com.alibaba.android.rimet:id/container").child("android.widget.FrameLayout").offspring("android.webkit.WebView").child("android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View")[0].child("android.view.View").click()'''


# 上班打卡
sleep(3.0)
poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("android.widget.ListView")[0].child("android.view.View").child("android.view.View").child("android.view.View")[2].click()


