'''
As part of your job as coordinator for your town's youth soccer team,
you need to divide the 18 children who have signed up for
the league into three even teams - Dragons, Sharks and Raptors. In years past,
the teams have been unevenly matched, so this year you are doing your best to
fix that. For each child, you will have the following information: Name, height
(in inches), whether or not they have played soccer before, and their
guardians' names. You'll take a list of these children, divide them into teams
and output a text file listing the three teams and the players on them. There
are three main tasks you'll need to complete to get this done:

In your Python program, read the data from the supplied CSV file.
Store that data in an appropriate data type so that it can be used in
the next task.

Create logic that can iterate through all 18 players and assign them to teams
such that each team has the same number of players. The number of experienced
players on each team should also be the same.

Finally, the program should output a text file named -- teams.txt -- that
contains the league roster listing the team name, and each player on the team
including the player's information: name, whether they've played soccer before
and their guardians' names.

'''
import csv

# Global variables

# this counter is for iterating over the teams, so as to acheive and even
# distribution of players
COUNTER = 0
# dictionary of the players, to store information for the csv
PLAYERS = {}
# Save start date so it's easy to find and change later
START_DATE = "12/15/18 at 5:30 PM"
# dictionary of the teams, to store which plays is on which team
TEAM_PLAYERS = {
    'Dragons': [],
    'Sharks': [],
    'Raptors': []}


# read the data from the supplied CSV file.
with open('soccer_players.csv') as spreadsheet:
    csvreader = csv.reader(spreadsheet)
    # Store that data in an appropriate data type so that it can be used in
    # the next task.
    for i, row in enumerate(csvreader):
        # skip the first row, that only has titles
        if i == 0:
            pass
        # for the rest of the spreadsheet,
        else:
            # build a dictionary of the players
            player_dict = {
                'Height': row[1],
                'Experience': row[2],
                'Guardians': row[3],
                'Team': "",
            }
            # at the dictionary to the global dictionary
            PLAYERS[row[0]] = player_dict
    # Create logic that can iterate through all 18 players and assign them to
    # teams such that each team has the same number of players. The number of
    # experienced players on each team should also be the same.

    # we're going to iterated over the experienced players first
    for bool in ['YES', 'NO']:
        # for all of the players
        for i in list(PLAYERS.keys()):
            # if they are, or aren't experienced
            if PLAYERS[i]['Experience'] == bool:
                while True:
                    # we'll get an IndexError if the counter needs to be reset
                    try:
                        # assign the player to a team on their dictionary
                        PLAYERS[i]['Team'] = list(TEAM_PLAYERS.keys())[COUNTER]
                        # add the player name to the team roster
                        TEAM_PLAYERS[PLAYERS[i]['Team']].append(
                            i)
                        # increment the counter
                        COUNTER += 1
                        # break the while True loop
                        break
                    # if we get an IndexError
                    except IndexError:
                        # reset the counter
                        COUNTER = 0

    # Finally, the program should output a text file named -- teams.txt -- that
    # contains the league roster listing the team name, and each player on the
    # team including the player's information: name, whether they've played
    # soccer before and their guardians' names.

    # create a blank string for export into txt format
    output_string = ""
    # for each team
    for team in list(TEAM_PLAYERS.keys()):
        # add the team name with a new line
        output_string += """TEAM {}
""".format(team.upper())
        # for each player on the team
        for player in TEAM_PLAYERS[team]:
            # add the player name
            output_string += '{} - '.format(player)
            # add their experience
            output_string += 'Has Played Before: {} '.format(
                PLAYERS[player]['Experience'])
            # add their Guardian(s) name(s)
            output_string += '''Guardian(s): {}
'''.format(
                PLAYERS[player]['Guardians'])

            ''' EXTRA CREDIT:
Create 18 text files ("welcome" letters to the players' guardians).
You'll create 1 text file for each player. Use the player's name as the name
of the file, in lowercase and with underscores and ending in .txt. For example
kenneth_love.txt.

Make sure that each file begins with the text "Dear" followed by the
guardian(s) name(s). Also include the additional required information:
player's name, team name, and date & time of first practice.
'''

            welcome_text = """Dear {},
    Thank you for signing up {} for our Youth Soccer League.
They have been assigned to Team {}. Their first practice is to be held at {}.
We look forward to a great season with them!""".format(
                PLAYERS[player]['Guardians'],
                player.split(" ")[0],
                PLAYERS[player]['Team'],
                START_DATE,
                )
            player_name_w_underscores = "_".join(player.split(" "))
            with open(player_name_w_underscores+".txt", 'w') as f:
                f.write(welcome_text)
        # add two blank lines between the teams
        output_string += """

"""
    # save output string as a txt file
    with open('teams.txt', 'w') as f:
        f.write(output_string)

    print('fin')
