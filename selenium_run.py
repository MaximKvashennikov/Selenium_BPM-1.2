from datetime import datetime
from Mail.send_mail import SendMail
import win32com.client as win32
import os
from win_err_bpm import Ui_MainWindow
from BPM.input_bpm import Bpm
import time
import os
from Template.get_data_file import TempTable
from win_successfully_bpm import Ui_Main_Successfully


def log(log_str):
    """ Перехват всех исключений и запись в файл """

    path_file = os.getcwd()
    with open(path_file + "\\error_log.txt", "a", ) as file_log:
        print(log_str)
        file_log.writelines([datetime.now().strftime("%d-%m-%Y %H.%M.%S# "), '  ', log_str, '\n'])


def main():
    try:
        for vendor_on_list in ["Ericsson", "NEC", "Ceragon", "Huawei"]:
            """Обходим каждую страницу листа и заводим заявки, отправляем письма."""

            print("vendor_on_list: ", vendor_on_list)

            table_class = TempTable(vendor=vendor_on_list)
            if table_class.check_list()[0] == "Лист не пуст":

                if vendor_on_list != "Huawei":
                    sa_bpm = Bpm(vendor=vendor_on_list).input_fields()
                else:
                    sa_bpm = 'новый пролет'
                if table_class.check_list()[2] == "YES_NEW_RRL":
                    SendMail(
                        win32=win32,
                        get_sr=sa_bpm,
                        vendor=vendor_on_list
                    ).send_mail()
                    table_class.general_vault()
                    time.sleep(1)
        Ui_Main_Successfully().run_win()
    except Exception as err_str:
        err = 'Ошибка: ' + str(err_str)
        log(err)
        Ui_MainWindow().run_win()


if __name__ == "__main__":
    main()
