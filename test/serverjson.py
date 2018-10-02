import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
import hashlib
sys.path.append("../")
from settings import KEY, SECRET_KEY, FROM_HASH, TO_HASH, COUPON_REDEEM, COUPON, COUPON_APPLY, UUID_CANCEL, UUID, UUID_APPLY

f = open('logfile.txt', 'a')


class wrapper:

    example = {"jsonrpc": "2.0", "result": {}, "id": 1}
    example_error = {"jsonrpc": "2.0", "error": {}, "id": None}

    def user_account_list(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        values = [
            {
                "balance": "0",
                "currency": "btc",
                "hash": "2N9nyspTXQmFXvMg4scNEWkU7FnTTQfWnyr",
                "type": "crypto"
            },
            {
                "balance": "0",
                "currency": "eth",
                "hash": "0xa274a71b6fa3b26f2faa03a20d5254f",
                "type": "crypto"
            }
        ]
        dump = dict(wrapper.example)

        if "max_count" in params.keys():
            dump["result"] = {"accounts": [values[0]]}
        else:
            dump["result"] = {"accounts": values}

        return dump

    def currency_convert(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        amount = None
        from_currency = None
        to_currency = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            amount = params["amount"]
            from_currency = params["from_currency"]
            to_currency = params["to_currency"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {"status": "ok"}

        return dump

    def account_withdraw(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        from_hash = None
        to_hash = None
        amount = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            from_hash = params["from_hash"]
            to_hash = params["to_hash"]
            amount = params["amount"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if from_hash != FROM_HASH or to_hash != TO_HASH:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33103, "message": "Hash not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "balance": "5.99999",
            "currency": "cnx",
            "hash": "mh7xBx3MBQvPkmsKwW3akAJk2CQFxzLmnh",
            "id": 38020,
            "user_id": 1299551335
        }

        return dump

    def transaction_list(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "summary": {
                "first_stamp": "2018-09-07 12:20:30.53858",
                "last_stamp": "2018-09-08 12:01:51.135346",
                "total": 12
            },
            "transactions": [
                {
                    "block_hash": "",
                    "from_amount": "1",
                    "from_commission": "0",
                    "from_currency": "cnx",
                    "from_hash": "mh7xBx3MBQvPkmsKwW3akAJk2CQFxzLmnh",
                    "id": 492971,
                    "post_stamp": "2018-09-08 12:01:51.135346",
                    "rate": "0",
                    "status": "complete",
                    "to_amount": "1",
                    "to_currency": "cnx",
                    "to_hash": "n2Kg2k6FrGtP1u8i8oQowm64FowuFJXEy9",
                    "tx_id": "",
                    "type": "transfer",
                    "update_stamp": "2018-09-08 12:01:51.31795"
                }
            ]
        }

        return dump

    def currency_pair_get_rate_list(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "rates": [
                {
                    'alias': 'BTC/GBP',
                    'ask': '4961.25',
                    'base_currency': 'btc',
                    'base_type': 'crypto',
                    'bid': '4765.39',
                    'convert_type': 'cancel',
                    'last_price': '0',
                    'rel_currency_id': 'gbp',
                    'rel_type': 'fiat',
                    'update_stamp': '2018-09-10 09:45:07.012473',
                    'value_last_24h': '0'
                }
            ]
        }

        return dump

    def coupon_list(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "coupons": [
                {
                    "amount": "2",
                    "code": "TSTCNX398C40D6032B4B4D9338700BD6AD65FD22",
                    "comment": "",
                    "create_at": "2018-09-08 10:24:24.24758",
                    "currency": "cnx",
                    "expire_at": "",
                    "password": False,
                    "receiver": "",
                    "redeem_at": "",
                    "status": "actived",
                    "type": "debit"
                }
            ],
            "summary": {
                "first_stamp": "2018-09-08 10:24:24.24758",
                "last_stamp": "2018-09-08 10:24:24.24758",
                "total": 1
            }
        }

        return dump

    def coupon_apply(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        amount = None
        coupon = None
        currency = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            amount = params["amount"]
            coupon = params["coupon"]
            currency = params["currency"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if coupon != COUPON_APPLY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33104, "message": "Coupon not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "0.005",
            "comment": "",
            "coupon": "CNXTST1111111111111111111111111111111120",
            "creator": "miyafodoxa@zep-hyr.com",
            "currency": "cnx",
            "expire_at": "",
            "password": True,
            "receiver": "",
            "redeem_at": "",
            "status": "actived",
            "type": "empty"
        }

        return dump

    def coupon_create(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        amount = None
        currency = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            amount = params["amount"]
            currency = params["currency"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "2",
            "comment": "",
            "coupon": "TSTCNX398C40D6032B4B4D9338700BD6AD65FD22",
            "creator": "miyafodoxa@zep-hyr.com",
            "currency": "cnx",
            "expire_at": "",
            "password": False,
            "receiver": "",
            "redeem_at": "",
            "status": "actived",
            "type": "debit"
        }

        return dump

    def coupon_redeem(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        coupon = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            coupon = params["coupon"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if coupon != COUPON_REDEEM:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33104, "message": "Coupon not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "2",
            "comment": "",
            "coupon": "TSTCNX398C40D6032B4B4D9338700BD6AD65FD22",
            "creator": "miyafodoxa@zep-hyr.com",
            "currency": "cnx",
            "expire_at": "",
            "password": False,
            "receiver": "",
            "redeem_at": "2018-09-08 10:39:08.841028",
            "status": "redeemed",
            "type": "debit"
        }

        return dump

    def coupon_check(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        coupon = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            coupon = params["coupon"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if coupon != COUPON:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33104, "message": "Coupon not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "2",
            "comment": "",
            "coupon": "TSTCNX398C40D6032B4B4D9338700BD6AD65FD22",
            "creator": "miyafodoxa@zep-hyr.com",
            "currency": "cnx",
            "expire_at": "",
            "password": False,
            "receiver": "",
            "redeem_at": "",
            "status": "actived",
            "type": "debit"
        }

        return dump

    def mining_list(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "minings": [
                {
                    "amount": "1",
                    "create_at": "2018-09-08 10:54:33.309776",
                    "description": "",
                    "hold_expire_at": "",
                    "id": 895,
                    "is_active": True,
                    "percent": 11,
                    "update_at": "2018-09-08 10:54:33.309776"
                }
            ],
            "summary": {
                "first_stamp": "2018-09-08 10:54:33.309776",
                "last_stamp": "2018-09-08 10:54:33.309776",
                "total": 1
            }
        }

        return dump

    def mining_create(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        amount = None
        hold = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            amount = params["amount"]
            hold = params["hold"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {"status": "ok"}

        return dump

    def user_info(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "auth_2fa": False,
            "deposit_auto_convert": True,
            "deposit_auto_mining": True,
            "eth_cnx_bonus": "0.0",
            "id": 1299551335,
            "login": "miyafodoxa@zep-hyr.com",
            "post_stamp": "2018-09-07 12:16:42.182827",
            "username": "miyafodoxa@zep-hyr.com"
        }

        return dump

    def invoice_cancel(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        uuid = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            uuid = params["uuid"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if uuid != UUID_CANCEL:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33105, "message": "Uuid not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "1",
            "creator": "miyafodoxa@zep-hyr.com",
            "currency": "cnx",
            "description": "",
            "expire_at": "",
            "status": "canceled_creator",
            "uuid": "2a2a1245-27c9-453b-82a7-182084aa272c"
        }

        return dump

    def invoice_apply(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        uuid = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            uuid = params["uuid"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if uuid != UUID_APPLY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33105, "message": "Uuid not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "1",
            "creator": "lade@fidelium10.com",
            "currency": "cnx",
            "description": "",
            "executor": "miyafodoxa@zep-hyr.com",
            "expire_at": "",
            "status": "completed",
            "uuid": "d9858136-7f1a-4bf9-a56f-4eac62691cdc"
        }

        return dump

    def invoice_create(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        amount = None
        currency = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            amount = params["amount"]
            currency = params["currency"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "1",
            "currency": "cnx",
            "description": "",
            "expire_at": "",
            "status": "created",
            "uuid": "2a2a1245-27c9-453b-82a7-182084aa272c"
        }

        return dump

    def invoice_list(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "invoices": [
                {
                    "amount": "1",
                    "create_at": "2018-09-08 11:23:15.932776",
                    "creator": "miyafodoxa@zep-hyr.com",
                    "currency": "cnx",
                    "description": "",
                    "expire_at": "",
                    "status": "canceled_creator",
                    "update_at": "2018-09-08 11:39:31.029991",
                    "uuid": "2a2a1245-27c9-453b-82a7-182084aa272c"
                },
                {
                    "amount": "1",
                    "create_at": "2018-09-08 11:13:20.953876",
                    "creator": "miyafodoxa@zep-hyr.com",
                    "currency": "cnx", "description": "",
                    "expire_at": "",
                    "status": "canceled_creator",
                    "update_at": "2018-09-08 11:13:28.460887",
                    "uuid": "39742096-057e-49a8-bfbb-e9090775834d"
                }
            ],
            "summary": {
                "first_stamp": "2018-09-08 11:13:20.953876",
                "last_stamp": "2018-09-08 11:23:15.932776",
                "total": 2
            }
        }

        return dump

    def invoice_get(query):
        method = query["method"]
        params = query["params"]

        key = None
        sign = None
        nonce = None
        uuid = None

        try:
            key = params["key"]
            sign = params["sign"]
            nonce = params["nonce"]
            uuid = params["uuid"]
        except KeyError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32602, "message": "Invalid params"}
            return dump_er

        if key != KEY:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33101, "message": "Key not valid"}
            return dump_er

        if not wrapper.check_sign(method, nonce, sign):
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33102, "message": "Sign not valid"}
            return dump_er

        if uuid != UUID:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -33105, "message": "Uuid not valid"}
            return dump_er

        dump = dict(wrapper.example)
        dump["result"] = {
            "amount": "1",
            "creator": "miyafodoxa@zep-hyr.com",
            "currency": "cnx",
            "description": "",
            "expire_at": "",
            "status": "canceled_creator",
            "uuid": "2a2a1245-27c9-453b-82a7-182084aa272c"
        }

        return dump

    def wrapper_run(query):
        if "method" not in query.keys() or "params" not in query.keys():
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32700, "message": "Parse error"}
            return dump_er

        method = query["method"].replace('.', '_')

        try:
            result = getattr(wrapper, method)(query)
        except AttributeError:
            dump_er = dict(wrapper.example_error)
            dump_er["error"] = {"code": -32601, "message": "Method not found"}
            return dump_er

        return result

    def check_sign(method, nonce, sign):
        my_sign = hashlib.sha256(method.encode(
            'utf-8') + str(nonce).encode('utf-8') + SECRET_KEY.encode('utf-8')).hexdigest()

        if sign != my_sign:
            return False

        return True


class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(wrapper.wrapper_run(message)).encode())


def run(server_class=HTTPServer, handler_class=Server, port=5000):
    sys.stderr = f
    sys.stdout = f
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        # print('Starting httpd on port %d...' % port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        httpd.socket.close()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
