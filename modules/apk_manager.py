import os


class APKManager:

    def __init__(self, apps_folder):

        self.apps_folder = apps_folder

        os.makedirs(
            self.apps_folder,
            exist_ok=True
        )


    def scan_apks(self):

        apk_list = []

        for file in os.listdir(self.apps_folder):

            if file.lower().endswith(".apk"):

                apk_list.append(file)

        return apk_list


    def get_apk_path(self, apk_name):

        return os.path.join(
            self.apps_folder,
            apk_name
        )