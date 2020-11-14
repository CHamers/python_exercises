#capitalises the first and fourth letters of a name

def oldMacDonald1(name):
    return name[0].upper() + name[1:3].lower() + name[3].upper() + name[4:].lower()
        

print(oldMacDonald1('Banfield'))

# second method

def oldMacDonald2(name):
    return name[:3].capitalize() +  name[3:].capitalize() 
        

print(oldMacDonald2('Banfield'))