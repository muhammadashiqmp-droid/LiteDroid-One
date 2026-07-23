import os
import shutil


class APKManager:

    def __init__(self, apps_folder):
        self.apps_folder = apps_folder

        os.makedirs(
            self.apps_folder,
            exist_ok=True
        )


    def get_apks(self):
        """
        Find all APK files
        """

        apks = []

        for file in os.listdir(self.apps_folder):

            if file.lower().endswith(".apk"):
                apks.append(file)

        return apks



    def install_apk(self, apk_path):
        """
        Copy APK into apps folder
        """

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



    def remove_apk(self, apk_name):
        """
        Delete APK
        """

        file_path = os.path.join(
            self.apps_folder,
            apk_name
        )


        if os.path.exists(file_path):

            os.remove(file_path)

            return True


        return False