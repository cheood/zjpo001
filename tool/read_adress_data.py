import yaml


def read_address_data(file_name):
    # with open("../data/" + file_name, "r", encoding="utf-8")as f:
    #     return yaml.load(f)
    with open("./data/" + file_name, "r", encoding="utf-8")as f:
        return yaml.load(f)

