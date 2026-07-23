import os
import shutil


class APKManager:

    def __init__(self, apps_folder):

        self.apps_folder = apps_folder

        os.makedirs(
            self.apps_folder,
            exist_ok=True
        )


    def scan_apks(self):

        apps = []

        for file in os.listdir(self.apps_folder):

            if file.lower().endswith(".apk"):

                apps.append(file)

        return apps


    def import_apk(self, apk_path):

        if not apk_path.lower().endswith(".apk"):

            return False


        destination = os.path.join(
            self.apps_folder,
            os.path.basename(apk_path)
        )


        shutil.copy2(
            apk_path,
            destination
        )


        return True