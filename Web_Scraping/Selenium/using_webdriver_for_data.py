import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


print("Waking up the automated robot...")

# create box to store chrome settings
options = webdriver.ChromeOptions()

'''
below lines act as like our chrome tells website to iam controlled by software on top
of opened website so these lines will keep hide it
'''
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# --headless is used to make the browser INVISIBLE and fast
options.add_argument('--headless')

# headless now works
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)
driver.maximize_window()
# below all roles will search our scraper
target_roles = ["Java Developer", "Full Stack Developer", "Software Engineer", "Frontend Developer",
                 "Data Engineer", "Data Engineering","react js developer",
                 "node js developer","react.js", "node.js"]


master_job_list = []


for role in target_roles:

    print(f"SEARCHING THE ROLE: {role.upper()}")


    driver.get("https://www.naukri.com/")
    time.sleep(3)

    try:
        # type role in search box
        all_text_boxes = driver.find_elements(By.CLASS_NAME, "suggestor-input")
        skills_box = all_text_boxes[0]
        skills_box.send_keys(role)
        time.sleep(1)

        #Select Fresher Experience
        driver.find_element(By.CLASS_NAME, "qsbExperience").click()
        time.sleep(2)
        '''
        why used .execute_script is for scroll down and select fresher its changing layout so 
        we just used force click on fresher by .execute_scrript
        '''
        fresher_btn = driver.find_element(By.XPATH, "//*[text()='Fresher']")
        driver.execute_script("arguments[0].click();", fresher_btn)
        time.sleep(1)

        #Click Search
        driver.find_element(By.CLASS_NAME, "qsbSubmit").click()
        print(f"Searching... Waiting 5 seconds for Page 1 of {role} to load...")
        time.sleep(5)

    except Exception as e:
        print(f"Something went wrong searching for {role}. Skipping to next role...")
        continue  # If the homepage breaks, skip to the next job title!


    page_number = 1
        while True:
        print(f"\n--- Scraping Page {page_number} for {role} ---")

        # get every job on page we are!
        all_job_cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
        print(f"Found {len(all_job_cards)} jobs on this page. Extracting...")

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
                    "Target_Role": role,
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

        # CLICKING THE NEXT BUTTON
        try:
            '''
                   why used .execute_script is for search next and click next cause of too many tags inbetween so 
                   we just used force click on next by .execute_scrript
                   '''
            next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
            driver.execute_script("arguments[0].click();", next_button)
            print("Clicking Next... Waiting 4 seconds for new page to load...")
            time.sleep(5)
            page_number += 1

        except Exception as e:
            print(f"No Next button found. We scraped all available pages for {role}!")
            break  #get out of the page loop, moves to the next role!


print(f"SCRAPING COMPLETELY FINISHEd!")
print(f"We successfully extracted {len(master_job_list)} total jobs across our target roles: {target_roles}.")


print("Converting data and saving to CSV...")


df = pd.DataFrame(master_job_list)


df.to_csv("other_roles.csv", index=False)

print("SUCCESS! Check your PyCharm folder for 'master_jobs_dataset.csv'.")
print("You are now ready for the Pandas cleanup phase!")

# close the robot
driver.quit()
