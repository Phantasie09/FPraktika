import numpy as np
path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharine/"
name="2.1.10pa"
i=2
arbeit = np.load(name+"/Image_time_"+str(i+1)+".npy")
bearbeitet=arbeit[288:372]
print(arbeit)