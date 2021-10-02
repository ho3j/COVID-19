"""
COVID-19 and VACCINE in Iran & Usa & World
from API disease.sh
Hossein JALILI
mehr 1400
ver 1.0
"""
import requests

################################covid-19 world#################################
api_covid = "https://disease.sh/v3/covid-19/all"
json_data=requests.get(api_covid).json()
#print(json_data)
updated=str(json_data['updated'])
cases=str(json_data['cases'])
todayCases=str(json_data['todayCases'])
deaths=str(json_data['deaths'])
todayDeaths=str(json_data['todayDeaths'])
recovered=str(json_data['recovered'])
todayRecovered=str(json_data['todayRecovered'])
active=str(json_data['active'])
critical=str(json_data['critical'])
casesPerOneMillion=str(json_data['casesPerOneMillion'])
deathsPerOneMillion=str(json_data['deathsPerOneMillion'])
tests=str(json_data['tests'])
testsPerOneMillion=str(json_data['testsPerOneMillion'])
population=str(json_data['population'])
activePerOneMillion=str(json_data['activePerOneMillion'])
recoveredPerOneMillion=str(json_data['recoveredPerOneMillion'])
criticalPerOneMillion=str(json_data['criticalPerOneMillion'])
affectedCountries=str(json_data['affectedCountries'])

print("\n\tcovid-19 in worldwide".upper())
print("-----------------------------------------")
print("Updated \t\t",updated)
print("Cases\t\t\t",cases)
print("TodayCases\t\t",todayCases)
print("Deaths\t\t\t",deaths)
print("TodayDeaths\t\t",todayDeaths)
print("Rrecovered\t\t",recovered)
print("TodayRecovered\t\t",todayRecovered)
print("Active\t\t\t",active)
print("Critical\t\t",critical)
print("CasesPerOneMillion\t",casesPerOneMillion)
print("DeathsPerOneMillion\t",deathsPerOneMillion)
print("Tests\t\t\t",tests)
print("TestsPerOneMillion\t",testsPerOneMillion) 
print("Population\t\t",population)
print("ActivePerOneMillion\t",activePerOneMillion)
print("RecoveredPerOneMillion\t",recoveredPerOneMillion)
print("CriticalPerOneMillion\t",criticalPerOneMillion)
print("AffectedCountries\t",affectedCountries)
print("-----------------------------------------")
print("\n\n")

################################covid-19 usa #################################
api_covid_usa = "https://disease.sh/v3/covid-19/countries/usa"
json_data_usa=requests.get(api_covid_usa).json()
#print(json_data_usa)

updated_usa=str(json_data_usa['updated'])
cases_usa=str(json_data_usa['cases'])
todayCases_usa=str(json_data_usa['todayCases'])
deaths_usa=str(json_data_usa['deaths'])
todayDeaths_usa=str(json_data_usa['todayDeaths'])
recovered_usa=str(json_data_usa['recovered'])
todayRecovered_usa=str(json_data_usa['todayRecovered'])
active_usa=str(json_data_usa['active'])
critical_usa=str(json_data_usa['critical'])
casesPerOneMillion_usa=str(json_data_usa['casesPerOneMillion'])
deathsPerOneMillion_usa=str(json_data_usa['deathsPerOneMillion'])
test_usa=str(json_data_usa['tests'])
testsPerOneMillion_usa=str(json_data_usa['testsPerOneMillion'])
population_usa=str(json_data_usa['population'])
continent_usa=str(json_data_usa['continent'])
oneCasePerPeople_usa=str(json_data_usa['oneCasePerPeople'])
oneDeathPerPeople_usa=str(json_data_usa['oneDeathPerPeople'])
oneTestPerPeople_usa=str(json_data_usa['oneTestPerPeople'])
activePerOneMillion_usa=str(json_data_usa['activePerOneMillion'])
recoveredPerOneMillion_usa=str(json_data_usa['recoveredPerOneMillion'])
criticalPerOneMillion_usa=str(json_data_usa['criticalPerOneMillion'])


print("\tcovid-19 in usa ".upper())
print("-----------------------------------------")
print("Updated \t\t",updated_usa)
print("Cases\t\t\t",cases_usa)
print("TodayCases\t\t",todayCases_usa)
print("Deaths\t\t\t",deaths_usa)
print("TodayDeaths\t\t",todayDeaths_usa)
print("Rrecovered\t\t",recovered_usa)
print("TodayRecovered\t\t",todayRecovered_usa)
print("Active\t\t\t",active_usa)
print("Critical\t\t",critical_usa)
print("CasesPerOneMillion\t",casesPerOneMillion_usa)
print("DeathsPerOneMillion\t",deathsPerOneMillion_usa)
print("Tests\t\t\t",test_usa)
print("TestsPerOneMillion\t",testsPerOneMillion_usa) 
print("Population\t\t",population_usa)
print("Continent\t\t",continent_usa)
print("OneCasePerPeople\t",oneCasePerPeople_usa)
print("OneCasePerPeople\t",oneCasePerPeople_usa)
print("OneCasePerPeople\t",oneCasePerPeople_usa)
print("ActivePerOneMillion\t",activePerOneMillion_usa)
print("RecoveredPerOneMillion\t",recoveredPerOneMillion_usa)
print("CriticalPerOneMillion\t",criticalPerOneMillion_usa)

print("-----------------------------------------")
print("\n\n")


################################covid-19 iran #################################
api_covid_ir = "https://disease.sh/v3/covid-19/countries/iran"
json_data_ir=requests.get(api_covid_ir).json()
#print(json_data_ir)

updated_ir=str(json_data_ir['updated'])
cases_ir=str(json_data_ir['cases'])
todayCases_ir=str(json_data_ir['todayCases'])
deaths_ir=str(json_data_ir['deaths'])
todayDeaths_ir=str(json_data_ir['todayDeaths'])
recovered_ir=str(json_data_ir['recovered'])
todayRecovered_ir=str(json_data_ir['todayRecovered'])
active_ir=str(json_data_ir['active'])
critical_ir=str(json_data_ir['critical'])
casesPerOneMillion_ir=str(json_data_ir['casesPerOneMillion'])
deathsPerOneMillion_ir=str(json_data_ir['deathsPerOneMillion'])
test_ir=str(json_data_ir['tests'])
testsPerOneMillion_ir=str(json_data_ir['testsPerOneMillion'])
population_ir=str(json_data_ir['population'])
continent_ir=str(json_data_ir['continent'])
oneCasePerPeople_ir=str(json_data_ir['oneCasePerPeople'])
oneDeathPerPeople_ir=str(json_data_ir['oneDeathPerPeople'])
oneTestPerPeople_ir=str(json_data_ir['oneTestPerPeople'])
activePerOneMillion_ir=str(json_data_ir['activePerOneMillion'])
recoveredPerOneMillion_ir=str(json_data_ir['recoveredPerOneMillion'])
criticalPerOneMillion_ir=str(json_data_ir['criticalPerOneMillion'])


print("\tcovid-19 in iran ".upper())
print("-----------------------------------------")
print("Updated \t\t",updated_ir)
print("Cases\t\t\t",cases_ir)
print("TodayCases\t\t",todayCases_ir)
print("Deaths\t\t\t",deaths_ir)
print("TodayDeaths\t\t",todayDeaths_ir)
print("Rrecovered\t\t",recovered_ir)
print("TodayRecovered\t\t",todayRecovered_ir)
print("Active\t\t\t",active_ir)
print("Critical\t\t",critical_ir)
print("CasesPerOneMillion\t",casesPerOneMillion_ir)
print("DeathsPerOneMillion\t",deathsPerOneMillion_ir)
print("Tests\t\t\t",test_ir)
print("TestsPerOneMillion\t",testsPerOneMillion_ir) 
print("Population\t\t",population_ir)
print("Continent\t\t",continent_ir)
print("OneCasePerPeople\t",oneCasePerPeople_ir)
print("OneCasePerPeople\t",oneCasePerPeople_ir)
print("OneCasePerPeople\t",oneCasePerPeople_ir)
print("ActivePerOneMillion\t",activePerOneMillion_ir)
print("RecoveredPerOneMillion\t",recoveredPerOneMillion_ir)
print("CriticalPerOneMillion\t",criticalPerOneMillion_ir)

print("-----------------------------------------")
print("\n\n")



################################vaccine#################################
api_vaccine="https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1"
json_data_vaccine=requests.get(api_vaccine).json()
# iran=json_data_vaccine[91]['timeline'].values() #Iran
# iran=list(json_data_vaccine[91]['timeline'].values())[0]
# usa=list(json_data_vaccine[206]['timeline'].values())[0]
# uk=list(json_data_vaccine[205]['timeline'].values())[0]

Afghanistan=list(json_data_vaccine[0]['timeline'].values())[0]
Albania=list(json_data_vaccine[1]['timeline'].values())[0]
Algeria=list(json_data_vaccine[2]['timeline'].values())[0]
Andorra=list(json_data_vaccine[3]['timeline'].values())[0]
Angola=list(json_data_vaccine[4]['timeline'].values())[0]
Anguilla=list(json_data_vaccine[5]['timeline'].values())[0]
Antigua_and_Barbuda=list(json_data_vaccine[6]['timeline'].values())[0]
Argentina=list(json_data_vaccine[7]['timeline'].values())[0]
Armenia=list(json_data_vaccine[8]['timeline'].values())[0]
Aruba=list(json_data_vaccine[9]['timeline'].values())[0]
Australia=list(json_data_vaccine[10]['timeline'].values())[0]
Austria=list(json_data_vaccine[11]['timeline'].values())[0]
Azerbaijan=list(json_data_vaccine[12]['timeline'].values())[0]
Bahamas=list(json_data_vaccine[13]['timeline'].values())[0]
Bahrain=list(json_data_vaccine[14]['timeline'].values())[0]
Bangladesh=list(json_data_vaccine[15]['timeline'].values())[0]
Barbados=list(json_data_vaccine[16]['timeline'].values())[0]
Belarus=list(json_data_vaccine[17]['timeline'].values())[0]
Belgium=list(json_data_vaccine[18]['timeline'].values())[0]
Belize=list(json_data_vaccine[19]['timeline'].values())[0]
Benin=list(json_data_vaccine[20]['timeline'].values())[0]
Bermuda=list(json_data_vaccine[21]['timeline'].values())[0]
Bhutan=list(json_data_vaccine[22]['timeline'].values())[0]
Bolivia=list(json_data_vaccine[23]['timeline'].values())[0]
Caribbean_Netherlands=list(json_data_vaccine[24]['timeline'].values())[0]
Bosnia=list(json_data_vaccine[25]['timeline'].values())[0]
Botswana=list(json_data_vaccine[26]['timeline'].values())[0]
Brazil=list(json_data_vaccine[27]['timeline'].values())[0]
British_Virgin_Islands=list(json_data_vaccine[28]['timeline'].values())[0]
Brunei=list(json_data_vaccine[29]['timeline'].values())[0]
Bulgaria=list(json_data_vaccine[30]['timeline'].values())[0]
Burkina_Faso=list(json_data_vaccine[31]['timeline'].values())[0]
Cambodia=list(json_data_vaccine[32]['timeline'].values())[0]
Cameroon=list(json_data_vaccine[33]['timeline'].values())[0]
Canada=list(json_data_vaccine[34]['timeline'].values())[0]
Cabo_Verde=list(json_data_vaccine[35]['timeline'].values())[0]
Cayman_Islands=list(json_data_vaccine[36]['timeline'].values())[0]
Central_African_Republic=list(json_data_vaccine[37]['timeline'].values())[0]
Chad=list(json_data_vaccine[38]['timeline'].values())[0]
Chile=list(json_data_vaccine[39]['timeline'].values())[0]
China=list(json_data_vaccine[40]['timeline'].values())[0]
Colombia=list(json_data_vaccine[41]['timeline'].values())[0]
Comoros=list(json_data_vaccine[42]['timeline'].values())[0]
Congo=list(json_data_vaccine[43]['timeline'].values())[0]
Cook_Islands=list(json_data_vaccine[44]['timeline'].values())[0]
Costa_Rica=list(json_data_vaccine[45]['timeline'].values())[0]
Cote_d_Ivoire=list(json_data_vaccine[46]['timeline'].values())[0]
Croatia=list(json_data_vaccine[47]['timeline'].values())[0]
Cuba=list(json_data_vaccine[48]['timeline'].values())[0]
Curacao=list(json_data_vaccine[49]['timeline'].values())[0]
Cyprus=list(json_data_vaccine[50]['timeline'].values())[0]
Czechia=list(json_data_vaccine[51]['timeline'].values())[0]
DRCc=list(json_data_vaccine[52]['timeline'].values())[0]
Denmark=list(json_data_vaccine[53]['timeline'].values())[0]
Djibouti=list(json_data_vaccine[54]['timeline'].values())[0]
Dominica=list(json_data_vaccine[55]['timeline'].values())[0]
Dominican_Republic=list(json_data_vaccine[56]['timeline'].values())[0]
Ecuador=list(json_data_vaccine[57]['timeline'].values())[0]
Egypt=list(json_data_vaccine[58]['timeline'].values())[0]
El_Salvador=list(json_data_vaccine[59]['timeline'].values())[0]
Equatorial_Guinea=list(json_data_vaccine[60]['timeline'].values())[0]
Estonia=list(json_data_vaccine[61]['timeline'].values())[0]
Swaziland=list(json_data_vaccine[62]['timeline'].values())[0]
Ethiopia=list(json_data_vaccine[63]['timeline'].values())[0]
Faroe_Islands=list(json_data_vaccine[64]['timeline'].values())[0]
Falkland__Islands=list(json_data_vaccine[65]['timeline'].values())[0]
Fiji=list(json_data_vaccine[66]['timeline'].values())[0]
Finland=list(json_data_vaccine[67]['timeline'].values())[0]
France=list(json_data_vaccine[68]['timeline'].values())[0]
French_Polynesia=list(json_data_vaccine[69]['timeline'].values())[0]
Gabon=list(json_data_vaccine[70]['timeline'].values())[0]
Gambia=list(json_data_vaccine[71]['timeline'].values())[0]
Georgia=list(json_data_vaccine[72]['timeline'].values())[0]
Germany=list(json_data_vaccine[73]['timeline'].values())[0]
Ghana=list(json_data_vaccine[74]['timeline'].values())[0]
Gibraltar=list(json_data_vaccine[75]['timeline'].values())[0]
Greece=list(json_data_vaccine[76]['timeline'].values())[0]
Greenland=list(json_data_vaccine[77]['timeline'].values())[0]
Grenada=list(json_data_vaccine[78]['timeline'].values())[0]
Guatemala=list(json_data_vaccine[79]['timeline'].values())[0]
Guernsey=list(json_data_vaccine[80]['timeline'].values())[0]
Guinea=list(json_data_vaccine[81]['timeline'].values())[0]
Guinea_Bissau=list(json_data_vaccine[82]['timeline'].values())[0]
Guyana=list(json_data_vaccine[83]['timeline'].values())[0]
Haiti=list(json_data_vaccine[84]['timeline'].values())[0]
Honduras=list(json_data_vaccine[85]['timeline'].values())[0]
Hong_Kong=list(json_data_vaccine[86]['timeline'].values())[0]
Hungary=list(json_data_vaccine[87]['timeline'].values())[0]
Iceland=list(json_data_vaccine[88]['timeline'].values())[0]
India=list(json_data_vaccine[89]['timeline'].values())[0]
Indonesia=list(json_data_vaccine[90]['timeline'].values())[0]
Iran=list(json_data_vaccine[91]['timeline'].values())[0]
Iraq=list(json_data_vaccine[92]['timeline'].values())[0]
Ireland=list(json_data_vaccine[93]['timeline'].values())[0]
Isle_of_Man=list(json_data_vaccine[94]['timeline'].values())[0]
Israel=list(json_data_vaccine[95]['timeline'].values())[0]
Italy=list(json_data_vaccine[96]['timeline'].values())[0]
Jamaica=list(json_data_vaccine[97]['timeline'].values())[0]
Japan=list(json_data_vaccine[98]['timeline'].values())[0]
Channel_Islands=list(json_data_vaccine[99]['timeline'].values())[0]
Jordan=list(json_data_vaccine[100]['timeline'].values())[0]
Kazakhstan=list(json_data_vaccine[101]['timeline'].values())[0]
Kenya=list(json_data_vaccine[102]['timeline'].values())[0]
Kiribati=list(json_data_vaccine[103]['timeline'].values())[0]
Kuwait=list(json_data_vaccine[104]['timeline'].values())[0]
Kyrgyzstan=list(json_data_vaccine[105]['timeline'].values())[0]
Lao_Peoples_Democratic_Republic=list(json_data_vaccine[106]['timeline'].values())[0]
Latvia=list(json_data_vaccine[107]['timeline'].values())[0]
Lebanon=list(json_data_vaccine[108]['timeline'].values())[0]
Lesotho=list(json_data_vaccine[109]['timeline'].values())[0]
Liberia=list(json_data_vaccine[110]['timeline'].values())[0]
Libyan_Arab_Jamahiriya=list(json_data_vaccine[111]['timeline'].values())[0]
Liechtenstein=list(json_data_vaccine[112]['timeline'].values())[0]
Lithuania=list(json_data_vaccine[113]['timeline'].values())[0]
Luxembourg=list(json_data_vaccine[114]['timeline'].values())[0]
Macao=list(json_data_vaccine[115]['timeline'].values())[0]
Madagascar=list(json_data_vaccine[116]['timeline'].values())[0]
Malawi=list(json_data_vaccine[117]['timeline'].values())[0]
Malaysia=list(json_data_vaccine[118]['timeline'].values())[0]
Maldives=list(json_data_vaccine[119]['timeline'].values())[0]
Mali=list(json_data_vaccine[120]['timeline'].values())[0]
Malta=list(json_data_vaccine[121]['timeline'].values())[0]
Mauritania=list(json_data_vaccine[122]['timeline'].values())[0]
Mauritius=list(json_data_vaccine[123]['timeline'].values())[0]
Mexico=list(json_data_vaccine[124]['timeline'].values())[0]
Moldova=list(json_data_vaccine[125]['timeline'].values())[0]
Monaco=list(json_data_vaccine[126]['timeline'].values())[0]
Mongolia=list(json_data_vaccine[127]['timeline'].values())[0]
Montenegro=list(json_data_vaccine[128]['timeline'].values())[0]
Montserrat=list(json_data_vaccine[129]['timeline'].values())[0]
Morocco=list(json_data_vaccine[130]['timeline'].values())[0]
Mozambique=list(json_data_vaccine[131]['timeline'].values())[0]
Myanmar=list(json_data_vaccine[132]['timeline'].values())[0]
Namibia=list(json_data_vaccine[133]['timeline'].values())[0]
Nauru=list(json_data_vaccine[134]['timeline'].values())[0]
Nepal=list(json_data_vaccine[135]['timeline'].values())[0]
Netherlands=list(json_data_vaccine[136]['timeline'].values())[0]
New_Caledonia=list(json_data_vaccine[137]['timeline'].values())[0]
New_Zealand=list(json_data_vaccine[138]['timeline'].values())[0]
Nicaragua=list(json_data_vaccine[139]['timeline'].values())[0]
Niger=list(json_data_vaccine[140]['timeline'].values())[0]
Nigeria=list(json_data_vaccine[141]['timeline'].values())[0]
Niue=list(json_data_vaccine[142]['timeline'].values())[0]
Macedonia=list(json_data_vaccine[143]['timeline'].values())[0]
Norway=list(json_data_vaccine[144]['timeline'].values())[0]
Oman=list(json_data_vaccine[145]['timeline'].values())[0]
Pakistan=list(json_data_vaccine[146]['timeline'].values())[0]
Palestine=list(json_data_vaccine[147]['timeline'].values())[0]
Panama=list(json_data_vaccine[148]['timeline'].values())[0]
Papua_New_Guinea=list(json_data_vaccine[149]['timeline'].values())[0]
Paraguay=list(json_data_vaccine[150]['timeline'].values())[0]
Peru=list(json_data_vaccine[151]['timeline'].values())[0]
Philippines=list(json_data_vaccine[152]['timeline'].values())[0]
Pitcairn=list(json_data_vaccine[153]['timeline'].values())[0]
Poland=list(json_data_vaccine[154]['timeline'].values())[0]
Portugal=list(json_data_vaccine[155]['timeline'].values())[0]
Qatar=list(json_data_vaccine[156]['timeline'].values())[0]
Romania=list(json_data_vaccine[157]['timeline'].values())[0]
Russia=list(json_data_vaccine[158]['timeline'].values())[0]
Rwanda=list(json_data_vaccine[159]['timeline'].values())[0]
Saint_Helena=list(json_data_vaccine[160]['timeline'].values())[0]
Saint_Kitts_and_Nevis=list(json_data_vaccine[161]['timeline'].values())[0]
Saint_Lucia=list(json_data_vaccine[162]['timeline'].values())[0]
Saint_Vincent_and_the_Grenadines=list(json_data_vaccine[163]['timeline'].values())[0]
Samoa=list(json_data_vaccine[164]['timeline'].values())[0]
San_Marino=list(json_data_vaccine[165]['timeline'].values())[0]
Sao_Tome_and_Principe=list(json_data_vaccine[166]['timeline'].values())[0]
Saudi_Arabia=list(json_data_vaccine[167]['timeline'].values())[0]
Senegal=list(json_data_vaccine[168]['timeline'].values())[0]
Serbia=list(json_data_vaccine[169]['timeline'].values())[0]
Seychelles=list(json_data_vaccine[170]['timeline'].values())[0]
Sierra_Leone=list(json_data_vaccine[171]['timeline'].values())[0]
Singapore=list(json_data_vaccine[172]['timeline'].values())[0]
Sint_Maarten=list(json_data_vaccine[173]['timeline'].values())[0]
Slovakia=list(json_data_vaccine[174]['timeline'].values())[0]
Slovenia=list(json_data_vaccine[175]['timeline'].values())[0]
Solomon_Islands=list(json_data_vaccine[176]['timeline'].values())[0]
Somalia=list(json_data_vaccine[177]['timeline'].values())[0]
South_Africa=list(json_data_vaccine[178]['timeline'].values())[0]
S_Korea=list(json_data_vaccine[179]['timeline'].values())[0]
South_Sudan=list(json_data_vaccine[180]['timeline'].values())[0]
Spain=list(json_data_vaccine[181]['timeline'].values())[0]
Sri_Lanka=list(json_data_vaccine[182]['timeline'].values())[0]
Sudan=list(json_data_vaccine[183]['timeline'].values())[0]
Suriname=list(json_data_vaccine[184]['timeline'].values())[0]
Sweden=list(json_data_vaccine[185]['timeline'].values())[0]
Switzerland=list(json_data_vaccine[186]['timeline'].values())[0]
Syrian=list(json_data_vaccine[187]['timeline'].values())[0]
Taiwan=list(json_data_vaccine[188]['timeline'].values())[0]
Tajikistan=list(json_data_vaccine[189]['timeline'].values())[0]
Tanzania=list(json_data_vaccine[190]['timeline'].values())[0]
Thailand=list(json_data_vaccine[191]['timeline'].values())[0]
Timor_Leste=list(json_data_vaccine[192]['timeline'].values())[0]
Togo=list(json_data_vaccine[193]['timeline'].values())[0]
Tokelau=list(json_data_vaccine[194]['timeline'].values())[0]
Tonga=list(json_data_vaccine[195]['timeline'].values())[0]
Trinidad =list(json_data_vaccine[196]['timeline'].values())[0]
Tunisia=list(json_data_vaccine[197]['timeline'].values())[0]
Turkey=list(json_data_vaccine[198]['timeline'].values())[0]
Turkmenistan=list(json_data_vaccine[199]['timeline'].values())[0]
Caicos_Islands=list(json_data_vaccine[200]['timeline'].values())[0]
Tuvalu=list(json_data_vaccine[201]['timeline'].values())[0]
Uganda=list(json_data_vaccine[202]['timeline'].values())[0]
Ukraine=list(json_data_vaccine[203]['timeline'].values())[0]
UAEe=list(json_data_vaccine[204]['timeline'].values())[0]
UKk=list(json_data_vaccine[205]['timeline'].values())[0]
USAa=list(json_data_vaccine[206]['timeline'].values())[0]
Uruguay=list(json_data_vaccine[207]['timeline'].values())[0]
Uzbekistan=list(json_data_vaccine[208]['timeline'].values())[0]
Vanuatu=list(json_data_vaccine[209]['timeline'].values())[0]
Venezuela=list(json_data_vaccine[210]['timeline'].values())[0]
Vietnam=list(json_data_vaccine[211]['timeline'].values())[0]
Wallis_and_Futuna=list(json_data_vaccine[212]['timeline'].values())[0]
Yemen=list(json_data_vaccine[213]['timeline'].values())[0]
Zambia=list(json_data_vaccine[214]['timeline'].values())[0]
Zimbabwe=list(json_data_vaccine[215]['timeline'].values())[0]



print("\tvaccine in some countries".upper())
print("----------Vaccines rolled out-------------")
# print("iran\t\t\t".upper(),"{:,}".format(iran))
# print("usa\t\t\t".upper(),"{:,}".format(usa))
print("Afghanistan\t\t".upper(),"{:,}".format(Afghanistan))
print("Albania\t\t\t".upper(),"{:,}".format(Albania))
print("Algeria\t\t\t".upper(),"{:,}".format(Algeria))
print("Andorra\t\t\t".upper(),"{:,}".format(Andorra))
print("Angola\t\t\t".upper(),"{:,}".format(Angola))
print("Anguilla\t\t".upper(),"{:,}".format(Anguilla))
print("Antigua and Barbuda\t".upper(),"{:,}".format(Antigua_and_Barbuda))
print("Argentina\t\t".upper(),"{:,}".format(Argentina))
print("Armenia\t\t\t".upper(),"{:,}".format(Armenia))
print("Aruba\t\t\t".upper(),"{:,}".format(Aruba))
print("Australia\t\t".upper(),"{:,}".format(Australia))
print("Austria\t\t\t".upper(),"{:,}".format(Austria))
print("Azerbaijan\t\t".upper(),"{:,}".format(Azerbaijan))
print("Bahamas\t\t\t".upper(),"{:,}".format(Bahamas))
print("Bahrain\t\t\t".upper(),"{:,}".format(Bahrain))
print("Bangladesh\t\t".upper(),"{:,}".format(Bangladesh))
print("Barbados\t\t".upper(),"{:,}".format(Barbados))
print("Belarus\t\t\t".upper(),"{:,}".format(Belarus))
print("Belgium\t\t\t".upper(),"{:,}".format(Belgium))
print("Belize\t\t\t".upper(),"{:,}".format(Belize))
print("Benin\t\t\t".upper(),"{:,}".format(Benin))
print("Bermuda\t\t\t".upper(),"{:,}".format(Bermuda))
print("Bhutan\t\t\t".upper(),"{:,}".format(Bhutan))
print("Bolivia\t\t\t".upper(),"{:,}".format(Bolivia))
print("Caribbean Netherlands\t".upper(),"{:,}".format(Caribbean_Netherlands))
print("Bosnia\t\t\t".upper(),"{:,}".format(Bosnia))
print("Botswana\t\t".upper(),"{:,}".format(Botswana))
print("Brazil\t\t\t".upper(),"{:,}".format(Brazil))
print("British Virgin Islands\t".upper(),"{:,}".format(British_Virgin_Islands))
print("Brunei\t\t\t".upper(),"{:,}".format(Brunei))
print("Bulgaria\t\t".upper(),"{:,}".format(Bulgaria))
print("Burkina Faso\t\t".upper(),"{:,}".format(Burkina_Faso))
print("Cambodia\t\t".upper(),"{:,}".format(Cambodia))
print("Cameroon\t\t".upper(),"{:,}".format(Cameroon))
print("Canada\t\t\t".upper(),"{:,}".format(Canada))
print("Cabo Verde\t\t".upper(),"{:,}".format(Cabo_Verde))
print("Cayman Islands\t\t".upper(),"{:,}".format(Cayman_Islands))
print("Central AfricanRepublic\t".upper(),"{:,}".format(Central_African_Republic))
print("Chad\t\t\t".upper(),"{:,}".format(Chad))
print("Chile\t\t\t".upper(),"{:,}".format(Chile))
print("China\t\t\t".upper(),"{:,}".format(China))
print("Colombia\t\t".upper(),"{:,}".format(Colombia))
print("Comoros\t\t\t".upper(),"{:,}".format(Comoros))
print("Congo\t\t\t".upper(),"{:,}".format(Congo))
print("Cook Islands\t\t".upper(),"{:,}".format(Cook_Islands))
print("Costa Rica\t\t".upper(),"{:,}".format(Costa_Rica))
print("Cote dIvoire\t\t".upper(),"{:,}".format(Cote_d_Ivoire))
print("Croatia\t\t\t".upper(),"{:,}".format(Croatia))
print("Cuba\t\t\t".upper(),"{:,}".format(Cuba))
print("Curacao\t\t\t".upper(),"{:,}".format(Curacao))
print("Cyprus\t\t\t".upper(),"{:,}".format(Cyprus))
print("Czechia\t\t\t".upper(),"{:,}".format(Czechia))
print("DRC\t\t\t".upper(),"{:,}".format(DRCc))
print("Denmark\t\t\t".upper(),"{:,}".format(Denmark))
print("Djibouti\t\t".upper(),"{:,}".format(Djibouti))
print("Dominica\t\t".upper(),"{:,}".format(Dominica))
print("Dominican Republic\t".upper(),"{:,}".format(Dominican_Republic))
print("Ecuador\t\t\t".upper(),"{:,}".format(Ecuador))
print("Egypt\t\t\t".upper(),"{:,}".format(Egypt))
print("El Salvador\t\t".upper(),"{:,}".format(El_Salvador))
print("Equatorial Guinea\t".upper(),"{:,}".format(Equatorial_Guinea))
print("Estonia\t\t\t".upper(),"{:,}".format(Estonia))
print("Swaziland\t\t".upper(),"{:,}".format(Swaziland))
print("Ethiopia\t\t".upper(),"{:,}".format(Ethiopia))
print("Faroe Islands\t\t".upper(),"{:,}".format(Faroe_Islands))
print("Falkland Islands\t".upper(),"{:,}".format(Falkland__Islands))
print("Fiji\t\t\t".upper(),"{:,}".format(Fiji))
print("Finland\t\t\t".upper(),"{:,}".format(Finland))
print("France\t\t\t".upper(),"{:,}".format(France))
print("French Polynesia\t".upper(),"{:,}".format(French_Polynesia))
print("Gabon\t\t\t".upper(),"{:,}".format(Gabon))
print("Gambia\t\t\t".upper(),"{:,}".format(Gambia))
print("Georgia\t\t\t".upper(),"{:,}".format(Georgia))
print("Germany\t\t\t".upper(),"{:,}".format(Germany))
print("Ghana\t\t\t".upper(),"{:,}".format(Ghana))
print("Gibraltar\t\t".upper(),"{:,}".format(Gibraltar))
print("Greece\t\t\t".upper(),"{:,}".format(Greece))
print("Greenland\t\t".upper(),"{:,}".format(Greenland))
print("Grenada\t\t\t".upper(),"{:,}".format(Grenada))
print("Guatemala\t\t".upper(),"{:,}".format(Guatemala))
print("Guernsey\t\t".upper(),"{:,}".format(Guernsey))
print("Guinea\t\t\t".upper(),"{:,}".format(Guinea))
print("Guinea Bissau\t\t".upper(),"{:,}".format(Guinea_Bissau))
print("Guyana\t\t\t".upper(),"{:,}".format(Guyana))
print("Haiti\t\t\t".upper(),"{:,}".format(Haiti))
print("Honduras\t\t".upper(),"{:,}".format(Honduras))
print("Hong Kong\t\t".upper(),"{:,}".format(Hong_Kong))
print("Hungary\t\t\t".upper(),"{:,}".format(Hungary))
print("Iceland\t\t\t".upper(),"{:,}".format(Iceland))
print("India\t\t\t".upper(),"{:,}".format(India))
print("Indonesia\t\t".upper(),"{:,}".format(Indonesia))
print("Iran\t\t\t".upper(),"{:,}".format(Iran))
print("Iraq\t\t\t".upper(),"{:,}".format(Iraq))
print("Ireland\t\t\t".upper(),"{:,}".format(Ireland))
print("Isle of Man\t\t".upper(),"{:,}".format(Isle_of_Man))
print("Israel\t\t\t".upper(),"{:,}".format(Israel))
print("Italy\t\t\t".upper(),"{:,}".format(Italy))
print("Jamaica\t\t\t".upper(),"{:,}".format(Jamaica))
print("Japan\t\t\t".upper(),"{:,}".format(Japan))
print("Channel Islands\t\t".upper(),"{:,}".format(Channel_Islands))
print("Jordan\t\t\t".upper(),"{:,}".format(Jordan))
print("Kazakhstan\t\t".upper(),"{:,}".format(Kazakhstan))
print("Kenya\t\t\t".upper(),"{:,}".format(Kenya))
print("Kiribati\t\t".upper(),"{:,}".format(Kiribati))
print("Kuwait\t\t\t".upper(),"{:,}".format(Kuwait))
print("Kyrgyzstan\t\t".upper(),"{:,}".format(Kyrgyzstan))
print("Lao Peoples\t\t".upper(),"{:,}".format(Lao_Peoples_Democratic_Republic))
print("Latvia\t\t\t".upper(),"{:,}".format(Latvia))
print("Lebanon\t\t\t".upper(),"{:,}".format(Lebanon))
print("Lesotho\t\t\t".upper(),"{:,}".format(Lesotho))
print("Liberia\t\t\t".upper(),"{:,}".format(Liberia))
print("Libyan_Arab_J\t\t".upper(),"{:,}".format(Libyan_Arab_Jamahiriya))
print("Liechtenstein\t\t".upper(),"{:,}".format(Liechtenstein))
print("Lithuania\t\t".upper(),"{:,}".format(Lithuania))
print("Luxembourg\t\t".upper(),"{:,}".format(Luxembourg))
print("Macao\t\t\t".upper(),"{:,}".format(Macao))
print("Madagascar\t\t".upper(),"{:,}".format(Madagascar))
print("Malawi\t\t\t".upper(),"{:,}".format(Malawi))
print("Malaysia\t\t".upper(),"{:,}".format(Malaysia))
print("Maldives\t\t".upper(),"{:,}".format(Maldives))
print("Mali\t\t\t".upper(),"{:,}".format(Mali))
print("Malta\t\t\t".upper(),"{:,}".format(Malta))
print("Mauritania\t\t".upper(),"{:,}".format(Mauritania))
print("Mauritius\t\t".upper(),"{:,}".format(Mauritius))
print("Mexico\t\t\t".upper(),"{:,}".format(Mexico))
print("Moldova\t\t\t".upper(),"{:,}".format(Moldova))
print("Monaco\t\t\t".upper(),"{:,}".format(Monaco))
print("Mongolia\t\t".upper(),"{:,}".format(Mongolia))
print("Montenegro\t\t".upper(),"{:,}".format(Montenegro))
print("Montserrat\t\t".upper(),"{:,}".format(Montserrat))
print("Morocco\t\t\t".upper(),"{:,}".format(Morocco))
print("Mozambique\t\t".upper(),"{:,}".format(Mozambique))
print("Myanmar\t\t\t".upper(),"{:,}".format(Myanmar))
print("Namibia\t\t\t".upper(),"{:,}".format(Namibia))
print("Nauru\t\t\t".upper(),"{:,}".format(Nauru))
print("Nepal\t\t\t".upper(),"{:,}".format(Nepal))
print("Netherlands\t\t".upper(),"{:,}".format(Netherlands))
print("New Caledonia\t\t".upper(),"{:,}".format(New_Caledonia))
print("New Zealand\t\t".upper(),"{:,}".format(New_Zealand))
print("Nicaragua\t\t".upper(),"{:,}".format(Nicaragua))
print("Niger\t\t\t".upper(),"{:,}".format(Niger))
print("Nigeria\t\t\t".upper(),"{:,}".format(Nigeria))
print("Niue\t\t\t".upper(),"{:,}".format(Niue))
print("Macedonia\t\t".upper(),"{:,}".format(Macedonia))
print("Norway\t\t\t".upper(),"{:,}".format(Norway))
print("Oman\t\t\t".upper(),"{:,}".format(Oman))
print("Pakistan\t\t".upper(),"{:,}".format(Pakistan))
print("Palestine\t\t".upper(),"{:,}".format(Palestine))
print("Panama\t\t\t".upper(),"{:,}".format(Panama))
print("Papua New Guinea\t".upper(),"{:,}".format(Papua_New_Guinea))
print("Paraguay\t\t".upper(),"{:,}".format(Paraguay))
print("Peru\t\t\t".upper(),"{:,}".format(Peru))
print("Philippines\t\t".upper(),"{:,}".format(Philippines))
print("Pitcairn\t\t".upper(),"{:,}".format(Pitcairn))
print("Poland\t\t\t".upper(),"{:,}".format(Poland))
print("Portugal\t\t".upper(),"{:,}".format(Portugal))
print("Qatar\t\t\t".upper(),"{:,}".format(Qatar))
print("Romania\t\t\t".upper(),"{:,}".format(Romania))
print("Russia\t\t\t".upper(),"{:,}".format(Russia))
print("Rwanda\t\t\t".upper(),"{:,}".format(Rwanda))
print("Saint Helena\t\t".upper(),"{:,}".format(Saint_Helena))
print("Saint K and N\t\t".upper(),"{:,}".format(Saint_Kitts_and_Nevis))
print("Saint Lucia\t\t".upper(),"{:,}".format(Saint_Lucia))
print("Saint Vincent\t\t".upper(),"{:,}".format(Saint_Vincent_and_the_Grenadines))
print("Samoa\t\t\t".upper(),"{:,}".format(Samoa))
print("San Marino\t\t".upper(),"{:,}".format(San_Marino))
print("Sao Tome\t\t".upper(),"{:,}".format(Sao_Tome_and_Principe))
print("Saudi Arabia\t\t".upper(),"{:,}".format(Saudi_Arabia))
print("Senegal\t\t\t".upper(),"{:,}".format(Senegal))
print("Serbia\t\t\t".upper(),"{:,}".format(Serbia))
print("Seychelles\t\t".upper(),"{:,}".format(Seychelles))
print("Sierra Leone\t\t".upper(),"{:,}".format(Sierra_Leone))
print("Singapore\t\t".upper(),"{:,}".format(Singapore))
print("Sint Maarten\t\t".upper(),"{:,}".format(Sint_Maarten))
print("Slovakia\t\t".upper(),"{:,}".format(Slovakia))
print("Slovenia\t\t".upper(),"{:,}".format(Slovenia))
print("Solomon Islands\t\t".upper(),"{:,}".format(Solomon_Islands))
print("Somalia\t\t\t".upper(),"{:,}".format(Somalia))
print("South Africa\t\t".upper(),"{:,}".format(South_Africa))
print("S Korea\t\t\t".upper(),"{:,}".format(S_Korea))
print("South Sudan\t\t".upper(),"{:,}".format(South_Sudan))
print("Spain\t\t\t".upper(),"{:,}".format(Spain))
print("Sri Lanka\t\t".upper(),"{:,}".format(Sri_Lanka))
print("Sudan\t\t\t".upper(),"{:,}".format(Sudan))
print("Suriname\t\t".upper(),"{:,}".format(Suriname))
print("Sweden\t\t\t".upper(),"{:,}".format(Sweden))
print("Switzerland\t\t".upper(),"{:,}".format(Switzerland))
print("Syrian\t\t\t".upper(),"{:,}".format(Syrian))
print("Taiwan\t\t\t".upper(),"{:,}".format(Taiwan))
print("Tajikistan\t\t".upper(),"{:,}".format(Tajikistan))
print("Tanzania\t\t".upper(),"{:,}".format(Tanzania))
print("Thailand\t\t".upper(),"{:,}".format(Thailand))
print("Timor Leste\t\t".upper(),"{:,}".format(Timor_Leste))
print("Togo\t\t\t".upper(),"{:,}".format(Togo))
print("Tokelau\t\t\t".upper(),"{:,}".format(Tokelau))
print("Tonga\t\t\t".upper(),"{:,}".format(Tonga))
print("Trinidad\t\t".upper(),"{:,}".format(Trinidad ))
print("Tunisia\t\t\t".upper(),"{:,}".format(Tunisia))
print("Turkey\t\t\t".upper(),"{:,}".format(Turkey))
print("Turkmenistan\t\t".upper(),"{:,}".format(Turkmenistan))
print("Caicos Islands\t\t".upper(),"{:,}".format(Caicos_Islands))
print("Tuvalu\t\t\t".upper(),"{:,}".format(Tuvalu))
print("Uganda\t\t\t".upper(),"{:,}".format(Uganda))
print("Ukraine\t\t\t".upper(),"{:,}".format(Ukraine))
print("UAE\t\t\t".upper(),"{:,}".format(UAEe))
print("UK\t\t\t".upper(),"{:,}".format(UKk))
print("USA\t\t\t".upper(),"{:,}".format(USAa))
print("Uruguay\t\t\t".upper(),"{:,}".format(Uruguay))
print("Uzbekistan\t\t".upper(),"{:,}".format(Uzbekistan))
print("Vanuatu\t\t\t".upper(),"{:,}".format(Vanuatu))
print("Venezuela\t\t".upper(),"{:,}".format(Venezuela))
print("Vietnam\t\t\t".upper(),"{:,}".format(Vietnam))
print("Wallis and F\t\t".upper(),"{:,}".format(Wallis_and_Futuna))
print("Yemen\t\t\t".upper(),"{:,}".format(Yemen))
print("Zambia\t\t\t".upper(),"{:,}".format(Zambia))
print("Zimbabwe\t\t".upper(),"{:,}".format(Zimbabwe))

print("-----------------------------------------")
print("")