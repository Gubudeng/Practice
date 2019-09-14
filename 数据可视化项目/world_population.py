#导入json包
import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import LightColorizedStyle, RotateStyle

#将数据加载到列表中
filename = 'data_json.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
cc2_populations = {}

#打印每个国家2010年人口的数量
def get_population_year(value):
    for pop_dict in pop_data:
        if pop_dict['Year'] == value:
            country_name = pop_dict['Country Name']
            population = int(pop_dict['Value'])
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population
    return cc_populations
        #     print(code + ':' + str(population))
        # else:
        #     print('ERROR - ' + country_name)




#打印每个国家2011年人口的数量
# for pop_dict in pop_data:
#     if pop_dict['Year'] == 2011:
#         country_name = pop_dict['Country Name']
#         population = int(pop_dict['Value'])
#         code = get_country_code(country_name)
#         if code:
#             cc2_populations[code] = population
cc_populations = get_population_year(2010)
#根据人口数量将所有的国家分成三组
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop
print(len(cc_pop_1),len(cc_pop_2),len(cc_pop_3))


wm = pygal_maps_world.maps.World()
wm.style = LightColorizedStyle
wm.style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm.title = 'World Population in 2010,2011, by Country'
# wm.add('2010', cc_populations)
# wm.add('2011', cc2_populations)
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_populations.svg')
