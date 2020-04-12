from threading import Thread

import mido
from playsound import playsound
import requests
import time

music = r"SNA.mid"


class Decode(Thread):
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        playsound(music)


class Play(Thread):

    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        time.sleep(0.5)
        mid = mido.MidiFile(music)
        for msg in mid.play():
            note = str(msg).split(" ")[2].split("=")[1]
            volume = str(msg).split(" ")[3].split("=")[1]
            res = int(note) * int(volume) / 100
            print(note)
            if int(res) <= 0:
                res = 0
            if 0 < int(res) <= 10:
                res = 11
            res = int(res)
            res = str(res)
            try:
                req = requests.get("http://109.254.211.5:1234/brig_r/" + res + "/brig_g/" + res + "/brig_b/" + res)
            except:
                None


def create_threads():
    Playy = Play()
    Decodee = Decode()
    Playy.start()
    Decodee.start()


if __name__ == "__main__":
    create_threads()
