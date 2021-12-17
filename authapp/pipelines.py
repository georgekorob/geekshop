from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from authapp.models import UserProfile
from geekshop.settings import MEDIA_ROOT
import requests


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('http', 'api.vk.com', 'method/users.get', None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_400_orig', 'lang')),   #
                                                access_token=response['access_token'], v=5.131)), None))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex'] == 1:
        user.userprofile.gender = UserProfile.FEMALE
    elif data['sex'] == 2:
        user.userprofile.gender = UserProfile.MALE
    else:
        pass
    if data['about']:
        user.userprofile.about = data['about']

    lang_dict = {0: ('ru', 'русский'),
                 1: ('uk', 'украинский'),
                 2: ('be', 'белорусский'),
                 3: ('en', 'английский'),
                 4: ('es', 'испанский'),
                 5: ('fi', 'финский'),
                 6: ('de', 'немецкий'),
                 7: ('it', 'итальянский')}
    print(lang_dict.get(int(data['language'])))

    uid_vk = data.get('id')
    username_vk = kwargs.get('details').get('username')
    p = requests.get(data['photo_400_orig'])
    file_name = f'users_image/{uid_vk}_{username_vk}.jpg'
    out = open(MEDIA_ROOT / file_name, "wb")
    out.write(p.content)
    out.close()
    user.image = file_name

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
    age = timezone.now().date().year - bdate.year
    user.age = age
    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.save()
