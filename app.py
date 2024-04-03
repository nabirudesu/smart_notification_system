from fastapi import FastAPI, Request
from ai_text_generator import queries
from ai_text_generator.notification_generator import generate_notification_message
app = FastAPI()

@app.get("/")
def get_user_data():
    return{"message":"This is the smart notification system"}

@app.post("/user_data/{user_data}")
async def insert_user_data(user_data: Request):
    request_data= await user_data.json()
    return{"message":"this the user data recieved",
           "data":request_data}

@app.post("/activity_notification/{activity}")
async def activity_notification(activity:Request):
    activity_recieved = await activity.json() 
    notification_message = generate_notification_message(queries.activity_notification,activity_recieved)
    return {"request_data":activity_recieved,
            "notification":notification_message}

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

    