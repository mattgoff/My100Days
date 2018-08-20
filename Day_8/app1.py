cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    return [models[0] for manfacturer, models in cars.items()]


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep_list = []
    for x in cars.items():
        for car in x[1]:
            if grep.lower() in car.lower():
                grep_list.append(car)
    return sorted(grep_list)

def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for manfacturer, model in cars.items():
        cars[manfacturer] = sorted(cars[manfacturer])
    return cars

print(get_all_matching_models('CO'))
