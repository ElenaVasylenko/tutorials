from threading import Lock, Thread

# Classic banking example

accountone = Lock()
accounttwo = Lock()


def transfer(accountone, accounttwo):
    accountone.acquire()
    accounttwo.acquire()
    print("Transaction done")
    accountone.release()
    accounttwo.release()


def transfer_do(accountone, accounttwo):
    while True:
        transfer(accountone, accounttwo) # send money from first account to second
        transfer(accounttwo, accountone) # send money from second account to first


for x in range(30):
    t = Thread(target=transfer_do, args=(accountone, accounttwo))
    t.start()