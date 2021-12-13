from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
import os
from Template.get_data_file import TempTable


class Bpm:
    def __init__(self, vendor):
        self.vendor = vendor
        self.driver = webdriver.Chrome()

    # vendor = TempTable().check_list()[1]
    # if vendor != "Huawei":
    #     driver = webdriver.Chrome()

    def input_vendor(self):
        """Заполняет поле вендора в BPM. Аргумент vendor передается из файла xlsx и означает имя вендора"""

        time.sleep(7)

        self.driver.find_elements_by_class_name(
            'base-edit-with-right-icon')[13].click()
        self.driver.implicitly_wait(10)

        vendor_list = [item.text for item in self.driver.find_element_by_class_name(
            'listview').find_elements_by_tag_name("li")]

        print(vendor_list)

        vendor_map = {
            vendor_list[0]: 1,
            vendor_list[1]: 2,
            vendor_list[2]: 3
        }

        action = ActionChains(self.driver)
        for _ in range(vendor_map[self.vendor]):
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        action.send_keys(Keys.ENTER)
        action.perform()
        self.driver.implicitly_wait(10)

    def upload_file(self):
        """ Загрузка файла в BPM """

        time.sleep(2)
        self.driver.execute_script("document.getElementById('CasePageTabsTabPanel-tabpanel-items').children[5].click()")

        time.sleep(7)
        self.driver.implicitly_wait(10)

        path_file = os.getcwd()

        self.driver.find_element_by_id('FileDetailV2AddRecordButtonButton-fileupload').send_keys(
            path_file + "\\Шаблоны для заявки в BPM_РРЛ.xlsx")
        time.sleep(17)
        self.driver.implicitly_wait(10)

    def get_sr(self):
        """ Получение номера заявки """

        if self.vendor != "Huawei":
            text_sa = self.driver.find_element_by_id('MainHeaderSchemaPageHeaderCaptionLabel').text.split()[1]
        else:
            text_sa = "новые пролеты"

        return text_sa

    def authorization_bpm(self):
        time.sleep(4)
        action = ActionChains(self.driver)
        action.key_down(Keys.ALT).key_down(Keys.ENTER).perform()
        time.sleep(10)

    def input_fields(self):
        """Заполняет поля в BPM"""

        self.driver.get("https://bpm.tele2.ru/0/Nui/ViewModule.aspx#SectionModuleV2/CaseSection/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.authorization_bpm()

        self.driver.find_element_by_class_name("actions-button-margin-right").click()
        self.driver.implicitly_wait(20)

        self.driver.find_element_by_xpath('//*[@id="CasePageSymptomsMemoEdit-el"]').send_keys(
            "Внести корректировки в СМ РРЛ")
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//*[@id="CasePageUsrSystemLookupEdit-el"]').send_keys("NOC", Keys.ENTER)
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_class_name('grid-listed-row').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_class_name('main-buttons').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//*[@id="CasePageServiceItemLookupEdit-el"]').send_keys(
            "TN: Изменение в системе мониторинга РРЛ", Keys.ENTER)
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_class_name('grid-listed-row').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_class_name('main-buttons').click()
        self.driver.implicitly_wait(10)

        self.input_vendor()
        self.upload_file()

        """ Нажатие на кнопку "Запуск в работу" """
        self.driver.find_element_by_xpath('//*[@id="CasePageBeginProcessingButtonButton-textEl"]').click()
        self.driver.implicitly_wait(10)
        sa_bpm = self.get_sr()
        time.sleep(3)
        self.driver.quit()

        return sa_bpm
