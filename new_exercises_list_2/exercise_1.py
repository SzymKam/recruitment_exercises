"""Proszę zaimplementować w Pythonie funkcję group_by , która dla listy słowników zwróci pogrupowaną
listę słowników wg. wskazanego pola. Np. dla wywołania:
group_by (
elements = [
{ 'name' : 'Pierogi' , 'category' : 'główne' , 'value' : 21 },
{ 'name' : 'Rosół' , 'category' : 'zupa' , 'value' : 16 },
{ 'name' : 'Ogórkowa' , 'category' : 'zupa' , 'value' : 17 },
{ 'name' : 'Mascarpone' , 'category' : 'deser' , 'value' : 10 },
{ 'name' : 'Lody' , 'category' : 'deser' , 'value' : 6 },
],
field = 'category'
)
zwróci:
[
{ 'category' : 'główne' , 'items' : [{ 'name' : 'Pierogi' , 'value' : 21 }]},
{ 'category' : 'zupa' , 'items' : [{ 'name' : 'Rosół' , 'value' : 16 }, { 'name' : 'Ogórkowa' , 'value' : 17 }]},
{ 'category' : 'deser' , 'items' : [{ 'name' : 'Mascarpone' , 'value' : 10 }, { 'name' : 'Lody' , 'value' : 6 }]},
]"""
from typing import Dict, List


def group_by(elements: List[Dict], field: str) -> List[Dict]:

    results = []
    for element in elements:

        if not any(element[field] in category.values() for category in results):
            results.append({field: element[field], 'items': [{'name': element['name'], 'value': element['value']}]})

        else:
            to_update = next(result for result in results if result[field] == element[field])
            to_update['items'].append({'name': element['name'], 'value': element['value']})

    return results



enter_list = [
    {'name': 'Pierogi', 'category': 'główne', 'value': 21},
    {'name': 'Rosół', 'category': 'zupa', 'value': 16},
    {'name': 'Ogórkowa', 'category': 'zupa', 'value': 17},
    {'name': 'Mascarpone', 'category': 'deser', 'value': 10},
    {'name': 'Lody', 'category': 'deser', 'value': 6}
]
enter_field = 'category'

outer_dict = group_by(elements=enter_list, field=enter_field)
print(outer_dict)