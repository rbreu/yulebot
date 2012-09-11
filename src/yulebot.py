#!/usr/bin/env python
import irc.bot
import time
import threading
import ConfigParser
import logging
import item_list
import re


# Create our bot class
class YuleBot(irc.bot.SingleServerIRCBot):

    def __init__(self, server_list, nickname, realname, channel,
                 delay, reconnection_interval=60):
        self.channel = channel
        self.delay = delay
        irc.bot.SingleServerIRCBot.__init__(self, server_list, nickname,
                                            realname, reconnection_interval)

    # Join the channel when welcomed
    def on_welcome (self, connection, event):
        logging.info("Got welcome from server")
        connection.join(self.channel)
        logging.info("Joined channel %s" % self.channel)
        threading.Thread(target=self.show_loop).start()

    def on_privmsg(self, connection, event):
        logging.debug("Received private message from: %s" % event.source())
        logging.debug("Content: %s" % event.arguments())
        msg = event.arguments()[0]
        sender =  event.source().split("!")[0]
        
        match = re.match(r"\s*add\s+(\S.*)", msg)
        if match:
            item = match.group(1)
            item_list.add(item)
            connection.privmsg(self.channel, "%s added: %s" % (sender, item))
            return
            
        match = re.match(r"\s*delete\s+(\d+)", msg)
        if match:
            index = int(match.group(1))
            item = item_list.delete(index)
            connection.privmsg(self.channel, "%s deleted: %s" % (sender, item))
            return
            
        match = re.match(r"\s*show\s*", msg)
        if match:
            self.show(sender)
            return

        self.help(sender)
        
    def on_disconnect(self, connection, event):
        sys.exit(0)

    def show_loop(self):
        while True:
            self.show()
            time.sleep(self.delay * 60)

    def show(self, recipient=None):
        recipient = self.channel if recipient == None else recipient
        logging.debug("Showing list to %s" % recipient)
        for (i, item) in enumerate(item_list.get()):
            self.connection.privmsg(recipient, "%i: %s" % (i, item))
                
    def help(self, recipient=None):
        recipient = self.channel if recipient == None else recipient
        logging.debug("Showing help to %s" % recipient)
        self.connection.privmsg(recipient, "Hi, you can see a description at https://github.com/rbreu/yulebot#yuletide-bot")
            

# Create the bot
config = ConfigParser.SafeConfigParser()
config.read(["config.ini"])
loglevel = config.get("DEFAULT", "loglevel")
logging.basicConfig(level=getattr(logging, loglevel, "INFO"))
logging.info("Read config from config.ini")
bot = YuleBot([(config.get("DEFAULT", "server"), int(config.get("DEFAULT", "port")))],
              config.get("DEFAULT", "nick"),
              config.get("DEFAULT", "name"),
              config.get("DEFAULT", "channel"),
              int(config.get("DEFAULT", "delay")))

logging.info("Created bot %s (%s) at %s:%s %s, delay %s" %
             (config.get("DEFAULT", "nick"),
              config.get("DEFAULT", "name"),
              config.get("DEFAULT", "server"),
              config.get("DEFAULT", "port"),
              config.get("DEFAULT", "channel"),
              config.get("DEFAULT", "delay")))
bot.start()
