from firebase import firebase

firebase = firebase.FirebaseApplication('https://nline-61fe6.firebaseio.com', None)



if __name__ == '__main__':
	result = firebase.get('/saurav', None)
	print result