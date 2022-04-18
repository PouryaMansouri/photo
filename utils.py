from kavenegar import KavenegarAPI, APIException, HTTPException

from site_settings.models import SiteSetting


def send_otp_code(phone, code):
    site_setting = SiteSetting.load()
    try:
        api = KavenegarAPI(site_setting.kavenegar_api_key)
        params = {
            'sender': site_setting.kavenegar_sender,
            'receptor': f'{phone}',
            'message': f'{site_setting.kavenegar_message}\nکد تایید: {code}',
        }
        print(code)
        # response = api.sms_send(params)
        # todo: uncomment up line (sms sender)
        # print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
