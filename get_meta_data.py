from bs4 import BeautifulSoup
import os


def retreive_all_soup() -> list:
    """Retrieve BeautifulSoup objects from HTML files in the 'rawfiles/' directory."""

    soup_list = []
    rawfile_names_list = os.listdir("rawfiles/")
    for rawfile_name in rawfile_names_list:
        with open(f"rawfiles/{rawfile_name}", "r", encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")
            soup_list.append(soup)
    print("\nSoup List Finalized...")
    return soup_list


def extract_financial_data(soup: BeautifulSoup) -> list:
    """Extracts financial data from the given BeautifulSoup object and returns it as a dictionary."""

    financial_data_dict = {}

    movie_title = soup.find("h1", class_="a-size-extra-large").text.strip()

    try:
        rollout_table = soup.find_all("span", class_="a-size-medium a-text-bold")
    except:
        rollout_table = "Rollout Table Not Found"

    if rollout_table != "Rollout Table Not Found":
        domestic_profit = rollout_table[0].text.strip()
        international_profit = rollout_table[1].text.strip()
        worldwide_profit = rollout_table[2].text.strip()

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

    financial_data_dict = {
        "movie_title": movie_title,
        "domestic_profit": domestic_profit,
        "international_profit": international_profit,
        "worldwide_profit": worldwide_profit,
        "release_date": release_date,
        "opening_profit": opening_profit,
        "gross_profit": gross_profit,
    }

    return financial_data_dict


def verify_and_write_data(financial_data_dict: dict) -> None:
    """Verify and write financial data to 'financial_data.txt' file with '-' for missing or empty values."""

    for key in financial_data_dict:
        if financial_data_dict[key] == "" or financial_data_dict[key] == "–":
            financial_data_dict[key] = None

    movie_title = financial_data_dict.get("movie_title")
    domestic_profit = financial_data_dict.get("domestic_profit")
    international_profit = financial_data_dict.get("international_profit")
    worldwide_profit = financial_data_dict.get("worldwide_profit")
    release_date = financial_data_dict.get("release_date")
    opening_profit = financial_data_dict.get("opening_date")
    gross_profit = financial_data_dict.get("gross_profit")

    with open("financial_data.txt", "a", encoding="utf-8") as f:
        f.write(
            f"Title: {movie_title}\nDomestic Profit: {domestic_profit}\nInternational Profit: {international_profit}\nWorldwide Profit: {worldwide_profit}\nRelease Date: {release_date}\nOpening Profit: {opening_profit}\nGross Profit: {gross_profit}\n\n"
        )
