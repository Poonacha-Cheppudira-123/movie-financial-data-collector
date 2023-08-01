from bs4 import BeautifulSoup
import os


rawfile_names_list = os.listdir("rawfiles/")


count = 1

for rawfile_name in rawfile_names_list:
    with open(f"rawfiles/{rawfile_name}", "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")

    # Movie Title
    try:
        movie_title = soup.find("h1", class_="a-size-extra-large").text
    except:
        movie_title = "Not Found"

    # Domestic, International, Worldwide Profits
    try:
        rollout_table = soup.find_all("span", class_="a-size-medium a-text-bold")
    except:
        rollout_table = "Rollout Table Not Found"

    if rollout_table != "Rollout Table Not Found":
        domestic_profit = rollout_table[0].text.strip()
        international_profit = rollout_table[1].text.strip()
        worldwide_profit = rollout_table[2].text.strip()

    if domestic_profit == "":
        domestic_profit = "Domestic Profit Not Found"
    if international_profit == "":
        international_profit = "International Profit Not Found"
    if worldwide_profit == "":
        worldwide_profit = "Worldwide Profit Not Found"

    # Release Date, Opening Profits, Gross Profits
    try:
        domestic_table = soup.find_all(
            "table",
            class_="a-bordered a-horizontal-stripes mojo-table releases-by-region",
        )
    except:
        domestic_table = "Domestic Table Not Found"

    if domestic_table != "Domestic Table Not Found":
        domestic_table_row = domestic_table[0].find_all("tr")[2].find_all("td")
        release_date = domestic_table_row[1].text.strip()
        opening_profit = domestic_table_row[2].text.strip()
        gross_profit = domestic_table_row[3].text.strip()

        # release_date = (
        #     domestic_table[0]
        #     .find_all("tr")[2]
        #     .find_all("td", class_="a-align-center")[1]
        #     .text.strip()
        # )
        # opening_profit = (
        #     domestic_table[0]
        #     .find_all("tr")[2]
        #     .find_all("td", class_="a-text-right a-align-center")[0]
        #     .text.strip()
        # )
        # gross_profit = (
        #     domestic_table[0]
        #     .find_all("tr")[2]
        #     .find_all("td", class_="a-text-right a-align-center")[1]
        #     .text.strip()
        # )

    if release_date == "":
        release_date = "–"
    if opening_profit == "":
        opening_profit = "Opening Profit Not Found"
    if gross_profit == "":
        gross_profit = "Gross Profit Not Found"

    with open("financial_data.txt", "a", encoding="utf-8") as f:
        f.write(
            f"Title {count}: {movie_title}\nDomestic Profit: {domestic_profit}\nInternational Profit: {international_profit}\nWorldwide Profit: {worldwide_profit}\nRelease Date: {release_date}\nOpening Profit: {opening_profit}\nGross Profit: {gross_profit}\n\n"
        )

    count += 1
