import traceback
try:
    raise Exception('Error Message')
except:
    errorFile = open('ErrorLog.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback info was written to error log')