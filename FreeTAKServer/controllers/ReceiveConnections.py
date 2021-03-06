#######################################################
# 
# ReceiveConnections.py
# Python implementation of the Class ReceiveConnections
# Generated by Enterprise Architect
# Created on:      19-May-2020 6:21:05 PM
# Original author: Natha Paquette
# 
#######################################################
import socket
from FreeTAKServer.controllers.configuration.LoggingConstants import LoggingConstants
from FreeTAKServer.model.RawConnectionInformation import RawConnectionInformation as sat
from FreeTAKServer.controllers.CreateLoggerController import CreateLoggerController
from FreeTAKServer.controllers.configuration.ReceiveConnectionsConstants import ReceiveConnectionsConstants
from FreeTAKServer.controllers.SSLSocketController import SSLSocketController
loggingConstants = LoggingConstants()
logger = CreateLoggerController("ReceiveConnections").getLogger()
import logging
import logging.handlers
import ssl
import time
#TODO: move health check values to constants and create controller for HealthCheck data

class ReceiveConnections:
    def __init__(self):
        pass


    def listen(self, sock, sslstatus = False):
        #logger = CreateLoggerController("ReceiveConnections").getLogger()
        #listen for client connections
        sock.listen(0)
        try:
            #establish the socket variables
            if sslstatus == True:
                sock.settimeout(60)
                #sock.setblocking(0)
            #logger.debug('receive connection started')
            try:
                client, address = sock.accept()
                if sslstatus == True:
                    client = SSLSocketController().wrap_client_socket(client)
            except ssl.SSLError as e:
                print(e)
                client.close()
                logger.warning('ssl error thrown in connection attempt '+str(e))
                return -1
            if sslstatus == True:
                logger.info('client connected over ssl ' + str(address) + ' ' + str(time.time()))
            #wait to receive client
            client.settimeout(int(ReceiveConnectionsConstants().RECEIVECONNECTIONDATATIMEOUT))
            data = client.recv(1024)
            if data == ReceiveConnectionsConstants().TESTDATA:
                client.send(b'success')
                return -1
            else:
                pass
            client.settimeout(0)
            logger.info(loggingConstants.RECEIVECONNECTIONSLISTENINFO)
            #establish the socket array containing important information about the client
            RawConnectionInformation = sat()
            RawConnectionInformation.ip = address[0]
            RawConnectionInformation.socket = client
            RawConnectionInformation.xmlString = data.decode('utf-8')
            try:
                if socket != None and data != b'':
                    return RawConnectionInformation
                else:
                    return -1
            except Exception as e:
                logger.warning('exception in returning data '+str(e))
                return -1

        except Exception as e:
            logger.warning(loggingConstants.RECEIVECONNECTIONSLISTENERROR+str(e))
            return -1
