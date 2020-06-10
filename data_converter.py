import json
from static.data.people import victims
from static.data.projects import data
from static.data.photography import pictures


if __name__ == "__main__":
    with open('./static/data/projects.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open("./static/data/people.json", "w", encoding="utf-8") as p:
        json.dump(victims, p, ensure_ascii=False, indent=4)

    with open("./static/data/photography.json", "w", encoding="utf-8") as pics:
        json.dump(pictures, pics, ensure_ascii=False, indent=4)
