import shutil

class Test:
    test_folder = "temporary_test_folder"
    test_yaml_path  = "tests/test_config.yaml"
    template_location = "templates"
    __test__ = False

    def __init__(self, interactive = False):
        if interactive is True:
            self.test_yaml_path = "test_config.yaml"
            self.template_location = "../templates"

    def cleanup(self):
        try:
            shutil.rmtree(self.test_folder)
        except:
            pass

    def config(self):
        testing_config = {
            "project_root": self.test_folder,
            "config": self.test_yaml_path,
            "template_location": self.template_location
            }

        return testing_config
