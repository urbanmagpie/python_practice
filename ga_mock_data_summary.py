import json
import datetime


def get_mock_ga_data():
    """
    Simulates fetching Google Analytics data from an API.
    Returns mock data similar to a GA API response.
    """
    mock_response = {
        "dateRange": {
            "startDate": "2025-07-01",
            "endDate": "2025-07-20"
        },
        "totals": {
            "users": 1234,
            "sessions": 1500,
            "pageviews": 4567
        },
        "dailyBreakdown": [
            {"date": "2025-07-18", "users": 55, "sessions": 60, "pageviews": 120},
            {"date": "2025-07-19", "users": 65, "sessions": 70, "pageviews": 140},
            {"date": "2025-07-20", "users": 70, "sessions": 80, "pageviews": 160},
        ]
    }
    return mock_response


def print_summary(ga_data):
    """Prints a summary of GA data."""
    start = ga_data['dateRange']['startDate']
    end = ga_data['dateRange']['endDate']
    users = ga_data['totals']['users']
    sessions = ga_data['totals']['sessions']
    pageviews = ga_data['totals']['pageviews']

    print(f"Google Analytics Summary ({start} to {end}):")
    print(f"Total Users: {users}")
    print(f"Total Sessions: {sessions}")
    print(f"Total Pageviews: {pageviews}\n")


def print_daily_details(ga_data):
    """Prints daily breakdown of GA data."""
    print("Daily Breakdown:")
    for day in ga_data['dailyBreakdown']:
        print(f"{day['date']}: {day['users']} users, {day['sessions']} sessions, {day['pageviews']} pageviews")


def save_data_to_json(ga_data, filename="ga_data_mock.json"):
    """Saves the GA data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(ga_data, file, indent=4)
    print(f"\nMock GA data saved to {filename}")


if __name__ == "__main__":
    data = get_mock_ga_data()
    print_summary(data)
    print_daily_details(data)
    save_data_to_json(data)

