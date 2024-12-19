import requests
from pynput.keyboard import Controller

keyboard = Controller()

response = requests.post('https://10fastfingers.com/speedtests/get_words', data={'speedtest_mode': '', 'speedtest_id': 1}, headers={'x-requested-with':'XMLHttpRequest'}, cookies={'CAKEPHP': 'd97gf7iol5rak58e6khehsccpa'})


print(response.text.replace('|', " "))






#curl 'https://10fastfingers.com/speedtests/get_words' \
#  -H 'cookie: CAKEPHP=saffbkr6311r8jqda6olqv7nms; CakeCookie[lang]=Q2FrZQ%3D%3D.5exP; _gid=GA1.2.1896787829.1734601400; consentUUID=c8dac5b1-9253-46d2-b481-9a39889d9c06_39; consentDate=2024-12-19T09:43:21.983Z; usnatUUID=abd082a8-90fd-4241-9968-563bbf3a2392; __qca=P0-538982440-1734601402637; _cc_id=b72bbe82d048c41cb9c09f9027fd3ac4; panoramaId_expiry=1735206202548; panoramaId=9fd462e64bd5209e9f7b0fe91a224945a7022ce84d9fcf389a3e051201b3398a; panoramaIdType=panoIndiv; CakeCookie[alternate_language_suggestion]=Q2FrZQ%3D%3D.9PBdWA%3D%3D; _pk_id.1.0767=77a8d674ba243565.1734601403.; ccuid=78e919b6-daf8-47fc-8da3-42a5031d7d0e; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%228f51c82a-bd28-4246-a37b-1b8259a3b484%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-11-19T09%3A43%3A27%22%7D; pbjs-unifiedid_last=Thu%2C%2019%20Dec%202024%2009%3A43%3A27%20GMT; _pk_ses.1.0767=1; ccsid=41345c5d-f5ec-467a-ba41-30bbb194efda; _lr_retry_request=true; __gads=ID=a5a545128cad3c3d:T=1734601406:RT=1734611864:S=ALNI_MaBxrve3-cYVEbQzJIz8UKU4WiEdw; __gpi=UID=00000f71d7bd1336:T=1734601406:RT=1734611864:S=ALNI_MZIJJioiWWB8M7gb4tV5x39IcbGew; __eoi=ID=f3033e195fc4fbf4:T=1734601406:RT=1734611864:S=AA-AfjYSAL78LB5dPcQe7UUN3HCG; _gat=1; _ga=GA1.1.1851950266.1734601400; cto_bundle=5WJTt19ERUlZeGY0bDlmbGNabnR5bFEyJTJCbTBzNFhrNG5SQVo3dnRRMG9VbjdXWWVjTSUyQnpaVkpCd2d6bjlOZDQlMkJvaUVPRGEzT3YybEpqZk93Q2xoU2Rha0xiJTJCbFR0Smt4Q2FPZjY5bjJKb2lLcGVla21IQXgwSHJURFdEZlNzU3UxSklNVlFkZHVBYXRTOGNHR2dqTUZmM0hYZGlZbkZ5dTh4Z0tMTEFNZGZYcyUyQkd3JTNE; _ga_TVXDNQX0VM=GS1.1.1734610948.2.1.1734612027.0.0.0' \
#  -H 'x-requested-with: XMLHttpRequest' \
#  --data-raw 'speedtest_mode=&speedtest_id=1'