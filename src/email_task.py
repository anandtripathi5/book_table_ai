# -*- coding: utf-8 -*-
from mailin import Mailin

from config import SEND_IN_BLUE_API_KEY, EMAIL_FROM_ADDRESS


def send_email(email_address, user_name, data):
        m = Mailin("https://api.sendinblue.com/v2.0", SEND_IN_BLUE_API_KEY)
        data = {"to": {email_address: user_name},
                "from": [EMAIL_FROM_ADDRESS, "HutPizza"],
                "subject": "Table Booking Summary of HutPizza",
                "html": """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="apple-mobile-web-app-capable" content="yes" /><meta name="apple-mobile-web-app-status-bar-style" content="black" /><meta name="format-detection" content="telephone=no" /><title>hello</title><style type="text/css">
    <tbody><tr style="display:none !important; font-size:1px; mso-hide: all;"><td></td><td></td></tr>
    <tr>
        <td align="center" valign="top">
        <!--[if gte mso 9]>
                        <table align="center" border="0" cellspacing="0" cellpadding="0" width="590" style="width:590px;">
                        <tr>
                        <td align="center" valign="top" width="590" style="width:590px;">
                        <![endif]-->
            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer" style="max-width:590px!important; width: 590px;">
        <tbody><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" style="min-width:590px; background-color:#ffffff;" name="Layout_4051" id="Layout_4051">
                <tbody><tr>
                    <td class="rnb-del-min-width" valign="top" align="center" bgcolor="#ffffff" style="min-width:590px; background-color:#ffffff;">
                        <table width="100%" cellpadding="0" border="0" height="30" cellspacing="0" bgcolor="#ffffff" style="background-color:#ffffff;">
                            <tbody><tr>
                                <td valign="top" height="30">
                                    <img width="20" height="30" style="display:block; max-height:30px; max-width:20px;" alt="" src="http://img.mailinblue.com/new_images/rnb/rnb_space.gif">
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
            </td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <div>

                <!--[if mso]>
                <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
            
            <table width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="background-color:#ffffff;" name="Layout_14" id="Layout_14"><tbody><tr>
                    <td align="center" valign="top" bgcolor="#ffffff" style="background-color: #ffffff;"><table border="0" width="100%" cellpadding="0" cellspacing="0" class="rnb-container" bgcolor="#ffffff" style="height: 0px; background-color: rgb(255, 255, 255); border-radius: 0px; border-collapse: separate; padding-left: 20px; padding-right: 20px;"><tbody><tr>
                                <td class="rnb-container-padding" bgcolor="#ffffff" style="background-color: #ffffff; font-size: px;font-family: ; color: ;">

                                    <table border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container" align="center" style="margin:auto;">
                                        <tbody><tr>

                                            <td class="rnb-force-col" align="center">

                                                <table border="0" cellspacing="0" cellpadding="0" align="center" class="rnb-col-1">

                                                    <tbody><tr>
                                                        <td height="10"></td>
                                                    </tr>

                                                    <tr>
                                                        <td style="font-family:Arial,Helvetica,sans-serif; color:#3c4858; text-align:center;">

                                                            <span style="color:#3c4858;"><span style="font-size:31px;"><span style="color:#8B4513;"><strong>Hut Pizza</strong></span></span></span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td height="10"></td>
                                                    </tr>
                                                    </tbody></table>
                                                </td></tr>
                                    </tbody></table></td>
                            </tr>

                        </tbody></table>

                    </td>
                </tr>

            </tbody></table><!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->
        </div></td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <div>
                <!--[if mso]>
                <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="min-width:100%; -webkit-backface-visibility: hidden; line-height: 10px; background-color:#ffffff;" name="Layout_5" id="Layout_5">
                <tbody><tr>
                    <td class="rnb-del-min-width" valign="top" align="center" style="min-width: 590px;">
                        <table width="100%" class="rnb-container" cellpadding="0" border="0" bgcolor="#ffffff" align="center" cellspacing="0" style="background-color:#ffffff;">
                            <tbody><tr>
                                <td valign="top" align="center">
                                    <table cellspacing="0" cellpadding="0" border="0">
                                        <tbody><tr>
                                            <td>
                                                <div style="display:block; border-radius:0px; width:590;;max-width:590px !important;border-top:0px None #000;border-right:0px None #000;border-bottom:0px None #000;border-left:0px None #000;border-collapse: separate;border-radius: 0px;">
                                                    <div><img border="0" hspace="0" vspace="0" width="590" class="rnb-header-img" alt="" style="display:block; float:left; border-radius: 0px; " src="http://img.mailinblue.com/1172781/images/rnb/original/58191abc150ba0cc4c8b4577.jpg">
                                                        </div><div style="clear:both;"></div>
                                                    </div></td>
                                        </tr>
                                    </tbody></table>

                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr></tbody></table>
            <!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->
        </div></td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <div>
                <!--[if mso]>
                <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="min-width:100%; background-color:#ffffff;" name="Layout_11">
                <tbody><tr>
                    <td class="rnb-del-min-width" align="center" valign="top" bgcolor="#ffffff" style="background-color: #ffffff;">
                        <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-container" bgcolor="#fff4e9" style="background-color: rgb(255, 244, 233); padding-left: 20px; padding-right: 20px; border-collapse: separate; border-radius: 0px; border-bottom: 0px none rgb(200, 200, 200);">

                                        <tbody><tr>
                                            <td height="30" style="font-size:1px; line-height:1px;"> </td>
                                        </tr>
                                        <tr>
                                            <td valign="top" class="rnb-container-padding" bgcolor="#fff4e9" style="background-color: #fff4e9;" align="left">

                                                <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container">
                                                    <tbody><tr>
                                                        <td class="rnb-force-col" valign="top" style="padding-right: 0px;">

                                                            <table border="0" valign="top" cellspacing="0" cellpadding="0" width="100%" align="left" class="rnb-col-1">

                                                                <tbody><tr>
                                                                    <td style="font-size:14px; font-family:'Arial',Helvetica,sans-serif, sans-serif; color:#555; line-height: 21px;"><div style="text-align: center;"><font color="#ffffff"><span style="font-size: 40px; background-color: rgb(230, 111, 50);"><b>Summary of Booking</b></span></font></div>
</td>
                                                                </tr>
                                                                </tbody></table>

                                                            </td></tr>
                                                </tbody></table></td>
                                        </tr>
                                        <tr>
                                            <td height="30" style="font-size:1px; line-height:1px;border-bottom:0px;"> </td>
                                        </tr>
                                    </tbody></table>
                    </td>
                </tr>
            </tbody></table><!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->

            </div></td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <div>
                <!--[if mso]>
                <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="min-width:100%; background-color:#ffffff;" name="Layout_13">
                <tbody><tr>
                    <td class="rnb-del-min-width" align="center" valign="top" bgcolor="#ffffff" style="background-color: #ffffff;">
                        <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-container" bgcolor="#fff4e9" style="background-color: rgb(255, 244, 233); padding-left: 20px; padding-right: 20px; border-collapse: separate; border-radius: 0px; border-bottom: 0px none rgb(200, 200, 200);">

                                        <tbody><tr>
                                            <td height="0" style="font-size:1px; line-height:1px;"> </td>
                                        </tr>
                                        <tr>
                                            <td valign="top" class="rnb-container-padding" bgcolor="#fff4e9" style="background-color: #fff4e9;" align="left">

                                                <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container">
                                                    <tbody><tr>
                                                        <td class="rnb-force-col" valign="top" style="padding-right: 0px;">

                                                            <table border="0" valign="top" cellspacing="0" cellpadding="0" width="100%" align="left" class="rnb-col-1">

                                                                <tbody><tr>
                                                                    <td style="font-size:14px; font-family:'Georgia',serif, sans-serif; color:#555; line-height: 21px;"><div style="text-align: center;"><span style="font-size:16px;"><span style="color:#e66f32;">{}</span></span></div>
</td>
                                                                </tr>
                                                                </tbody></table>

                                                            </td></tr>
                                                </tbody></table></td>
                                        </tr>
                                        <tr>
                                            <td height="20" style="font-size:1px; line-height:1px;border-bottom:0px;"> </td>
                                        </tr>
                                    </tbody></table>
                    </td>
                </tr>
            </tbody></table><!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->

            </div></td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <div>
                <!--[if mso]>
                <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="min-width:100%; background-color:#ffffff;" name="Layout_7">
                <tbody><tr>
                    <td class="rnb-del-min-width" align="center" valign="top" bgcolor="#ffffff" style="background-color: #ffffff;">
                        <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-container" bgcolor="#fff4e9" style="background-color: rgb(255, 244, 233); padding-left: 20px; padding-right: 20px; border-collapse: separate; border-radius: 0px; border-bottom: 0px none rgb(200, 200, 200);">

                                        <tbody><tr>
                                            <td height="10" style="font-size:1px; line-height:1px;"> </td>
                                        </tr>
                                        <tr>
                                            <td valign="top" class="rnb-container-padding" bgcolor="#fff4e9" style="background-color: #fff4e9;" align="left">

                                                <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container">
                                                    <tbody><tr>
                                                        <td class="rnb-force-col" valign="top" style="padding-right: 0px;">

                                                            <table border="0" valign="top" cellspacing="0" cellpadding="0" width="100%" align="left" class="rnb-col-1">

                                                                <tbody><tr>
                                                                    <td style="font-size:14px; font-family:'Georgia',serif, sans-serif; color:#555; line-height: 21px;"><div style="line-height: 200%; text-align: center;"><em style="color: rgb(153, 153, 153); font-size: 13px;">"Like" us on Facebook to receive an additional discount code for your order</em><br>
<span style="color:#e66f32;"><span style="font-size:18px;"><span style="display: none;"> </span></span></span></div>
</td>
                                                                </tr>
                                                                </tbody></table>

                                                            </td></tr>
                                                </tbody></table></td>
                                        </tr>
                                        <tr>
                                            <td height="40" style="font-size:1px; line-height:1px;border-bottom:0px;"> </td>
                                        </tr>
                                    </tbody></table>
                    </td>
                </tr>
            </tbody></table><!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->

            </div></td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <table class="rnb-del-min-width rnb-tmpl-width" width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="min-width:590px; background-color:#ffffff;" name="Layout_9" id="Layout_9">
                <tbody><tr>
                    <td class="rnb-del-min-width" align="center" valign="top" bgcolor="#ffffff" style="min-width:590px; background-color: #ffffff;">
                        <table width="590" class="rnb-container" cellpadding="0" border="0" align="center" cellspacing="0">
                            <tbody><tr>
                                <td height="20" style="font-size:1px; line-height:1px;"> </td>
                            </tr>
                            <tr>
                                <td valign="top" class="rnb-container-padding" style="font-size: 14px; font-family: 'Arial',Helvetica,sans-serif; color: #919191;" align="left">

                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container">
                                        <tbody><tr>
                                            <td class="rnb-force-col" style="padding-right:20px; padding-left:20px; mso-padding-alt: 0 0 0 20px;" valign="top">

                                                <table border="0" valign="top" cellspacing="0" cellpadding="0" width="264" align="left" class="rnb-col-2" style="border-bottom:0;">

                                                    <tbody><tr>
                                                        <td valign="top">
                                                            <table cellpadding="0" border="0" align="left" cellspacing="0" class="rnb-btn-col-content">
                                                                <tbody><tr>
                                                                    <td valign="middle" align="left" style="font-size:14px; font-family:'Arial',Helvetica,sans-serif; color:#919191;" class="rnb-text-center">
                                                                        <div><div>HutPizza<br>
123 Main Street<br>
Your Town, WA 54321<br>
Phone: 555.555.5555</div>
</div>
                                                                    </td></tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                    </tbody></table>
                                                </td><td ng-if="item.text.align=='left'" class="rnb-force-col rnb-social-width" valign="top" style="mso-padding-alt: 0 20px 0 0; padding-right: 15px;">

                                                <table border="0" valign="top" cellspacing="0" cellpadding="0" width="246" align="right" class="rnb-last-col-2">

                                                    <tbody><tr>
                                                        <td valign="top">
                                                            <table cellpadding="0" border="0" cellspacing="0" class="rnb-social-align" style="float: right;" align="right">
                                                                <tbody><tr>
                                                                    <td valign="middle" class="rnb-text-center" ng-init="width=setSocialIconsBlockWidth(item)" width="205" align="right">
                                                                        <div class="rnb-social-center">
                                                                        <table align="left" style="float:left; display: inline-block; mso-table-lspace:0pt; mso-table-rspace:0pt;" border="0" cellpadding="0" cellspacing="0">
                                                                        <tbody><tr>
                                                                                <td style="padding:0px 5px 5px 0px; mso-padding-alt: 0px 2px 5px 0px;" align="left">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <img alt="Facebook" border="0" hspace="0" vspace="0" style="vertical-align:top;" target="_blank" src="http://img.mailinblue.com/new_images/rnb/theme2/rnb_ico_fb.png"></span>
                                                                        </td></tr></tbody></table>
                                                                        </div><div class="rnb-social-center">
                                                                        <table align="left" style="float:left; display: inline-block; mso-table-lspace:0pt; mso-table-rspace:0pt;" border="0" cellpadding="0" cellspacing="0">
                                                                        <tbody><tr>
                                                                                <td style="padding:0px 5px 5px 0px; mso-padding-alt: 0px 2px 5px 0px;" align="left">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <img alt="Twitter" border="0" hspace="0" vspace="0" style="vertical-align:top;" target="_blank" src="http://img.mailinblue.com/new_images/rnb/theme2/rnb_ico_tw.png"></span>
                                                                        </td></tr></tbody></table>
                                                                        </div><div class="rnb-social-center">
                                                                        <table align="left" style="float:left; display: inline-block; mso-table-lspace:0pt; mso-table-rspace:0pt;" border="0" cellpadding="0" cellspacing="0">
                                                                        <tbody><tr>
                                                                                <td style="padding:0px 5px 5px 0px; mso-padding-alt: 0px 2px 5px 0px;" align="left">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <img alt="Google+" border="0" hspace="0" vspace="0" style="vertical-align:top;" target="_blank" src="http://img.mailinblue.com/new_images/rnb/theme2/rnb_ico_gp.png"></span>
                                                                        </td></tr></tbody></table>
                                                                        </div><div class="rnb-social-center">
                                                                        <table align="left" style="float:left; display: inline-block; mso-table-lspace:0pt; mso-table-rspace:0pt;" border="0" cellpadding="0" cellspacing="0">
                                                                        <tbody><tr>
                                                                                <td style="padding:0px 5px 5px 0px; mso-padding-alt: 0px 2px 5px 0px;" align="left">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <img alt="Instagram" border="0" hspace="0" vspace="0" style="vertical-align:top;" target="_blank" src="http://img.mailinblue.com/new_images/rnb/theme2/rnb_ico_ig.png"></span>
                                                                        </td></tr></tbody></table>
                                                                        </div><div class="rnb-social-center">
                                                                        <table align="left" style="float:left; display: inline-block; mso-table-lspace:0pt; mso-table-rspace:0pt;" border="0" cellpadding="0" cellspacing="0">
                                                                        <tbody><tr>
                                                                                <td style="padding:0px 5px 5px 0px; mso-padding-alt: 0px 2px 5px 0px;" align="left">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <img alt="Pinterest" border="0" hspace="0" vspace="0" style="vertical-align:top;" target="_blank" src="http://img.mailinblue.com/new_images/rnb/theme2/rnb_ico_pi.png"></span>
                                                                        </td></tr></tbody></table>
                                                                        </div></td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                    </tbody></table>
                                                </td></tr>
                                    </tbody></table></td>
                            </tr>
                            <tr>
                                <td height="0" style="font-size:1px; line-height:1px;"> </td>
                            </tr>
                        </tbody></table>

                    </td>
                </tr></tbody></table>
            </td>
    </tr><tr>

        <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff;">

            <table class="rnb-del-min-width rnb-tmpl-width" width="100%" cellpadding="0" border="0" cellspacing="0" bgcolor="#ffffff" style="min-width:590px; background-color:#ffffff;" name="Layout_4" id="Layout_4">
                <tbody><tr>
                    <td class="rnb-del-min-width" align="center" valign="top" bgcolor="#ffffff" style="min-width:590px; background-color: #ffffff;">
                        <table width="590" class="rnb-container rnb-yahoo-width" cellpadding="0" border="0" align="center" cellspacing="0" style="padding-right:20px; padding-left:20px;">
                            <tbody><tr>
                                <td height="20" style="font-size:1px; line-height:1px;"> </td>
                            </tr>
                            <tr>
                                <td style="font-size:14px; color:#999999; font-weight:normal; text-align:center; font-family:'Georgia',serif;">
                                    <div><div>© 2017 HutPizza</div>
</div>
                                </td></tr>
                            <tr>
                                <td height="20" style="font-size:1px; line-height:1px;"> </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
            </td>
    </tr></tbody></table>
            <!--[if gte mso 9]>
                        </td>
                        </tr>
                        </table>
                        <![endif]-->
                        </td>
        </tr>
        </tbody></table>

</body></html>""".format(data)
                }
        response = m.send_email(data)
        print response
        return True
