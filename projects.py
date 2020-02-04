data = {
    "data": [
        {
        "id": 1,
        "Title": "Instagram, Remade",
        "Description": "Remade Instagram with client side and server side dynamic "
                       "pages.",
        "Tech Stack": ["Flask", "MySQL", "React.js"],
        "Demo Link": "https://www.youtube.com/watch?v=d_IBDNTvAfs",
        "Source Code": ""
        }
    ]
}

import json
if __name__ == "__main__":
    with open('projects.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

