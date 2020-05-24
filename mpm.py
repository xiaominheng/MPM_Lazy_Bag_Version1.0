import json

expected_mpm = json.loads(open('mpm_model.json').read())

def set_mpm_characteristics(fric_coef = 0.5, density = 1800, poss_ratio = 0.3, fric_ang = 15, cohesion = 1000):
    expected_mpm['mesh']['boundary_conditions']['friction_constraints'][0]['friction'] = fric_coef
    expected_mpm['materials'][0]['density'] = density
    expected_mpm['materials'][0]['possion_ratio'] = poss_ratio
    expected_mpm['materials'][0]['friction'] = fric_ang
    expected_mpm['materials'][0]['cohesion'] = cohesion

    fw = open('mpm.json', 'w')
    json.dump(expected_mpm, fw, indent=4)

    return None

if __name__ == '__main__':
    set_mpm_characteristics(10,10,1,1,1)