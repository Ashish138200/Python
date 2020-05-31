import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#----------------------for writing logging msgs in a file---------------------------------------------------------------
logging.basicConfig(filename='log.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#-----------------------------disable all the logging msg(critical)-----------------------------------------------------
logging.disable(logging.CRITICAL)
#-----------------------but passing logging.warning/error/info will disable the particular one--------------------------
logging.debug("Start")
def fact(n):
    logging.info("Start of fact(%s)"%(n))
    t = 1
    for i in range(1,n+1):
        t *= i
        logging.debug('i is %s, is %s' %(i, t))
    return t
print(fact(5))
logging.debug("End")

'''
##Log Levels##
debug(lowest)
info
warning
error
critical(highest)
'''