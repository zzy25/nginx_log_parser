This ptoject is inspired by [chriso/nginx_parser](https://github.com/chriso/nginx_parser), big thanks to him.

#Installation

Currently, there is only python implementation. You can just download the single python file into your working directory.
I will add ruby implementation when time permits.

#Usage

##python
read nginx log file

``` python
from nginx_log_parser import NginxLogParser

parser = NginxLogParser('$remote_addr - $remote_user [$time_local] "$request" ' + \
                        '$status $body_bytes_sent "$http_referer" "X" ' + \
                        '$server_name "$http_user_agent" "$request_time" "-X-" "$upstream_addr" "$upstream_response_time" "$bytes_sent" "$request_length" ') #feed a nginx log config 
with open('path/to/nginx/log','w') as fp:
    for f in fp:
        parser.parse_line(f)#will return a dict.keys in the dict is the variablename in the nginx config, values is the real result in the log file
        #do things
```

#Limitation
You should provide properly wrapped nginx log config.If there is a space in the value, you should wrapp it with a " or anything that is not part of variable name([\d\w\_]). Of course, you should make sure the wrapping character will never show up in the value.

#License
MIT License! Do what you want.
