from api.api_auth import AuthAPI
from api.api_locations import LocationAPI
from api.api_occurrence import OccurrenceAPI
import getpass

LOGIN_URL = "https://api-service.fogocruzado.org.br/api/v2/auth/login"
REFRESH_URL = "https://api-service.fogocruzado.org.br/api/v2/auth/refresh"
TOKEN_FILE = "api/access_token.txt"


def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)
    print(f"AccessToken saved in {TOKEN_FILE}")

def get_token_from_file():
    try:
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def main():
    print("Choose an option:")
    print("1 - Login")
    print("2 - Refresh token")
    print("3 - Get city data")
    print("4 - Get occurrences by city")
    print("5 - Get occurrences by state")
    print("6 - Get all states")
    option = input("Enter 1, 2, 3, 4, 5 or 6: ")
    match option:
        case "1":
            auth = AuthAPI(LOGIN_URL, verify_ssl=False)
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password: ")
            auth.login(email, password)
            if auth.access_token:
                print(f"AccessToken: {auth.access_token}")
                save_token(auth.access_token)
            else:
                print("Failed to get accessToken.")
        case "2":
            auth = AuthAPI(LOGIN_URL, verify_ssl=False)
            token = input("Enter the current accessToken (or press Enter to use the saved one): ")
            if not token:
                token = get_token_from_file()
                if not token:
                    print("No saved token found.")
                    return
            auth.refresh(REFRESH_URL, token=token)
            if auth.access_token:
                print(f"New AccessToken: {auth.access_token}")
                save_token(auth.access_token)
            else:
                print("Failed to refresh the accessToken.")
        case "3":
            city_name = input("Enter the city name: ")
            location_api = LocationAPI(token_file=TOKEN_FILE, verify_ssl=False)
            data = location_api.get_city_data(city_name)
            print(f"City data saved to data/{city_name.lower()}.json")
        case "4":
            city_id = input("Enter the city id: ")
            state_id = input("Enter the state id (or press Enter to skip): ")
            initial_date = input("Enter initial date (YYYY-MM-DD): ")
            final_date = input("Enter final date (YYYY-MM-DD): ")
            order = input("Enter order (ASC or DESC, default ASC): ") or "ASC"
            occurrence_api = OccurrenceAPI(token_file=TOKEN_FILE, verify_ssl=False)
            occurrence_api.get_occurrences(initial_date, final_date, city_id, id_state=state_id if state_id else None, order=order)
            print(f"Occurrences data saved to data/occurrences_{initial_date}_{final_date}_state_{state_id}_city_{city_id}.json")
        case "5":
            state_id = input("Enter the state id: ")
            initial_date = input("Enter initial date (YYYY-MM-DD): ")
            final_date = input("Enter final date (YYYY-MM-DD): ")
            occurrence_api = OccurrenceAPI(token_file=TOKEN_FILE, verify_ssl=False)
            occurrence_api.get_occurrences_by_state(initial_date, final_date, state_id)
            print(f"Occurrences data saved to data/occurrences_{initial_date}_{final_date}_state_{state_id}.json")
        case "6":
            location_api = LocationAPI(token_file=TOKEN_FILE, verify_ssl=False)
            location_api.get_all_states()
            print("States data saved to data/states.json")
        case _:
            print("Invalid option.")

if __name__ == "__main__":
    main()

