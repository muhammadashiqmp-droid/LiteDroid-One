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
        """
        Find all APK files
        """

        apk_list = []

        for file in os.listdir(self.apps_folder):

            if file.lower().endswith(".apk"):
                apk_list.append(file)

        return apk_list


    def get_apk_path(self, apk_name):
        """
        Get full APK location
        """

        return os.path.join(
            self.apps_folder,
            apk_name
        )


    def install_apk(self, apk_path):
        """
        Copy APK into LiteDroid apps folder
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
        Remove APK from apps folder
        """

        file_path = self.get_apk_path(
            apk_name
        )


        if os.path.exists(file_path):

            os.remove(file_path)

            return True


        return False