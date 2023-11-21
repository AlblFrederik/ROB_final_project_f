import numpy as np

rob = robCRS93() # nebo rob = robCRS97()
c = Commander(rob)
c.open_comm(tty_dev)  ???/dev/ttyUSB0 ???
c.init()

c.soft_home()
c.rcon.close()
