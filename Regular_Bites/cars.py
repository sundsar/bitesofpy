cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
  """return a comma  + space (', ') separated string of jeep models
     (original order)"""
  jeeps = cars['Jeep']
  return ', '.join(jeeps)


def get_first_model_each_manufacturer(cars=cars):
  """return a list of matching models (original ordering)"""
  return [v[0] for k, v in cars.items()]


def get_all_matching_models(cars=cars, grep='trail'):
  """return a list of all models containing the case insensitive
     'grep' string which defaults to 'trail' for this exercise,
     sort the resulting sequence alphabetically"""
  return sorted([item for v in cars.values() for item in v if grep.lower() in item.lower()])


def sort_car_models(cars=cars):
  """return a copy of the cars dict with the car models (values)
     sorted alphabetically"""
  return {k: sorted(v) for k, v in cars.items()}


# print(get_all_jeeps())
# print(get_first_model_each_manufacturer())
# print(get_all_matching_models())
# print(sort_car_models())
