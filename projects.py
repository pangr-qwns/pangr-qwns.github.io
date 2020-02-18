data = {
    "data": [
        {
            "Title": "Mobile Barcode Scanner",
            "Description": "A barcode scanner that is used in store and "
                           "serves as a personal cashier.",
            "Skills": ["HTML/CSS", "Javascript", "Wireframing"],
            "Demo": "https://www.youtube.com/watch?v=kTKF-1_lmnc",
            "Source": "https://github.com/stirfrypapi/waitless",
            "Image": "./static/waitless.jpg"
        },
        {
            "Title": "Predicting Suicide Factors",
            "Description": "Ran suicide data on models to predict what "
                           "factors contributed to suicides.",
            "Skills": ["R", "Linear Regression", "Splines", "GAM"],
            "Demo": "./static/suicide_report.pdf",
            "Source": "https://github.com/stirfrypapi/predictingSuicideRates/blob/master/Predicting%20Suicide%20Rates.pdf",
            "Image": "./static/suicide.jpg"
        },
        {
            "Title": "Interaction of Things",
            "Description": "A user interface that predicted how people were "
                           "interacting with things.",
            "Skills": ["Python", "Multi-Processing", "SVM's"],
            "Demo": "https://www.youtube.com/watch?v=_nMauMXDqf8",
            "Source": "https://github.com/stirfrypapi/t_for_train",
            "Image": "./static/rfid.jpg"
        },
        {
            "Title": "Insta485",
            "Description": "Cloned Instagram, recreating client side and "
                           "server side dynamic features.",
            "Skills": ["Flask", "MySQL", "React.js", "Web Dev"],
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

