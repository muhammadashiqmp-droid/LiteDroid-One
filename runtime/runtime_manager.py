import os
import json


class RuntimeManager:

    def __init__(self):

        self.base_path = os.path.dirname(
            os.path.abspath(__file__)
        )

        self.config_file = os.path.join(
            self.base_path,
            "runtime_config.json"
        )

        self.runtime_path = None

        self.load_config()


    def load_config(self):

        if os.path.exists(self.config_file):

            with open(
                self.config_file,
                "r"
            ) as file:

                data = json.load(file)

                self.runtime_path = data.get(
                    "runtime_path"
                )


    def save_config(self):

        data = {
            "runtime_path": self.runtime_path
        }

        with open(
            self.config_file,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )


    def set_runtime(self, path):

        if os.path.exists(path):

            self.runtime_path = path

            self.save_config()

            return True

        return False



    def check_runtime(self):

        if self.runtime_path:

            return os.path.exists(
                self.runtime_path
            )

        return False



    def get_status(self):

        if self.check_runtime():

            return "Android Runtime Ready"

        return "Android Runtime Not Found"



if __name__ == "__main__":

    runtime = RuntimeManager()

    print(
        runtime.get_status()
    )