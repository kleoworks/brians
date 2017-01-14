import csv

#open csv file in read universal mode
with open('us-500.csv', 'rU') as my_file:

    # create a READER OBJECT that maps the information read into dict keys based on values in first row
    reader = csv.DictReader(my_file, delimiter=',')

    #iterate through each row in reader object
    #print each key as a label for corresponding value
    for row in reader:
        print row['first_name'], row['last_name']
        print 'first_name: {}'.format(row['first_name'])
        print 'last_name: {}'.format(row['last_name'])
        print 'company_name: {}'.format(row['company_name'])
        print 'address: {}'.format(row['address'])
        print 'city: {}'.format(row['city'])
        print 'county: {}'.format(row['county'])
        print 'state: {}'.format(row['state'])
        print 'zip: {}'.format(row['zip'])
        print 'phone1: {}'.format(row['phone1'])
        print 'phone2: {}'.format(row['phone2'])
        print 'email: {}'.format(row['email'])
        print 'web: {}'.format(row['web'])
        print '--------------'
