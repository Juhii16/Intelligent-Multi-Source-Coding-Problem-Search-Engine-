# Import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Chrome options to run headless (without a visible browser window)
chrome_options = Options()
chrome_options.add_argument("--headless")

# Define the chromedriver service with options
s = Service(ChromeDriverManager().install(), chrome_options=chrome_options)

# Instantiate the webdriver
driver = webdriver.Chrome(service=s)

# The base URL for the pages to scrape
page_URL = "https://leetcode.com/problemset/all/?page="

# Function to get all the 'a' tags from a given URL
def get_a_tags(url):
    # Load the URL in the browser
    driver.get(url)
    
    # Wait for page to load (you can adjust the time if needed)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    
    # Get the page source
    page_source = driver.page_source
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Find all the 'a' elements on the page
    links = soup.find_all('a')
    
    ans = []
    
    # Iterate over each 'a' element
    for link in links:
        href = link.get('href')
        # Check if '/problems/' is in the href of the 'a' element
        if href and "/problems/" in href:
            # If it is, append it to the list of links
            ans.append(href)
    
    # Remove duplicate links using set
    ans = list(set(ans))
    
    return ans

# List to store the final list of links
my_ans = []

# Loop through the pages you're interested in (in this case, pages 1-54)
for i in range(1, 55):
    # Call the function to get the 'a' tags from each page and append the results to your list
    my_ans += get_a_tags(page_URL + str(i))

# Remove any duplicates that might have been introduced in the process
my_ans = list(set(my_ans))

# Open a file to write the results to
with open('lc.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in my_ans:
        # Write each link to the file, followed by a newline
        f.write(j + '\n')

# Print the total number of unique links found
print("Total unique links found:", len(my_ans))

# Close the browser
driver.quit()
