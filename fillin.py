import sqlite3

conn = sqlite3.connect('./registrants.db')
db = conn.cursor()

data = [
    {
        'city': 'Brampton',
        'name': 'Purple Purlers',
        'phone': 6475449781,
        'website': 'https://sites.google.com/view/purple-purlers',
        'email': 'thepurplepurlers@gmail.com',
        'description': 'Purple Purlers is a group of students who attend Fairlawn Public School that have a passion for knitting. They are helping the forgotten and abandoned animals in the world with their knitted items. Over the last few years, they have donated over 100 hand-made articles of clothing and blankets to different foundations across Ontario. They have donated to organizations such as the Brampton Animal Services, Forgotten Ones Cat Rescue, Toronto Cat Rescue. For 2020, they are preparing a package of Animal Blankets to send to the Aspen Wildlife Lodge. Currently, they require assistance in web development, marketing needs and promotional material.'
    },
    {
        'city': 'Brampton',
        'name': 'Splash Tutors',
        'phone': 4163575821,
        'website': 'http://www.splashtutor.com/index.html',
        'email': 'info@splashtutor.com',
        'description': 'Splash Tutors is a tutoring business specializing in Math, Chemistry and Biology Tutoring. They also have an online math tutoring service that will save your time and money. Take tutoring in the comfort of your own home, they say! Parent with a busy work schedule can enjoy the convenience of their online Learning at home. Not only this, but they also specialize in IB Tutoring! IB Tutoring is extremely hard to find but with Splash Tutors, all the resources are right under your nose. Currently, they require assistance in app development and web development.'
    },
    {
        'city': 'Markham',
        'name': '39 Spices',
        'phone': 2895548881,
        'website': 'https://www.39spices.com/index.html',
        'email': 'info@39spices.com',
        'description': "39 Spices is a restaurant which is known for its authentic Indian food. It is a fine dining Indian restaurant serving Halal & vegetarian dishes. They offer an exceptional dining experience -or if you're in a rush, a hot and flavourful take out menu. They also offer many Indian sweets and drinks that you would not want to miss out on! Currently, they require assistance in web development."
    },
    {
        'city': 'Mississauga',
        'name': 'TJF Auto Services',
        'phone': 9058486872,
        'website': 'https://tjfauto.com/',
        'email': 'info@tjfautoservice.com',
        'description': "TJF Auto Services is a private company that focuses on auto manufacturing and repair. They are currently located in Missisauga, Ontario. They provide many services such as oil changes, tire changes, fixing bumpers, and so much more! Currently, they require assistance in marketing needs and promotional material."
    }
]

for business in data:
    db.execute(
        'INSERT INTO registrants (city, name, phone, website, email, description)\
        VALUES (?, ?, ?, ?, ?, ?)',
        (
            business['city'],
            business['name'],
            business['phone'],
            business['website'],
            business['email'],
            business['description']
        )
    )

conn.commit()