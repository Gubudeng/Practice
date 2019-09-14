# def get_formatted_name(first_name, last_name):
#     full_name = first_name +' '+  last_name
#     return full_name.title()
#
# musician = get_formatted_name('john', 'dave')
# print(musician)

# def build_person(first_name, last_name):
#     person = {'first':first_name,'last':last_name}
#     return person
#
# musician = build_person('jimi','hendrix')
# print(musician)

# def city_country(city_name, country):
#     full_name = city_name + ' ' + country
#     return full_name.title()
# city = city_country('xinjiang', 'china')
# print(city)

# def make_album(siger_name, album):
#     siger_album = {'siger':siger_name,'alb':album}
#     return siger_album
# siger = make_album('john', 'love')
# print(siger)
# siger = {}
# while True:
#     siger_namee = input("\nPlease input the siger name: ")
#     siger_album = input("\nPlease input the siger's album")
#     siger[siger_namee] = siger_album
#     if siger_namee == 'q':
#         break
#     elif siger_album =='q':
#         break
# print(siger)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_models = unprinted_designs.pop()
#         print("Printing model: " + current_models)
#         completed_models.append(current_models)
#
# def show_completed_models(completed_models):
#     for name in completed_models:
#         print(name)
#
# unprinted_designs = ['ipsad','sada','asdww']
# completed_models = []
#
# print_models(unprinted_designs[:],completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)
# nmagicians = []
# magicians = ['kenan','jide','liuqian']
# def show_magicians(magicians):
#     print('打印魔术师的名字')
#     for name in magicians:
#         print(name.title())
#
# def make_great(magicians,nmagicians):
#     while magicians:
#         current_magician = magicians.pop()
#         nmagicians.append('the Great ' + current_magician)
#
# make_great(magicians[:],nmagicians)
# show_magicians(nmagicians)
# print(magicians)
# def make_pizza(size,*toppings):
#
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- "+ topping)
# make_pizza(12, 'awsss')
# make_pizza(16,'asswww','qqqw','adaapqi')

# def build_profile(first, last , **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key,value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('albert', 'einstein', location = 'princeton',field = 'physics')
# print(user_profile)
# def make_sandwich(*toppings):
#     print("\nPlease choose your favorite ingredients:")
#     for topping in toppings:
#         print("- "+ topping)
#
# make_sandwich('niurou', 'huacai', 'haocide')
# make_sandwich('brokeli', 'tomato')
#
# def make_car(car_name, xinghao, **car_info):
#     profile = {}
#     profile['c_name'] = car_name
#     profile['c_xinghao'] = xinghao
#     for key, value in car_info.items():
#         profile[key] = value
#     return profile
#
# car = make_car('subaru','outback',color = 'blue',tow_package = True)
# print(car)
