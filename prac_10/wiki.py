import wikipedia


def main():
    """Ask user for a search topic or title for Wikipedia and return the title, summary and URL."""
    title = input("What would you like to search for in Wikipedia? ")
    while title != "":
        chosen_page = handle_disambiguation_page(title)
        if chosen_page:
            print(chosen_page.title)
            print(chosen_page.summary)
            print(chosen_page.url)
        title = input("What would you like to search for in Wikipedia? ")
    print("Farewell.")


def handle_disambiguation_page(title):
    """Handle page if it raises a DisambiguationError."""
    try:
        return wikipedia.page(title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)  # BeautifulSoup error runs here however we ignore it
        return None  # Return None to avoid NameError for print states ('chosen page being undefined')


main()
