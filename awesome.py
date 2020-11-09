import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        try:
            voice = r.recognize_google(audio , language = 'tr-TR')
        except sr.UnknownValueError:
            speak("dediğinizi anlamadım efendim")
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak("iyiyim efendim. umarımki sizde iyisinizdir")
    if 'ne haber' in voice:
        speak("iyiyim efendim. umarımki sizde iyisinizdir")
    if 'naber' in voice:
        speak("iyidir efnedim. umarımki sizde iyisinizdir")
    if 'teşekkür ederim' in voice:
        speak("bişey deil efendim")
    if 'teşekkürler' in voice:
        speak("bişey deil efendim")
    if 'Sağ ol' in voice:
        speak("bişey deil efendim")
    if 'saat kaç' in voice:
        speak(datetime.now().strftime("efendim saat"+'%H:%M:'))
    if 'saati söyle' in voice:
        speak(datetime.now().strftime("efendim saat"+'%H:%M:'))
    if 'zamanı söyle' in voice:
        speak(datetime.now().strftime("efendim bulunduğunuz zaman"+'%H:%M:'))
    if 'Google' in voice:
        search = record("google dan ne aratmamı istersiniz efendim?")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + 'için bunları buldum efendim')
    if 'YouTube' in voice:
        search = record("ne açmamı istersiniz efendim")
        url = 'https://www.youtube.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + 'için bunları buldum efendim')
    if 'trendler' in voice:
        url = 'https://www.youtube.com/feed/trending'
        webbrowser.get().open(url)
        speak("türkiye deki trendler karşınızda")
    if 'Trendler' in voice:
        url = 'https://www.youtube.com/feed/trending'
        webbrowser.get().open(url)
        speak("türkiye deki trendler karşınızda")


    if 'Komik bir şey aç' in voice:
        url = 'https://www.youtube.com/watch?v=9JuDGFaKR-E'
        webbrowser.get().open(url)
        speak('sizi güldürmesini umuyorum efendim')
    if 'canım sıkılıyor' in voice:
        url = 'https://www.youtube.com/watch?v=jOP1n61NIdU'
        webbrowser.get().open(url)
        speak('sizi güldürmesini umuyorum efendim')

    if 'netflix' in voice:
        url = 'https://www.netflix.com/browse'
        webbrowser.get().open(url)
        speak("netflix açılıyor efendim iyi eğlenceler. prison bireyki tavsiye ederim efendim")

    if 'Netflix' in voice:
        url = 'https://www.netflix.com/browse'
        webbrowser.get().open(url)
        speak("netflix açılıyor efendim iyi eğlenceler. prison bireyki tavsiye ederim efendim")

    if 'netfilik' in voice:
        url = 'https://www.netflix.com/browse'
        webbrowser.get().open(url)
        speak("netflix açılıyor efendim iyi eğlenceler. prison bireyki tavsiye ederim efendim")

    if 'en sevdiğim filmi aç' in voice:
        url = 'https://www.fullhdfilmizlesene.com/film/demir-adam-1-filmi-izle/'
        webbrowser.get().open(url)
        time.sleep(1.5)
        speak("efendim en sevdiğiniz film ayrın man. keyifli izlemeler dilerim")

    if 'en sevdiğin filmi aç' in voice:
        url = 'https://www.fullhdfilmizlesene.com/film/demir-adam-1-filmi-izle/'
        webbrowser.get().open(url)
        time.sleep(1.5)
        speak("efendim en sevdiğiniz film ayrın man. keyifli izlemeler dilerim")


    if 'en sevdiğim diziyi aç' in voice:
        url = 'https://www.netflix.com/title/70143824'
        webbrowser.get().open(url)
        speak("efendim en sevdiğiniz dizi hav ay met yor madır.keyifli izlemeler dilerim")


    if 'video aç' in voice:
        search = record("ne açmamı istersiniz efendim")
        url = 'https://www.youtube.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + 'için bunları buldum efendim')



    if "Oyun 1'i aç" in voice:
        speak("oyun açılıyor efendim iyi eğlenceler")
        os.startfile(r"D:\Among Us\Among Us.exe")
    if "Oyun 2'yi aç" in voice:
        speak("oyun açılıyor iyi eğlenceler efendim")
        os.startfile(r"D:\Riot Games\Riot Games\League of Legends\LeagueClient.exe")
        time.sleep(3)


    if 'beni seviyomusun' in voice:
        speak("sizi çok seviyorum efendim")


    if 'Facebook' in voice:
        url = 'https://www.facebook.com/login/'
        webbrowser.get().open(url)
        speak("işte facebook. efendim.. kullanıcı adı ve şifrenizi yazarak hesabınıza girebilirsiniz")
    if 'Instagram' in voice:
        url = 'https://www.instagram.com/accounts/login/?next=/login/'
        webbrowser.get().open(url)
        speak("işte instagram. efendim.. kullanıcı adı ve şifrenizi yazarak hesabınıza girebilirsiniz")
    if 'Twitter' in voice:
        url = 'https://twitter.com/login'
        webbrowser.get().open(url)
        speak("işte twitter. efendim.. kullanıcı adı ve şifrenizi yazarak hesabınıza girebilirsiniz")
    if 'tivitır' in voice:
        url = 'https://twitter.com/login'
        webbrowser.get().open(url)
        speak("işte twitter. efendim.. kullanıcı adı ve şifrenizi yazarak hesabınıza girebilirsiniz")
    if "Twitir'ı aç" in voice:
        url = 'https://twitter.com/login'
        webbrowser.get().open(url)
        speak("işte twitter. efendim.. kullanıcı adı ve şifrenizi yazarak hesabınıza girebilirsiniz")


    if 'yemeksepeti' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")
    if 'Yemeksepeti' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")
    if 'yemek sepeti' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")
    if 'Yemek sepeti' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")
    if 'Karnım aç' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")
    if 'acıktım' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")
    if 'sipariş' in voice:
        url = 'https://www.yemeksepeti.com/ankara'
        webbrowser.get().open(url)
        speak("efendim haram olmamak şartıyla burdan sipariş verebilirsiniz")


    if 'müzik bir' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Mark Eliyahu - Journey (official video).mp3")
    if 'müzik 1' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Mark Eliyahu - Journey (official video).mp3")

    if 'müzik 2' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Simge - Yankı.mp3")
    if 'müzik iki' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Simge - Yankı.mp3")

    if 'müzik 3' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Seksendört - Kendime Yalan Söyledim.mp3")
    if 'müzik üç' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Seksendört - Kendime Yalan Söyledim.mp3")

    if 'müzik 4' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Bir Sana Bir de Bana -BaBa ZuLa.mp3")
    if 'müzik dört' in voice:
        os.startfile(r"C:\Users\ASUS\Downloads\Bir Sana Bir de Bana -BaBa ZuLa.mp3")



    if 'hava durumu' in voice:
        url = 'https://www.google.com/search?q=hava+durumu'
        webbrowser.get().open(url)
        speak("hava durumu gördüğünüz gibi efendim")
    if 'hava nasıl' in voice:
        url = 'https://www.google.com/search?q=hava+durumu'
        webbrowser.get().open(url)
        speak("hava durumu gördüğünüz gibi efendim")


    if 'Twitch' in voice:
        url = 'https://www.twitch.tv/'
        webbrowser.get().open(url)
        speak("iyi eğlenceler efendim. bu arada elraenn'i izlemenizi öneririm")
    if 'tiviç' in voice:
        url = 'https://www.twitch.tv/'
        webbrowser.get().open(url)
        speak("iyi eğlenceler efendim. bu arada elraenn'i izlemenizi öneririm")
    if "twitch'i aç" in voice:
        url = 'https://www.twitch.tv/'
        webbrowser.get().open(url)
        speak("iyi eğlenceler efendim. bu arada elraenn'i izlemenizi öneririm")

    if "github" in voice:
        url = 'https://github.com/'
        webbrowser.get().open(url)
        speak("github açılıyor")
    if "kitap" in voice:
        url = 'https://github.com/'
        webbrowser.get().open(url)
        speak("github açılıyor")
    if "kitab" in voice:
        url = 'https://github.com/'
        webbrowser.get().open(url)
        speak("github açılıyor")

    if 'WhatsApp' in voice:
        url = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)
        speak("vatsap açılıyor")



    if 'haritalar' in voice:
        url = 'https://www.google.com.tr/maps/@39.8794962,32.8422953,14z'
        webbrowser.get().open(url)
        speak("haritalar açılıyor")

    if 'Haritalar' in voice:
        url = 'https://www.google.com.tr/maps/@39.8794962,32.8422953,14z'
        webbrowser.get().open(url)
        speak("haritalar açılıyor")

    if 'Wikipedia' in voice:
        search = record("vikipedyadan ne aratmak istersiniz")
        url = 'https://tr.wikipedia.org/wiki/' + search
        webbrowser.get().open(url)
        speak("vikipedya açılıyor efendim")

    if 'vikipedi' in voice:
        search = record("vikipedyadan ne aratmak istersiniz")
        url = 'https://tr.wikipedia.org/wiki/' + search
        webbrowser.get().open(url)
        speak(search + 'için bunu buldum')


    if 'Gmail' in voice:
        url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
        webbrowser.get().open(url)
        speak("cimeiliniz açılıyor")



    if 'Ankara' in voice:
        os.startfile(r"C:\Users\ASUS\Desktop\Projeler\ankaradurum.py")


    if 'kapat' in voice:
        speak("kendimi kapatıyorum efendim size iyi günler")
        exit()
    if 'dinlen' in voice:
        speak("dinlenme moduna geçiyorum efendim size iyi günler")
        exit()
    if 'uyku' in voice:
        speak("uyku moduna geçiyorum efendim size iyi günler")

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("Merhabaa efendim ben jarvis.Size nasıl yardımcı olabilirim")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)

