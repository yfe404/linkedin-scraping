import getopt, sys
import codecs

      

def usage():

    print("Usage: lkscrap [OPTION]...")
    print("Scrap Linkedin. Fetch information about people matching some keywords.")
    print("Get their name, current position and city area.")
    print()
    print("All arguments are optional and default values are provided, see below: ")
    print("  -n,                        Number of pages to scrap in the results search.")
    print("                             => default: 5")
    print()                             
    print("  -o, --output-file          write results in specified file.")
    print('                             => default: "./out.csv"')
    print()
    print("  -k, --keywords             keyword terms to search for (must be double quoted if multiple keywords")
    print("                             are given.")
    print('                             => default: "Software Engineer"')
    print()                             
    print("  -v  --verbose              Print results on stdin AND output file.")
    print()
    print()
    print("Author: Yann Feunteun <yfe@protonmail.com>")

def processCLI():
    # Default values
    output = "./output.csv"
    verbose = False
    keywords = "Software Engineer"
    number_of_pages = 5
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:k:n:v",
                                   ["help",
                                    "output-file",
                                    "keywords"])
    except getopt.GetoptError as err:
        print(err)  
        usage()
        sys.exit(2)
    
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output-file"):
            output = a
        elif o in ("-k", "--keywords"):
            keywords = a
        elif o == "-n":
            number_of_pages = a
        else:
            assert False, "unhandled option"

    return output, verbose, keywords, int(number_of_pages)


def printEndingMessage(nb_page, nb_people_retrieved):
    print("========== END ==========")
    print("Successfully scraped {} pages and retrieved {} peoples".format(nb_page, nb_people_retrieved))

def getOutputStream(filename):
    try:
        out = codecs.open(filename, 'w', encoding='utf-8')
        return out
    except Error as err:
        print(err)
        sys.exit(2)
