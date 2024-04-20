import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    # URL of the website
    url = 'https://dharani.telangana.gov.in/knowLandStatus'

    # Parameters for the POST request
    data = {
        'searchType': 'Survey',
        'criteria': 'Survey',
        'district': district,
        'mandal': mandal,
        'village': village
    }

    # Sending a POST request to the website
    response = requests.post(url, data=data)

    # Parsing the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding the survey number elements
    survey_numbers = soup.find_all('select', {'name': 'surveyNumber'})[0].find_all('option')

    # Extracting survey numbers
    survey_numbers_list = [survey_number.text.strip() for survey_number in survey_numbers]

    return survey_numbers_list

# Example usage
district = 'Your District'
mandal = 'Your Mandal'
village = 'Your Village'

survey_numbers = get_survey_numbers(district, mandal, village)
print("Survey Numbers for {} district, {} mandal, and {} village:".format(district, mandal, village))
print(survey_numbers)
