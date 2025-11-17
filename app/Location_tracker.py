import phonenumbers
from phonenumbers import geocoder, carrier
import requests 

import os
from dotenv import load_dotenv

load_dotenv()  # loads from .env file

NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")
if not NUMVERIFY_API_KEY:
    raise ValueError("NUMVERIFY_API_KEY not found in environment variables")

def lookup_number(phone_number: str):
    try:
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


def get_location_and_carrier(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get the location (region) of the phone number
        location = geocoder.description_for_number(parsed_number, "en")

        # Get the carrier (service provider) of the phone number
        service_provider = carrier.name_for_number(parsed_number, "en")

        return location, service_provider
    except phonenumbers.NumberParseException:
        return None, None
    
    
  #Testing the function
if __name__ == "__main__":
    test_number = "+14158586273"  # Example number
    details = lookup_number(test_number)
    print(details)  