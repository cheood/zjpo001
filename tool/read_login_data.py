import yaml


def read_login_data(file_name):
    # with open("../data/" + file_name, "r", encoding="utf-8")as f:
    #     return yaml.load(f)
    with open("./data/" + file_name, "r", encoding="utf-8")as f:
        return yaml.load(f)


