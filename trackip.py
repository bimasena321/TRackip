import requests
import json



R = '\033[31m' #merah
W = '\033[0m' #putih


print(f"""{R}
████████╗██████╗  █████╗  ██████╗██╗  ██╗        ██╗██████╗     
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝        ██║██╔══██╗    
   ██║   ██████╔╝███████║██║     █████╔╝         ██║██████╔╝    
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗         ██║██╔═══╝     
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║██║         
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝         
                                                                
=============================================================
Github: https://github.com/bimasena321
Youtube: bima020
created by: bima020
""")

i = input(f"{W}Masukan ip addres: ")
key = '1a9dea3fe1404a4e920b79b3bd83bbff'
url = f'https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={i}'
url_requests = requests.get(f"{url}")
if url_requests.status_code == 200:
    data = json.loads(url_requests.text)
    print(f"{R}ip: ",data['ip'])
    print(f"{R}negara: ", data['country_name'])
    print(f"{R}ibukota: ", data['country_capital'])
    #print(f"{R}hotname: ", data['hostname'])
    print(f"{R}kecamatan: ", data['district'])
    print(f"{R}provinsi: ", data['state_prov'])
    print(f"{R}kota: ", data['city'])
    print(f"{R}zip_code: ", data['zipcode'])
    print(f"{R}latitude && logtitude: ", data['latitude'],",", data['longitude'])
    print(f"{W}kode_telpon: ", data['calling_code'])
    print(f"{W}kode_internet: ", data['country_tld'])
    print(f"{W}isp: ", data['isp'])
    print(f"{W}mata uang: ",data[f'currency'])
    print(f"{W}zona waktu: ",data['time_zone'])
    print(f"{W}kontinen: ",data['continent_code'])


