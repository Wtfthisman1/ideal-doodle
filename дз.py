import requests
data = requests.get('http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml')
data = data.split('\n')
data.remove ('')
data = data + ['[new chapter]']
print(data[:100])
