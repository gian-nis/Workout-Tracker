import json

manage_on = True

while manage_on:

    def check_file():
        try:
            with open('workout_data.json', "r") as f:
                workout_dict = json.loads(f.read())
            return workout_dict
        except FileNotFoundError:
            workout_dict = {}
            return workout_dict

    print("\n")
    prompt = "Would you like to add a new workout? 'Add Workout'\n"
    prompt += "Would you like to view data? 'View Data'\n"
    answer = input(prompt).upper()

    if answer == 'ADD WORKOUT':
        workout_dict = check_file()
        if workout_dict:
            day = input("Has a day passed since your most recent input? ").upper()
            if day == "NO":
                workout_name = input("Which workout did you do? ")
                reps = input("How many reps did you do? ")
                sets = input("How many sets did you do? ")
                weight = input("How heavy did you go? ")
                date = input("What is the date in MM/DD/YY? ")
                if date in workout_dict:
                    data = {
                        "Workout Name": workout_name,
                        "Reps": reps,
                        "Sets": sets,
                        "Weight": weight
                    }
                    workout_dict[date].append(data)
                    with open('workout_data.json', 'w') as f:
                        json.dump(workout_dict, f)
            else:
                workout_name = input("Which workout did you do? ")
                reps = input("How many reps did you do? ")
                sets = input("How many sets did you do? ")
                weight = input("How heavy did you go? ")
                date = input("What is the date in MM/DD/YY? ")
                data = {
                    "Workout Name": workout_name,
                    "Reps": reps,
                    "Sets": sets,
                    "Weight": weight
                }
                workout_dict[date] = data
                with open('workout_data.json', 'w') as f:
                    json.dump(workout_dict, f)

        else:
            workout_name = input("Which workout did you do? ")
            reps = input("How many reps did you do? ")
            sets = input("How many sets did you do? ")
            weight = input("How heavy did you go? ")
            date = input("What is the date in MM/DD/YY? ")
            data = {
                "Workout Name": workout_name,
                "Reps": reps,
                "Sets": sets,
                "Weight": weight
            }
            workout_dict = {
                date: [data]
            }
            with open('workout_data.json', 'w') as f:
                json.dump(workout_dict, f)

    elif answer == "VIEW DATA":
        data_view = input("What date do you want to see the data for? ")
        workout_dict = check_file()
        if data_view in workout_dict:
            for j in workout_dict[data_view]:
                print(j)

    continue_or_leave = input("\nDo you wish to exit? 'no' or 'yes'. ").upper()

    if continue_or_leave == "YES":
        manage_on = False