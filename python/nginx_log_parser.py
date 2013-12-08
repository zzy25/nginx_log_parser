import re

class NginxLogParser:
    """
    This class implements a nginx log parser. After feeding a nginx log format, it generates a regex for
    that specify format. Then we use this regex to extract useful information from nginx log.
    """
    format_directive = r'(\S)?\$([\w_]+)(\S)?'
    def __init__(self,formatter):
        self.parser = formatter
        self.directive = {}
        i = 0
        for re_matched in re.finditer(self.format_directive,formatter):
            left,variable,right = re_matched.groups()
            self.directive[variable] = i
            i = i + 1
            if left:
                left = self.escape(left)
            else:
                left = ''
            if right:
                right = self.escape(right)
            else:
                right = ''
            if left or right:
                if left != right:
                    regex = left + '([^' +left + right + ']+)' + right
                else:
                    regex = left + '([^' + right + ']+)' + right
            else:
                regex = r'([^\s]+)'
            self.parser = self.parser.replace(re_matched.group(0),regex,1)
        self.regex = self.parser + '$'
        self.result = self.directive.copy()

    def escape(self,string):
        return re.sub(r'[.*+?|()\[\]{}]',r'\\\g<0>',string)

    def parse_line(self,line):
        find_result = re.findall(self.regex,line)
        if find_result:
            for k in self.result:
                self.result[k] = find_result[0][self.directive[k]]
            return self.result
        else:
            return {}
