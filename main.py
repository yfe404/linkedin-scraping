import os
import time
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from linkedin.linkedin import Linkedin, Person
from utils import utils


if __name__ == "__main__":
    
    output, verbose, keywords, number_of_pages = utils.processCLI()
    nb_page = 0
    nb_people_retrieved = 0
    out = utils.getOutputStream(output)
    linkedin = Linkedin()
    
    linkedin.connect()
    time.sleep(6)

    linkedin.search(keywords)
    time.sleep(5)

    while nb_page < number_of_pages:

        # Scrap current page
        linkedin.scrollBy(0, 10000)
        time.sleep(5)
        people = linkedin.getPeopleOnCurrentPage()

        # CSV header
        out.writelines("name;job;localisation\n")
        for pers in people:
            out.writelines("{};{};{}\n".format(pers.name, pers.job, pers.locale))
            if verbose:
                print ("{};{};{}".format(pers.name, pers.job, pers.locale))

        nb_page = nb_page + 1
        nb_people_retrieved = nb_people_retrieved + len(people)
        
        if linkedin.hasNext():
            linkedin.next()
            time.sleep(6)
        else:
            utils.printEndingMessage(nb_page, nb_people_retrieved)
            out.close()
            linkedin.close()
            exit(1)
            
    utils.printEndingMessage(nb_page, nb_people_retrieved)
    linkedin.close()
    out.close()
    exit(0)
