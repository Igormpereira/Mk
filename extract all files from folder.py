import pandas as pd
from glob import glob
arquivos =sorted(glob('T:\Publico\Igor_Maier\shorts\Shorts Creations\\*.csv'))
todos=pd.concat((pd.read_csv(cont) for cont in arquivos),ignore_index=True)
print(todos)
exit()


