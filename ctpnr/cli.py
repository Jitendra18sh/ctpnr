import argparse
import json
from .api import fetch_pnr

def main():
    parser = argparse.ArgumentParser(description="Check Indian Railways PNR Status")
    parser.add_argument("pnr", help="PNR number")
    parser.add_argument("--json", action="store_true", help="Show raw JSON output")

    args = parser.parse_args()

    data = fetch_pnr(args.pnr)

    if args.json:
        print(json.dumps(data, indent=2))
        return

    if "error" in data:
        print("❌ Error:", data["error"])
        return

    print("\n===== PNR STATUS =====")
    print("PNR:", data["pnr"])
    print("Train:", data["train_no"], "-", data["train_name"])
    print("From:", data["from"], " → To:", data["to"])
    print("Date of Journey:", data["doj"])
    print("Class:", data["class"])
    print("Chart Prepared:", data["chart_prepared"])
    print("\n--- Passenger Status ---")

    for p in data["passengers"]:
        print(f"Passenger {p['no']}:")
        print("  Booking Status :", p["booking_status"])
        print("  Current Status :", p["current_status"])
        print("  Prediction     :", p["prediction"])
        print()

    print("Departure Time  :", data.get("departure_time"))
    print("Arrival Time    :", data.get("arrival_time"))
    print("Expected Platform:", data.get("expected_platform"))
    print("=======================\n")
