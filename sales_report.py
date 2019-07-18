"""Generate sales report showing total melons each salesperson sold."""


# salespeople = []    # Initialize a salesperson list
# melons_sold = []    # Initialize a melons sold list

# f = open('sales-report.txt')    # opens file
# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')   # splits line into entries
#     salesperson = entries[0]    # assigns salesperson with entries at index 0
#     melons = int(entries[2])    # assigns melons with entries at index 2

#     if salesperson in salespeople:  # if salesperson in salespeople find index
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson) # append person and melons to lists
#         melons_sold.append(melons)


# for i in range(len(salespeople)):   # Iterate through list of salespeople by index
#     print(f'{salespeople[i]} sold {melons_sold} melons') # print sales record

"""
Suggested improvents to program.


Create a class Sales

create attributes that define the three inquiries needed

set attribute name
set attribute total_sales 
set attribute melons

class will maintiained structure of entiries

"""

class Sales:
    """ Organizes sales report.
    """
    def __init__(self,name,total_sales,melon):
        self.name = name.title()
        self.total_sales = float(total_sales)
        self.melons = int(melon)




f = open('sales-report.txt')

for line in f:
    line = line.rstrip()
    entries = line.split('|') 
    
    name = entries[0]
    total_sales = entries[1]
    melons = entries[2]

    sales_person = name
    sales_person = Sales(name, total_sales, melons)


    print("{name} sold {melons} melons.".format(
        name=sales_person.name,
        melons=sales_person.melons
        ))







