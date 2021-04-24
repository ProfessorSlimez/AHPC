#Made by _PugPlayz#8683 (Discord) or _PugPlayzMC (IGN)

import json,requests,re,threading,time,os,ujson,datetime
while True:
    pStart = time.time()
    CompareList = []
    APIList = []
    data = requests.get("https://api.hypixel.net/skyblock/auctions",  timeout=10).json()
    totalPages = data['totalPages']
    #Calculates pages for even numbers
    if (totalPages % 2) == 0:
        totalPage1 = totalPages / 4
        totalPage2 = totalPages / 4 + totalPage1
        totalPage3 = totalPages / 4 + totalPage2
        page2 = totalPages / 4 + 1
        page3 = totalPages / 4 + page2
        page4 = totalPages / 4 + page3
        totalPage1 = int(totalPage1)
        totalPage2 = int(totalPage2)
        totalPage3 = int(totalPage3)
        page2 = int(page2)
        page3 = int(page3)
        page4 = int(page4)

    #Calculates pages for odd numbers
    else:
        totalPage1 = totalPages / 4 + 1
        totalPage2 = totalPages / 4 + totalPage1 + 1
        totalPage3 = totalPages / 4 + totalPage2 + 1
        page2 = totalPages / 4 + 2
        page3 = totalPages / 4 + page2 + 1
        page4 = totalPages / 4 + page3 + 1
        totalPage1 = int(totalPage1)
        totalPage2 = int(totalPage2)
        totalPage3 = int(totalPage3)
        page2 = int(page2)
        page3 = int(page3)
        page4 = int(page4)
    page1 = 1
    totalPage4 = totalPages

    print(page1,totalPage1,page2,totalPage2, page3, totalPage3,page4,totalPage4)

    def Sort():
        #Sorts ADVProfitFinder's data and converts it to dict
        profit = {'auction':[]}
        with open('Profit.json','w') as outfile:
            jsonDump = ujson.dump(profit,outfile,indent=4)
        with open('Profit.json') as infile:
            profit = ujson.load(infile)
        global CompareList
        CompareList = sorted(CompareList, key = lambda i: i[6], reverse=True)
        CompareList = sorted(CompareList, key = lambda i: i[3])
        for item in CompareList:
                compare_price = item[5]
                pet_price = item[3]
                gap = item[6]
                compare_price = '{:,}'.format(compare_price)
                pet_price = '{:,}'.format(pet_price)
                gap = '{:,}'.format(gap)
                
                profit['auction'].append({
                    'name':item[0],
                    'tier':item[1],
                    'lvl':item[2],
                    'price':pet_price,
                    'user':item[4],
                    'estSP':compare_price,
                    'profit':gap
                })
        with open('Profit.json','w') as outfile:
            jsonDump = ujson.dump(profit,outfile,indent=4)
            
            


    

    def ADVProfitFinder():
        print('Starting Phase 2')
        with open('data.json') as data_file:
            data = ujson.load(data_file)   
        for pet in data['auction']: #scrolls through pets and compares them
            Compare(pet)





                           
                                                
    def Compare(pet):
        num=0
        volume=0
        pet_lvl = pet['lvl']
        pet_lvl = int(pet_lvl)
        pet_uuid = pet['uuid']
        pet_name = pet['name']
        pet_item_tier = pet['tier']
        pet_price = pet['price']
        pet_price = int(pet_price)

        
        with open('data.json') as data1:
            data1 = ujson.load(data1)
        for compare in data1['auction']:
            compare_uuid = compare['uuid']
            compare_name = compare['name']
            compare_lvl = compare['lvl']
            compare_lvl = int(compare_lvl)
            if pet_name == "Ghoul":
                pass
            elif pet_name == "Hound":
                pass
            elif pet_name == "Endermite":
                pass
            elif pet_name == "Spirit":
                pass
            elif pet_name == "Jerry":
                pass
            elif pet_name == "Bee":
                pass
            else:
                if compare_uuid == pet_uuid and pet_name == compare_name and compare_lvl == pet_lvl:
                    #checks if the comparison is the same pet, if it is skip
                    pass
                else:
                    compare_item_tier = compare['tier']
                    if pet_item_tier == compare_item_tier and pet_name == compare_name:
                        if num == 0:
                            #compares pets
                            Bottom = pet_lvl - 15
                            Top = pet_lvl + 100
                            if compare_lvl in range(Bottom, Top):
                                compare_price = compare['price']
                                if compare_lvl > pet_lvl:
                                    middle = compare_lvl - pet_lvl
                                    middle = middle / 100
                                    estSP = compare_price - compare_price * middle
                                else:
                                    estSP = compare_price
                                estSP = round(estSP, None)
                                gap = estSP - pet_price
                                if gap >=500000:
                                    username = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/{}".format(pet_uuid)).json()  
                                    username = username['name']
                                    CompareList.append([
                                        pet['name'],
                                        pet['tier'],
                                        pet['lvl'],
                                        pet_price,
                                        username,
                                        estSP,
                                        gap
                                    ])
                                    num+=1

                                else:
                                    num+=1
                                    pass        
                        else:
                            pass



    


    def JsonWrite(): #converts list to dict and writes as encoded pretty json to data file
        open('data.json','w')
        data = {'auction':[]}
        with open('data.json','w') as outfile:
            jsonDump = ujson.dump(data,outfile,indent=4)
        global APIList
        APIList = sorted(APIList, key = lambda x:x[3])
        for item in APIList:
            data['auction'].append({
                'name':item[0],
                'tier':item[1],
                'lvl':item[2],
                'price':item[3],
                'uuid':item[4]
                })
        with open('data.json','w') as outfile:
            jsonDump = ujson.dump(data,outfile,indent=4)





    def APILister(auction, lvl): #lists bulk data from api and then writes (saves time)
        global APIList
        item_name = auction['item_name']
        item_name =  re.sub("[\(\[].*?[\)\]]", "", item_name)
        item_name = item_name.lstrip()
        item_name = item_name.replace("\u2726","")
        item_name = item_name.rstrip()
        item_name = item_name.replace(" ", "")
        APIList.append([
            item_name,
            auction['tier'],
            lvl,
            auction['starting_bid'],
            auction['auctioneer']
            ])

    def APIGrabber(page,totalPages): #quad threaded API grabber
        while page != totalPages+1:
            try:
                    
                data = requests.get("https://api.hypixel.net/skyblock/auctions?page={}".format(page)).json()  
                auctions = data["auctions"]
                page+=1
                data = {}
                data['auction'] = []
                for auction in auctions:
                    try:
                        if auction["bin"]:
                            item_name = auction["item_name"]
                            isint = item_name[5:8].strip(" []")
                            if isint.isnumeric() == True:
                                lvl = int(isint)
                                if lvl > 55:
                                    item_tier = auction['tier']
                                    if item_tier.lower() =='mythic':
                                         APILister(auction, lvl)
                                    elif item_tier.lower() =='epic':
                                         APILister(auction, lvl)
                                    elif item_tier.lower() =='legendary':
                                         APILister(auction, lvl)
                                    
                    except KeyError as error:
                        pass
            except:
                pass
    print('Starting Phase 1 {}'.format(datetime.datetime.today()))
    ##
    x1 = threading.Thread(target=APIGrabber, args=(page1,totalPage1))
    x1.start()
    x2 = threading.Thread(target=APIGrabber, args=(page2,totalPage2))
    x2.start()
    x3 = threading.Thread(target=APIGrabber, args=(page3,totalPage3))
    x3.start()
    x4 = threading.Thread(target=APIGrabber, args=(page4,totalPage4))
    x4.start()
    x1.join()
    x2.join()
    x3.join()
    x4.join()
    ## Threads 
    JsonWrite()
    ADVProfitFinder()
    Sort()
    now = time.time()
    tDiff = now - pStart
    tDiff = round(tDiff, None)
    print('Finished After:',tDiff, 'Seconds.')
    time.sleep(90)

    
