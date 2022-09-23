#2022/09/23 Speechrecognizer 라이브러리를 이용하여 음성을 Text로 변환
import speech_recognition as sr
import pygame
pygame.mixer.init()
#import sys #-- 텍스트 저장시 사용

def findStartText(strAudio):
    if "스티브" in strAudio:
        return True
    return False

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        speech = r.listen(source)

    #sys.stdout = open('audio_output.txt', 'w') #-- 텍스트 저장시 사용

    try:
        audio = r.recognize_google(speech, language="ko-KR")
        if findStartText(audio) :
            try :
                pygame.mixer.music.load('start.mp3')
                pygame.mixer.music.play()
            except :
                print("error")
        else :
            print("Your speech thinks like\n " + audio)
            continue
            #다시 대기...
        print("Your speech thinks like\n " + audio)

    except sr.UnknownValueError:
        print("Your speech can not understand")
    except sr.RequestError as e:
        print("Request Error!; {0}".format(e))

