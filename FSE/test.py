import xmltodict
range_start = 0 #old
range_end = 15 #new
old_ammount = int(xmltodict.parse(open("file.xml").read())["PaymentsByMonthYear"]["@total"])
xml_file = xmltodict.parse(open("file.xml").read())["PaymentsByMonthYear"]["Payment"]
#print(old_ammount)
#print(xml_file[2])
for i in reversed(range(range_start,range_end)):
    print(i)