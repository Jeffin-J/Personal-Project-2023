"""
Jeffin Johnykutty

#NOTES:
    I delete sme of the test code for searching elements in the lists I used. I use test code by printing created lists on the screen. In line 104 for example, I print the list "phi_positions" to see what elements that I do not need.
    Below, are all the variables I used for the interactive program code of the project. I organized them by team.

Variables used for interactive program:
PHI EAGLES:
    phi_record
    final_phi_positions
    final_phi_players
    phi_career_record_str
    phi_season_record_website_name
    phi_season_record_website_link
    phi_lineup_website_name
    phi_lineup_website_link
    phi_career_record_website_name
    phi_career_record_website_link

DAL COWBOYS:
    dal_record
    final_dal_positions
    final_dal_players
    dal_career_record_str
    dal_season_record_website_name
    dal_season_record_website_link
    dal_lineup_website_name
    dal_lineup_website_link
    dal_career_record_website_name
    dal_career_record_website_link

NYG GIANTS:
    nyg_record
    final_nyg_positions
    final_nyg_players
    nyg_career_record_str
    nyg_season_record_website_name
    nyg_season_record_website_link
    nyg_lineup_website_name
    nyg_lineup_website_link
    nyg_career_record_website_name
    nyg_career_record_website_link

WAS COMMANDERS:
    was_record
    final_was_positions
    final_was_players
    was_career_record_str
    was_season_record_website_name
    was_season_record_website_link
    was_lineup_website_name
    was_lineup_website_link
    was_career_record_website_name
    was_career_record_website_link
"""


#Packages used
from bs4 import BeautifulSoup
import requests
import csv
import sys

#SCRAPING CODE STARTS HERE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PHILADELPHIA EAGLES SCRAPING----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phi_season_record_website_name = "Pro Football Reference"
phi_season_record_website_link = "https://www.pro-football-reference.com/teams/phi/2022.htm"
phi_lineup_website_name = "Our Lads NFL Scouting"
phi_lineup_website_link = "https://www.ourlads.com/nfldepthcharts/depthchart/PHI"
phi_career_record_website_name = "Pro Football Reference"
phi_career_record_website_link = "https://www.pro-football-reference.com/teams/phi/"

phi_scrape_1 = requests.get("https://www.pro-football-reference.com/teams/phi/2022_roster.htm")
soup_phi_scrape_1 = BeautifulSoup(phi_scrape_1.text, "html.parser")

#EXTRACT AND PARSE Eagle's SEASON RECORD
phi_find_all_p_tags_1 = soup_phi_scrape_1.findAll("p")
phi_record_draft_string = phi_find_all_p_tags_1[2].text
phi_record = phi_record_draft_string[9:15]

#Create an empty csv file named "staring_lineup.csv" and store a table from the given website below into the file.
phi_scrape_2 = requests.get("https://www.ourlads.com/nfldepthcharts/depthchart/PHI")
soup_phi_scrape_2 = BeautifulSoup(phi_scrape_2.text, "html.parser")
find_phi_table = soup_phi_scrape_2.find("table")
find_phi_rows = find_phi_table.find_all("tr")
phi_sl_file_name = "eagles_starting_lineup.csv"
with open(phi_sl_file_name, "w", newline='') as csvfile:
    writer_sl_csv = csv.writer(csvfile)
    for row in find_phi_rows: #Iterate through all the rows in the csv file
        cells = row.find_all("td")
        data = [cell.text for cell in cells]
        writer_sl_csv.writerow(data)

#Extract the first column and second columns from the csv file. Store them in their respective lists.
with open(phi_sl_file_name, "r") as file: #name object as file
    reader = csv.reader(file)
    phi_positions = []
    phi_players = []
    for row in reader:
        if len(row) >= 2:
            phi_positions.append(row[0])
            phi_players.append(row[2])

#Taking out all the irrelevant positions such as reserves and practice squad.
phi_indices = [0, 12, 25, 33, 34, 35, 36, 37, 38, 39, 40, 41]
final_phi_positions = []
for i in range(len(phi_positions)):
    if i not in phi_indices:
        final_phi_positions.append(phi_positions[i])

final_phi_players = []
for i in range(len(phi_players)):
    if i not in phi_indices:
        final_phi_players.append(phi_players[i])

#EXTRACT AND PARSE Eagle's CAREER RECORD
phi_scrape_3 = requests.get("https://www.pro-football-reference.com/teams/phi/")
soup_phi_scrape_3 = BeautifulSoup(phi_scrape_3.text, "html.parser")
phi_find_all_p_tags_2 = soup_phi_scrape_3.findAll("p")

phi_career_record_draft_str = phi_find_all_p_tags_2[3].text
phi_career_record_str = phi_career_record_draft_str[20:30]


#DALLAS COWBOYS SCRAPING----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dal_season_record_website_name = "Pro Football Reference"
dal_season_record_website_link = "https://www.pro-football-reference.com/teams/dal/2022.htm"
dal_lineup_website_name = "Our Lads NFL Scouting"
dal_lineup_website_link = "https://www.ourlads.com/nfldepthcharts/depthchart/DAL"
dal_career_record_website_name = "Pro Football Reference"
dal_career_record_website_link = "https://www.pro-football-reference.com/teams/dal/"

dal_scrape_1 = requests.get(dal_season_record_website_link)
soup_dal_scrape_1 = BeautifulSoup(dal_scrape_1.text, "html.parser")

#EXTRACT AND PARSE Cowboy's SEASON RECORD
dal_find_all_p_tags_1 = soup_dal_scrape_1.findAll("p")
dal_record_draft_string = dal_find_all_p_tags_1[3].text
dal_record = dal_record_draft_string[22:28]

#Create an empty csv file named "cowboys_staring_lineup.csv" and store a table from the given website below into the file.
dal_scrape_2 = requests.get(dal_lineup_website_link)
soup_dal_scrape_2 = BeautifulSoup(dal_scrape_2.text, "html.parser")
find_dal_table = soup_dal_scrape_2.find("table")
find_dal_rows = find_dal_table.find_all("tr")
dal_sl_file_name = "cowboys_starting_lineup.csv"
with open(dal_sl_file_name, "w", newline='') as csvfile:
    writer_sl_csv = csv.writer(csvfile)
    for row in find_dal_rows:
        cells = row.find_all("td")
        data = [cell.text for cell in cells]
        writer_sl_csv.writerow(data)

#Extract the first column and second columns from the csv file. Store them in their respective lists.
with open(dal_sl_file_name, "r") as file:
    reader = csv.reader(file)
    dal_positions = []
    dal_players = []
    for row in reader:
        if len(row) >= 2:
            dal_positions.append(row[0])
            dal_players.append(row[2])


#Taking out all the irrelevant positions such as reserves and practice squad.
dal_indices = [0, 12, 25, 33, 34, 35, 36]
final_dal_positions = []
for i in range(len(dal_positions)):
    if i not in dal_indices:
        final_dal_positions.append(dal_positions[i])
final_dal_players = []
for i in range(len(dal_players)):
    if i not in dal_indices:
        final_dal_players.append(dal_players[i])

#EXTRACT AND PARSE Cowboys CAREER RECORD
dal_scrape_3 = requests.get(dal_career_record_website_link)
soup_dal_scrape_3 = BeautifulSoup(dal_scrape_3.text, "html.parser")
dal_find_all_p_tags_2 = soup_dal_scrape_3.findAll("p")

"""
for i in range(len(dal_find_all_p_tags_2)):
    print(str(i) + " " + dal_find_all_p_tags_2[i].text)
"""
dal_career_record_draft_str = dal_find_all_p_tags_2[3].text
dal_career_record_str = dal_career_record_draft_str[20:29]


#NEW YORK GIANTS SCRAPING----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nyg_season_record_website_name = "Pro Football Reference"
nyg_season_record_website_link = "https://www.pro-football-reference.com/teams/nyg/2022.htm"
nyg_lineup_website_name = "Our Lads NFL Scouting"
nyg_lineup_website_link = "https://www.ourlads.com/nfldepthcharts/depthchart/NYG"
nyg_career_record_website_name = "Pro Football Reference"
nyg_career_record_website_link = "https://www.pro-football-reference.com/teams/nyg/"

nyg_scrape_1 = requests.get(nyg_season_record_website_link)
soup_nyg_scrape_1 = BeautifulSoup(nyg_scrape_1.text, "html.parser")

#EXTRACT AND PARSE Giants SEASON RECORD
nyg_find_all_p_tags_1 = soup_nyg_scrape_1.findAll("p")
"""
for i in range (len(nyg_find_all_p_tags_1)):
    print(str(i) + " " + nyg_find_all_p_tags_1[i].text)
"""
nyg_record_draft_string = nyg_find_all_p_tags_1[3].text
nyg_record = nyg_record_draft_string[21:26]

#Create an empty csv file named "giants_staring_lineup.csv" and store a table from the given website below into the file.
nyg_scrape_2 = requests.get(nyg_lineup_website_link)
soup_nyg_scrape_2 = BeautifulSoup(nyg_scrape_2.text, "html.parser")
find_nyg_table = soup_nyg_scrape_2.find("table")
find_nyg_rows = find_nyg_table.find_all("tr")
nyg_sl_file_name = "giants_starting_lineup.csv"
with open(nyg_sl_file_name, "w", newline='') as csvfile:
    writer_sl_csv = csv.writer(csvfile)
    for row in find_nyg_rows:
        cells = row.find_all("td")
        data = [cell.text for cell in cells]
        writer_sl_csv.writerow(data)

#Extract the first column and second columns from the csv file. Store them in their respective lists.
with open(nyg_sl_file_name, "r") as file:
    reader = csv.reader(file)
    nyg_positions = []
    nyg_players = []
    for row in reader:
        if len(row) >= 2:
            nyg_positions.append(row[0])
            nyg_players.append(row[2])

"""
for i in range(len(nyg_positions)):
    print(str(i) + " " + nyg_positions[i])
"""
#Taking out all the irrelevant positions such as reserves and practice squad.
nyg_indices = [0, 12, 24, 32, 33, 34, 35]
final_nyg_positions = []
for i in range(len(nyg_positions)):
    if i not in nyg_indices:
        final_nyg_positions.append(nyg_positions[i])
final_nyg_players = []
for i in range(len(nyg_players)):
    if i not in nyg_indices:
        final_nyg_players.append(nyg_players[i])
"""        
for pos, player in zip(final_nyg_positions, final_nyg_players):
    print(pos, player)
"""

#EXTRACT AND PARSE Giants CAREER RECORD
nyg_scrape_3 = requests.get(nyg_career_record_website_link)
soup_nyg_scrape_3 = BeautifulSoup(nyg_scrape_3.text, "html.parser")
nyg_find_all_p_tags_2 = soup_nyg_scrape_3.findAll("p")

"""
for i in range(len(nyg_find_all_p_tags_2)):
    print(str(i) + " " + nyg_find_all_p_tags_2[i].text)
"""
nyg_career_record_draft_str = nyg_find_all_p_tags_2[3].text
nyg_career_record_str = nyg_career_record_draft_str[20:30]


#WASHINGTON COMMANDERS SCRAPING----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
was_season_record_website_name = "Pro Football Reference"
was_season_record_website_link = "https://www.pro-football-reference.com/teams/was/2022.htm"
was_lineup_website_name = "Our Lads NFL Scouting"
was_lineup_website_link = "https://www.ourlads.com/nfldepthcharts/depthchart/WAS"
was_career_record_website_name = "Pro Football Reference"
was_career_record_website_link = "https://www.pro-football-reference.com/teams/was/"

was_scrape_1 = requests.get(was_season_record_website_link)
soup_was_scrape_1 = BeautifulSoup(was_scrape_1.text, "html.parser")

#EXTRACT AND PARSE Commanders SEASON RECORD
was_find_all_p_tags_1 = soup_was_scrape_1.findAll("p")
was_record_draft_string = was_find_all_p_tags_1[2].text
was_record = was_record_draft_string[9:14]

#Create an empty csv file named "commanders_staring_lineup.csv" and store a table from the given website below into the file.
was_scrape_2 = requests.get(was_lineup_website_link)
soup_was_scrape_2 = BeautifulSoup(was_scrape_2.text, "html.parser")
find_was_table = soup_was_scrape_2.find("table")
find_was_rows = find_was_table.find_all("tr")
was_sl_file_name = "commanders_starting_lineup.csv"
with open(was_sl_file_name, "w", newline='') as csvfile:
    writer_sl_csv = csv.writer(csvfile)
    for row in find_was_rows:
        cells = row.find_all("td")
        data = [cell.text for cell in cells]
        writer_sl_csv.writerow(data)

#Extract the first column and second columns from the csv file. Store them in their respective lists.
with open(was_sl_file_name, "r") as file:
    reader = csv.reader(file)
    was_positions = []
    was_players = []
    for row in reader:
        if len(row) >= 2:
            was_positions.append(row[0])
            was_players.append(row[2])


#Taking out all the irrelevant positions such as reserves and practice squad.
was_indices = [0, 10, 13, 25, 33, 34, 35]
final_was_positions = []
for i in range(len(was_positions)):
    if i not in was_indices:
        final_was_positions.append(was_positions[i])
final_was_players = []
for i in range(len(was_players)):
    if i not in was_indices:
        final_was_players.append(was_players[i])

#EXTRACT AND PARSE Commanders CAREER RECORD
was_scrape_3 = requests.get(was_career_record_website_link)
soup_was_scrape_3 = BeautifulSoup(was_scrape_3.text, "html.parser")
was_find_all_p_tags_2 = soup_was_scrape_3.findAll("p")

was_career_record_draft_str = was_find_all_p_tags_2[3].text
was_career_record_str = was_career_record_draft_str[20:30]

#SCRAPING CODE ENDS HERE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Global variables
options = ("1", "2", "3", "4")
team_names = ["Philadelphia Eagles", "Dallas Cowboys", "New York Giants", "Washington Commanders"]

def interactive_program():
    main_menu()

def main_menu():
    print_main_menu_screen()
    while True:
        user_input = input("Please select which NFC East team would you like to learn about by entering their respective numbers: ")
        if (user_input.isdigit()) and (options.__contains__(user_input) == True):
            if user_input == "1":
                team_options(user_input, team_names[0])
            elif user_input == "2":
                team_options(user_input, team_names[1])
            elif user_input == "3":
                team_options(user_input, team_names[2])
            else:
                team_options(user_input, team_names[3])
        elif user_input == "5":
            exit_prog()
        else:
            print("Invalid response. Please try again.")


def print_main_menu_screen():
    print("\nTHE NFL'S NATIONAL FOOTBALL  EASTERN CONFERENCE (NFC EAST) OVERVIEW")
    print("\t[1] Philadelphia Eagles (PHI)")
    print("\t[2] Dallas Cowboys (DAL)")
    print("\t[3] New York Giants (NYG)")
    print("\t[4] Washington Commanders (WAS)")
    print("\t[5] Exit")

def print_select_team_options():
    print("\nTEAM MAIN MENU")
    print("[1] Starting lineup of the 2023 season")
    print("[2] Franchise win record")
    print("[3] 2022-23 win record")
    print("[4] Sources and links about the team")
    print("[5] Exit")
    print("[6] Go back")

def team_options(team_num, team_name):
    print_select_team_options()

    while True:
        user_choice = input("Please select what you want to know about the " + team_name + ": ")

        if user_choice == "5":
            exit_prog()
        elif user_choice == "6":
            main_menu()
        elif user_choice == "1":
            starting_lineup(team_num, team_name[0])
        elif user_choice == "2":
            franchise_record(team_num, team_name[1])
        elif user_choice == "3":
            season_record(team_num, team_name[2])
        elif user_choice == "4":
            sources(team_num, team_name[3])
        else:
            print("Invalid response. Please try again.")

def exit_prog():
    print("You have exited the program. Goodbye!")
    sys.exit(0)

def starting_lineup(team_num, team_name):
    sys.exit(0)

def franchise_record(team_num, team_name):
    sys.exit(0)

def season_record(team_num, team_name):
    sys.exit(0)

def sources(team_num, team_name):
    sys.exit(0)

interactive_program()


