from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
# below lines act as like our chrome tells website to iam controlled by software on top
# of opened website so these lines will keep hide it
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)



driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.naukri.com/")
time.sleep(2)


#this creates a list.
all_text_boxes = driver.find_elements(By.CLASS_NAME, "suggestor-input")
# print(all_text_boxes)

 # The first box [0] is Skills, the second box [1] is Location
skills_box = all_text_boxes[0]
location_box = all_text_boxes[1]

#  Type the Role & Location FIRST
skills_box.send_keys("data analyst")
time.sleep(1)
# location_box.send_keys("hyderabad")
# time.sleep(1)

# NOW Select Fresher Experience (Dropdowns last)

driver.find_element(By.CLASS_NAME, "qsbExperience").click()
time.sleep(2)
fresher_btn = driver.find_element(By.XPATH, "//*[text()='Fresher']")
driver.execute_script("arguments[0].click();", fresher_btn)
time.sleep(1)


driver.find_element(By.CLASS_NAME, "qsbSubmit").click()
time.sleep(5)
print("getting Data")
master_job_list = []

# we can use while for as many pages
for page_number in range(1, 3):
    print(f"\n--- Scraping Page {page_number} ---")

    #gets every job on page we are
    all_job_cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
    print(f"Found {len(all_job_cards)} jobs on this page.")


    for card in all_job_cards:
        try:
            job_title = card.find_element(By.CLASS_NAME, "title").text
            company_name = card.find_element(By.CLASS_NAME, "comp-name").get_attribute("title")
            experience = card.find_element(By.CLASS_NAME, "exp-wrap").text

            try:
                salary = card.find_element(By.CLASS_NAME, "sal-wrap").text
            except:
                salary = "Not Disclosed"

            try:
                location = card.find_element(By.CLASS_NAME, "loc-wrap").text
            except:
                location = "Not Specified"

            try:
                skill_tags = card.find_element(By.CLASS_NAME, "tags-gt").find_elements(By.TAG_NAME, "li")
                clean_skills_list = []
                for tag in skill_tags:
                    clean_skills_list.append(tag.text)
                skills = ", ".join(clean_skills_list)
            except:
                skills = "Not Specified"

            job_data = {
                "Target_Role": "Data Analyst",
                "Title": job_title,
                "Company": company_name,
                "Experience": experience,
                "Salary": salary,
                "Location": location,
                "Skills": skills
            }
            master_job_list.append(job_data)

        except Exception as e:
            pass


    try:
        #with the text "Next"
        next_button = driver.find_element(By.XPATH, "//span[text()='Next']")


        driver.execute_script("arguments[0].click();", next_button)

        print("Clicking Next, Waiting for the new page to load...")
        time.sleep(4)

    except Exception as e:
        print("No Next button found. We at the very end!")
        break


print("\n--- FINAL EXTRACTED DATA ---")
for job in master_job_list:
    print(job)

print(f"\nScraping Complete! We extracted {len(master_job_list)} total jobs.")

time.sleep(10)
driver.quit()
