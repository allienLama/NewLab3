import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from getpass import getpass

# Döngünü başlatmaq üçün bir dəyişən
successful_login = False

while not successful_login:
    # 1. İstifadəçidən giriş məlumatlarını alırıq
    user_input = input("İstifadəçi adınızı daxil edin: ")
    
    # Şifrəni *** ilə gizlətmək üçün getpass istifadə edirik
    password_input = getpass("Şifrənizi daxil edin: ")
    
    try:
        # 2. Firefox brauzerini başlatmaq
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # 3. Sayta daxil olma
        driver.get('https://sso.aztu.edu.az/')

        # Giriş etmək üçün username və password sahələrinin adları
        username = driver.find_element(By.NAME, "UserId")
        password = driver.find_element(By.NAME, "Password")

        # 4. İstifadəçi adı və şifrəni daxil edirik
        username.send_keys(user_input)  # Konsoldan alınan istifadəçi adı
        password.send_keys(password_input)  # Konsoldan alınan şifrə

        # Giriş düyməsini tapırıq və klikləyirik
        login_button = driver.find_element(By.XPATH, '/html/body/section/div/div[1]/div/div/form/div[3]/button')
        login_button.click()

        # Saytın yüklənməsini gözləyirik
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/aside[1]/div/nav/ul/li[1]/a')))

        # Uğurlu giriş zamanı
        print("Giriş uğurludur. Davam edilir...")
        successful_login = True  # Döngünü dayandırırıq

        # "Tələbəyə keçid" düyməsini klikləyirik
        telebe_kecid_button = driver.find_element(By.XPATH, '/html/body/div/aside[1]/div/nav/ul/li[1]/a')
        telebe_kecid_button.click()

        # "Fənlər" düyməsini klik etmədən əvvəl yüklənmə göstəricisinin yox olmasını gözləyirik
        wait.until(EC.invisibility_of_element_located((By.ID, "loader")))

        # "Fənlər" düyməsini klikləyirik
        fenler_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu6i"]/a/span[2]/span')))
        fenler_button.click()

        # "Python programlaşdırma dili" düyməsini seçirik
        python_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu6i"]/ul/li[3]/a')))
        python_button.click()

        # Wait for loader to disappear again before interacting
        wait.until(EC.invisibility_of_element_located((By.ID, "loader")))

        # Now make sure the 'Davamiyyet' button is visible and clickable
        try:
            # Wait for the button to be clickable
            davamiyyet_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_content"]/div[1]/div/div[2]/a[7]')))
            
            # Retry clicking if the element is obstructed (navbar, etc.)
            try:
                davamiyyet_button.click()
            except ElementClickInterceptedException:
                print("Click was intercepted by another element, retrying...")
                # Wait for any possible obstruction like navbar to disappear
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.navbar-custom')))
                time.sleep(1)  # Give a brief time for UI to stabilize
                # Retry clicking
                davamiyyet_button.click()

            # Allow page to load
            time.sleep(5)  # Adjust as needed

            # Ensure attendance data section is fully loaded
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'attend-label')))  # This class may vary

            # Use BeautifulSoup to scrape data after page is loaded
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Extract dates and attendance status
            dates = soup.find_all('font', {'style': 'font-size:11px;'})
            attendance = soup.find_all('span', {'class': 'attend-label'})

            # Check if data is found
            if dates and attendance:
                # Open the log file in append mode
                with open("log_davamiyyet.txt", "a") as log_file:
                    for date, attend in zip(dates, attendance):
                        date_text = date.get_text().strip()
                        attendance_text = attend.get_text().strip()
                        if attendance_text == "i/e":
                            status = "Tələbə dərsdə iştirak edib."
                        elif attendance_text == "q/b":
                            status = "Tələbə dərsdə iştirak etməyib."
                        else:
                            status = f"Naməlum status: {attendance_text}"
                        
                        # Write the information to the log file
                        log_file.write(f"Tarix: {date_text}, Status: {status}\n")
                
                print("Davamiyyet məlumatları 'log_davamiyyet.txt' faylında yazıldı.")
            else:
                print("Davamiyyet məlumatları tapılmadı.")

        except TimeoutException:
            print("Davamiyyet bölməsi tapılmadı və ya zaman aşımı oldu.")
            driver.quit()
            continue

    except TimeoutException:
        # Giriş uğursuz olarsa
        print("İstifadəçi adı və ya şifrə yanlışdır. Yenidən cəhd edin.")
    finally:
        # Brauzeri bağlayırıq
        driver.quit()
