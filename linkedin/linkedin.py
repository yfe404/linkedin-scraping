from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import os
import time


class Person():
    def __init__(self, name, job, locale):
        self.name = name
        self.job = job
        self.locale = locale

        
class Linkedin(webdriver.Firefox):
    def connect(self, user=os.environ['USER_LINKEDIN'], password=os.environ['PASSWORD_LINKEDIN']):
        self.get("https://www.linkedin.com/login")
        email_field = self.find_element_by_id("username")
        email_field.send_keys(user)
        pass_field = self.find_element_by_id("password")
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.ENTER)
    
    def search(self, keywords):
        self.get("https://www.linkedin.com/search/results/people/?keywords=" + keywords +"&origin=SWITCH_SEARCH_VERTICAL")


    def scrollBy(self, begin, end):
        self.execute_script("window.scrollBy({}, {})".format(begin, end))
        

    def getPeopleOnCurrentPage(self):
        list_of_people = []
        names = self.find_elements_by_class_name("actor-name")
        jobs = self.find_elements_by_class_name("subline-level-1")
        localisations = self.find_elements_by_class_name("subline-level-2")

        for i in range(len(names)):
            name = names[i].text.replace(';', ',')
            job = jobs[i].text.replace(';', ',')
            locale  = localisations[i].text.replace(';', ',')

            person = Person(name, job, locale)
            list_of_people.append(person)

        return list_of_people


    def hasNext(self):
        try:
            button_next = self.find_elements_by_class_name("next")[0]
            button_next.text
            return True
        except IndexError:
            return False

    
    def next(self):
        button_next = self.find_elements_by_class_name("next")[0]
        button_next.click()

    def close(self):
        self.quit()
        
