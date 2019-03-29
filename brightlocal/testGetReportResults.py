import json
import pprint
import csv
from brightlocal import BrightLocalAPI, BrightLocalBatch



def testBatchReportResults():

    count = 0

    fhand = open('KeywordRankings.csv', 'w', newline='',encoding='utf-8')
    csvfhand = csv.writer(fhand, delimiter=',')
    csvfhand.writerow(['Hospital Name','Location','Campaign ID','Keyword','Ranking'])

    with open('credentials.json', 'rb') as creds:
        credentials = json.load(creds)

        api_key = credentials['key'].encode('utf-8')
        api_secret = credentials['secret'].encode('utf-8')

        pass

    # Set up API wrappers
    api = BrightLocalAPI(key=api_key, secret=api_secret)
    batchapi = BrightLocalBatch(api=api)

    # Step 1: create a new batch
    batch_id = batchapi.create()

    print('Created Batch ID {}'.format(batch_id))

    pp = pprint.PrettyPrinter(indent=4)

    # Step 3: add campaign_id jobs to batch
    with open('allReports.csv') as fh:
        next(fh)
        for campaign_id in fh:
            print('Campaign ID: ', campaign_id)
            result = api.call(method='/v2/lsrc/results/get',params={'campaign-id':campaign_id})

            try:
                campaign_id = result['response']['result']['campaign_details']['campaign_id']
                googloc = result['response']['result']['campaign_details']['google_location']
                lastprocess = result['response']['result']['campaign_details']['last_processed']
                name = result['response']['result']['campaign_details']['name']
                zipcode = result['response']['result']['campaign_details']['postcode']
                # rankings = result['response']['result']['rankings']
                kwrankings = result['response']['result']['rankings']['keywords_num_rankings']

                print(campaign_id)
                print(name)
                print(zipcode)
                print(googloc)
                print(lastprocess)
                csvfhand.writerow([name,googloc,campaign_id,'',''])
                # print(rankings.keys())
                # print(rankingNum.values())

                for keyword, ranking in kwrankings.items():
                    print('Keyword: ', keyword, ' -- ', ranking)
                    # print(ranking)
                    csvfhand.writerow([name,googloc,campaign_id,keyword,ranking])
                    pass

                count += 1
                print('Total records accessed: ', count)
            except:
                pass

        print('campaignRankings.csv written with keyword rankings')
        fhand.close()

    return

testBatchReportResults()
