import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
edge_options = Options()
edge_options.set_capability("ms:inPrivate", True)


def enter_user_data(driver, username, password):
    radio_button = driver.find_element(By.ID, 'usertype_1')
    radio_button.click()
    username_input = driver.find_element(By.ID, "name")
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    submit_button = driver.find_element(By.XPATH, '//input[@id="login_btn"]')
    submit_button.click()
    time.sleep(4)

def action_taken_highlighter(driver,element):
        highlight_js = """
            var element = arguments[0];
            var original_style = element.getAttribute('style');
            element.setAttribute('style', original_style + '; background: yellow; border: 2px solid red;');
            setTimeout(function(){
                element.setAttribute('style', original_style);
            }, 1000);
        """
        driver.execute_script(highlight_js, element)

def login(driver):
    # Go to the login page
    driver.get("http://std.eng.alexu.edu.eg/static/index.html")

    # Wait for the login page to load
    wait = WebDriverWait(driver, 0.1)
    login_form_address = (By.XPATH, '/html/body/div/div')
    wait.until(EC.presence_of_element_located(login_form_address))

def convert_to_arabic_text(number):
    # Create a dictionary of numbers to Arabic text
    switch_case = {
        1: "الأولى",
        2: "الثانية",
        3: "الثالثة",
        4: "الرابعة",
    }
    # Return the Arabic text for the number
    return switch_case.get(number, "")

def get_term(driver,term):
    el_term = driver.find_element(By.ID, str(term-1))
    el_term.click()
    time.sleep(1)

def register_courses(driver, courses_to_register):
    try:
        time.sleep(2)
        table = driver.find_element(By.ID,'tblLvl35.16.10.')
        # Loop through the courses
        for course in courses_to_register:
                term = int(course['Term'])
                get_term(driver,term)

                # Check if the 'course' key exists
                if 'course' in course:
                    course_name = course['course']
                    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{course_name}')]")
                    action_taken_highlighter(driver,element)
                    time.sleep(1)

                # Check if the 'Group Number' key exists
                if 'Group Number' in course:
                    group_number=convert_to_arabic_text(int(course['Group Number']))
                    next_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{group_number}')]")



                    # print(next_element)
                else:
                    group_number = 0

                # Check if the 'Section Number' key exists
                if 'Section Number' in course:
                    section_number = int(course['Section Number'])
                else:
                    section_number = 0

                # Check if the 'Lab Number' key exists
                if 'Lab Number' in course:
                    lab_number = int(course['Lab Number'])
                else:
                    lab_number = 0

    except Exception as e:
        print("An error occurred:", e)

def handle_alert(driver):
    try:
        time.sleep(0.1)
        accept_error_button = driver.find_element(By.ID, 'popup_ok')
        accept_error_button.click()
        navigate_to_tasgeel(driver)
    except Exception as e:
        print("An error occurred:", e)

def save(driver):
    try:
        submit_button = driver.find_element(By.ID, 'SavestuRegFrm')
        submit_button.click()
    except selenium.common.exceptions.NoSuchElementException as err:
        print(err)
        print("Error: Could not Save")
        time.sleep(20)
        input("error: Could not Save")

def navigate_to_tasgeel(driver):
    try:
        time.sleep(1)
        el_tasgeel = driver.find_element(
            By.ID, 'timetable')
        el_tasgeel.click()
        time.sleep(1)
    except selenium.common.exceptions.NoSuchElementException as err:
        handle_alert(driver)
        navigate_to_tasgeel(driver)
        print (err)
        print("Error: Could not open the login page")
        time.sleep(20)

def mainloop(username, password,courses_to_register):
    try:
        driver = webdriver.Edge( options=edge_options)
        login(driver)
        enter_user_data(driver, username, password)
        navigate_to_tasgeel(driver)
        register_courses(driver, courses_to_register)
        # save(driver)

    except Exception as err:
        print(err)
        print("Error: Could not complete the registration process....")
        print ("Retrying...")
        driver.quit()
        # Note: You can make it retry until it succeeds
        # mainloop(username, password,courses_to_register)
        return ("Success")



# NOTE: This is an example of how to use the mainloop function
# You can uncomment the following lines to test it
# You need to provide the username, password, and the courses to register
# Fill out the courses_to_register array exactly as the example below



# courses_to_register = [
#     {
#         'course': 'Computer and Network Security',
#         'Term': '10',
#         'Group Number': '1',
#         'Section Number': '1'
#     },
#     {
#         'course': 'Specifications and Feasibility Studies',
#         'Term': '9',
#         'Group Number': '1',
#     },
#     {
#         'course': 'Communication Systems',
#         'Term': '9',
#         'Group Number': '1',
#         'Section Number': '1',
#         'Lab Number': '1'
#     }
# ]

# username = "XXXX"
# password = "XXXXXXXXXX"
# mainloop(username, password,courses_to_register)
