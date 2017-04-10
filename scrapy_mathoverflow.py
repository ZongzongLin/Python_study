import urllib
import urllib2
import re
import requests

number = 5000
stack = 50
iteration = int(number/stack)
output = []
for j in xrange(iteration):
    s = j+1
    url = 'http://mathoverflow.net/questions?page='+str(s)+'&sort=votes'
    reads = urllib2.urlopen(url)
    html = reads.read()
    pattern = re.compile(
        r'<span class="vote-count-post "><strong>(.*?)</strong>')
    patterna = re.compile(r'class="question-hyperlink">(.*?)</a>')
    results = re.findall(pattern, html)
    resultsa = re.findall(patterna, html)
    for i in xrange(len(results)):
        print 'number:'+str(j*stack+i)+' '+'vote:'+str(results[i])+' '+'title:'+str(resultsa[i])
    print j

#work = open('data.txt', 'w')
# work.write(output)
# work.close()
