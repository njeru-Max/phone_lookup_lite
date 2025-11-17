import phonenumbers
from phonenumbers import geocoder, carrier
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")

def lookup_number(phone_number: str):
    try:
        if not phone_number.strip():
            return {"error": "No phone number entered"}

        # Validate format with phonenumbers
        parsed = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed):
            return {"error": "Invalid phone number"}

        # Basic offline details
        country_basic = geocoder.description_for_number(parsed, "en") or "Unknown"
        carrier_basic = carrier.name_for_number(parsed, "en") or "Unknown"

        # API call to Numverify
        url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone_number}"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            return {"error": f"API Error: {data['error']['info']}"}

        # Extract details from API
        country_api = data.get("country_name", country_basic)
        city_api = data.get("location", "Unknown")
        carrier_api = data.get("carrier", carrier_basic)
        line_type = data.get("line_type", "Unknown")

        return {
            "country": country_api,
            "city": city_api,
            "carrier": carrier_api,
            "line_type": line_type
        }

    except Exception as e:
        return {"error": str(e)}

# --------------------------
# Example run
# --------------------------
if __name__ == "__main__":
    number = input("Enter phone number with country code (e.g. , +254712345678): ")
    result = lookup_number(number)

    if "error" in result:
        print("Error:", result["error"])
    else:
        print("Country:", result["country"])
        print("City/Region:", result["city"])
        print("Carrier:", result["carrier"])
        print("Line Type:", result["line_type"])
