# import unittest,time
# from selenium import webdriver
#
# class Test_BaiDu_SouSuo(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(5)
#         self.driver.maximize_window()
#         self.driver.get("https://www.baidu.com/")
#
#     def tearDown(self):
#         time.sleep(5)
#         self.driver.quit()
#
#
#     def test_001(self):
#
#         self.driver.find_element_by_id("kw").send_keys("五星红旗")
#         self.driver.find_element_by_id("su").click()
#         time.sleep(2)
#         # 断言判断五星红旗_百度搜索等于标题
#         self.assertEqual("五星红旗_百度搜索",self.driver.title)
#
#     def test_002(self):
#
#         self.driver.find_element_by_id("kw").send_keys("Demon")
#         self.driver.find_element_by_id("su").click()
#         time.sleep(2)
#         # 断言判断lDemon_百度搜索等于标题
#         self.assertEqual("Demon_百度搜索",self.driver.title)
#
#     def test_003(self):
#
#         self.driver.find_element_by_id("kw").send_keys("laohu")
#         self.driver.find_element_by_id("su").click()
#         time.sleep(2)
#         # 断言判断laohu在源码里面
#         # self.assertIn("laohu",self.driver.page_source)
#         # 断言判断laohu等于源码
#         self.assertEqual("laohu",self.driver.page_source)
#
#
# if __name__ == "__main__":
#     unittest.main()# 调用main方法执行unitetest内所有test开头方法