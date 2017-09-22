# -*- coding: utf-8 -*-
"""
Generate CSV files with fake data. Based on the Faker Python package.
"""
import codecs
import csv
import copy
import argparse
import sys
import inspect
import faker
import random
from datetime import datetime, timedelta

__version__ = '0.1.0'


objMap={"customer":["first_name","last_name","company"],"contactPerson":["first_name","last_name","phone_number","cell_phone","email_address"],
        "lead":["company","first_name","last_name","phone_number","cell_phone"], "campaign":["campaign_name","cost"],"warehouse":["warehouse_name"],
        "product":["product_name"], "warehouse":["warehouse_name"], "UoM":["UoM"], "targetGroup":[],"batch":["batch_number"],"serial":["serial_code"], "salesOrder":["unit_price","quantity","past_date"],"goodReceipt":["quantity"],
        "salesOpportunity":["unit_price","quantity","past_date"]
       }



def object_methods(object_method):
    """Validate list of provider methods."""
    object_list=[]
    for kv in object_method.split(","):
        k,v = kv.split("=")
        object_list.append(k)
        if k not in objMap.keys():
            raise argparse.ArgumentTypeError('Invalid fake object {0}. For a list of all available fakes, run with --list-fakes'.format(k))
    if "salesOrder" in object_list and not all(i in object_list for i in ["customer","product","warehouse"]):
        raise argparse.ArgumentTypeError('Fake sales orders need "customer, product, warehouse", please add these three objects into your bo_pairs arguments like "--bo_pairs customer=10,product=10,warehouse=5,salesOrder=10"')   
    if "salesOpportunity" in object_list and not all(i in object_list for i in ["customer","product"]):
        raise argparse.ArgumentTypeError('Fake sales opportunity need "customer, product", please add these twi objects into your bo_pairs arguments like "--bo_pairs customer=10,product=10,salesOpportunity=10"')   

    return object_method


def show_fakeObjects():
    """Show a list of all available object methods."""
    print objMap.keys()


def provider_methods(provider_method):
    """Validate list of provider methods."""
    fake = faker.Factory.create()
    if provider_method not in dir(fake):
        raise argparse.ArgumentTypeError('Invalid fake {0}. For a list of all available fakes, run with --list-fakes'
                                         .format(provider_method))
    return provider_method


def show_fakes():
    """Show a list of all available provider methods."""
    # TODO: There must be a better way to do that.
    fake = faker.Factory.create()
    fakes = []
    providers_list = fake.get_providers()
    for provider in providers_list:
        provider_list = inspect.getmembers(provider, predicate=inspect.ismethod)
        for method_name, method_value in provider_list:
            if not method_name.startswith('_'):
                fakes.append(method_name)

    """Print a sorted list of unique methods."""
    print(" ".join(sorted(list(set(fakes)))))
    print("")
    print("For details see http://fake-factory.readthedocs.io/en/latest/providers.html")

def generate_csv_file(fake,fakeObject,rows,locale):
    with open('%s.csv'%fakeObject, 'wb') as csvfile:
        if locale == "zh_CN":
            csvfile.write(codecs.BOM_UTF8)
        writer = csv.writer(csvfile)
        properties=objMap[fakeObject]
        writer.writerow(["-"]+properties) if locale == "zh_CN" else  writer.writerow(properties)
        for r in range(rows):
            row = []
            for provider_method in properties:
                if sys.version_info >= (3, 0):
                    cell = getattr(fake, provider_method)()
                else:
                    cell = unicode(getattr(fake, provider_method)()).encode("utf-8")
                row.append(cell)
            writer.writerow(["-"]+row) if locale == "zh_CN" else  writer.writerow(row)

def main():


    parser = argparse.ArgumentParser(description='Generate CSV files with fake data.')
    '''
    parser.add_argument(metavar="FAKE", dest='methods', type=provider_methods, nargs='*',
                        default=['name', 'job', 'state'],
                        help="The name of the fake(s) to use to generate output, separated by space. Will also be used "
                             "as column headers. If omitted, the fakes 'name job state' will be used.")
    '''

    my_dict = {}
    class StoreDictKeyPair(argparse.Action):
         def __call__(self, parser, namespace, values, option_string=None):
             for kv in values.split(","):
                 k,v = kv.split("=")
                 my_dict[k] = int(v)
             setattr(namespace, self.dest, my_dict)

    parser.add_argument('--bo_pairs', dest="objects_dict", type=object_methods,action=StoreDictKeyPair,default={"customer":50,"contactPerson":30,"lead":10,"targetGroup":10,"campaign":10,
                        "product":80,"batch":20,"serial":20,"UoM":15,"warehouse":10,"salesOrder":100,"goodReceipt":20,"salesOpportunity":80}, metavar="customer=10,product=10...",
                        help="The supported bos and related volume data will be geneated, please run with --list-fakes to see supported bos. ")


    #parser.add_argument(dest='methods', type=object_methods, nargs='*', default=['customer', 'product', 'salesOrder','warehouse'],help="The name of the fake(s) to use to generate objects, separated by space.")

    parser.add_argument('-f', '--list-fakes', action='store_true',
                        help='Show a list of all available fake bos.')
    #parser.add_argument('-r', '--rows', type=int, default=10,help='Number of rows to generate. If omitted it defaults to 10.')
    parser.add_argument('-l', '--locale', type=str,
                        help="Locale to use. Examples: 'en_US', 'zh_CN'.")
    #parser.add_argument('-s', '--seed', type=str,help="Seed to use. Generated result will be the same when called with the same seed.")
    #parser.add_argument('-n', '--no-headers-row', dest='headers', action='store_false',help='Do not output columns headers.')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args()


    if args.list_fakes:
        show_fakeObjects()
        exit(0)


    fake = faker.Factory.create(args.locale)
        
    if args.locale == "zh_CN":
        fake2 = faker.Factory.create("en_US")
    else:
        fake2 = faker.Factory.create("zh_CN")

    if "customer" in args.objects_dict.keys():
        #generate_csv_file(fake,"customer",args.objects_dict["customer"],args.locale)
        with open('customer.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvfile)
            properties=objMap["customer"]
            writer.writerow(["-"]+properties+["customer_type"]) if args.locale == "zh_CN" else  writer.writerow(properties+["customer_type"])
            for r in range(args.objects_dict["customer"]):
                row = []
                customer_type = random.choice(["INDIVIDUAL_CUSTOMER","CORPORATE_CUSTOMER"])
                for provider_method in properties:
                    if customer_type == "INDIVIDUAL_CUSTOMER" and provider_method != "company":
                        cell = unicode(getattr(fake, provider_method)()).encode("utf-8") 
                    elif customer_type == "CORPORATE_CUSTOMER" and provider_method == "company":
                        cell = unicode(getattr(fake, provider_method)()).encode("utf-8") 
                    else:
                        cell = ""    
                    row.append(cell)
                row.append(customer_type)
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

    if "contactPerson" in args.objects_dict.keys():
        #generate_csv_file(fake,"customer",args.objects_dict["customer"],args.locale)
        customer_data = list(csv.reader(open("customer.csv", "r")))
        with open('contactPerson.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)
                customer_type_index = 4
                corporate_name_index = 3
            else:
                customer_type_index = 3
                corporate_name_index = 2   
            writer = csv.writer(csvfile)
            properties=objMap["contactPerson"]
            writer.writerow(["-"]+["corporate_name"]+properties) if args.locale == "zh_CN" else  writer.writerow(["corporate_name"]+properties)
            corporate_index=0
            for r in range(args.objects_dict["contactPerson"]):
                row = []               
                if customer_data[r+1][customer_type_index] == "CORPORATE_CUSTOMER":
                    row.append(customer_data[r+1][corporate_name_index])
                    for provider_method in properties:
                        if args.locale == "zh_CN" and provider_method == "email_address":
                            cell = unicode(getattr(fake2, provider_method)()).encode("utf-8")
                        else:
                            cell = unicode(getattr(fake, provider_method)()).encode("utf-8")
                        row.append(cell)
                    writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)
                    corporate_index += 1
            if corporate_index < args.objects_dict["contactPerson"]:
                for i in range(args.objects_dict["contactPerson"]-corporate_index):
                    row2 = [] 
                    row2.append("null")
                    for provider_method in properties:
                        if args.locale == "zh_CN" and provider_method == "email_address":
                            cell = unicode(getattr(fake2, provider_method)()).encode("utf-8")
                        else:
                            cell = unicode(getattr(fake, provider_method)()).encode("utf-8")
                        row2.append(cell)
                    writer.writerow(["-"]+row2) if args.locale == "zh_CN" else  writer.writerow(row2)

    if "lead" in args.objects_dict.keys():
        #generate_csv_file(fake,"customer",args.objects_dict["customer"],args.locale)
        with open('lead.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvfile)
            properties=objMap["lead"]
            writer.writerow(["-"]+properties+["Temperature","status"]) if args.locale == "zh_CN" else  writer.writerow(properties+["Temperature","status"])
            for r in range(args.objects_dict["lead"]):
                row = []
                for provider_method in properties:
                    cell = unicode(getattr(fake, provider_method)()).encode("utf-8") 
                    row.append(cell)
                #Temperature + status
                row.append(random.choice(["Cold","Warm","Hot"]))
                row.append(random.choice(["Open","In_process","Closed"]))
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

    if "targetGroup" in args.objects_dict.keys():
        #generate_csv_file(fake,"customer",args.objects_dict["customer"],args.locale)
        with open('targetGroup.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvfile)
            writer.writerow(["-"]+["targetGroup_name","description"]) if args.locale == "zh_CN" else  writer.writerow(["targetGroup_name","description"])
            for r in range(args.objects_dict["targetGroup"]):
                row = []
                if args.locale == "zh_CN":   
                    cell = unicode(u"目标组 %s"%(r+1)).encode("utf-8") 
                else:
                    cell = unicode("Target Group %s"%(r+1)).encode("utf-8") 
                row.append(cell)
                row.append(cell)
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

    if "campaign" in args.objects_dict.keys():
        #generate_csv_file(fake,"customer",args.objects_dict["customer"],args.locale)
        with open('campaign.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvfile)
            properties=objMap["campaign"]
            writer.writerow(["-"]+properties+["campaign_type","status"]) if args.locale == "zh_CN" else  writer.writerow(properties+["campaign_type","status"])            
            for r in range(args.objects_dict["campaign"]):
                row = []
                for provider_method in properties:
                    cell = unicode(getattr(fake, provider_method)()).encode("utf-8") 
                    row.append(cell)
                #campaign_type + status
                row.append(random.choice(["Email","Phone","Letter","Social"]))
                row.append(random.choice(["Planned","Active","Canceled","Closed"]))
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

    if "product" in args.objects_dict.keys():
        with open('product.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvfile)
            properties=objMap["product"]
            writer.writerow(["-"]+properties+["batchSerial","isBackOrderAllowed","isDropShipAllowed"]) if args.locale == "zh_CN" else  writer.writerow(properties+["batchSerial","isBackOrderAllowed","isDropShipAllowed"])
            for r in range(args.objects_dict["product"]):
                row = []
                for provider_method in properties:
                    cell = unicode(getattr(fake, provider_method)()).encode("utf-8")
                    row.append(cell)
                #batchSerial + isBackOrderAllowed + isDropShipAllowed
                row.append(random.choice(["SerialProduct","None","BatchProduct"]))
                row.append(random.choice(["true","false"]))
                row.append(random.choice(["true","false"]))           
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

    if "warehouse" in args.objects_dict.keys():
        generate_csv_file(fake,"warehouse",args.objects_dict["warehouse"],args.locale)  
    if "batch" in args.objects_dict.keys():
        generate_csv_file(fake,"batch",args.objects_dict["batch"],args.locale)     
    if "serial" in args.objects_dict.keys():
        generate_csv_file(fake,"serial",args.objects_dict["serial"],args.locale)      
    if "UoM" in args.objects_dict.keys():
        generate_csv_file(fake,"UoM",args.objects_dict["UoM"],args.locale)  

    if "salesOrder" in args.objects_dict.keys():
        customer_data = list(csv.reader(open("customer.csv", "r")))
        product_data = list(csv.reader(open("product.csv", "r")))
        warehouse_data = list(csv.reader(open("warehouse.csv", "r")))
        if args.locale == "zh_CN":
            customer_data.remove(customer_data[0])
            for i in range (0,len(customer_data)):
                customer_data[i].remove(customer_data[i][0])
            # Remove all batch+serial products
            product_data.remove(product_data[0])
            simple_product_data = copy.copy(product_data)
            for i in range (0,len(simple_product_data)):
                if simple_product_data[i][2]!="None":
                    product_data.remove(simple_product_data[i])
            for i in range (0,len(product_data)):
                product_data[i].remove(product_data[i][0])

            warehouse_data.remove(warehouse_data[0])
            for i in range (0,len(warehouse_data)):
                warehouse_data[i].remove(warehouse_data[i][0])                
        else:
            customer_data.remove(customer_data[0])
            # Remove all batch+serial products            
            product_data.remove(product_data[0])
            simple_product_data = copy.copy(product_data)
            for i in range (0,len(simple_product_data)):
                if simple_product_data[i][1]!="None":
                    product_data.remove(simple_product_data[i])
            warehouse_data.remove(warehouse_data[0])
        with open('salesOrder.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)            
            writer = csv.writer(csvfile)
            properties=objMap["salesOrder"]
            header_row = ["customer_name","product_name","warehouse_name","unit_price","quantity","doc_date"]
            writer.writerow(["-"]+header_row) if args.locale == "zh_CN" else  writer.writerow(header_row)
            for i in range (0,args.objects_dict["salesOrder"]):
                row = []
                # customer_name + product_name
                random_customer_index = random.randint(1,args.objects_dict["customer"])-1
                random_product_index = random.randint(1,len(product_data))-1
                if customer_data[random_customer_index][3] == "INDIVIDUAL_CUSTOMER":
                    row.append("{} {}".format(customer_data[random_customer_index][0],customer_data[random_customer_index][1]))
                else:
                    row.append(customer_data[random_customer_index][2])               
                row.append(product_data[random_product_index][0])
                # warehouse
                         
                row.append(random.choice(warehouse_data)[0])
                # unit_price + quantity + doc_date
                for provider_method in properties:
                    if provider_method != "past_date" :
                        cell2 = getattr(fake, provider_method)()
                    elif random.randint(0,1)==1:
                        cell2 = getattr(fake, provider_method)()
                    else:
                        cell2 = datetime.now().strftime("%Y-%m-%d")
                    row.append(cell2)                        
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)




    if "goodReceipt" in args.objects_dict.keys():
        product_data = list(csv.reader(open("product.csv", "r")))
        warehouse_data = list(csv.reader(open("warehouse.csv", "r")))
        if args.locale == "zh_CN":
            # Remove all batch+serial products            
            product_data.remove(product_data[0])
            simple_product_data = copy.copy(product_data)
            for i in range (0,len(simple_product_data)):
                if simple_product_data[i][2]!="None":
                    product_data.remove(simple_product_data[i])
            for i in range (0,len(product_data)):
                product_data[i].remove(product_data[i][0])

            warehouse_data.remove(warehouse_data[0])
            for i in range (0,len(warehouse_data)):
                warehouse_data[i].remove(warehouse_data[i][0])                
        else:
            # Remove all batch+serial products            
            product_data.remove(product_data[0])
            simple_product_data = copy.copy(product_data)
            for i in range (0,len(simple_product_data)):
                if simple_product_data[i][1]!="None":
                    product_data.remove(simple_product_data[i])            
            warehouse_data.remove(warehouse_data[0])

        with open('goodReceipt.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)            
            writer = csv.writer(csvfile)
            properties=objMap["goodReceipt"]
            header_row = ["warehouse_name","product_name","quantity"]
            writer.writerow(["-"]+header_row) if args.locale == "zh_CN" else  writer.writerow(header_row)
            for i in range (0,args.objects_dict["goodReceipt"]):
                row = []
                # warehouse     
                row.append(random.choice(warehouse_data)[0])                
                # product
                row.append(random.choice(product_data)[0])
                #  quantity
                for provider_method in properties:
                    cell = getattr(fake, provider_method)()
                    row.append(cell*100)                        
                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

    if "salesOpportunity" in args.objects_dict.keys():
        customer_data = list(csv.reader(open("customer.csv", "r")))
        product_data = list(csv.reader(open("product.csv", "r")))
        if args.locale == "zh_CN":
            customer_data.remove(customer_data[0])
            for i in range (0,len(customer_data)):
                customer_data[i].remove(customer_data[i][0])
            product_data.remove(product_data[0])
            for i in range (0,len(product_data)):
                product_data[i].remove(product_data[i][0])                 
        else:
            customer_data.remove(customer_data[0])
            product_data.remove(product_data[0])

        with open('salesOpportunity.csv', 'wb') as csvfile:
            if args.locale == "zh_CN":
                csvfile.write(codecs.BOM_UTF8)              
            writer = csv.writer(csvfile)
            properties=objMap["salesOpportunity"]
            header_row = ["customer_name","product_name","status","unit_price","quantity","start_date","closing_date"]          
            writer.writerow(["-"]+header_row) if args.locale == "zh_CN" else  writer.writerow(header_row)
            for i in range (0,args.objects_dict["salesOpportunity"]):
                row = []
                # customer_name + product_name
                random_customer_index = random.randint(1,args.objects_dict["customer"])-1
                random_product_index = random.randint(1,args.objects_dict["product"])-1

                if customer_data[random_customer_index][3] == "INDIVIDUAL_CUSTOMER":
                    row.append("{} {}".format(customer_data[random_customer_index][0],customer_data[random_customer_index][1]))
                else:
                    row.append(customer_data[random_customer_index][2])  

                row.append(product_data[random_product_index][0])

                # status
                status = random.choice(["OPEN","MISSED","SOLD"])
                row.append(status)
                # unit_price + quantity + start_date + closing_date 
                for provider_method in properties:
                    cell2 = getattr(fake, provider_method)()
                    row.append(cell2)
                    if provider_method == "past_date" and status is not "OPEN":
                        row.append(cell2 + timedelta(days=1))

                writer.writerow(["-"]+row) if args.locale == "zh_CN" else  writer.writerow(row)

if __name__ == "__main__":
    main()