# encoding: utf-8

"""This is a docstring"""

import os
import sys
sys.path.append("..")
from selenium.common.exceptions import NoSuchElementException
import driver.appdriver as appdriver
from time import sleep
from xml.etree import ElementTree as elementTree
import config.config as readConfig

global  outtimes
configLocal = readConfig.ReadConfig()



class Operation(object):
    """This is a docstring"""


    def is_exist(self, operationdriver, type, value):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """

        if self.get_context(operationdriver) != "NATIVE_APP":
            operationdriver.switch_to.context(operationdriver.contexts[-1])

        try:
            if type == "id":
                return operationdriver.find_element_by_id(value)
            
            if type == "classname":
                return operationdriver.find_element_by_class_name(value)
            if type == "xpath":
                return operationdriver.find_element_by_xpath(value)
                 
            if type == "name":
                return operationdriver.find_element_by_name(value)
                 
            return False
        except NoSuchElementException as e:
            return e

    def does_exist(self, operationdriver, type, value):
        """
        To determine whether an element is exits
        :return:
        """
        i = 1
        while not self.is_exist(operationdriver, type, value):
            sleep(1)
            i += 1

            if i >= int(configLocal.get_config_value("findElementTimes")):
                return False
        else:
            return True

    def get_element(self, operationdriver, type, value, index='0'):
        """
        get one element
        :return:
        """
        if self.does_exist(operationdriver, type, value):
            if type == "id":
                element = operationdriver.find_element_by_id(value)
                return element
            if type == "classname":
                element = operationdriver.find_element_by_class_name(value)
                return element
            if type == "xpath":
                element = operationdriver.find_element_by_xpath(value)
                return element
            if type == "name":
                element = operationdriver.find_element_by_name(value)
                return element
            if type == "link_text":
                element_list = operationdriver.find_element_partial_by_link_text(value)
                return element
            if type == "tag_name":
                element_list = operationdriver.find_element_by_tag_name(value)
                return element
            if type == "css_selector":
                element_list = operationdriver.find_element_by_css_selector(value)
                return element
            return None
        else:
            return None

    def get_element_list(self, operationdriver, type, value):
        """
        get elementList
        :return:elements
        """
        if self.does_exist(operationdriver, type, value):
            if type == "id":
                element_list = operationdriver.find_elements_by_id(value)
                return element_list
            if type == "classname":
                element_list = operationdriver.find_elements_by_class_name(value)
                return element_list
            if type == "xpath":
                element_list = operationdriver.find_elements_by_xpath(value)
                return element_list
            if type == "name":
                element_list = operationdriver.find_elements_by_name(value)
                return element_list
            if type == "link_text":
                element_list = operationdriver.find_elements_by_partial_link_text(value)
                return element_list
            if type == "tag_name":
                element_list = operationdriver.find_elements_by_tag_name(value)
                return element_list
            if type == "css_selector":
                element_list = operationdriver.find_elements_by_css_selector(value)
                return element_list
            return None
        else:
            return None

    def get_element_byios_uiautomation(self, operationdriver, elements):
        """
        get_element_byios_uiautomation
        """
        return operationdriver.find_element_by_ios_uiautomation(element)

    def get_element_by_accessibility_id(self, operationdriver, id):
        """
        get_element_by_accessibility_id
        """
        return operationdriver.find_elements_by_accessibility_id(id)

    def get_element_value(self, operationdriver, type, value, index='0'):
        """
        # 返回元素的文本值
        """
        element = self.get_element(operationdriver, type, value, index)
        return element.text()

    def get_element_size(self, operationdriver, type, value, index='0'):
        """
        # 返回元素的文本值
        """
        element = self.get_element(operationdriver, type, value, index)
        return element.size()

    def get_element_location(self, operationdriver, type, value, index='0'):
        """
        # 返回元素的文本值
        """
        element = self.get_element(operationdriver, type, value, index)
        return element.location()

    def is_selected(self, operationdriver, type, value, index='0'):
        """
        is_selected
        """
        element = self.get_element(operationdriver, type, value, index)
        return  element.is_slected()

    def click(self, operationdriver, type, value, index='0'):
        """
        click element
        :return:
        """
        try:
            element = self.get_element(operationdriver, type, value, index)
            if element:

                element.click()
            else:
                print value,
                print 'is not exits'
        except AttributeError as e:
            raise e
 
    def send_key(self, operationdriver, type, value, index='0', values='fengshuai'):
        """
        input the key
        :param values
        :return:
        """
        try:
            element = self.get_element(operationdriver, type, value, index)
            element.clear()
            element.send_keys(values)
        except AttributeError as e:
            raise e

    def get_contexts(self, operationdriver):
        """
        :param values
        :return: 返回当前会话中的上下文，使用后可以识别h5的页面控件
        """
        values = operationdriver.contexts
        return values


    def get_context(self, operationdriver):
        """
        :param values
        :return: 返回当前会话中的上下文
        """
        value = operationdriver.context
        return value

    def get_tag_name(self, operationdriver, type, value, index='0'):
        """
        get_tag_name
        """
        element = self.get_element(operationdriver, type, value, index)
            
        return element.tag_name()

    def get_window_size(self, operationdriver):
        """
        get current windows size mnn
        :return:windowSize
        """
        global windowSize
        windowSize = operationdriver.get_window_size()
        return windowSize

    def scroll(self, operationdriver, origin_element, destination_element):
        """# 从元素origin_el滚动至元素destination_el
        """
        operationdriver.scroll(origin_element, destination_element)

    def drag_and_drop(self, operationdriver, origin_element, destination_element):
        """# 将元素origin_el拖到目标元素destination_el
        """
        operationdriver.drag_and_drop(origin_element, destination_element)

    def tap(self, operationdriver, positions, duration=1000):
        """"#模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）
        #operationdriver.tap([(x,y),[x1,y1]]),500)
        """
        operationdriver.tap(positions, duration)

    def swipe(self, operationdriver, start_x, start_y, end_x, end_y, duration=None):
        """#从A点滑动至B点，滑动时间为毫秒
        """
        operationdriver.swipe(start_x, start_y, end_x, end_y, duration)

    def flick(self, operationdriver, start_x, start_y, end_x, end_y, duration=None):
        """#按住A点后快速滑动至B点
        """
        operationdriver.flick(start_x, start_y, end_x, end_y, duration)
        
    def swipe_to_up(self, operationdriver, during=None):
        """
        swipe UP
        :param during:
        :return:
        """
        # if windowSize == None:
        window_size = get_window_size()

        width = window_size.get("width")
        height = window_size.get("height")
        operationdriver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, during)

    def swipe_to_down(self, operationdriver, during=None):
        """
        swipe down
        :param during:
        :return:
        """
        window_size = get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        operationdriver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, during)

    def swipe_to_left(self, operationdriver, during=None):
        """
        swipe left
        :param during:
        :return:
        """
        window_size = get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        operationdriver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, during)

    def swipe_to_right(self, operationdriver, during=None):
        """
        swipe right
        :param during:
        :return:
        """
        window_size = get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        operationdriver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, during)

    def reset(self):
        """
        #重置应用(类似删除应用数据)
        """
        operationdriver.reset()

    def hide_keyboard(self, operationdriver, key_name=None, key=None, strategy=None):
        """
        #隐藏键盘,iOS使用key_name隐藏，安卓不使用参数
        #Hides the software keyboard on the device. In iOS, use `key_name` to press a particular key, or `strategy`. 
        #In Android, no parameters are used.
        """
        operationdriver.hide_keyboard(key_name)

    def long_press_keycode(self, operationdriver, keycode, metastate=None):
        """
        #发送一个长按的按键码（长按某键）
        """
        operationdriver.long_press_keycode(keycode)

    def background_app(self, operationdriver, seconds):
        """
        # 后台运行app多少秒
        """
        operationdriver.background_app(seconds)

    def is_app_installed(self, operationdriver, bundle_id):
        """
        app is_app_installed
        """
        operationdriver.is_app_installed(bundle_id)

    def remove_app(self, operationdriver, bundle_id):
        """
        remove_app
        """
        operationdriver.remove_app(bundle_id)

    def lock(self, operationdriver, seconds):
        """#锁屏一段时间  iOS专有"""
        operationdriver.lock(seconds)

    def set_location(self, operationdriver, latitude, longitude, altitude):
        """
        设置设备的经纬度
        :Args:
         - latitude纬度 - String or numeric value between -90.0 and 90.00
         - longitude经度 - String or numeric value between -180.0 and 180.0
         - altitude海拔高度- String or numeric value
        """
        operationdriver.set_location(operationdriver, latitude, longitude, altitude)




































