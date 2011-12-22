import json
import logging

FILENAME = "data/items.json"

def get():
    try:
        json_file = file(FILENAME)
    except IOError:
        logging.warning("File doesn't exist: %s" % FILENAME)
        return []
    
    return json.load(json_file)


def add(item):
    logging.debug("Adding item %s." % item)
    items = get() + [item]
    json_file = file(FILENAME, "w")
    json.dump(items, json_file)
    json_file.close()


def delete(index):
    logging.debug("Deleting item %i." % index)
    items = get()
    try:
        item = items.pop(index)
    except IndexError:
        return "Item with index %i does not exist" % index
    json_file = file(FILENAME, "w")
    json.dump(items, json_file)
    json_file.close()
    return item
