import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:
        headers = list()
        for line_ in f:
            headers = (line_[:-len(new_line)].split(delimiter))
            break
        itog = list()
        for line_ in f:
            line_ = line_[:-len(new_line)].split(delimiter)
            itog.append({headers[line_.index(each)]: each for each in line_})
    return itog


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
