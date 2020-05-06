import requests
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Website-ul target") # specificam prima optiune pe care o folosim
    parser.add_option("-s", "--wsub", dest="wsub", help="Calea catre wordlist-ul pentru a cauta subdomenii pentru target")
    parser.add_option("-d", "--wdir", dest="wdir", help="Calea catre wordlist-ul pentru a cauta directoare si fisiere pentru target")
    (option, arguments) = parser.parse_args()
    if not option.url:
        parser.error("Specifica te rog un url!. Foloseste --help pentru mai multe informatii")
    #elif not option.wsub:
        parser.error("Specifica te rog un wordlist pentru subdomenii! Foloseste --help pentru mai multe informatii")
    elif not option.wdir:
        parser.error("Specifica te rog o wordlist pentru directoare! Foloseste --help pentru mai multe informatii")
    else:
        return option

def request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response # returneaza 200 ceea ce inseamna ca totul este ok
    except Exception:
        pass

def read_subdomenies(url, wordlistPath):
    #target_url = "google.com"
    print("-->> Cautare subdomenii {}...".format(url))
    with open(wordlistPath, "r") as wordlistFile:
        # citim fisierul de este in wordlist
        for line in wordlistFile:
            word = line.strip() # ia toate spatiile goale si le da remove
            #pentru directories asta e singura linie care se schimba e cu /
            concatenate_url = word + '.' + url
            print("-->> Testare subdomeniu: {} ".format(concatenate_url), end="\r")
            result = request(concatenate_url)
            if result:
                print("-->> Subdomeniu gasit {}".format(concatenate_url))

def read_filesDirectories(url, wordlistPath):
    #target_url = "google.com"
    print("-->> Cautare foldere la {}...".format(url))
    with open(wordlistPath, "r") as wordlistFile:
        # citim fisierul de este in wordlist
        for line in wordlistFile:
            word = line.strip() # ia toate spatiile goale si le da remove
            #pentru directories asta e singura linie care se schimba e cu /
            concatenate_url = url + '/' + word
            print("-->> Testare cale: {} ".format(concatenate_url), end="\r")
            result = request(concatenate_url)
            if result:
                print("-->> Cale gasita {}".format(concatenate_url))


# se apeleaza functiile pe rand pentru a le 
option = get_arguments()
# prima data se cauta subdomenii
print("-->> Inceput cautare subdomenii.. Va rugam asteptati")
read_subdomenies(option.url,option.wsub)
print("-->> Sfarsit cautare subdomenii")
print("-->> Inceput cautare foldere.. Va rugam asteptati")
read_filesDirectories(option.url,option.wdir)
print("-->> Sfarsit cautare subdomenii")