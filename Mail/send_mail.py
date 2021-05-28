import win32com.client as win32
from Mail.body_mail import BodyMail
from Template.get_data_file import TempTable


class SendMail:
    def __init__(self, win32, get_sr, vendor):
        self.win32 = win32
        self.text_sa = get_sr
        self.vendor = vendor

    def send_mail(self):
        region = TempTable(vendor=self.vendor).get_region()
        outlook = self.win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        """ Разработка отправки определенных почтовых групп"""

        regions_list = region.split(', ')
        print(regions_list)

        mail_dict = {'KA': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, tn_krs@tele2.ru',
                     'TO': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, bss.tom@tele2.ru',
                     'AL': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, BSS.BRN@tele2.ru',
                     'GA': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, BSS.BRN@tele2.ru',
                     'TY': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, BSS.TYV@tele2.ru',
                     'HK': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, BSS.KHA@tele2.ru',
                     'KE': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, bss.kem@tele2.ru',
                     'NS': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, bss.nsk@tele2.ru',
                     'OM': 'Sib_LRD@tele2.ru, Transport.CP_Access@tele2.ru, bss.oms@tele2.ru',
                     'CV': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.CHV@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'IZ': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.izh@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'KI': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.kir@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'NN': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, Transport.NIN@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'SR': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.sam@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'TT': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, Transport.TT@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'UL': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.ULN@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'YO': ('MR_VOLGA_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.YOL@tele2.ru, '
                            'Transport.VGA@tele2.ru'),
                     'CH': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, Transport.CHE@tele2.ru',
                     'EK': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, TR.EKT@tele2.ru',
                     'HM': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, BSS.HAN@tele2.ru',
                     'KG': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, TR.TUM@tele2.ru',
                     'KO': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, bss.kom@tele2.ru',
                     'OB': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, BSS.ORB@tele2.ru',
                     'PM': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, Transport.PRM@tele2.ru',
                     'TU': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, TR.TUM@tele2.ru',
                     'UF': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, Transport.CHE@tele2.ru',
                     'YN': 'all_License_Ural@tele2.ru, Transport.CP_Access@tele2.ru, BSS.YNR@tele2.ru',
                     'EL': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru',
                     'KC': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru',
                     'KR': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru, bss.kra@tele2.ru',
                     'KD': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru, bss.kra@tele2.ru',
                     'RO': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru, TN.ROS@tele2.ru',
                     'VD': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru, tn.vlg@tele2.ru',
                     'AD': 'ALL_LICENSE_SOUTH@tele2.ru, Transport.CP_Access@tele2.ru, bss.kra@tele2.ru',
                     'AR': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.arh@tele2.ru',
                     'KN': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.kln@tele2.ru',
                     'MU': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.mur@tele2.ru',
                     'NE': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.NEA@tele2.ru',
                     'PS': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.PSK@tele2.ru',
                     'PZ': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.PZV@tele2.ru',
                     'SP': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, Transport.SPB@tele2.ru',
                     'SC': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, Transport.SPB@tele2.ru',
                     'VG': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, BSS.VOL@tele2.ru',
                     'VN': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, bss.nov@tele2.ru',
                     'LE': 'MR_NW_LLA@tele2.ru, Transport.CP_Access@tele2.ru, Transport.SPB@tele2.ru',
                     'MS': 'Transport.CP_Access@tele2.ru',
                     'MO': 'Transport.CP_Access@tele2.ru',
                     'BI': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, BSS.BIR@tele2.ru',
                     'BU': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, bss.brt@tele2.ru',
                     'IR': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, transport@tele2.ru',
                     'KM': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, BSS.KAM@tele2.ru',
                     'MD': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, BSS.MGD@tele2.ru',
                     'HB': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, BSS.KHB@tele2.ru',
                     'SA': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, bss.sah@tele2.ru',
                     'VV': 'RICH_Irkutsk@tele2.ru, Transport.CP_Access@tele2.ru, bss.vld@tele2.ru',
                     'KL': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, bss.klg@tele2.ru',
                     'KS': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, BSS.KOS@tele2.ru',
                     'RZ': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, bss.ryz@tele2.ru',
                     'SM': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, bss.smo@tele2.ru',
                     'TL': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, bss.tul@tele2.ru',
                     'TV': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, bss.tve@tele2.ru',
                     'VL': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, bss.vla@tele2.ru',
                     'IV': 'LRD.CNT@tele2.ru, Transport.CP_Access@tele2.ru, BSS.IVN@tele2.ru',
                     'BE': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.bel@tele2.ru',
                     'BR': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.bry@tele2.ru',
                     'KU': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.kur@tele2.ru',
                     'LI': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.lip@tele2.ru',
                     'MV': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.mrd@tele2.ru',
                     'OR': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.orl@tele2.ru',
                     'PN': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, BSS.PNZ@tele2.ru',
                     'SV': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, BSS.SRV@tele2.ru',
                     'TM': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.tam@tele2.ru',
                     'VO': 'CBS_License@tele2.ru, Transport.CP_Access@tele2.ru, bss.vrn@tele2.ru',
                     }
        mail_list = []
        for region in regions_list:
            try:
                mail_list.append(mail_dict[region])
            except KeyError:
                mail_list.append('Transport.CP_Access@tele2.ru')

        mail_str = str(mail_list).replace(",", ";").replace("'", "")

        print(mail_str)

        mail.To = mail_str
        # mail.To = "denis.kozhin@tele2.ru"
        # mail.To = "Transport.CP_Access@tele2.ru"
        # mail.CC = "Nikolay.Pogodin@tele2.ru"
        mail.Subject = 'В регионе {region} Изменение элемента в СМ {text_sa} {vendor}'.format(
            text_sa=self.text_sa,
            vendor=self.vendor,
            region=region
        )
        self.html_body(mail)
        mail.Send()

    def html_body(self, mail):
        mail.HTMLBody = BodyMail(vendor=self.vendor).body_mail()
