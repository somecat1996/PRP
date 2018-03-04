import re
from scanner_lib import Result


tmp = open('456.xml', 'r').read()
result = []
results = re.findall("(<result.*?</result>)", tmp, re.S)
for i in results:
    tmp = Result(i)
    if tmp.name == '':
        continue
    else:
        flag = True
        for j in result:
            if j.Compare(tmp):
                flag = False
        if flag:
            result.append(tmp)

for i in result:
    print "id:%s" % i.id
    # print "ownername:%s" % i.ownername
    # print "comment:%s" % i.comment
    # print "host:%s" % i.host
    print "port:%s" % i.port
    print "nvt_oid:%s" % i.nvt_oid
    print "name:%s" % i.name
    print "family:%s" % i.family
    print "summary:%s" % i.summary
    print "solution:%s" % i.solution
    print "scan_nvt_version:%s" % i.scan_nvt_version
    print "threat:%s" % i.threat
    print "severity:%s" % i.severity
    print "type:%s" % i.type
    print "qod:%s" % i.qod
    print "description:%s" % i.description
    print '\n\n\n'