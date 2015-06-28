'''
Created on 27/06/2015

@author: Anderson
'''
import time
from es2_aproject.settings import BASE_DIR
import os
from PIL.Image import Image


class FileControl:
    def gen_id(self):
        return str(int(round(time.time() * 1000)))

    def save(self, file, file_id=None):
        if file_id is None:
            file_id = self.gen_id()

        print(file_id)

        to = self.get_path(file_id)
        with open(to, "w+b") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_id

    def store(self, file_id):
        img = Image.open(self.get_path(file_id))
        img.load()
        img.convert("RGB")
        fp = os.path.join(BASE_DIR, "files", "daem-" + file_id + ".png")
        img.save(fp, "PNG")
        return fp

    def get_path(self, file_id):
        return os.path.join(BASE_DIR, "files", "tmp", "daem-" + file_id)
