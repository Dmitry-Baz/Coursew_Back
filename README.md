<div>
  <script src="https://unpkg.com/@vkid/sdk@<3.0.0/dist-sdk/umd/index.js"></script>
  <script type="text/javascript">
    if ('VKIDSDK' in window) {
      const VKID = window.VKIDSDK;

      VKID.Config.init({
        app: 52546533,
        redirectUrl: 'https://siberia.com',
        responseMode: VKID.ConfigResponseMode.Callback,
        source: VKID.ConfigSource.LOWCODE,
      });

      const oneTap = new VKID.OneTap();

      oneTap.render({
        container: document.currentScript.parentElement,
        showAlternativeLogin: true,
        oauthList: [
          'ok_ru',
          'mail_ru'
        ]
      })
      .on(VKID.WidgetEvents.ERROR, vkidOnError)
      .on(VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload) {
        const code = payload.code;
        const deviceId = payload.device_id;

        VKID.Auth.exchangeCode(code, deviceId)
          .then(vkidOnSuccess)
          .catch(vkidOnError);
      });
    
      function vkidOnSuccess(data) {
        // Обработка полученного результата
      }
    
      function vkidOnError(error) {
        // Обработка ошибки
      }
    }
  </script>
</div>


# x1L1z6woAMHUhZnEQ6Be  Защищённый ключ  API  vk
# 507201d3507201d3507201d34b5353ca3655072507201d33768401b6e69c9ec1acb18e8   Сервисный ключ доступа для выполнения запросов к API

### y0_AgAAAAAF63IeAADLWwAAAAEV4OoiAAAVbWH9w0FHnoRP6Usgoc7vkoyeoA    Полигон

import os.path

import requests
from dotenv import load_dotenv

# APP_ID = '15272050'


dotenv_path = 'config.env'
if os.path.exists(dotenv_path): # Это просто проверка
    load_dotenv(dotenv_path)

vk_token = os.getenv('VK_TOKEN')
ya_token = os.getenv('YA_TOKEN')

class VKBazyk:
    def __init__(self, access_token, version='5.199'):
        self.access_token = access_token
        self.version = version
        self.base_url = 'https://api.vk.com/method/'
        self.params = {
            'access_token': self.access_token,
            'v': self.version
        }

        def user_info(self, user_id):
            url = f'{self.base_url}user.get'
            params = {
                **self.params,
                'user_ids': user_id
            }
            response = requests.get(url, params=params)
            return response.json()
        
    VKBazyk = VKBazyk(vk_token)
    user_info = VKBazyk.user_info(97694748)
    pprint(user_info)

    {'href': 'https://uploader22o.disk.yandex.net:443/upload-target/20241025T220214.026.utd.8dbwiy9p75uzlt0ywru6516g9-k22o.7336115',
 'method': 'PUT',
 'operation_id': '8b0365110dd88b3e0c0aec4aef3fda14621ddd7bde8fe55de317dda8edc8ef92',
 'templated': False}
