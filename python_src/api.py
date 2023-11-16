from fastapi import FastAPI

app = FastAPI()

power = False

@app.get("/")
async def root():
    return {"power": power}

@app.put("/change_power/{new_power}")
async def change_power(new_power: bool):
    global power

    power = new_power
    return {"message": "Power value changed successfully", "power": power}

