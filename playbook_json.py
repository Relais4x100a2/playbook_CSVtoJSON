import csv
import json
import click


@click.command()
@click.argument("input_file", type=click.File(mode="r", encoding='utf-8'), default=None)
@click.argument("name_playbook", type=str)
@click.argument("output_file", type=click.File(mode="w"), default=None)
def json_playbook(input_file, name_playbook, output_file):
    reader = csv.reader(input_file, delimiter=',')
    group_list = []
    for row in reader:
        liste = row
        group_list.append(liste)

    d = {}
    for row in group_list:
        if row[0] not in d:
            d[row[0]] = []
        d[row[0]].append(row[1:])
    cle = list(d.keys())
    valeur = list(d.values())
    data = {}
    for i in range(0, len(valeur)):
        f = []
        for a in range(0, (len(valeur[i]))):
            s_f = {"type": valeur[i][a][0], "content": valeur[i][a][1]}
            f.append(s_f)
        data[str(i)] = {'section_name': cle[i], 'fields': f}
    data["playbook_name"] = name_playbook

    json.dump(data, output_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    json_playbook()
