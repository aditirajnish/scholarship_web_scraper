
universities = ["University of Manitoba",
                "York University",
                "University of Saskatchewan",
                "University of British Columbia",
                "University of Calgary",
                "Dalhousie University",
                "University of Ottawa",
                "University of Waterloo",
                "Western University",
                "Memorial University",
                "McGill University",
                "Université Laval",
                "Queen's University",
                "McMaster University",
                "University of New Brunswick",
                "University of Victoria",
                "University of Toronto",
                "Université de Montréal",
                "University of Alberta",
                "Simon Fraser University"]

# empty string is for all years
years = ["", "2020", "2019", "2018", "2017",
         "2016", "2015", "2014", "2013", "2012"]


def verify_university(university):
    if university in universities:
        return True
    print("Invalid university. Must be one of the following:\n")
    for valid_university in universities:
        print(valid_university + "\n")
    print("----------------------------------------------------")


def verify_year(year):
    if year in years:
        return True
    print("Invalid year. Must be one of the following:")
    for valid_year in years:
        print(valid_year + "\n")
