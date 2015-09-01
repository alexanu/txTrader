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
print('API status=%s' % api.status())

# bypass account configuration; use the first available account
account = api.query_accounts()[0]
api.set_account(account)

# order 10 shares of IBM at the market, returning an order structure
order = api.market_order('IBM', 10)
print'order:'
print order
print

order_id = order['permid'] if order and 'permid' in order.keys() else None

# query the status of an order given it's permanent id
if order_id:
  print 'Order Status:'
  status = api.query_order(order_id)
  print status
  print

# query all the currently known order ids
print 'All Current Order IDs:'
print api.query_orders().keys()
print

# query the execution structure for this order
if order_id:
  result = 'Not Found'
  print 'Execution Report:'
  execution_reports = api.query_executions()
  for report in execution_reports.values():
    if report['permid'] == order_id:
      result = repr(report)
  print result
