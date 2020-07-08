import unittest,time
from selenium import webdriver

class Test_BaiDu_SouSuo(unittest.TestCase):
    # 一个类里面打开一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    # 一个类里面关闭一次
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    # 每个对象都打开一次
    def setUp(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)
        time.sleep(3)
    # # 每个对象都关闭一次
    # def tearDown(self):
    #     print("一条用例执行完毕")

    def test_001(self):

        self.driver.find_element_by_id("kw").send_keys("五星红旗")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        # 断言判断五星红旗_百度搜索等于标题
        self.assertEqual("五星红旗_百度搜索",self.driver.title)

    def test_002(self):

        self.driver.find_element_by_id("kw").send_keys("Demon")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        # 断言判断lDemon_百度搜索等于标题
        self.assertEqual("Demon_百度搜索",self.driver.title)

    def test_003(self):

        self.driver.find_element_by_id("kw").send_keys("laohu")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        # 断言判断laohu在源码里面
        # self.assertIn("laohu",self.driver.page_source)
        # 断言判断laohu等于源码
        self.assertEqual("laohu",self.driver.page_source)

if __name__ == "__main__":
    unittest.main()# 调用main方法执行unitetest内所有test开头方法