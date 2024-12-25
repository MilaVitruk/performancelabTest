import json
import sys
path_1 = sys.argv[1]
path_2 = sys.argv[2]
path_3 = sys.argv[3]

with open(path_1, 'r') as tests_file, open(path_2, 'r') as values_file:
    tests_data = json.load(tests_file)
    values_data = json.load(values_file)

report = tests_data.copy()
id_value = {i_dict['id']: i_dict['value'] for i_dict in values_data['values']}


def recursive(dict_1: dict, dict_2):
    if dict_1.get('values') is None:
        # В задании не сказано, что делать, если id теста нет в values
        dict_1['value'] = dict_2.get(dict_1['id'], 'No value in values json')
    else:
        dict_1['value'] = dict_2.get(dict_1['id'], 'No value in values json')
        for elem in dict_1['values']:
            recursive(elem, dict_2)


for test in report['tests']:
    recursive(test, id_value)

with open(path_3, 'w') as report_file:
    json.dump(report, report_file, indent=4)
