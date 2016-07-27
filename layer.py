from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        #self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        from actions import actiondict
        # just print info
        mess = messageProtocolEntity.getBody()
        print("Saw %s from %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))
        if len(mess) > 0 and mess[0] == "?":
            for m,f in actiondict.items():
                if mess[1:].split()[0].lower() == m:
                    self.send(messageProtocolEntity.getFrom(False),f(mess[1:]))
                    break
            else:
                self.send(messageProtocolEntity.getFrom(False),"I didn't understand your command. Sorry!")

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))

    def send(self,to,message):
        print("Sending %s to %s" % (message,to))
        outgoingMessage = TextMessageProtocolEntity(message, to=self.normalizeJid(to))
        self.toLower(outgoingMessage)

    def normalizeJid(self, number):
        if '@' in number:
            return number
        if '-' in number:
            return "%s@g.us" % number
        return "%s@s.whatsapp.net" % number
