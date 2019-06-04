import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(% s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is '+ str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(% s)' % (n))
    return total

print(factorial(3))
logging.debug('End of program')