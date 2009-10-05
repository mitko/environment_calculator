import cPickle as pickle

finite_resourses=['gas','oil','whales','uran']
renewable_resources=['water_gravity','sun_light','wheat','tomatoes']

products ={
    'sushi':[1000, {'whales':1,
                   'gas':200}],
    'dry_sushi':[1, {'sushi':2,
                    'sun_light':5}],
    'burger':[1, {'beef':0.100,
                  'bread':0.200,
                  'ketchup':0.030,
                  'dry_sushi':0.05}],
    'bread' :[1, {'wheat':4}],
    'ketchup':[1, {'tomatoes':3}],
    'beef': [1000, {'wheat': 2000,
                   'gas' :10,
                   'oil' :50}],
    'tomatoes':[20,{'sun_light':7,
                    'ketchup':3}]
}




def find_footprint(product):
    info=products[product]
    number_of_copies=info[0]
    footprint=info[1]
    pre_products=0
    while(True):
        lst_ftpr=[]
        changed=False
        for part in footprint:
            if (part not in finite_resourses) and (part not in renewable_resources):
                if products[part]!=None:
                    changed = True
                    lst_ftpr.append(multiply((footprint[part]+0.0)/products[part][0],products[part][1]));
                else:
                    lst_ftpr.append({part:footprint[part]})
            else:
                lst_ftpr.append({part:footprint[part]})
        if not changed:
            break

        new_footprint = aggregate(lst_ftpr)
        footprint = new_footprint
    footprint = multiply(1.0/number_of_copies,footprint)
    return footprint        
                    

def multiply(value,dictionary):
    new = {}
    for key in dictionary.keys():
        new[key]=dictionary[key]*value
    return new


def aggregate(lst_footprints):
    parts = []
    aggr = {}
    for footprint in lst_footprints:
        parts.extend(footprint.keys())
    for part in parts:
        s=0
        for ftprint in lst_footprints:
            if part in ftprint:
                s+=ftprint[part]
        aggr[part]=s
    return aggr


##print find_footprint('tomatoes')

##print find_footprint('dry_sushi')
print find_footprint('burger')
##print finite_resourses
