#-*- coding: utf-8 -*-
import re
import xlwt
import os
url = os.getcwd()
url = url.replace('\\', '/')
urls = url+'/example.txt'
workbook = xlwt.Workbook()
for key in urlts:
    f = open(urlt+key, 'r')
    d = f.read()
    dlists = d.split(
        "-----------------------------------------------------------------------")
    if len(dlists[-1]) == 0:
        n = len(dlists)-1
    else:
        n = len(dlists)
    output = [[u"【文件序号】", u"【来源篇名】", u"【英文篇名】", u"【来源作者】", u"【文章类型】", u"【基    金】", u"【期    刊】",
               u"【第一机构】", u"【机构名称】", u"【学科分类】", u"【第一作者】", u"【中图类号】", u"【年代卷期】", u"【关 键 词】", u"【基金类别】", u"【参考文献】"]]
    position = 0
    maxwide = 20*n
    for i in xrange(n):
        delistsutf8 = dlists[i].decode('utf8')
        result = re.split(u'\u3010|\u3011', delistsutf8)
        result[-1] = result[-1].replace('\n', '$')
        result[-1] = result[-1][1:]
        del result[0]
        content = [' ' for i in xrange(maxwide)]
        for j in range(1, len(result), 2):
            result[j] = result[j][:-1]
        for j in range(0, len(result), 2):
            flag = 0
            for k in xrange(len(output[0])):
                if u'【'+result[j]+u'】' == output[0][k]:
                    content[k] = result[j+1]
                    flag = 1
            if flag == 0:
                output[0].append(u'【'+result[j]+u'】')
                content[len(output[0])-1] = result[j+1]
        output.append(content)
    wide = len(output[0])
    for i in xrange(n):
        output[i+1] = output[i+1][:wide]
    booksheet = workbook.add_sheet(key, cell_overwrite_ok=True)
    for i, row in enumerate(output):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
workbook.save('result.xls')
