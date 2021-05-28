from Template.get_data_file import TempTable
import re


class BodyMail:
    def __init__(self, vendor):
        self.vendor = vendor

    def body_mail(self):

        html_table = TempTable(vendor=self.vendor).conversion_to_html()
        region = f",<br> регион {TempTable(vendor=self.vendor).get_region()}"

        body_mail = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <!--[if gte mso 9]><xml>
           <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
           </o:OfficeDocumentSettings>
          </xml><![endif]-->
          <!-- fix outlook zooming on 120 DPI windows devices -->
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1"> <!-- So that mobile will display zoomed in -->
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- enable media queries for windows phone 8 -->
          <meta name="format-detection" content="date=no"> <!-- disable auto date linking in iOS 7-9 -->
          <meta name="format-detection" content="telephone=no"> <!-- disable auto telephone linking in iOS 7-9 -->
          <title>Single Column</title>
          
          <style type="text/css">
        body {
          margin: 0;
          padding: 0;
          -ms-text-size-adjust: 100%;
          -webkit-text-size-adjust: 100%;
        }
        
        table {
          border-spacing: 0;
        }
        
        table td {
          border-collapse: collapse;
        }
        
        .ExternalClass {
          width: 100%;
        }
        
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
          line-height: 100%;
        }
        
        .ReadMsgBody {
          width: 100%;
          background-color: #ebebeb;
        }
        
        table {
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
        }
        
        img {
          -ms-interpolation-mode: bicubic;
        }
        
        .yshortcuts a {
          border-bottom: none !important;
        }
        
        @media screen and (max-width: 599px) {
          .force-row,
          .container {
            width: 100% !important;
            max-width: 100% !important;
          }
        }
        @media screen and (max-width: 400px) {
          .container-padding {
            padding-left: 12px !important;
            padding-right: 12px !important;
          }
        }
        .ios-footer a {
          color: #aaaaaa !important;
          text-decoration: underline;
        }
        a[href^="x-apple-data-detectors:"],
        a[x-apple-data-detectors] {
          color: inherit !important;
          text-decoration: none !important;
          font-size: inherit !important;
          font-family: inherit !important;
          font-weight: inherit !important;
          line-height: inherit !important;
        }
        </style>
        <style id="Шаблоны для заявки в BPM_19842_Styles">
        <!--table
            {mso-displayed-decimal-separator:"\,";
            mso-displayed-thousand-separator:" ";}
        .xl1519842
            {padding:0px;
            mso-ignore:padding;
            color:black;
            font-size:11.0pt;
            font-weight:400;
            font-style:normal;
            text-decoration:none;
            font-family:Calibri, sans-serif;
            mso-font-charset:0;
            mso-number-format:General;
            text-align:general;
            vertical-align:bottom;
            mso-background-source:auto;
            mso-pattern:auto;
            white-space:nowrap;}
        .xl6319842
            {padding:0px;
            mso-ignore:padding;
            color:black;
            font-size:11.0pt;
            font-weight:400;
            font-style:normal;
            text-decoration:none;
            font-family:Calibri, sans-serif;
            mso-font-charset:0;
            mso-number-format:General;
            text-align:general;
            vertical-align:bottom;
            border:.5pt solid windowtext;
            mso-background-source:auto;
            mso-pattern:auto;
            white-space:nowrap;}
        .xl6419842
            {padding:0px;
            mso-ignore:padding;
            color:black;
            font-size:11.0pt;
            font-weight:700;
            font-style:normal;
            text-decoration:none;
            font-family:Calibri, sans-serif;
            mso-font-charset:204;
            mso-number-format:General;
            text-align:center;
            vertical-align:middle;
            border-top:.5pt solid windowtext;
            border-right:.5pt solid windowtext;
            border-bottom:none;
            border-left:.5pt solid windowtext;
            background:#D9D9D9;
            mso-pattern:black none;
            white-space:normal;}
        -->
        </style>
        
        </head>
        
        <body style="margin:0; padding:0;" bgcolor="#F0F0F0" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
        
        <!-- 100% background wrapper (grey background) -->
        <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" bgcolor="#F0F0F0">
          <tr>
            <td align="center" valign="top" bgcolor="#F0F0F0" style="background-color: #F0F0F0;">
        
              <br>
        
              <!-- 600px container (white background) -->
              <table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px">
                <tr>
                  <td class="container-padding header" align="left" style="font-family:Helvetica, Arial, sans-serif;font-size:24px;font-weight:bold;padding-bottom:15px;color:#DF4726;padding-left:24px;padding-right:24px">
                    Инициирована заявка на изменение элементов в СМ<% region %>
                  </td>
                </tr>
                <tr>
                  <td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:12px;padding-bottom:12px;background-color:#ffffff">
                    <br>
        
        <div class="title" style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;color:#374550">Прошу произвести корректировку данных в системах мониторинга.</div>
        <br>
        
        <div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">
        
          Полную версию шаблона вы можете найти в заявке BPM
          
        <div id="Шаблоны для заявки в BPM_19842" align=center x:publishsource="Excel">
        
        <br><br>
        <% html_table %>
        
        </div>
          <br><br>
        </div>
        
                  </td>
                </tr>
                <tr>
                  <td class="container-padding footer-text" align="left" style="font-family:Helvetica, Arial, sans-serif;font-size:12px;line-height:16px;color:#aaaaaa;padding-left:24px;padding-right:24px">
                    <br><br>
                    Transport.CP_Access_Exploitation
                    <br><br>
        
                  </td>
                </tr>
              </table>
        <!--/600px container -->
        
        
            </td>
          </tr>
        </table>
        <!--/100% background wrapper-->
        
        </body>
        </html> 
        '''
        body_mail = re.sub(r'<% html_table %>', html_table, body_mail)
        body_mail = re.sub(r'<% region %>', region, body_mail)

        return body_mail
