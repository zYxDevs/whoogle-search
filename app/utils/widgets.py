from pathlib import Path
from bs4 import BeautifulSoup


# root
BASE_DIR = Path(__file__).parent.parent.parent

def add_ip_card(html_soup: BeautifulSoup, ip: str) -> BeautifulSoup:
    """Adds the client's IP address to the search results
        if query contains keywords

    Args:
        html_soup: The parsed search result containing the keywords
        ip: ip address of the client

    Returns:
        BeautifulSoup

    """
    if main_div := html_soup.select_one('#main'):
        # HTML IP card tag
        ip_tag = html_soup.new_tag('div')
        ip_tag['class'] = 'ZINbbc xpd O9g5cc uUPGi'

        # For IP Address html tag
        ip_address = html_soup.new_tag('div')
        ip_address['class'] = 'kCrYT ip-address-div'
        ip_address.string = ip

        # Text below the IP address
        ip_text = html_soup.new_tag('div')
        ip_text.string = 'Your public IP address'
        ip_text['class'] = 'kCrYT ip-text-div'

        # Adding all the above html tags to the IP card
        ip_tag.append(ip_address)
        ip_tag.append(ip_text)

        # Insert the element at the top of the result list
        main_div.insert_before(ip_tag)
    return html_soup

def add_calculator_card(html_soup: BeautifulSoup) -> BeautifulSoup:
    """Adds the a calculator widget to the search results
        if query contains keywords

    Args:
        html_soup: The parsed search result containing the keywords

    Returns:
        BeautifulSoup
    """
    if main_div := html_soup.select_one('#main'):
        with open(BASE_DIR / 'app/static/widgets/calculator.html', encoding="utf8") as widget_file:
            widget_tag = html_soup.new_tag('div')
            widget_tag['class'] = 'ZINbbc xpd O9g5cc uUPGi'
            widget_tag['id'] = 'calculator-wrapper'
            calculator_text = html_soup.new_tag('div')
            calculator_text['class'] = 'kCrYT ip-address-div'
            calculator_text.string = 'Calculator'
            calculator_widget = html_soup.new_tag('div')
            calculator_widget.append(BeautifulSoup(widget_file, 'html.parser'))
            calculator_widget['class'] = 'kCrYT ip-text-div'
            widget_tag.append(calculator_text)
            widget_tag.append(calculator_widget)
            main_div.insert_before(widget_tag)
    return html_soup
