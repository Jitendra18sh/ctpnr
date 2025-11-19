import requests

API_URL = "https://cttrainsapi.confirmtkt.com/api/v2/ctpro/mweb/{}"
BODY = {"proPlanName": "CP7"}

def fetch_pnr(pnr):
    url = API_URL.format(pnr)
    try:
        response = requests.post(url, json=BODY, timeout=10)
        response.raise_for_status()
        data = response.json().get("data", {})
        return parse_useful_data(data)
    except Exception as e:
        return {"error": str(e)}


def parse_useful_data(data):
    pnr_info = data.get("pnrResponse", {})

    return {
        "pnr": pnr_info.get("pnr"),
        "train_no": pnr_info.get("trainNo"),
        "train_name": pnr_info.get("trainName"),
        "from": pnr_info.get("from"),
        "to": pnr_info.get("to"),
        "doj": pnr_info.get("doj"),
        "class": pnr_info.get("class"),
        "chart_prepared": pnr_info.get("chartPrepared"),

        "passengers": [
            {
                "no": p.get("number"),
                "booking_status": p.get("bookingStatus"),
                "current_status": p.get("currentStatus"),
                "prediction": p.get("prediction"),
            }
            for p in pnr_info.get("passengerStatus", [])
        ],

        "departure_time": pnr_info.get("departureTime"),
        "arrival_time": pnr_info.get("arrivalTime"),
        "expected_platform": pnr_info.get("expectedPlatformNo"),
    }
