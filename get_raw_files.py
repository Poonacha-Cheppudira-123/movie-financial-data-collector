import requests
from bs4 import BeautifulSoup


def create_movie_links_list(headers: dict) -> list:
    """
    Scrape movie links from Box Office Mojo for the years 1977 to 2023.
    Args:
        headers (dict): A dictionary containing custom headers to be used for HTTP requests.
    Returns:
        movie_link (list): A list of strings representing the movie links.
    """

    years_list = [str(year) for year in range(1977, 2024)]
    movie_links = []

    for year in years_list:
        URL = f"https://www.boxofficemojo.com/year/world/{year}/"

        content = requests.get(URL, headers=headers)
        soup = BeautifulSoup(content.text, "html.parser")

        tr_tags = soup.find_all("tr")
        tr_tags.remove(tr_tags[0])
        for tr_tag in tr_tags:
            link = "https://www.boxofficemojo.com/" + tr_tag.a["href"]
            movie_links.append(link)

    return movie_links


def get_raw_files(headers: dict) -> None:
    """
    Fetch raw HTML files for movies from Box Office Mojo based on their links.
    Args:
        headers (dict): A dictionary containing custom headers to be used for HTTP requests.
    Returns:
        None
    """

    movie_links = create_movie_links_list(headers)

    count = 1
    for movie_link in movie_links:
        content = requests.get(movie_link, headers=headers)
        soup = BeautifulSoup(content.text, "html.parser")
        with open(f"rawfiles/movie-{count}.html", "w", encoding="utf-8") as f:
            f.write(str(soup))
        count += 1
