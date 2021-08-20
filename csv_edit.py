import os

path = os.getcwd()

csv_path = path + "\\files\\"

old_file = csv_path + "LCP.csv"
new_file = csv_path + "LCP_edited.csv"

with open(old_file, "r") as rf:
    with open(new_file, "w") as wf:
        contacts = rf.readlines()
        for contact in contacts:
            if "Name,Phone," in contact:
                wf.write(contact)
            else:
                wf.write("XX "+contact)

print(csv_path)
