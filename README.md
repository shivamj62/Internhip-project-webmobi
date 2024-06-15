# Conference Data Scraper

This project is a web scraper for extracting information about B2B conferences from the Quarry website. The extracted data is saved in a JSON file.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required Python packages**:
    ```sh
    pip install selenium
    ```

3. **Download Chrome WebDriver**:
    - Ensure you have Google Chrome installed.
    - Download the Chrome WebDriver that matches your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Add the Chrome WebDriver to your system PATH.

## Usage

1. **Run the script**:
    ```sh
    python scrape_conferences.py
    ```

2. **Output**:
    - The script will scrape the conference data from the specified URL.
    - The data will be saved in a file named `event_data.json` in the current directory.

## Script Explanation

The script performs the following tasks:

1. **Initialize WebDriver**: Opens a Chrome browser and navigates to the specified URL.
2. **Scrape Data**: Extracts conference information such as Name, Date, Location, Website URL, Description, and Registration Link.
3. **Save Data**: Writes the extracted data to a JSON file.

## Example

Here's an example of the JSON data structure that will be saved:

```json
{
    "Name": ["Conference 1", "Conference 2"],
    "Date": ["January 1, 2024", "February 15, 2024"],
    "Location": ["New York, NY", "San Francisco, CA"],
    "WebsiteURL": ["https://example.com/conference1", "https://example.com/conference2"],
    "Description": ["Description of Conference 1", "Description of Conference 2"],
    "RegistrationLink": ["https://example.com/register1", "https://example.com/register2"]
}
