from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"
}

lt = []
razme = []
obnovlen = []
okonch = []
sts = []
obj = []
cnt = []
nms = []
rz = []

db = pd.DataFrame()

for i in range(1, 77):
    print("Processing page " + str(i))
    req = requests.get('https://zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&sortBy=UPDATE_DATE&pageNumber=' + str(i) + '&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&af=on&priceContractAdvantages44IdNameHidden=%7B%7D&priceContractAdvantages94IdNameHidden=%7B%7D&currencyIdGeneral=-1&customerPlace=5277356&selectedSubjectsIdNameHidden=%7B%7D&okdpGroupIdsIdNameHidden=%7B%7D&koksIdsIdNameHidden=%7B%7D&OrderPlacementSmallBusinessSubject=on&OrderPlacementRnpData=on&OrderPlacementExecutionRequirement=on&orderPlacement94_0=0&orderPlacement94_1=0&orderPlacement94_2=0&contractPriceCurrencyId=-1&budgetLevelIdNameHidden=%7B%7D&nonBudgetTypesIdNameHidden=%7B%7D&gws=Выберите+тип+закупки', headers=headers)
    get = req.text

    with open("doc.html", "w", encoding="utf-8") as file:
        file.write(get)

    with open("doc.html", encoding="utf-8") as file:
        src = file.read()

    page = BeautifulSoup(src, "lxml")

    lot = page.find_all(class_='registry-entry__header-mid__number')
    for item in lot:
        it = item.text.replace('№', '').strip()
        lt.append(it)

    status = page.find_all(class_='registry-entry__header-mid__title text-normal')
    for item in status:
        it = item.text.strip()
        sts.append(it)

    object = page.find_all(class_='registry-entry__body-value')
    for item in object:
        it = item.text.strip()
        obj.append(it)

    contractor = page.find_all(class_ = 'registry-entry__body-href')
    for item in contractor:
        it = item.text.strip()
        cnt.append(it)

    nachms = page.find_all(class_ = 'price-block__value')
    for item in nachms:
        it = item.text.strip()
        nms.append(it)

    razmesh = page.find_all(class_ = 'data-block__value')
    for item in razmesh:
        it = item.text.strip()
        rz.append(it)

    obnovl = page.find_all(class_ = 'data-block mt-auto')
    for item in obnovl:
        processed = str(item)
        to_p = BeautifulSoup(processed, 'lxml')
        dates = to_p.find_all(class_ = 'data-block__value')
        razm = dates[0].text
        obn = dates[1].text
        okn = dates[2].text
        razme.append(razm)
        obnovlen.append(obn)
        okonch.append(okn)
        # print(razm, obn, okn)

for i in range(78, 100):
    print("Processing page " + str(i))
    req = requests.get('https://zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&sortBy=UPDATE_DATE&pageNumber=' + str(i) + '&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&af=on&priceContractAdvantages44IdNameHidden=%7B%7D&priceContractAdvantages94IdNameHidden=%7B%7D&currencyIdGeneral=-1&customerPlace=5277356&selectedSubjectsIdNameHidden=%7B%7D&okdpGroupIdsIdNameHidden=%7B%7D&koksIdsIdNameHidden=%7B%7D&OrderPlacementSmallBusinessSubject=on&OrderPlacementRnpData=on&OrderPlacementExecutionRequirement=on&orderPlacement94_0=0&orderPlacement94_1=0&orderPlacement94_2=0&contractPriceCurrencyId=-1&budgetLevelIdNameHidden=%7B%7D&nonBudgetTypesIdNameHidden=%7B%7D&gws=Выберите+тип+закупки', headers=headers)
    get = req.text

    with open("doc.html", "w", encoding="utf-8") as file:
        file.write(get)

    with open("doc.html", encoding="utf-8") as file:
        src = file.read()

    page = BeautifulSoup(src, "lxml")

    lot = page.find_all(class_='registry-entry__header-mid__number')
    for item in lot:
        it = item.text.replace('№', '').strip()
        lt.append(it)

    status = page.find_all(class_='registry-entry__header-mid__title text-normal')
    for item in status:
        it = item.text.strip()
        sts.append(it)

    object = page.find_all(class_='registry-entry__body-value')
    for item in object:
        it = item.text.strip()
        obj.append(it)

    contractor = page.find_all(class_ = 'registry-entry__body-href')
    for item in contractor:
        it = item.text.strip()
        cnt.append(it)

    nachms = page.find_all(class_ = 'price-block__value')
    for item in nachms:
        it = item.text.strip()
        nms.append(it)

    razmesh = page.find_all(class_ = 'data-block__value')
    for item in razmesh:
        it = item.text.strip()
        rz.append(it)

    obnovl = page.find_all(class_ = 'data-block mt-auto')
    for item in obnovl:
        processed = str(item)
        to_p = BeautifulSoup(processed, 'lxml')
        dates = to_p.find_all(class_ = 'data-block__value')
        razm = dates[0].text
        obn = dates[1].text
        okn = dates[2].text
        razme.append(razm)
        obnovlen.append(obn)
        okonch.append(okn)
        # print(razm, obn, okn)

db = db.assign(lt = lt)
db = db.assign(sts = sts)
db = db.assign(obj = obj)
db = db.assign(cnt = cnt)
db = db.assign(nms = nms)
db = db.assign(razm = razme)
db = db.assign(obn = obnovlen)
db = db.assign(okn = okonch)

print(db)

db.to_csv('out.csv', encoding='utf-8')

file_path = 'out.csv'
df = pd.read_csv(file_path)


# Функция для классификации
def classify_tender(obj):
    obj_lower = obj.lower()
    if 'поставка' in obj_lower:
        return 'Товар'
    elif 'работ' in obj_lower or 'строительно' in obj_lower:
        return 'Работа'
    elif 'услуга' in obj_lower or 'обучение' in obj_lower or 'ввод в эксплуатацию' in obj_lower:
        return 'Услуга'
    else:
        # Присваиваем "Услуга" по умолчанию, если не найдено других ключевых слов
        return 'Услуга'


# Применение функции классификации к каждому объекту
df['classification'] = df['obj'].apply(classify_tender)

# Сохранение результата в новый CSV файл
df.to_csv('classified_tenders.csv', index=False)

# Вывод первых нескольких строк с новыми данными
df[['obj', 'classification']].head()
print(df[['obj', 'classification']])