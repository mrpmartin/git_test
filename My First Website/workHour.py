import json

# Your JSON code snippet
json_code = '''
[
    {
        "same_hours_every_day": true,
        "enable_auto_tracking_outside_hours": false,
        "trip_type_inside_hours": 1,
        "trip_type_outside_hours": 2,
        "hours": [[8, 18], [8, 18], [8, 18], [8, 18], [8, 18], [8, 18], [8, 18]],
        "enabled_days": [true, true, true, true, true, false, false],
        "week_schedule": {
            "mon": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "tue": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "wed": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "thu": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "fri": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "sat": {},
            "sun": {}
        }
    },
    {
        "same_hours_every_day": true,
        "enable_auto_tracking_outside_hours": true,
        "trip_type_inside_hours": 1,
        "trip_type_outside_hours": 2,
        "hours": [[8, 18], [8, 18], [8, 18], [8, 18], [8, 18], [8, 18], [8, 18]],
        "enabled_days": [true, true, true, true, true, false, false],
        "week_schedule": {
            "mon": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "tue": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "wed": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "thu": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "fri": {"shifts": [{"start": {"date": "1970-01-01T08:00:00.000Z"}, "end": {"date": "1970-01-01T18:00:00.000Z"}}]},
            "sat": {},
            "sun": {}
        }
    }
]
'''

# Parse the JSON code
parsed_data = json.loads(json_code)

# Function to print a configuration in a readable format
def print_configuration(config):
    print("Same hours every day:", config["same_hours_every_day"])
    print("Enable auto tracking outside hours:", config["enable_auto_tracking_outside_hours"])
    print("Trip type inside hours:", config["trip_type_inside_hours"])
    print("Trip type outside hours:", config["trip_type_outside_hours"])
    print("Hours:", config["hours"])
    print("Enabled days:", config["enabled_days"])
    print("Week schedule:", json.dumps(config["week_schedule"], indent=4))
    print("----")

# Iterate through each configuration and print in a readable format
for config in parsed_data:
    print_configuration(config)


    