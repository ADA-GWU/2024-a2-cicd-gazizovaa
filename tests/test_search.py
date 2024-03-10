from search_page.search_item import DribbleWebsiteSearchPage
from search_page.search_result import DribbleWebsiteResultPage


def dribble_website_search_test(browser_driver):
    search_page = DribbleWebsiteSearchPage(browser_driver)
    result_page = DribbleWebsiteResultPage(browser_driver)
    PHRASE = "news app ui"

    # Display Dribble website's home page
    search_page.load_page()

    # Search for the phrase - "news app ui"
    search_page.search_box(PHRASE)

    # Search the result title
    assert PHRASE in result_page.title()

    # Add the search result query
    assert PHRASE == result_page.search_input_values()

    titles = result_page.show_results_titles()
    matched_results = [tt for tt in titles if PHRASE.lower() in tt.lower()]
    assert len(matched_results) > 0


