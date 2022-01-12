# -*- coding: utf-8 -*-
from abc import ABC


class Model(ABC):
    def __init__(self, data):
        for key in self.__slots__:
            setattr(self, key, None)

        for key in data:
            if hasattr(self, key):
                setattr(self, key, data[key])

    def __repr__(self):
        state = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class InitPaymentResponse(Model):
    __slots__ = (
        'status',
        'payment_redirect_url',
        'url',
        'form_data'
    )


class StatusPaymentResponse(Model):
    __slots__ = (
        'status',
        'payment_status',
        'refund_status',
        'last_payment_error_code',
        'last_payment_error'
    )


class BalanceResponse(Model):
    __slots__ = (
        'status',
        'balance'
    )


class WithdrawalResponse(Model):
    __slots__ = (
        'status',
        'withdrawal_request'
    )


class StatusWithdrawalResponse(Model):
    __slots__ = (
        'status',
        'withdrawal_request'
    )


class WebhookData(Model):
    __slots__ = (
        'webhook_type',
        'amount',
        'product_id',
        'merchant_id',
        'order',
        'currency',
        'status',
        'webhook_id',
        'payment_error_code',
        'payment_error',
        'signature',
        'withdrawal_request_id',
        'requested_amount',
        'invoice_id',
        'customer_fee',
        'masked_pan'
    )
