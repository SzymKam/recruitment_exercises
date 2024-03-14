from typing import TypedDict, List, Dict


class Library(TypedDict):
    language: str
    name: str


libraries: List[Library] = [
    {"language": "Python", "name": "Flask"},
    {"language": "Java", "name": "Spring"},
    {"language": "Javascript", "name": "React"},
    {"language": "Javascript", "name": "Svelte"},
    {"language": "Python", "name": "Django"},
    {"language": "Ruby", "name": "Ruby on Rails"}
]


def group_by_language(libraries: List[Library]) -> Dict[str, List[Library]]:
    """returns a dictionary of lists, keyed by language"""
    to_return: Dict[str, List] = {}
    for library in libraries:
        language = library["language"]
        if language not in to_return:
            to_return.update({language: [library]})
        else:
            to_return[language].append(library)

    return to_return


final = group_by_language(libraries)
print(final)




