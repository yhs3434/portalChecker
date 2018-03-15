def convertDateStr(month,day):
    if(month>0 and month<10):
        monthStr="0"+str(month)
    elif(month>=10 and month<=12):
        monthStr=str(month)
    else:
        monthStr='-1'
    
    if(day>0 and day<10):
        dayStr="0"+str(day)
    elif(day>=10 and day<=31):
        dayStr=str(day)
    else:
        dayStr='-1'

    dateStr='2018.'+monthStr+'.'+dayStr
    return dateStr
