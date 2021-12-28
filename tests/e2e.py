from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from os import environ
import sys



def test_scores_service():
    try:
        e_path = environ.get('cd_path') + '/chromedriver.exe'
        print (e_path)
        chrome_driver = webdriver.Chrome(executable_path=environ.get('cd_path')+'/chromedriver.exe')
        page=chrome_driver.get("http://localhost:5001/scores")
        score=chrome_driver.find_element_by_id('score')
        current_score=int(score.text.replace('{', '').replace('}', ''))
        print (current_score)
        chrome_driver.close()
        return (1 <= current_score < 1000)
    except WebDriverException as exception:
        print ('Web driver exception', exception.msg)
        return -10
    except ValueError:
        print ('Value error')
        return -20
        
        

    


def main_function():
    if test_scores_service() == True:
        sys.exit(0)
    else :
        sys.exit(-1)
main_function()