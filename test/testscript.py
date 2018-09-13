import sys
sys.path.append("../")
from cryptonexapi import CryptonexAPI
from settings import KEY, SECRET_KEY, FROM_HASH, TO_HASH, COUPON, UUID

obj = CryptonexAPI(KEY, SECRET_KEY, is_test=True)

# test userAccountList
success_answer = {'balance', 'currency', 'hash', 'type'}
res = obj.userAccountList()

if  not res:
	print('Test userAccountList...OK')
elif res[0].keys() == success_answer:
	print('Test userAccountList...OK')
else:
	print('Test userAccountList...Error')

# test currencyConvert
success_answer = {'status'}
amount = 1
from_currency = 'cnx'
to_currency = 'btc'
res = obj.currencyConvert(amount, from_currency, to_currency)

if  not res:
	print('Test currencyConvert...OK')
elif res.keys() == success_answer:
	print('Test currencyConvert...OK')
else:
	print('Test currencyConvert...Error')

# test accountWithdraw
success_answer = {'balance', 'currency', 'hash', 'id', 'user_id'}
amount = 0.0005
res = obj.accountWithdraw(FROM_HASH, TO_HASH, amount)

if  not res:
	print('Test accountWithdraw...OK')
elif res.keys() == success_answer:
	print('Test accountWithdraw...OK')
else:
	print('Test accountWithdraw...Error')

# test transactionsList
success_answer = {'summary', 'transactions'}
max_count = 3
res = obj.transactionsList(max_count)

if  not res:
	print('Test transactionsList...OK')
elif res.keys() == success_answer:
	print('Test transactionsList...OK')
else:
	print('Test transactionsList...Error')

# test rateList
success_answer = {'alias', 'ask', 'base_currency', 'base_type', 'bid', 'convert_type', 'last_price', 'rel_currency_id', 'rel_type', 'update_stamp', 'value_last_24h'}
res = obj.rateList()

if  not res:
	print('Test rateList...OK')
elif res[0].keys() == success_answer:
	print('Test rateList...OK')
else:
	print('Test rateList...Error')

# test couponList
success_answer = {'coupons', 'summary'}
max_count = 3
res = obj.couponList(max_count)

if  not res:
	print('Test couponList...OK')
elif res.keys() == success_answer:
	print('Test couponList...OK')
else:
	print('Test couponList...Error')

# test couponApply
success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency', 'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
amount = 0.005
currency = 'cnx'
res = obj.couponApply(amount, COUPON, currency)

if  not res:
	print('Test couponApply...OK')
elif res.keys() == success_answer:
	print('Test couponApply...OK')
else:
	print('Test couponApply...Error')


# test couponCreate
success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency', 'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
amount = 0.005
currency = 'cnx'
res = obj.couponCreate(amount, currency)

if  not res:
	print('Test couponCreate...OK')
elif res.keys() == success_answer:
	print('Test couponCreate...OK')
else:
	print('Test couponCreate...Error')

# test couponRedeem
success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency', 'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
res = obj.couponRedeem(COUPON)

if  not res:
	print('Test couponRedeem...OK')
elif res.keys() == success_answer:
	print('Test couponRedeem...OK')
else:
	print('Test couponRedeem...Error')

# test couponCheck
success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency', 'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
res = obj.couponCheck(COUPON)

if  not res:
	print('Test couponCheck...OK')
elif res.keys() == success_answer:
	print('Test couponCheck...OK')
else:
	print('Test couponCheck...Error')

# test miningList
success_answer = {'minings', 'summary'}
max_count = 3
res = obj.miningList(max_count)

if  not res:
	print('Test miningList...OK')
elif res.keys() == success_answer:
	print('Test miningList...OK')
else:
	print('Test miningList...Error')

# test miningCreate
success_answer = {'status'}
amount = 2
res = obj.miningCreate(amount)

if  not res:
	print('Test miningCreate...OK')
elif res.keys() == success_answer:
	print('Test miningCreate...OK')
else:
	print('Test miningCreate...Error')

# test userInfo
success_answer = {'auth_2fa', 'deposit_auto_convert', 'deposit_auto_mining', 'eth_cnx_bonus', 'id', 'login', 'post_stamp', 'username'}
res = obj.userInfo()

if  not res:
	print('Test userInfo...OK')
elif res.keys() == success_answer:
	print('Test userInfo...OK')
else:
	print('Test userInfo...Error')

# test invoiceCancel
success_answer = {'amount', 'creator', 'currency', 'description', 'expire_at', 'status', 'uuid'}
res = obj.invoiceCancel(UUID)

if  not res:
	print('Test invoiceCancel...OK')
elif res.keys() == success_answer:
	print('Test invoiceCancel...OK')
else:
	print('Test invoiceCancel...Error')

# test invoiceApply
success_answer = {'amount', 'creator', 'currency', 'description', 'executor', 'expire_at', 'status', 'uuid'}
res = obj.invoiceApply(UUID)

if  not res:
	print('Test invoiceApply...OK')
elif res.keys() == success_answer:
	print('Test invoiceApply...OK')
else:
	print('Test invoiceApply...Error')

# test invoiceCreate
success_answer = {'amount', 'currency', 'description', 'expire_at', 'status', 'uuid'}
amount = 0.005
currency = 'cnx'
res = obj.invoiceCreate(amount, currency)

if  not res:
	print('Test invoiceCreate...OK')
elif res.keys() == success_answer:
	print('Test invoiceCreate...OK')
else:
	print('Test invoiceCreate...Error')

# test invoiceList
success_answer = {'invoices', 'summary'}
res = obj.invoiceList()

if  not res:
	print('Test invoiceList...OK')
elif res.keys() == success_answer:
	print('Test invoiceList...OK')
else:
	print('Test invoiceList...Error')

# test invoiceGet
success_answer = {'amount', 'creator', 'currency', 'description', 'expire_at', 'status', 'uuid'}
res = obj.invoiceGet(UUID)

if  not res:
	print('Test invoiceGet...OK')
elif res.keys() == success_answer:
	print('Test invoiceGet...OK')
else:
	print('Test invoiceGet...Error')