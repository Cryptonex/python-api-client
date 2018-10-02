import time
import hashlib
import requests
import json


class CryptonexException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class CryptonexHTTPException(CryptonexException):

    def __init__(self, msg, codehttp):
        super().__init__(msg)
        self.code = codehttp


class CryptonexRPCException(CryptonexException):

    def __init__(self, msg, codejsonrpc):
        super().__init__(msg)
        self.code = codejsonrpc


class CryptonexAPI(object):

    def setUrl(self, url):
        self._url = url

    def setHeaders(self, headers):
        self._headers = headers

    def setNonce(self, nonce):
        self._nonce = nonce

    def __init__(self, key, secret_key, is_test=False):
        self._key = key
        self._secret_key = secret_key
        if is_test:
            self._url = 'https://demo-userapi.cryptonex.org/api'
        else:
            self._url = 'https://userapi.cryptonex.org/api'
        self._headers = {'content-type': 'application/json'}
        self.__id = 0
        self._nonce = int(time.time())

    def __call_api(self, method, add_params=None):
        params = {}
        self.__id += 1
        self._nonce += 1
        sign = hashlib.sha256(method.encode(
            'utf-8') + str(self._nonce).encode('utf-8') + self._secret_key.encode('utf-8'))
        sign = sign.hexdigest()
        default = {"key": self._key, "sign": sign, "nonce": self._nonce}
        params.update(default)

        if add_params is not None:
            params.update(add_params)

        payload = {"jsonrpc": "2.0", "method": method,
                   "params": params, "id": self.__id}
        response = None

        try:
            response = requests.post(self._url, data=json.dumps(
                payload), headers=self._headers)
        except Exception:
            raise CryptonexException('Check the network connection')

        if response.status_code != requests.codes.ok:
            raise CryptonexHTTPException(
                'HTTP Error code', response.status_code)

        # print(response.json())
        if "error" in response.json().keys():
            err = response.json()["error"]
            raise CryptonexRPCException(
                err["message"], err["code"])

        if "result" not in response.json().keys():
            raise CryptonexRPCException(
                "Answer does not have result key", -33001)

        return response.json()

    def userAccountList(self, max_count=None):
        add_params = {}

        if max_count is not None:
            add_params["max_count"] = int(max_count)

        res = self.__call_api(method="user.account_list",
                              add_params=add_params)

        return res["result"]["accounts"]

    def currencyConvert(self, amount, from_currency, to_currency):
        add_params = {"amount": str(
            amount), "from_currency": from_currency, "to_currency": to_currency}

        res = self.__call_api(method="currency.convert", add_params=add_params)

        return res["result"]

    def accountWithdraw(self, from_hash, to_hash, amount, auth_2fa_code=None):
        add_params = {"from_hash": from_hash,
                      "to_hash": to_hash, "amount": str(amount)}

        if auth_2fa_code is not None:
            add_params["auth_2fa_code"] = auth_2fa_code

        res = self.__call_api(method="account.withdraw", add_params=add_params)

        return res["result"]

    def transactionsList(self, max_count=None, offset=None):
        add_params = {}

        if max_count is not None:
            add_params["max_count"] = int(max_count)

        if offset is not None:
            add_params["offset"] = int(offset)

        res = self.__call_api(method="transaction.list", add_params=add_params)

        return res["result"]

    def rateList(self):
        res = self.__call_api(method="currency_pair.get_rate_list")

        return res["result"]["rates"]

    def couponList(self, max_count=None, offset=None):
        add_params = {}

        if max_count is not None:
            add_params["max_count"] = int(max_count)

        if offset is not None:
            add_params["offset"] = int(offset)

        res = self.__call_api(method="coupon.list", add_params=add_params)

        return res["result"]

    def couponApply(self, amount, coupon, currency):
        add_params = {"amount": str(
            amount), "coupon": coupon, "currency": currency}

        res = self.__call_api(method="coupon.apply", add_params=add_params)

        return res["result"]

    def couponCreate(self, amount, currency, password=None, receiver=None, comment=None):
        add_params = {"amount": str(amount), "currency": currency}

        if password is not None:
            add_params["password"] = password

        if receiver is not None:
            add_params['receiver'] = receiver

        if comment is not None:
            add_params["comment"] = comment

        res = self.__call_api(method="coupon.create", add_params=add_params)

        return res["result"]

    def couponRedeem(self, coupon, password=None):
        add_params = {"coupon": coupon}

        if password is not None:
            add_params["password"] = password

        res = self.__call_api(method="coupon.redeem", add_params=add_params)

        return res["result"]

    def couponCheck(self, coupon):
        add_params = {"coupon": coupon}

        res = self.__call_api(method="coupon.check", add_params=add_params)

        return res["result"]

    def miningList(self, max_count=None):
        add_params = {}

        if max_count is not None:
            add_params["max_count"] = int(max_count)

        res = self.__call_api(method='mining.list', add_params=add_params)

        return res["result"]

    def miningCreate(self, amount, hold=False, description=''):
        add_params = {"amount": str(amount),
                      "hold": False, "description": description}

        if hold is True:
            add_params["hold"] = True

        res = self.__call_api(method='mining.create', add_params=add_params)

        return res["result"]

    def userInfo(self):
        res = self.__call_api(method="user.info")

        return res["result"]

    def invoiceCancel(self, uuid):
        add_params = {"uuid": str(uuid)}

        res = self.__call_api(method="invoice.cancel", add_params=add_params)

        return res["result"]

    def invoiceApply(self, uuid):
        add_params = {"uuid": str(uuid)}

        res = self.__call_api(method="invoice.apply", add_params=add_params)

        return res["result"]

    def invoiceCreate(self, amount, currency, executor=None, description=None, expire_at=None):
        add_params = {"amount": str(amount), "currency": currency}

        if executor is not None:
            add_params["executor"] = executor

        if description is not None:
            add_params["description"] = description

        if expire_at is not None:
            add_params["expire_at"] = expire_at

        res = self.__call_api(method="invoice.create", add_params=add_params)

        return res["result"]

    def invoiceList(self, is_executor=False):
        add_params = {"is_executor": False}

        if is_executor is True:
            add_params["is_executor"] = True

        res = self.__call_api(method="invoice.list", add_params=add_params)

        return res["result"]

    def invoiceGet(self, uuid):
        add_params = {"uuid": str(uuid)}

        res = self.__call_api(method="invoice.get", add_params=add_params)

        return res["result"]
