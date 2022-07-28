import csv
def write_into_csv(info_list):
    with open('stud_info_csv', 'a', newline='') as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-Mail_ID"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    stud_num = 1
    while(condition):
        stud_info = input("Enter student information for student #{} in the following format (Name Age Contact_Number E-Mail_ID) : ".format(stud_num))
        print("Entered information: " + stud_info)

        #split function
        stud_info_list = stud_info.split(' ')
        print("Entered split up information is : " + str(stud_info_list))

        print("\nThe entered information is -\nName: {}\nAge: {}\nContact number: {}\nE-Mail_ID: {}\n".format(stud_info_list[0], stud_info_list[1], stud_info_list[2], stud_info_list[3]))
        ch_check = input("Is the entered information correct? (yes/no): ")
        if ch_check== "yes":
            write_into_csv(stud_info_list)
            condition_check = input("Enter (yes/no) if you want to enter information for another student : ")
            if condition_check == "yes":
                condition = True
                stud_num= stud_num + 1
            elif condition_check == "no":
                condition = False
        elif ch_check== "no":
            print("\nPlease re-enter the values!")
