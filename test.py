from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from pymongo import MongoClient



options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


driver.get('https://www.indeed.com/')
search_box = driver.find_element(By.ID, 'text-input-what')
search_box.send_keys('Python developer')
search_box.submit()

job_listings = driver.find_elements(By.CLASS_NAME, 'jobsearch-SerpJobCard')

data = []
for job in job_listings:
    title = job.find_element(By.CLASS_NAME, 'title').text
    company = job.find_element(By.CLASS_NAME, 'company').text
    location = job.find_element(By.CLASS_NAME, 'location').text
    description = job.find_element(By.CLASS_NAME, 'summary').text

    data.append({
        'title': title,
        'company': company,
        'location': location,
        'description': description
    })

import mongoose from 'mongoose';
mongoose.connect("mongodb://localhost:27017/usersDB")
.then(() => {
    console.log("Connection of database is successful")
})
.catch((err) => {
    console.log(err)
})

driver.quit()