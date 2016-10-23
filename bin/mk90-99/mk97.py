# coding=utf-8

"""
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
"""

import sys
import cPickle as pickle
from sklearn.cluster import KMeans

country_vec_dic = pickle.load(sys.stdin)
country_names = country_vec_dic.keys()
country_vec = country_vec_dic.values()
km = KMeans(n_clusters=5)
country_vec_km = km.fit(country_vec)
labels = country_vec_km.labels_
for country_name, label in zip(country_names, labels):
    print country_name.rstrip(), label

"""
$ python mk97.py < country_vec_dic.pkl > country_vec_km.txt
$ cat country_vec_km.txt| sort -k2 | less
Australia 0
Bangladesh 0
Bhutan 0
Canada 0
China 0
Fiji 0
India 0
Indonesia 0
Japan 0
Malaysia 0
Nepal 0
New_Zealand 0
North_Korea 0
Pakistan 0
Philippines 0
Singapore 0
South_Africa 0
South_Korea 0
Sri_Lanka 0
Taiwan 0
Thailand 0
United_Kingdom 0
United_States 0
Vietnam 0
American_Samoa 1
Andorra 1
Anguilla 1
Antarctica 1
Antigua_and_Barbuda 1
Aruba 1
Bahamas 1
Barbados 1
Belize 1
Bermuda 1
British_Indian_Ocean_Territory 1
British_Virgin_Islands 1
Brunei 1
Cape_Verde 1
Cayman_Islands 1
Central_African_Republic 1
Christmas_Island 1
Comoros 1
Cook_Islands 1
Djibouti 1
Dominica 1
Equatorial_Guinea 1
Falkland_Islands 1
French_Guiana 1
French_Polynesia 1
Gambia 1
Georgia 1
Gibraltar 1
Greenland 1
Grenada 1
Guadeloupe 1
Guam 1
Guernsey 1
Guinea 1
Guinea-Bissau 1
Guyana 1
Isle_of_Man 1
Jamaica 1
Jersey 1
Johnston_Island 1
Kiribati 1
Lesotho 1
Madagascar 1
Maldives 1
Malta 1
Marshall_Islands 1
Martinique 1
Mauritius 1
Mayotte 1
Metropolitan_France 1
Micronesia 1
Monaco 1
Montserrat 1
Nauru 1
Netherlands_Antilles 1
New_Caledonia 1
Niue 1
Norfolk_Island 1
North_Vietnam 1
Northern_Mariana_Islands 1
Palau 1
Palestinian_Territories 1
Panama_Canal_Zone 1
Papua_New_Guinea 1
People's_Democratic_Republic_of_Yemen 1
Pitcairn_Islands 1
Saint_Helena 1
Saint_Kitts_and_Nevis 1
Saint_Lucia 1
Saint_Martin 1
Saint_Pierre_and_Miquelon 1
Saint_Vincent_and_the_Grenadines 1
Samoa 1
San_Marino 1
Serbia_and_Montenegro 1
Seychelles 1
Solomon_Islands 1
Suriname 1
Svalbard_and_Jan_Mayen 1
Swaziland 1
Timor-Leste 1
Togo 1
Tokelau 1
Tonga 1
Trinidad_and_Tobago 1
Turks_and_Caicos_Islands 1
Tuvalu 1
Union_of_Soviet_Socialist_Republics 1
Vanuatu 1
Vatican_City 1
Wake_Island 1
Wallis_and_Futuna 1
Western_Sahara 1
Albania 2
Armenia 2
Austria 2
Azerbaijan 2
Belarus 2
Belgium 2
Bosnia_and_Herzegovina 2
Bulgaria 2
Croatia 2
Cyprus 2
Czech_Republic 2
Denmark 2
East_Germany 2
Estonia 2
Finland 2
France 2
Germany 2
Greece 2
Hungary 2
Iceland 2
Ireland 2
Italy 2
Latvia 2
Liechtenstein 2
Lithuania 2
Luxembourg 2
Macedonia 2
Moldova 2
Montenegro 2
Netherlands 2
Norway 2
Poland 2
Romania 2
Russia 2
Serbia 2
Slovakia 2
Slovenia 2
Sweden 2
Switzerland 2
Turkey 2
Ukraine 2
Afghanistan 3
Algeria 3
Angola 3
Bahrain 3
Benin 3
Botswana 3
Burkina_Faso 3
Burundi 3
Cambodia 3
Cameroon 3
Chad 3
Egypt 3
Eritrea 3
Ethiopia 3
Gabon 3
Ghana 3
Iran 3
Iraq 3
Israel 3
Jordan 3
Kazakhstan 3
Kenya 3
Kuwait 3
Kyrgyzstan 3
Laos 3
Lebanon 3
Liberia 3
Libya 3
Malawi 3
Mali 3
Mauritania 3
Mongolia 3
Morocco 3
Mozambique 3
Namibia 3
Niger 3
Nigeria 3
Oman 3
Qatar 3
Rwanda 3
Saudi_Arabia 3
Senegal 3
Sierra_Leone 3
Somalia 3
Sudan 3
Syria 3
Tajikistan 3
Tanzania 3
Tunisia 3
Turkmenistan 3
Uganda 3
United_Arab_Emirates 3
Uzbekistan 3
Yemen 3
Zambia 3
Zimbabwe 3
Argentina 4
Bolivia 4
Brazil 4
Chile 4
Colombia 4
Costa_Rica 4
Cuba 4
Dominican_Republic 4
Ecuador 4
El_Salvador 4
Guatemala 4
Haiti 4
Honduras 4
Mexico 4
Nicaragua 4
Panama 4
Paraguay 4
Peru 4
Portugal 4
Puerto_Rico 4
Spain 4
Uruguay 4
Venezuela 4
"""
# label(0) = 24
# label(1) = 94
# label(2) = 41
# label(3) = 56
# label(4) = 23
