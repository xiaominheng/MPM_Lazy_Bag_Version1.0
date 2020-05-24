import json

def set_entity_sets(id_0, id_1):
    expected_entity_sets = json.loads(open('entity_sets_model.json').read())
    expected_entity_sets['node_sets'][0]['set'] = id_0
    expected_entity_sets['node_sets'][1]['set'] = id_1

    fw = open('entity_sets.json', 'w')
    json.dump(expected_entity_sets, fw, indent = 4)

    return None
