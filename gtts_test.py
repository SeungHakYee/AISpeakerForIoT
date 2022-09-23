from gtts import gTTS
from playsound import playsound


s = gTTS(
    text='네 안녕하세요. 저는 스티브 입니다.',
    lang='ko', slow=False
)

s.save('start.mp3')
playsound('start.mp3')