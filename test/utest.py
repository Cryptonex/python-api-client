import sys
import unittest
import serverjson
from multiprocessing import Process
sys.path.append("../")
from cryptonexapi import CryptonexAPI
from settings import KEY, SECRET_KEY, FROM_HASH, TO_HASH, COUPON_REDEEM, COUPON, COUPON_APPLY, UUID_CANCEL, UUID, UUID_APPLY


def startServer():
    serverjson.run()


server = Process(target=startServer)
# server.start()

obj = CryptonexAPI(KEY, SECRET_KEY, is_test=True)
obj.setUrl('http://127.0.0.1:5000')


class TestCryptonexAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        server.start()

    @classmethod
    def tearDownClass(cls):
        serverjson.f.close()
        server.terminate()

    def test_userAccountList(self):
        success_answer = {'balance', 'currency', 'hash', 'type'}
        max_count = 1
        self.assertEqual(obj.userAccountList()[0].keys(), success_answer)
        self.assertEqual(obj.userAccountList(max_count)
                         [0].keys(), success_answer)

    def test_currencyConvert(self):
        success_answer = {'status'}
        amount = 0.0001
        from_currency = 'cnx'
        to_currency = 'btc'
        self.assertEqual(obj.currencyConvert(
            amount, from_currency, to_currency).keys(), success_answer)

    def test_accountWithdraw(self):
        success_answer = {'balance', 'currency', 'hash', 'id', 'user_id'}
        amount = 0.0005
        self.assertEqual(obj.accountWithdraw(
            FROM_HASH, TO_HASH, amount).keys(), success_answer)

    def test_transactionsList(self):
        success_answer = {'summary', 'transactions'}
        self.assertEqual(obj.transactionsList().keys(), success_answer)

    def test_rateList(self):
        success_answer = {'alias', 'ask', 'base_currency', 'base_type', 'bid', 'convert_type',
                          'last_price', 'rel_currency_id', 'rel_type', 'update_stamp', 'value_last_24h'}
        self.assertEqual(obj.rateList()[0].keys(), success_answer)

    def test_couponList(self):
        success_answer = {'coupons', 'summary'}
        self.assertEqual(obj.couponList().keys(), success_answer)

    def test_couponApply(self):
        success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency',
                          'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
        amount = 0.005
        currency = 'cnx'
        self.assertEqual(obj.couponApply(amount, COUPON_APPLY,
                                         currency).keys(), success_answer)

    def test_couponCreate(self):
        success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency',
                          'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
        amount = 0.005
        currency = 'cnx'
        self.assertEqual(obj.couponCreate(
            amount, currency).keys(), success_answer)

    def test_couponRedeem(self):
        success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency',
                          'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
        self.assertEqual(obj.couponRedeem(
            COUPON_REDEEM).keys(), success_answer)

    def test_couponCheck(self):
        success_answer = {'amount', 'comment', 'coupon', 'creator', 'currency',
                          'expire_at', 'password', 'receiver', 'redeem_at', 'status', 'type'}
        self.assertEqual(obj.couponCheck(COUPON).keys(), success_answer)

    def test_miningList(self):
        success_answer = {'minings', 'summary'}
        self.assertEqual(obj.miningList().keys(), success_answer)

    def test_miningCreate(self):
        success_answer = {'status'}
        amount = 1
        self.assertEqual(obj.miningCreate(amount).keys(), success_answer)

    def test_userInfo(self):
        success_answer = {'auth_2fa', 'deposit_auto_convert', 'deposit_auto_mining',
                          'eth_cnx_bonus', 'id', 'login', 'post_stamp', 'username'}
        self.assertEqual(obj.userInfo().keys(), success_answer)

    def test_invoiceCancel(self):
        success_answer = {'amount', 'creator', 'currency',
                          'description', 'expire_at', 'status', 'uuid'}
        self.assertEqual(obj.invoiceCancel(UUID_CANCEL).keys(), success_answer)

    def test_invoiceApply(self):
        success_answer = {'amount', 'creator', 'currency',
                          'description', 'executor', 'expire_at', 'status', 'uuid'}
        self.assertEqual(obj.invoiceApply(UUID_APPLY).keys(), success_answer)

    def test_invoiceCreate(self):
        success_answer = {'amount', 'currency',
                          'description', 'expire_at', 'status', 'uuid'}
        amount = 0.005
        currency = 'cnx'
        self.assertEqual(obj.invoiceCreate(
            amount, currency).keys(), success_answer)

    def test_invoiceList(self):
        success_answer = {'invoices', 'summary'}
        self.assertEqual(obj.invoiceList().keys(), success_answer)

    def test_invoiceGet(self):
        success_answer = {'amount', 'creator', 'currency',
                          'description', 'expire_at', 'status', 'uuid'}
        self.assertEqual(obj.invoiceGet(UUID).keys(), success_answer)


if __name__ == '__main__':
    unittest.main()
