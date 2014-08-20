from gedcom import Gedcom
from tree.models import Tree, Family


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
            
            
def import_gedcom_data():
    gedcom_file = Gedcom('family.ged')
    people_elements = []
    fam_dict = {}
    family_codes = []
    for elem in gedcom_file.element_list():
        if elem.tag() == 'NAME':
            people_elements.append(elem)
            if elem.parent().tag() == 'INDI':
                for fam in gedcom_file.families(elem.parent()):
                    p = fam.pointer()
                    if p not in family_codes:
                        family_codes.append(p)
    for fc in family_codes:
        for pe in people_elements:
            if pe.parent().tag() == 'INDI':
                for fam in gedcom_file.families(pe.parent()):
                    if fam.pointer() == fc:
                        if fc in fam_dict.keys():
                            fam_dict[fc].append(pe)
                        else:
                            fam_dict[fc] = [pe]
                for fam in gedcom_file.families(pe.parent(), family_type='FAMC'):
                    if fam.pointer() == fc:
                        if fc in fam_dict.keys():
                            fam_dict[fc].append(pe)
                        else:
                            fam_dict[fc] = [pe]
    print fam_dict
    
    
#fam_dict = {} # dictionary of families.
#family_code = [] # unique list of family codes.
#people_elements = []
                
# create the people from the people elements, get the ids they're given
# and append them to them.

# create the families and add the relevant people by id.
# maybe pop file in a data directory and just use it directly to start.
# run it from a web page.  

        

