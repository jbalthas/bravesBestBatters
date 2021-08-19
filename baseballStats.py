from selenium import webdriver
import requests
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.mlb.com/braves/stats/batting-average/all-time-by-season")

index = 0

top_5_Names = []
top_5_hittingAVG = []
final_arr = []
sleep(1)

for i in range(5):
    #try:
    #Get Rid of weird name --Crappy site
        element = driver.find_element_by_xpath('//span[@class="full-3fV3c9pF"]')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

        #Get real name
        element = driver.find_element_by_xpath('//div[@class="custom-cell-wrapper-34Cjf9P0"]')
        name = element.find_element_by_xpath('//span[@class="full-3fV3c9pF"]').text        

        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)


        #Get avg
        element = driver.find_element_by_xpath('//td[@class="selected-1vxxHvFg col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT"]')
        
        avg = element.text

        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        

        top_5_Names.append(name)
        

        top_5_hittingAVG.append(avg)

        index +=1

        print(name + ": " +avg)
        final_arr.append(name + ": " + avg +"  ")
        sleep(.5)
        
   # except:
        #print("NO")


r = requests.post('https://maker.ifttt.com/trigger/jack/with/key/lmRrnJJWM7oHvMkAuqiYQSFUzA9vGGXET77e6igrvy4', json={"value1": final_arr})
driver.quit()
