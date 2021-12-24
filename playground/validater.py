import requests

"""valid = https://www.math.uzh.ch/typo3conf/ext/qfq/Classes/Api/download.php?s=61b15b754bfb2 

invalid = https://www.math.uzh.ch/typo3conf/ext/qfq/Classes/Api/download.php?s=61ae88c6e8518 
"""

url = 'http://www.math.uzh.ch/typo3conf/ext/qfq/Classes/Api/download.php?s=61b15b754bef7'

r = requests.get(url)
print(r.headers)
print(r.content)
print(r.text)