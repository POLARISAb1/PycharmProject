# _*_ coding: utf-8 _*_

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

JSON_Representation = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".common.MainActivity",
  "noReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", JSON_Representation)
driver.implicitly_wait(10)

el1 = driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
el2.click()
el2.send_keys("阿里巴巴")
el3 = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android"
                                          ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup"
                                          "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                          ".RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget"
                                          ".ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx"
                                          ".recyclerview.widget.RecyclerView/android.widget.LinearLayout["
                                          "1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
                                          ".LinearLayout/android.widget.FrameLayout["
                                          "1]/android.widget.RelativeLayout/android.widget.LinearLayout[1]")
el3.click()


