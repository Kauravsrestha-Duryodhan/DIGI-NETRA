import requests
import re
from rich import print

url = 'https://accounts.google.com/v3/signin/_/AccountsSignInUi/data/batchexecute'
email = input("Enter Your Email:- ")

cookies = {
    'AEC': 'AVh_V2hiukcJVM-JlxkRoUDUlLdUmnkfIEeyxhKUB4N8G4g2NMpZsS_Eock',
    '__Host-GAPS': '1:Q3urfvTWXjkgya-BADq8_fXL2ky3bA:FIMs2Jb4EPAtTTE2'
    }

headers = {
    'Host': 'accounts.google.com',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
    'Sec-Ch-Ua-Bitness': '""',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Mobile': '?0',
    'X-Same-Domain': '1',
    'Sec-Ch-Ua-Wow64': '?0',
    'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
    'Sec-Ch-Ua-Arch': '""',
    'Sec-Ch-Ua-Full-Version': '""',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'X-Goog-Ext-391502476-Jspb': '["S-955298194:1753880046067247",null,null,"AdBytiOuclqqSRRLJBg1eAWJUdKMa1kRng0M_jA84ZuXN-7X-YwckiXC-PqxZ6YAS_MFBUTHXirR"]',
    'Accept-Language': 'en-GB,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform-Version': '""',
    'Accept': '*/*',
    'Origin': 'https://accounts.google.com',
    'X-Client-Data': 'CKjwygE=',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://accounts.google.com/',
    'Priority': 'u=1, i',
}

params = {
    'rpcids': 'MI613e',
    'source-path': '/v3/signin/identifier',
    'f.sid': '-7509014708489656482',
    'bl': 'boq_identityfrontendauthuiserver_20250727.08_p0',
    'hl': 'en',
    '_reqid': '266248',
    'rt': 'c',
}

data = f'f.req=%5B%5B%5B%22MI613e%22%2C%22%5Bnull%2C%5C%22{email}%5C%22%2C1%2Cnull%2Cnull%2C1%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22%5C%22%2C%5C%22IN%5C%22%2Cnull%2C%5B%5C%22youtube%3A935%5C%22%2C%5C%22youtube%5C%22%2C1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C7%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5C%22S-955298194%3A1753880046067247%5C%22%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C1%2C1%5D%2C%5B%5B%5C%22identity-signin-identifier%5C%22%2C%5C%22!NzSlNGzNAAbs-qk5zPpCZQ8L4faYNNI7ADQBEArZ1Ieu1UFXN7zujnkXDtV4j1tgUt5lX5X9fBmTaaSlxVTye6fZFI6RqCdIIK2CCv9qAgAAAEtSAAAHYmgBB34AS_X9g-VptoEk7and8udWbfyt4UlohLMsCzvQwFn09Zkv8BcqMFs2UMilNmh3f5UdX4Iu1YyVw6ZYcErcBqW7kaP7Uy-RtuITlpQb75kHzTUTEW006RdyWUVEMpX0Da94fuMsCH7CPuL7AO6XLIJf9b5OglJeZWr_nyu0ag-jX7czW1RTJYhSNzNmysvOVhwIDmduD_S_Ss_EWtipZVJwgBrwvyNtgGJzvwFReuyPGdQCu5_e7j__Rnicgpf2QO1WzeGlIthI1zBOhO1tX_YF3MlGBiylO1E0qOi0TNx05BtgnARDEgMcLi4tzmlBERsKvvV6Cmq4Oc8J24McUGVjbTgBChYIn2QRWEtuEl_nXYltR30N9KdTyEYzfsr0GPCuZwijXUGyxmGZQQV2syKR08oeE5EoorkqQG24Uz8G-k2qiO_0zNAKmHpNCXgMXf1ax0BKWkICkXSSXTN2N_ugVGgVxMIlttMWlTTfL6bGhK3JT5akD4ymxKt2iYrRoGun7cmv2IBPSZG2Di1n2RF2XW0FGThArZR-3Jt4t3WiDKEiP8T0TqDRE_WJQ4helpgbwkPWlSMPU3_ZviIndHG0uIuQecbB_LuHt_KOBLsp5c-l1AWiiyYMFENB8mXEOWQQmWVSyXZ2_G0V6O0ofu0yGJOdQWyizXWAgoRUDdg0g7LCO3M7ctb-8dU54HLo7DidiqgBSGMwVcx2_m5Qv5jiblfXTqIrB8vKIAkRtlsKz41EdMlzwsJ92_QhmFSxyQLkv7WmJcWetM5VAg4lnvs4jUbL-WcbW05I3Oi2msp6Dsit_SgKan8UNB7UocKdXwy4mKOnBPJLZwEVvIK395Pf4B5UVhabsDFbMhURxzby0-vDWtMBgygq_rLyCkTmNs33HeIcJviZWd0rKLEiLl3ssJoH99hSNdYh2quX75edk__tSwR-8Jxy6FNN39su2m6q4pOUnjFsHVZCOr5avt8bvE9hImLVVk3FnS9KMA7yEqgoCybiW91G37oLrNu6c0_M1FsbX1Er0k5rRJtXHSzF_rS_4Sv6V2PQB12WMC62FdKMySxPCpMZz625tZWnlfm2C1GPJwT94VTBCQnblEbKZWPGgg3rgYwDn4pKU7G8OagJ62Di99OWttpIYoG2vuxQ4pbQYPA0OUksv6J-HiLlMdHXwVkC8sSixdr-WD-bx_M-b80JPfNafKnmriANuHoIegsMuMMluYnvOVaSKg5kH_hAlGbtU7Qbu5hBMeqgnQPIOpeKBwh1fXBMp4GmRG1eax29EvBfL80Sy5kM-kHjiUqqoNatTa5sdV5PFH17qmVu2UblVqZYOwnh00XYvKgYJBK9Nt2DOZuNPR5OTN2dAIWCosahkouFLUL5gRnmP473u5r7FloAeUv0zwjL3L33ivudzS36fMI6CWd9uKRROTeSfhw6a-Sr3Ywg-RGBjQjAiQMpEQClKtEX2gl49rVJ4vAsgkQP83NUaBgcKrQfct1n1HPWceY2RvT3sXWeMWeEczgRxLjxhYNq4Kj4quOrJKcbfSgUPzcA5X3F6PLrbl91kvzP6TpCO5bvRiozUgwQKuRC2-1UMolIecHMKxPLbul4U57kMfvrnpVIK3-lCtVHGoBcz-JxIuRQkhzEeYATQEdYY5Bmitfk8Leg7y15k4lPfhxjTNwW36-EUr0hNzBSGv6akSoxDSjojJGdhRfmUllxp6R8T0mqRfhbBbOwEqF2AKMY_046qx_xSw8uR6eccl0ABsDn4F1b42-y9VvKnu3Q1qZyjJCCUlF66k3cJ8wJ04Z6nS5JkfeptC7GHroXrOAf5FAwtVl1dkkfkO5th4xjeWkkssq1DSs0go6ONwRXknNUGceqrD5-HDTbIJn9gHK39K-gZ2QdQL0GgpQHpl8jAbKIOePw4D55uZ48rotVqODNLVeRGlgIvirQ297KqteU4rsrJaG_j4JJyozVQIZJ11VJrYnP2iloiCFgO2R3Mg0o3_iINxGsf7jn22ao6EetnuUtwIlpVRiOJmQyoHuGxFSUKgvIl9QkVlr0teWliMocIexpXYI0IYG7QwEblTB_9oAkJEJQeYgkggpYYu5To61lKMvFZF7Zh9AHx_mBuTclYWLE4NQ1eOU1Omaq7ogx59XaBtM4-e1XAzFIw9NuESMU8WHWfSu67i2tfm-XHBQEW464wBxrgE5kR7jPzsL0CiYt6YUDcFyWMjKbOO1bkMF_jjFDXp7jLJ2Lyw8PZTzb3j648LZbMGQ6bHgeJqv5uM6xCZYDQmJC63uIf2BsnzBTNDGl5gzYqOZCcyG14iM31OujjFEdi-InSf_vBfuMLk82R5he0kUnQUTjgFTi7gw9l-ZSEIv8kL6As5wJfqDJM6228_GbOfInY2NUzz84C1eE2VadcBLFU3kM5h-3HNpF5-MNs8wV6wiQTXlTiAhkj1bLXxDlFCSHN_92HgO5bluAQ3kYw7HHqh7-57xZF1TMoVdHPie-kfma0g2h5xvsuC8bepNVQ0ehJdwByRV9PPZXrg_2shJzN2rGspQwljLyzTZyxYjBBzuDXd-LE3E_1i2WeG3f_LAAYQIHoI_OskhHU0f48e0fKyKYkNXvYSeokhuk8uW2Cmk2s0epMKmP3yX45e45bvdf_wKQbXQXoPMDCrHBKipBu3UXR2JmzLpUN149iRxYfaXAIaOaT4XCrxoarwMnN76m0ypH2K8yXzf23i_wYkhd6ZSCVqgwIPUETPt6S2p3hDl0NA6OIXoLpXCEq8rZ%5C%22%5D%5D%2C%5B%5Bnull%2Cnull%2Cnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%5D%2C%5Bnull%2Cnull%2C%5C%22S-955298194%3A1753880046067247%5C%22%2C%5C%22ServiceLogin%5C%22%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%2Cnull%2C%5B%5B%5C%22continue%5C%22%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%5D%2C%5B%5C%22ec%5C%22%2C%5C%22futura_exp_og_so_72776762_e%5C%22%5D%2C%5B%5C%22hl%5C%22%2C%5C%22en%5C%22%5D%2C%5B%5C%22ifkv%5C%22%2C%5C%22AdBytiOuclqqSRRLJBg1eAWJUdKMa1kRng0M_jA84ZuXN-7X-YwckiXC-PqxZ6YAS_MFBUTHXirR%5C%22%5D%2C%5B%5C%22passive%5C%22%2C%5C%22true%5C%22%5D%2C%5B%5C%22flowName%5C%22%2C%5C%22GlifWebSignIn%5C%22%5D%2C%5B%5C%22flowEntry%5C%22%2C%5C%22ServiceLogin%5C%22%5D%2C%5B%5C%22dsh%5C%22%2C%5C%22S-955298194%3A1753880046067247%5C%22%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C%5B%5B%5C%22continue%5C%22%2C%5B%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%5D%5D%2C%5B%5C%22ec%5C%22%2C%5B%5C%22futura_exp_og_so_72776762_e%5C%22%5D%5D%2C%5B%5C%22hl%5C%22%2C%5B%5C%22en%5C%22%5D%5D%2C%5B%5C%22ifkv%5C%22%2C%5B%5C%22AdBytiOuclqqSRRLJBg1eAWJUdKMa1kRng0M_jA84ZuXN-7X-YwckiXC-PqxZ6YAS_MFBUTHXirR%5C%22%5D%5D%2C%5B%5C%22passive%5C%22%2C%5B%5C%22true%5C%22%5D%5D%2C%5B%5C%22flowName%5C%22%2C%5B%5C%22GlifWebSignIn%5C%22%5D%5D%2C%5B%5C%22flowEntry%5C%22%2C%5B%5C%22ServiceLogin%5C%22%5D%5D%2C%5B%5C%22dsh%5C%22%2C%5B%5C%22S-955298194%3A1753880046067247%5C%22%5D%5D%5D%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%5D%2Cnull%2C%5C%22S-955298194%3A1753880046067247%5C%22%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22true%5C%22%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AEObw43uILK0ky5bocuLDmIwx0xG%3A1753880046226&'

# Send the request
response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data)

# Check response using regex
if re.search(r'/v3/signin/rejected', response.text):
    print("Not registered")
else:
    print("Email is registered")
