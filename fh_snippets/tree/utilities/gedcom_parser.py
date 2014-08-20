from gedcom import Gedcom
#from tree.models import Tree, Family
#from optparse import OptionParser


#parser = OptionParser()
#parser.add_option("-f", "--file", dest="filename",
#                  help="gedcom FILE to parse", metavar="FILE")

#(options, args) = parser.parse_args()

#gedcom_file = Gedcom(options.filename)

#fam_dict = {} # dictionary of families.
#family_code = [] # unique list of family codes.
#people_elements = []

def do_later():
    for elem in gedcom_file.element_list():
        if elem.tag() == 'NAME':
            people_elements.append(elem)
            for fam in gedcom_file.families(elem):
                p = fam.pointer()
                if p not in family_code:
                    family_code.append(p)


def handle_uploaded_file(f):
    with open('family.ged', 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
                
# create the people from the people elements, get the ids they're given
# and append them to them.

# create the families and add the relevant people by id.
# maybe pop file in a data directory and just use it directly to start.
# run it from a web page.  

        

