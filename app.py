from fastapi import FastAPI
from ai_text_generator import queries
from ai_text_generator.notification_generator import generate_notification_message
app = FastAPI()

@app.get("/")
def get_user_data():
    pass

@app.post("/user_data/{user_data}")
def insert_user_data():
    pass

@app.post("/activity_notification/{activity}")
def activity_notification(activity:str):
    notification_message = generate_notification_message(queries.activity_notification,activity)
    return {"message":notification_message}

@app.get("/health_notification")
def get_health_notification():
    pass

@app.post("/upcomping_event_notification/{event}")
def upcoming_event_notification():
    pass

@app.post("/sleeping_notification/{time_data}")
def sleeping_notification():
    pass

@app.get("/tips_notification")
def get_tips_notification():
    pass

    