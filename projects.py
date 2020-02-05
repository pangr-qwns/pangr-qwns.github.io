data = {
    "data": [
        {
            "Title": "Mobile Barcode Scanner",
            "Description": "Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.",
            "Skills": ["Product Design"],
            "Demo": "Lorem ipsum",
            "Source": "Lorem ipsum",
            "Image": "./static/instagram.jpg"
        },
        {
            "Title": "Using Data Mining to Predict Suicide Rates",
            "Description": "Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.",
            "Skills": ["R", "Linear Regression", "Splines", "GAM"],
            "Demo": "Lorem ipsum",
            "Source": "Lorem ipsum",
            "Image": "./static/instagram.jpg"
        },
        {
            "Title": "Interactive RFID",
            "Description": "Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.",
            "Skills": ["Python"],
            "Demo": "Lorem ipsum",
            "Source": "Lorem ipsum",
            "Image": "./static/instagram.jpg"
        },
        {
            "Title": "Insta485",
            "Description": "My Web Systems class, EECS 485, had me recreating "
                           "Instagram. I implemented my own REST API to "
                           "handle database requests for comments, photos, "
                           "likes, and all the other good stuff in Instagram. "
                           "Unfortunately, the honor code does not let me "
                           "post my project code. But enjoy the demo!",
            "Skills": ["Flask", "MySQL", "React.js"],
            "Demo": "https://www.youtube.com/watch?v=d_IBDNTvAfs",
            "Source": "",
            "Image": "./static/instagram.jpg"
        }
    ]
}

import json
if __name__ == "__main__":
    with open('projects.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

