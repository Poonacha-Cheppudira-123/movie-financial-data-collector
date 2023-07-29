from get_raw_files import get_raw_files

headers = {"User-Agent": "Chrome/90.0.4430.212"}


def main() -> None:
    get_raw_files(headers)


if __name__ == "__main__":
    main()
