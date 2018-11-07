import requests ;
from bs4 import BeautifulSoup
import re

def EXPA(username, password):
	_ = {

	}

	def getNewToken():
		with requests.Session() as req :
			res = req.get("https://experience-v2.aiesec.org/auth")

			#code to retrieve authenticity_token
			soup = BeautifulSoup(res.content ,features="html.parser") 
			authenticity_token = (soup.find('meta' , attrs = {'name' : 'csrf-token'})['content'])

			login_data = {
				'authenticity_token': '', 
				'user[email]': username, 
				'user[password]': password,
				'commit':'Sign in',
			}
			login_data['authenticity_token'] = authenticity_token 


			res = req.post('https://auth.aiesec.org/users/sign_in' , data = login_data)
			if(re.search(r'<h2>Invalid email or password.' , res.text )):
				print('Invalid username or password !')
			else: 
				_['token'] = req.cookies['expa_token']
				return _['token']
				
	def getToken():
		if _.get("token") != None:
			print('Token already generated')
			return _['token']
		else:
			print('new')
			return getNewToken()

	def request(uri , options):
		#in progress ! x)
		#-----------
		return true

	def get(url , data):
		return(request(url , {
			form : data
		}))

	def post(url , data):
		return(request(url , {
			method : "POST", 
			form : data
		}))

	def graphql(query , vatiables):
		return(post(_graphqlUrl , {
			query, 
			variables
		}))



	_['getToken'] = getToken 
	_['getNewToken'] = getNewToken

	return(_)

