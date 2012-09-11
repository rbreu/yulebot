Yuletide Bot
============


Usage
-----

The bot keeps a list of items and displays it in a regular interval
to the whole chat. You can send commands to the bot by sending it a
private message. The commands are:

**show**

The bot sends you a private message with the current list of items

Example usage::

  /msg YuleListBot show

**add <item>**
 
This will add an item to the list.

Example usage::

  /msg YuleListBot add My awesome new item!

**delete <index>**
 
This will delete the item at index <index>.

Example usage::

  /msg YuleListBot delete 2


All messages the bot doesn't understand will send you a private
message with a link to this help file.


Installation
------------

The bot needs Python 2.x and the python packes listed in
requirements.txt to run. If you're using pip, you can install the
dependencies via::
 
  pip install ../requirements.txt

Once the dependencies are installed, run from the main directory::

  src/yulebot.py


