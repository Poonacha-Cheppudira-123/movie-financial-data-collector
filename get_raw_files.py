import requests
from bs4 import BeautifulSoup


def create_movie_links_list(headers: dict) -> list:
    """Scrape movie links from Box Office Mojo for the years 1977 to 2023."""

    years_list = [str(year) for year in range(1977, 2024)]
    movie_links = []

    count = 1
    for year in years_list:
        URL = f"https://www.boxofficemojo.com/year/world/{year}/"

        content = requests.get(URL, headers=headers)
        soup = BeautifulSoup(content.text, "html.parser")

        tr_tags = soup.find_all("tr")
        tr_tags.remove(tr_tags[0])
        for tr_tag in tr_tags:
            link = "https://www.boxofficemojo.com/" + tr_tag.a["href"]
            print(f"Movie Link {count}: {link}")
            movie_links.append(link)
            count += 1

    return movie_links


def get_raw_files(headers: dict) -> None:
    """Fetch raw HTML files for movies from Box Office Mojo based on their links."""

    movie_links = create_movie_links_list(headers)

    for movie_link in movie_links:
        content = requests.get(movie_link, headers=headers)
        soup = BeautifulSoup(content.text, "html.parser")
        movie_title = soup.find("h1", class_="a-size-extra-large").text.strip()

        file_name = ""
        for ch in movie_title.lower():
            if ch.isalnum() or ch == " ":
                file_name += ch
        file_name = file_name.replace(" ", "–")

        with open(f"rawfiles/{file_name}.html", "w", encoding="utf-8") as f:
            f.write(str(soup))

    print(f"\nRaw Files Finished Extracting...")
