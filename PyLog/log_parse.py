# coding=utf-8
import os
import re
import sys
import IP

class log:
    _fw1 = open("out\\visit.txt", 'w')
    _fw2 = open("out\\address.txt", 'w', encoding="utf-8")

    def __init__(self):
        self._fw1.write("date         uv   pv-index" + "\n" )

    def __del__(self):
        self._fw1.close()
        self._fw2.close()

    # delete folder
    def delete_file_folder(self, src):
        if os.path.isfile(src):
            try:
                os.remove(src)
            except:
                pass
        elif os.path.isdir(src):
            for item in os.listdir(src):
                item_src = os.path.join(src,item)
                self.delete_file_folder(item_src)
            try:
                os.rmdir(src)
            except:
                pass

    # only "localhost_access_log.XXX" is used
    def delete_unrelated_file(self, src):
        for item in os.listdir(src):
            if not item.startswith("localhost_access_log"):
                item_src = os.path.join(src,item)
                os.remove(item_src)

    # whether an ip address comes from NJU
    def is_NJU(self, ip):
        if ip.startswith("114.212"):
            return True
        else:
            return False

    '''
    tomcat log files
    input required: folder name
    '''
    def parse_tomcat_log(self, dir_name):
        self.delete_unrelated_file(dir_name)
        for i in os.listdir(dir_name):
            self.each_tomcat(i)

    def each_tomcat(self, name):
        # get date "localhost_access_log.2015-03-17.txt"
        date = name[name.index('.')+1: name.index('.', name.index('.')+1)]

        # data
        ip_list = []
        uv = 0
        non_nju = 0
        pv_index = 0

        address_tp = []
        address_list = []

        # read each file
        f = open("logs\\" + name, 'r')
        lines = f.readlines()
        for each in lines:
            item = each.split(' ')
            ip = item[0]
            req = item[6]

            if ip not in ip_list :
                ip_list.append(ip)
                uv = uv + 1
                if not self.is_NJU(ip):
                    non_nju = non_nju + 1

            if not self.is_NJU(ip):
                pattern = re.compile(r'.*ct_repository.*')
                match = pattern.match(req)
                if match:
                    pv_index += 1
                    test = IP.find(ip)
                    s = ' '.join(test.split())
                    if s not in address_tp:
                        address_tp.append(s)
                        address_list.append([s, " " + each])

        # write visit num of each day
        self._fw1.write( date + "   " + str(non_nju) + "   " + str(pv_index) + "\n" )

        # write address
        self._fw2.write(date + "\n")
        for each in address_list:
            self._fw2.writelines(each)
        self._fw2.write("\n")


if __name__=='__main__':
    print(sys.getdefaultencoding())
    l = log()
    l.parse_tomcat_log("logs")