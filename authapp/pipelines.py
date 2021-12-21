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
                          urlencode(OrderedDict(fields=','.join(('bdate',
                                                                 'sex',
                                                                 'about',
                                                                 'photo_400_orig',
                                                                 'personal')),
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

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
    age = timezone.now().date().year - bdate.year
    user.age = age
    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['photo_400_orig']:
        uid_vk = data.get('id')
        username_vk = kwargs.get('details').get('username')
        photo_link = data['photo_400_orig']
        photo_response = requests.get(photo_link)
        path_photo = f'users_image/{uid_vk}_{username_vk}.jpg'
        with open(MEDIA_ROOT / path_photo, 'wb') as photo:
            photo.write(photo_response.content)
        user.image = path_photo

    if data['personal']['langs']:
        user.userprofile.langs = data['personal']['langs'][0] if len(data['personal']['langs'][0]) > 0 else 'EN'

    user.save()
