import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',8585))
s.listen(3)
print('Waiting for connecting...')
coon,addr = s.accept()
while True:

	filename = 'C:/Users/彼梦之:/wenjian.txt'
	print('I want to get the file %s!' % filename)
	s.send(filename.encode('utf-8'))
	str1 = conn.recv(1024)
	str2 = str1.decode('utf-8')
	if str2=='no':
		print('To get the file %s is failed!' % filename)
	else:
		s.send(b'I am ready!')
		temp=filename.split('/')
		myname = 'my_' + temp[len(temp)-1]
		size=1024
		with open(myname,'wb') as f:
			while True:
				data = s.recv(size)
				f.write(data)
				if len(data)<size:
					break
	print('The downloaded file is %s.' % myname)

