#!/usr/bin/env python

import txtrader.client

from os import environ

# these should be set in the calling environment
environ['TXTRADER_HOST']='127.0.0.1'
environ['TXTRADER_USERNAME']='change_this_username'
environ['TXTRADER_PASSWORD']='change_this_password'
environ['TXTRADER_XMLRPC_PORT']='50080'
environ['TXTRADER_XMLRPC_RETRY_LIMIT']='3'
environ['TXTRADER_XMLRPC_TIMEOUT']='60'
environ['TXTRADER_API_ACCOUNT']='unknown'

# connect to the IB TWS API
api = txtrader.client.API('tws')

# bypass account configuration; use the first available account
account = api.query_accounts()[0]
api.set_account(account)

print api.query_positions()

