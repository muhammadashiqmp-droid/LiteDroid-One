import os


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