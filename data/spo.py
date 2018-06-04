# -*- coding: utf-8 -*- 



from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


entity_attr = {u"索引": "index", u"相关": "refer", u"名字": "name", u"定义":"education"}
edge_attr = {u" ": "position"}


entity_attr = dict(zip(entity_attr.values(), entity_attr.keys()))
edge_attr = dict(zip(edge_attr.values(), edge_attr.keys()))


dt = str(datetime.now())[:19]

def read_nodes(frname, fwname, refer, write_mode='w'):
    with open(frname, 'r') as fr, open(fwname, write_mode) as fw:
        header = fr.readline().strip()
        header = header.split('\t')[4:]
        for i,h in enumerate(header):
            header[i] = refer.get(h,h)
        if write_mode=='w':
            fw.write("subj\tpred\tobj\ttype\n")
        for line in fr:
            parts = line.strip().split('\t')
            subj = parts[0]
            for i,p in enumerate(parts[4:]):
                fw.write("%s\t%s\t%s\tproperty\n"%(subj, header[i], p))


def read_edges(frname, fwmang, fwspo, refer, write_mode='a'):
    with open(frname, 'r') as fr, open(fwmang, 'w') as fw, open(fwspo, write_mode) as spo:
        header = fr.readline().strip()
        header = header.split('\t')[5:]
        for i,h in enumerate(header):
            header[i] = refer.get(h,h)
        if write_mode=='w':
            fw.write("subj\tpred\tobj\ttype\tcreate_time\tupdate_time\n")
        fw.write("company_id\ttitle\tperson_id\ttype\tcreate_time\tupdate_time\t\n")
        for line in fr:
            parts = line.strip().split('\t')
            subj = parts[0]
            obj = parts[1]
            for i,p in enumerate(parts[5:]):
                fw.write("%s\t%s\t%s\trelation\t%s\t%s\n"%(subj, p, obj, dt, dt))
            # treate all management relation a
            spo.write("%s\t 管\t%s\trelation\t%s\t%s\n"%(subj, obj, dt, dt))


read_nodes('entities_se.txt', 'spo.txt', entity_attr)

