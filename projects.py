data = {
    "data": [
        {
            "Title": "Mobile Barcode Scanner",
            "Description": "I attended a hackathon in May 2018 and built a "
                           "shopping app. Users could scan item "
                           "barcodes and the item would appear in the user's "
                           "cart. I drafted wireframes and developed the "
                           "front end parts of the app.",
            "Skills": ["HTML/CSS", "Javascript", "Wireframing"],
            "Demo": "https://www.youtube.com/watch?v=kTKF-1_lmnc",
            "Source": "https://github.com/pangr-qwns/waitless",
            "Image": "./static/instagram.jpg"
        },
        {
            "Title": "Using Data Mining to Predict Suicide Rates",
            "Description": "Working with two other data scientists, I ran a "
                           "dataset of suicide information on different data "
                           "analysis models to predict what factors "
                           "contributed to suicide rates.",
            "Skills": ["R", "Linear Regression", "Splines", "GAM"],
            "Demo": "./static/suicide_report.pdf",
            "Source": "https://github.com/pangr-qwns/predictingSuicideRates/blob/master/Predicting%20Suicide%20Rates.pdf",
            "Image": "./static/instagram.jpg"
        },
        {
            "Title": "Interactive RFID",
            "Description": "I started researching RFID packets under Prof. "
                           "Alanson Sample. RFID are these cool and cheap "
                           "stickers that reflect waves to a sensor. I'm "
                           "building an GUI interface that non technical "
                           "people like doctors can use to examine patients "
                           "efficiently!",
            "Skills": ["Python"],
            "Demo": "https://www.youtube.com/watch?v=kEkylP-edp8",
            "Source": "https://github.com/pangr-qwns/kivy_research",
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
            "Demo": "https://youtu.be/utMnYlB-DQM",
            "Source": "",
            "Image": "./static/instagram.jpg"
        }
    ]
}

import json
if __name__ == "__main__":
    with open('projects.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

