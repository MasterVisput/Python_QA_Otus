import json
import csv

final_js_object = []
final_books_list = []
a = 0

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        final_books_list.append(
            {
                'title':line['Title'],
                'author':line['Author'],
                'height':line['Height']
            }
        )


with open('data/books-39204-271043.csv', newline='') as f_obj:
    csv_dict_reader(f_obj)


with open("data/users.json", "r") as json_file:
    users = json.loads(json_file.read())

for el in users:
    data = {
        'name': el['name'],
        'gender': el['gender'],
        'address': el['address'],
        'books': []
    }
    final_js_object.append(data)

for el in final_js_object:
    cnt = len(final_books_list)
    if a <= cnt:
        el['books'].append(final_books_list[a])
    a += 1

with open("answer.json", "w") as answer_file:
    s = json.dumps(final_js_object, indent=4)
    answer_file.write(s)
