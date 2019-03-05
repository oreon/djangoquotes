from mixer.backend.django import mixer
import pytest
from ..models import *

s = '''
ਨਿਰਮਲ ਸਬਦੁ ਨਿਰਮਲ ਹੈ ਬਾਣੀ ॥

Niramal Sabadh Niramal Hai Baanee ||

The Word of the Shabad is Immaculate and Pure; the Bani of the Word is Pure.

ਮਾਝ (ਮਃ ੩) ਅਸਟ (੨੦) ੧:੧ - ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ : ਅੰਗ ੧੨੧ ਪੰ. ੧ 
Raag Maajh Guru Amar Das


ਨਿਰਮਲ ਜੋਤਿ ਸਭ ਮਾਹਿ ਸਮਾਣੀ ॥

Niramal Joth Sabh Maahi Samaanee ||

The Light which is pervading among all is Immaculate.

ਮਾਝ (ਮਃ ੩) ਅਸਟ (੨੦) ੧:੨ - ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ : ਅੰਗ ੧੨੧ ਪੰ. ੨ 
Raag Maajh Guru Amar Das


ਨਿਰਮਲ ਬਾਣੀ ਹਰਿ ਸਾਲਾਹੀ ਜਪਿ ਹਰਿ ਨਿਰਮਲੁ ਮੈਲੁ ਗਵਾਵਣਿਆ ॥੧॥

Niramal Baanee Har Saalaahee Jap Har Niramal Mail Gavaavaniaa ||1||

So praise the Immaculate Word of the Lord's Bani; chanting the Immaculate Name of the Lord, all filth is washed away. ||1||

ਮਾਝ (ਮਃ ੩) ਅਸਟ (੨੦) ੧:੩ - ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ : ਅੰਗ ੧੨੧ ਪੰ. ੨ 
Raag Maajh Guru Amar Das
'''

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        mixer.blend('blog.Post', body=s)

def Xtest_tags():
    print(findTags(s))


@pytest.mark.django_db
class TestModels:

    def test_page(self):
        assert Post.objects.first().page == 121

    def test_link(self):
        assert Post.objects.first().get_link() == LNK_URL + '121'


    def test_info(self):
        assert Post.objects.first().info == 'Raag Maajh Guru Amar Das'


    #def test_tags(self): print(Post.objects.first().tags)

