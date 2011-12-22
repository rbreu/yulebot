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

  /msg YuleListBot add My aweome new item!

**delete <index>**
 
This will delete the item at index <index>.

Example usage::

  /msg YuleListBot delete 2


All messages the bot doesn't understand will send you a private
message with a list to this help file.


Installation
------------

The bot needs Python 2.x and the packages irclib and ircbot to run.
