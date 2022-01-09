from client_payment_sdk import ClientPaymentSDK, sign


api_secret = 'aa21444f3f71'
params = {
    'amount': '90',
    'merchant_id': '13',
    'order': 'fb11ff6c-7145-11ec-9e37-0242ac130022',
    'product_id': '15'
}

params['signature'] = sign('/init', 'POST', params, api_secret)

client = ClientPaymentSDK(None, api_secret)
html = client.init(params)

print(html)