"""Code to get FSE Data"""
import time
import datetime
import requests
import xmltodict
import mysql.connector

def get_xml_data():
    """Turns FSE XML Data Into a Python Dict"""
    today = datetime.date.today()
    year = today.year
    month = today.month
    xml_url = f"https://server.fseconomy.net/data?userkey=4560EEB6103696AA&format=xml&query=payments&search=monthyear&readaccesskey=A25C03C0FA41A8EB&month={month}&year={year}"
    print(xml_url)
    response = requests.get(xml_url,timeout=20).content
    return response
def write_xml_file(xml_data0,file_name):
    "takes the content of a html request and writes it to a xml file"
    with open(f"{file_name}.xml", "wb") as foutput:
        foutput.write(xml_data0)
        foutput.close()
def sql_insert(db,fse_payid,fse_name,amount,acc_id):
    """says it on the tin"""
    cursor = db.cursor()
    sql = f"INSERT INTO `Deposits` (`ID`, `FSE_ID`, `Date_Time`, `FSE_Name`, `Amount`, `acc_id`) VALUES (NULL, '{fse_payid}', current_timestamp(), '{fse_name}', '{amount}', '{acc_id}')"
    cursor.execute(sql)
    db.commit()
x = 1
month_check_new = 8
month_check_old = 8
no_key_error_check = False
while x != 0:
    old_ammount = int(xmltodict.parse(open("file.xml").read())["PaymentsByMonthYear"]["@total"])
    month_check_new = datetime.date.today().month
    xml_data = get_xml_data()
    new_ammount = int(xmltodict.parse(xml_data)["PaymentsByMonthYear"]["@total"])
    try:
        pay_list = xmltodict.parse(xml_data)["PaymentsByMonthYear"]["Payment"]
    except KeyError:
        print("There was a key error probably because there were no payments")
        no_key_error_check = False
    else:
        no_key_error_check = True
    ## need to make exception for when there is an empty list^^^^^^^
    print("Awake!")
    if month_check_new != month_check_old and no_key_error_check:
        print("New Month!")
        mydb = mysql.connector.connect(host="srv557.hstgr.io",
                                       user="u457137351_evan",
                                       password="Kuma@mesa15",
                                       database="u457137351_main")
        for payments in reversed(pay_list):
            sql_insert(mydb,payments['Id'],payments['From'],payments['Amount'],payments['Comment'])
            print(payments['Id'],payments['From'],payments['Amount'],payments['Comment'])
    elif new_ammount != old_ammount and no_key_error_check:
        print("New Payment!")
        mydb = mysql.connector.connect(host="srv557.hstgr.io",
                                       user="u457137351_evan",
                                       password="Kuma@mesa15",
                                       database="u457137351_main")
        range_end = new_ammount - old_ammount
        write_xml_file(xml_data,"file")
        print(range_end)
        for i in reversed(range(0,range_end)):
            iter_list = pay_list[i]
            sql_insert(mydb,iter_list['Id'],iter_list['From'],iter_list['Amount'],iter_list['Comment'])
            print(iter_list['Id'],iter_list['From'],iter_list['Amount'],iter_list['Comment'])
            write_xml_file(xml_data,"file")
    else:
        print("Something went wrong or there are new payments!")
    print("sleeping now!")
    month_check_old = datetime.date.today().month
    time.sleep(60)




#write_xml_file(xml_data,"swag")
#data = xmltodict.parse(xml_data)



    ##payment_list = data["PaymentsByMonthYear"]["Payment"]

#mydb = mysql.connector.connect(
#    host="srv557.hstgr.io",
#    user="u457137351_evan",
#    password="Kuma@mesa15",
#    database="u457137351_main"
#)
#mycursor = mydb.cursor()
#swag = get_xml_data()["PaymentsByMonthYear"]["Payment"]
#total_payments = int(swag["PaymentsByMonthYear"]["@total"])
#swag = get_xml_data()["PaymentsByMonthYear"]["Payment"]
#set1=xmltodict.parse(open("file_copy.xml").read())
#set2=xmltodict.parse(open("file.xml").read())
#print(type(set2["PaymentsByMonthYear"]["@total"]))