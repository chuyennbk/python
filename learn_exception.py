import requests
# from requests.exceptions import MissingSchema, InvalidURL
def test1():
    try:
        #print('a0')
        f=open('Learn_list.txt')
        if(f.name == 'Learn_list.txt'):
            raise FileNotFoundError # redirect to exception name
        #rint(f.readlissnes)
    except FileNotFoundError as e: #with errors
        print ('error')
    except Exception as e: #wit errors
        print (e)
    else: #without errors
        print(f.read())
        f.close()
    finally: #alway executive with/without errors
        print('Executing finally...')

def test2():
    try:
        print("--Test2--"+60*'-')
        f=requests.Session()
        f.get('http://github.com/adsdssdsdegsdxzcefsdcdmindsd').json()
        print(f)
    except requests.exceptions.InvalidURL:
        print('Invalid URL')
    except requests.exceptions.MissingSchema:
        print('wrong URL')
    except requests.exceptions.ConnectionError:
        print('Connection Error')
    except Exception as e:
        print('here222')
        print(e)
 
    
if __name__ == '__main__':
    test1()