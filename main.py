
import requests
from bs4 import BeautifulSoup
from verify import verify_university, verify_year


def write_file(information, university, year):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Writes information to a text file. Title contains the 
        university's name and the year (both are arguments passed 
        into the function).
        Name of university is formatted and name of text file is 
        formatted using an f string.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    university = university.lower().replace(" ", "_")

    with open(f"schulich_text_files/schulich_{university}_{year}.txt", "w") as file:
        file.write(information)


def get_page_info(link_suffix, university):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Scrapes a leader's profile page (using the link suffix 
        passed into the function) to obtain the university which 
        selected them as a recipient. If the leader's university 
        matches the university argument passed into the function, 
        the leader's name and their program's name are obtained.  
        
        Requests leader's profile page using link suffix and 
        parses the content using BeautifulSoup. Two <div> elements 
        and one <h1> element (each with a unique, identifying class) 
        contain the name of the university, the leader, and the 
        program. Finds elements and stores the text inside of them.
        
        Returns the leader's name and program name (in a formatted 
        string), if the leader's university matches the university 
        argument. Otherwise, returns None.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    page = requests.get(f"https://www.schulichleaders.com{link_suffix}", verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    university_div = soup.find("div", class_="person--selected-by")
    university_name = university_div.text

    if university_name == university:

        leader_heading = soup.find("h1", class_="person--title")
        leader_name = leader_heading.text

        program_div = soup.find("div", class_="person--program")
        program_name = program_div.text

        return f"Name: {leader_name}\nProgram: {program_name}"


def get_link_suffixes(year):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Scrapes main page for href link suffixes (to be appended
        to the domain), each of which go to a leader's profile.
        Example of link suffix: '/first_name-last_name'.

        Requests main page and parses the content using 
        BeautifulSoup. <span> elements (with a unique, 
        identifying class) contain these links. Finds all 
        of these <span> elements, finds the <a> tag nested 
        within each <span>, and gets the link suffix inside 
        the href attribute.

        Stores link suffixes (type string) inside of a list 
        and returns this list.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    page = requests.get(f"https://www.schulichleaders.com/scholars/{year}#slide-scholars", verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    spans = soup.find_all("span", class_="field-content")
    anchors = [name.find("a") for name in spans]
    link_suffixes = [anchor.get("href") for anchor in anchors if anchor]

    return link_suffixes


def main(year, university):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Initialize a list to store each leader's information
        in formatted strings.
        Get the link suffixes and loop through the corresponding
        profile pages. If the leader received a scholarship from
        the university passed into the function, append the 
        leader's information to the list.
        Join all of the list elements into one string and write 
        it to the file.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    all_information = []

    link_suffixes = get_link_suffixes(year)

    for link_suffix in link_suffixes:
        information = get_page_info(link_suffix, university)
        if information:
            all_information.append(information)

    file_information = "\n\n".join(all_information)

    write_file(file_information, university, year)


if __name__ == "__main__":

    # to get information for all years, set year = "" (an empty string)
    year = "2020"
    university = "University of British Columbia"

    valid_university = verify_university(university)
    valid_year = verify_year(year)

    # main() is only called if year and university are valid
    if valid_university and valid_year:
        main(year, university)
