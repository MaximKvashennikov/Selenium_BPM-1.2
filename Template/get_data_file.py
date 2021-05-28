import pandas as pd
from pandas import concat
import pretty_html_table
import os
import datetime
import pandas.io.formats.excel
import xlsxwriter

"""Явно указываю чтобы библиотека добавилась в исполняемый файл exe, баг pyinstaller"""


# from jinja2 import Template


class TempTable:
    def __init__(self, vendor):
        self.vendor = vendor

    def read_ex(self, sheet_name):
        # path_file = "\\".join(os.getcwd().split("\\")[:-1])

        """Основной путь"""
        path_file = os.getcwd()
        pd.set_option('display.max_colwidth', 2000)
        df1 = pd.read_excel(
            path_file + "\\Шаблоны для заявки в BPM_РРЛ.xlsx",
            sheet_name=sheet_name,
            encoding='cp1251',
        )

        return df1

    def check_list(self):
        """Проверка наличия строк на листе"""

        result_list = []
        df1 = self.read_ex(
            sheet_name=self.vendor
        )

        print(df1)
        if len(df1.index) == 0:
            check_result = "Лист пуст"
            result_list.extend([check_result, self.vendor, "NO_NEW_RRL"])
        else:
            check_result = "Лист не пуст"

            result_list.extend([check_result, self.vendor])

            df1 = df1[['IP адрес элемента', 'Новый пролет', 'Имя пролета', 'Диаметр антенн A', 'Диаметр антенн B',
                       'Высота подвеса А',
                       'Высота подвеса В']]

            df1 = df1[(df1['Новый пролет'] == 'Да')]

            # print("Количество новых пролетов :", len(df1.index))

            if len(df1.index) == 0:
                result_list.append("NO_NEW_RRL")
            else:
                result_list.append("YES_NEW_RRL")

            print('result_list: ', result_list)

        return result_list[0], result_list[1], result_list[2]

    def get_tab(self):
        df1 = self.read_ex(sheet_name=self.vendor)

        df1 = df1[['IP адрес элемента', 'Новый пролет', 'Имя пролета', 'Диаметр антенн A', 'Диаметр антенн B',
                   'Высота подвеса А',
                   'Высота подвеса В']]

        df1 = df1[(df1['Новый пролет'] == 'Да')]
        df1.drop(['Новый пролет'], axis='columns', inplace=True)

        return df1

    def conversion_to_html(self):
        df1 = self.get_tab()
        try:
            new_tab = pretty_html_table.build_table(df1, 'grey_dark')
        except Exception:
            new_tab = "Пустая таблица"

        # html_table = df1.to_html(open('my_file.html', 'w'), index=False)

        return new_tab

    def get_region(self):
        """Получение уникальных регионов из столбца с именем пролета, возвращает строку из регионов"""

        df = self.read_ex(sheet_name=self.vendor)
        df = df[(df['Новый пролет'] == 'Да')]
        # df = df['Имя пролета'].values[0]

        regions = []
        for rrl in list(df['Имя пролета'].tolist()):
            try:
                regions.append(rrl.split("_")[1][:2])

            except Exception:
                pass

        regions = list(set(regions))

        regions = ', '.join(regions)

        return regions

    def general_vault(self):
        """Добравлят данные из письма в общий свод. reset_index(drop=True)
        используется для работы стилей и уникальности"""

        # pandas.io.formats.excel.ExcelFormatter.header_style = None
        df1 = self.get_tab()
        df1['Дата'] = datetime.datetime.now().strftime("%d-%m-%Y")
        df1['Вендор'] = self.vendor

        path_vault = r'\\t2ru\CPFolders\T2CP-FPS-02\Transport_Data_Exploitation\\HAD.xlsx'
        path_vault_csv = r'\\t2ru\CPFolders\T2CP-FPS-02\Transport_Data_Exploitation\\HAD.csv'
        try:
            df_vault = pd.read_excel(
                path_vault,
                encoding='cp1251',
            )

            df_vault = concat([df1, df_vault], sort=False)
            print(df_vault)

            """Использует Jinja2, но при создании exe выйдет ошибка, баг pyinstaller"""
            # df_vault = df_vault.reset_index(drop=True).style.set_properties(**{'background-color': '#E6E6FA',
            #                                                                    'font-size': '11pt',
            #                                                                    'font-family': 'Malgun Gothic',
            #                                                                    })

            # df_vault.to_excel(path_vault, index=False)

            """Доп файл в формате csv"""
            df_vault.to_csv(path_vault_csv, encoding='utf-8-sig', index=False, sep=';')

            """Изменение формата заголовка и запись"""
            with pd.ExcelWriter(path_vault, engine='xlsxwriter') as writer:
                df_vault.to_excel(writer, sheet_name='Vault', index=False)

                workbook = writer.book
                worksheet = writer.sheets['Vault']

                header_format = workbook.add_format({
                    'bold': True,
                    'fg_color': '#B0C4DE',
                    'border': 2,
                })
                for col_num, value in enumerate(df_vault.columns.values):
                    worksheet.write(0, col_num, value, header_format)
                worksheet.set_column('A:A', 17)
                worksheet.set_column('B:B', 30)
                worksheet.set_column('C:C', 17)
                worksheet.set_column('D:D', 17)
                worksheet.set_column('E:E', 17)
                worksheet.set_column('F:F', 17)
                worksheet.set_column('G:G', 11)
                worksheet.set_column('H:H', 11)

        except Exception as er:
            print(er, ': Нет общего свода или доступа')


if __name__ == "__main__":
    TempTable(vendor='Huawei').general_vault()
