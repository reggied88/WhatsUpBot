from errbot import BotPlugin, botcmd

class WhatsUpBot(BotPlugin)
    """Example 'What Up!' plugin for Errbot"""

    @botcmd
    def hey(self, msg, args):
        """Say whats up to the world"""
        return "What's up, " + format(msg.frm)
