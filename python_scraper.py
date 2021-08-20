import requests
from bs4 import BeautifulSoup
from itertools import islice
from time import sleep
import threading

base_url = "https://www.google.com/search?q="
contact_details = "+contact+details"


def company_site(comp):
    print("\nStarting here\n")
    comp = comp[:-1]
    comp_and_link = set()
    comp_and_link.add(comp)
    comp_and_link.add("no")
    if "& " in comp:
        comp = comp.replace("& ", "")
    comp = comp.replace(" ", "+")
    comp = comp.lower()

    # print(comp)
    final_url = base_url + comp + contact_details
    print(final_url)
    page = requests.get(final_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)

    links = soup.find_all('a')
    # print(len(links))

    tags = comp.split("+")
    if "ltd" in tags:
        if "ltd." in tags:
            tags.remove("ltd.")
        else:
            tags.remove("ltd")
    elif "limited" in tags:
        tags.remove("limited")

    tags.append("contact")
    tags.append("us")

    found_link = False

    for link in links:
        print(link["href"])
        score = 0
        for tag in tags:
            if tag in link["href"]:
                score += 1
        # print(score)
        # if score > 0 and "search?q=" not in link["href"] and "url?q=" in link["href"] and "contact" in link["href"]:
        if score > 1 and "search?q=" not in link["href"] and "url?q=" in link["href"]:
            found_link = True
            # print(link["href"])
            # print(score)

    if found_link:
        comp_and_link.remove("no")
        comp_and_link.add("yes")
    else:
        print(comp_and_link)
        # pass


def open_file():
    with open("doc.txt", "r") as company_list:
        # print(dir(company_list))
        # print(company_list[0])
        # print(company_list[0])

        x = 0

        for company in company_list:
            # print(company.strip("\n"))
            # print(type(company.strip("\n")))
            # print(len(company.strip("\n")))
            # break
            # print("%s- " % company.strip("\n"))
            # t1 = threading.Thread(target=company_site, args=(company,))
            # t1.start()
            if x > 10:
                break
            x += 1
            # threading.enumerate()
            # if threading.activeCount() > 20:
            #     t1.join()
            # t1.join()
            # print(threading.activeCount())
            company_site(company)


open_file()
