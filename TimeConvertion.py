s='12:05:45PM'
s_splited = s.split(":")
meridian_list=s_splited[2].split(s_splited[2][1])
del(meridian_list[0])
meridian="".join(meridian_list)
seconds_list = s_splited[2].split(s_splited[2][2])
del(seconds_list[1])
seconds = "".join(seconds_list)
del(s_splited[2])
s_splited.append(seconds)
if meridian == "AM":
    print(":".join(s_splited))
elif meridian == "PM":
    if s_splited[0] == "12":
        print(":".join(s_splited))
    else:
        hours=int(s_splited[0]) +12
        del(s_splited[0])
        s_splited.insert(0,str(hours))
        print(":".join(s_splited))