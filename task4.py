import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:
        headers = list()
        for line in f:
            word = ""
            for each in line:
                if (each != delimiter) and (each != new_line[0]):
                    word += each
                else:
                    headers.append(word)
                    word = ""
            break
        data = list()
        for line in f:
            current_line = list()
            word = ""
            for each in line:
                if (each != delimiter) and (each != new_line[0]):
                    word += each
                else:
                    current_line.append(word)
                    word = ""
            data.append(current_line)
    return [{headers[list_.index(each)]: each for each in list_} for list_ in data]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
