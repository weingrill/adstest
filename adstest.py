#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Joerg Weingrill"
__copyright__ = "Copyright 2020 Leibniz-Insitute for Astrophysics Potsdam (AIP)"
__credits__ = ["Joerg Weingrill"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Joerg Weingrill"
__email__ = "jweingrill@aip.de"
__status__ = "Development"
__date__ = "1/24/20"

import pyads

if __name__ == "__main__":

    SENDER_AMS = '141.33.59.7.1.1'
    PLC_IP = '141.33.59.208'
    USERNAME = 'Administrator'
    PASSWORD = '1'
    ROUTE_NAME = '141.33.59.7'
    HOSTNAME = '141.33.59.7'
    PLC_AMS_ID = '5.34.116.124.1.1'
    pyads.add_route_to_plc(SENDER_AMS, HOSTNAME, PLC_IP, USERNAME, PASSWORD, route_name=ROUTE_NAME)

    adsport = pyads.PORT_TC3PLC1
    print('using port {}'.format(adsport))
    plc = pyads.Connection(PLC_AMS_ID, adsport, PLC_IP)
    plc.set_timeout(3000)
    print('Connecting ...')
    plc.open()
    print('Connected')
    print(plc.read_device_info())
    print(plc.read_state())
    q = plc.read_by_name('MAIN.Dust5.Q', pyads.PLCTYPE_BOOL)
    print(q)
    plc.write_by_name('MAIN.Dust5.PV', 8192, pyads.PLCTYPE_WORD)
    # plc.read_by_name('global.bool_value', pyads.PLCTYPE_BOOL)
    cv = plc.read_by_name('MAIN.Dust5.CV', pyads.PLCTYPE_WORD)
    print(cv)
    print('Closing ...')
    plc.close()
    print('Closed')