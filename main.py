from get_raw_files import get_raw_files
from get_meta_data import (
    retreive_all_soup,
    extract_financial_data,
    verify_and_write_data,
)

headers = {"User-Agent": "Chrome/90.0.4430.212"}


def main() -> None:
    get_raw_files(headers)
    soup_list = retreive_all_soup()
    for soup in soup_list:
        financial_data_dict = extract_financial_data(soup)
        verify_and_write_data(financial_data_dict)
    print("\nFinancial Data Extracted...")


if __name__ == "__main__":
    main()
