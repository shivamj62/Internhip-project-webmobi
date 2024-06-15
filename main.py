from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()
website_url = "https://quarry.com/better-practices/find-your-top-b2b-conferences"
driver.get(website_url)
time.sleep(5)
my_dict = {
    'Name': [],
    'Date': [],
    'Location': [],
    'WebsiteURL': [],
    'Description': [],
    'RegistrationLink': []
}

event_cards = driver.find_elements(By.CLASS_NAME, "confCard")

for card in event_cards:
    try:
        name = card.find_element(By.CLASS_NAME, "v-card__title").text
        date_location = card.find_element(By.TAG_NAME, "h4").text
        date, location = date_location.split('•')
        website_url = card.find_element(By.TAG_NAME, "a").get_attribute("href")
        description = card.find_element(By.CLASS_NAME, "v-card__text").find_element(By.TAG_NAME, "p").text
        try:
            registration_link = card.find_element(By.CLASS_NAME, "hashtag").find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            registration_link = None

        my_dict['Name'].append(name)
        my_dict['Date'].append(date.strip())
        my_dict['Location'].append(location.strip())
        my_dict['WebsiteURL'].append(website_url)
        my_dict['Description'].append(description)
        my_dict['RegistrationLink'].append(registration_link)

    except Exception as e:
        print(f"An error occurred: {e}")


driver.quit()

# Convert dictionary to JSON string
json_data = json.dumps(my_dict, indent=4)  # Add indent for readability

# Print the JSON data
print(json_data)

# You can also write the JSON data to a file:
# with open('events.json', 'w') as outfile:
#     json.dump(my_dict, outfile)
