#!/usr/bin/python
import sys
import dns
import clientsubnetoption
import pdb

def arg_parse(paramer):
    par_list = paramer.split('&')
    par_dic = {}
    for p in par_list:
        par_dic[p.split('=')[0]] = p.split('=')[1]
    
    message = dns.message.make_query(par_dic['domain'], 'A')
    if par_dic.has_key('ip'):
        ip = par_dic['ip']
        cso = clientsubnetoption.ClientSubnetOption(ip, 32)
        message.use_edns(edns=True, ednsflags=0, options=[cso])
        message.use_edns(options=[cso])
    data = dns.query.udp(message, '8.8.8.8')

    if not data.answer:
        return 'not rr'
    
    rr_str = ''
    for rdata in data.answer[-1]:
        rr_str = rr_str + str(rdata.to_text()) + ','
    #pdb.set_trace()
    if par_dic.has_key('ttl') and int(par_dic['ttl']) == 1:
        rr_str = rr_str + str(data.answer[0].ttl)
    else:
        rr_str = rr_str[:-1]
    return rr_str

def application(environ,start_response):
        start_response('200 OK',[('Content-Type','text/plain')])
        r = environ['QUERY_STRING']
        rr = arg_parse(r)
        yield rr

if __name__ == '__main__':
    print arg_parse('domain=dnstemplatenregion001.sina.com.cn&ip=32.22.12.25&ttl=1')

