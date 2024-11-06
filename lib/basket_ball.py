def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }




def num_points_per_game(player_name):
    data = game_dict()

    for player in data['home']['players']:
        if player['name'] == player_name:
            return player['points_per_game']

    for player in data['away']['players']:
        if player['name'] == player_name:
            return player['points_per_game'] 

    return 'Player not found'

print(num_points_per_game('Kevin Lov'))




def player_age(player_name):
    data = game_dict()

    for player in data['home']['players']:
        if player['name'] == player_name:
            return player['age']

    for player in data['away']['players']:
        if player['name'] == player_name:
            return player['age']

    return 'Player not found'

print(player_age('Kevin Love'))




def team_colors(team_name):
    data = game_dict()

    if data['home']['team_name'] == team_name:
        return data['home']['colors']

    if data['away']['team_name'] == team_name:
        return data['away']['colors']

print(team_colors('Washington Wizards'))




def team_names():
    data = game_dict()

    return data['home']['team_name'], data['away']['team_name']

print(team_names())




def player_numbers(team_name):
    data = game_dict()

    numbers = []

    if data['home']['team_name'] == team_name:
        for player in data['home']['players']:
            numbers.append(player['number'])

    elif data['away']['team_name'] == team_name:
        for player in data['away']['players']:
            numbers.append(player['number'])

    else:
        return 'team not found' 

    return numbers

print(player_numbers('Washington Wizards'))




def player_stats(player_name):
    data = game_dict()

    for player in data['home']['players']:
        if player['name'] == player_name:
            return player

    for player in data['away']['players']:
        if player['name'] == player_name:
            return player

    return f'{player_name} not found'

print(player_stats('Rui Hachimura'))




def average_rebounds_by_shoe_brand():
    data = game_dict()

    # Initialize lists for each shoe brand
    nike_list = []
    adidas_list = []
    puma_list = []
    jordan_list = []

    # Collect rebound data for each shoe brand (both home and away teams)
    for x in data['home']['players'] + data['away']['players']:
        if x['shoe_brand'] == 'Nike':
            nike_list.append(x['rebounds_per_game'])
        elif x['shoe_brand'] == 'Adidas':
            adidas_list.append(x['rebounds_per_game'])
        elif x['shoe_brand'] == 'Puma':
            puma_list.append(x['rebounds_per_game'])
        elif x['shoe_brand'] == 'Jordan':
            jordan_list.append(x['rebounds_per_game'])

    # Calculate the averages for each brand
    def calculate_avg(rebounds_list):
        return sum(rebounds_list) / len(rebounds_list) if rebounds_list else 0

    nike_avg = calculate_avg(nike_list)
    adidas_avg = calculate_avg(adidas_list)
    puma_avg = calculate_avg(puma_list)
    jordan_avg = calculate_avg(jordan_list)

    # Prepare the result
    result = (
        f'Nike: {nike_avg:.2f} rebounds\n'
        f'Adidas: {adidas_avg:.2f} rebounds\n'
        f'Puma: {puma_avg:.2f} rebounds\n'
        f'Jordan: {jordan_avg:.2f} rebounds'
    )

    return result

# Test the function
print(average_rebounds_by_shoe_brand())
