import json
import logging
import os

DATA_DIR = "data"
FILENAME = os.path.join(DATA_DIR, "items.json")

def get():
    try:
        json_file = file(FILENAME)
    except IOError:
        logging.warning("Couldn't read file, start empty list: %s" % FILENAME)
        return []
    
    return json.load(json_file)


def add(item):
    logging.debug("Adding item %s." % item)
    if not os.path.exists(DATA_DIR):
        logging.debug("Creating data directory %s" % DATA_DIR)
        os.mkdir(DATA_DIR)
    items = get() + [item]
    json_file = file(FILENAME, "w")
    json.dump(items, json_file)
    json_file.close()


def delete(index):
    logging.debug("Deleting item %i." % index)
    items = get()
    if not os.path.exists(DATA_DIR):
        logging.debug("Creating data directory %s" % DATA_DIR)
        os.mkdir(DATA_DIR)
    try:
        item = items.pop(index)
    except IndexError:
        return "Item with index %i does not exist" % index
    json_file = file(FILENAME, "w")
    json.dump(items, json_file)
    json_file.close()
    return item
