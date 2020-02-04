data = {
    "data": [
        {
            "id": 1,
            "Title": "Instagram, Remade",
            "Description": "Remade Instagram with client side and server side dynamic "
                           "pages.",
            "Skills": ["Flask", "MySQL", "React.js"],
            "Demo": "https://www.youtube.com/watch?v=d_IBDNTvAfs",
            "Source": ""
        },
        {
            "id": 2,
            "Title": "Using Data Mining to Predict Suicide Rates",
            "Description": "Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.",
            "Skills": ["R", "Linear Regression", "Splines", "GAM"],
            "Demo": "Lorem ipsum",
            "Source": "Lorem ipsum"
        },
        {
            "id": 3,
            "Title": "Interactive RFID",
            "Description": "Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.",
            "Skills": ["Python"],
            "Demo": "Lorem ipsum",
            "Source": "Lorem ipsum"
        },
        {
            "id": 4,
            "Title": "Mobile Barcode Scanner",
            "Description": "Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.",
            "Skills": ["Product Design"],
            "Demo": "Lorem ipsum",
            "Source": "Lorem ipsum"
        }
    ]
}

import json
if __name__ == "__main__":
    with open('projects.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

