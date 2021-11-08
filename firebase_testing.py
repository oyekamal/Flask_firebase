# import firebase_admin
# from firebase_admin import db
# from firebase_admin import credentials, auth


# from firebase_admin import credentials, auth

# cred = credentials.Certificate('fbAdminConfig.json')
# firebase = firebase_admin.initialize_app(cred)

# ref = db.reference("/")

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('fbAdminConfig.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flask-firebase-auth-2942c-default-rtdb.firebaseio.com/'
})


ref = db.reference('/')
ref.set({
        'boxes':
            {
                'box001': {
                    'color': 'red',
                    'width': 1,
                    'height': 3,
                    'length': 2
                },
                'box002': {
                    'color': 'green',
                    'width': 1,
                    'height': 2,
                    'length': 3
                },
                'box003': {
                    'color': 'yellow',
                    'width': 3,
                    'height': 2,
                    'length': 1
                }
            }
        })
