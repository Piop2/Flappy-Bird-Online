import os
import zipfile
import shutil
from _thread import start_new_thread

import pygame
import requests
from bs4 import BeautifulSoup
import urllib.request

from src.util.animation import Animation
from src.util.font import BitMapFont
from src.version import VERSION

GITHUB_RELEASE_TAG_URL = "https://github.com/Piop2/Flappy-Bird-Online/tags"
GITHUB_RELEASE_DOWNLOAD_URL = "https://github.com/Piop2/Flappy-Bird-Online/releases/download/{}/Flappy-Bird-Online.zip"

PATH = "download/release.zip"


class Downloader:
    def __init__(self):
        self.status = ""
        self.error = False
        self.done = False
        return

    def run(self):
        try:
            res = requests.get(GITHUB_RELEASE_TAG_URL)
        except requests.exceptions.ConnectionError:
            self.status = f"ERROR - NO CONNECTION"
            self.error = True
            return
        except Exception as e:
            self.status = f"ERROR - {str(e).upper()}"
            self.error = True
            return

        self.status = "CHECK LATEST VERSION..."

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        latest_tag = soup.select_one(
            "#repo-content-pjax-container > div > div:nth-child(2) > div > div.Box > div.Box-body.p-0 > div > div > "
            "div > div.d-flex > div.d-flex.inline.pr-2.pb-1.col-12 > h2 > a"
        )

        latest_version = latest_tag.text

        if latest_version == "v0.0.0":
            self.status = "RUNNING...000"
            self.error = True
            return

        if VERSION == latest_version:
            self.status = "RUNNING..."
            self.done = True
            return

        self.status = "READY TO DOWNLOAD..."

        download_url = GITHUB_RELEASE_DOWNLOAD_URL.format(latest_version)
        res = requests.get(download_url)

        with open(PATH, "wb") as f:
            total = urllib.request.urlopen(download_url).length
            downloaded = 0
            for chunk in res.iter_content(chunk_size=1024):
                downloaded += len(chunk)
                f.write(chunk)
                try:
                    self.status = f"DOWNLOAD... ({int(downloaded / total * 100)}%)"
                except TypeError:
                    self.status = f"DOWNLOAD... (0%)"

        self.status = "READY TO EXTRACT..."

        for file_path in os.listdir("/"):
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))

        self.status = "EXTRACTING..."
        zipfile.ZipFile(PATH).extractall("")

        os.remove(PATH)

        self.status = "RUNNING..."
        self.done = True
        return


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400), pygame.NOFRAME)
        pygame.display.set_icon(pygame.image.load("asset/icon/flappy29.png"))
        self.clock = pygame.time.Clock()

        self.bird = Animation.load("asset/animation/update_bird.json")
        self.background = pygame.image.load("asset/image/update_background.png")

        self.font = BitMapFont.load("asset/font/flappy_font.json", 3)

        self.downloader = Downloader()

    def run(self):
        start_new_thread(self.downloader.run, ())

        timer = 0

        running = True
        while running:
            dt = self.clock.tick(60)
            self.bird.update(dt)

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.bird.image, (200 - 51, 200 - 36))

            status = self.downloader.status
            if status == "":
                status = "WAITING..."

            text_image = self.font.get_image(status)
            self.screen.blit(text_image, (200 - (text_image.get_width() / 2), 350))

            if self.downloader.done or self.downloader.error:
                timer += dt
                if timer >= 6000:
                    running = False

                    if self.downloader.done:
                        pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

        pygame.quit()
        return


if __name__ == "__main__":
    App().run()
