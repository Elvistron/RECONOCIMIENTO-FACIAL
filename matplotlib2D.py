import pandas as pd
import matplotlib.pyplot as plt


datos= pd.read_csv("casasboston.csv")

df = datos[["RM","CRIM","MEDV","TOWN","CHAS"]]

df = datos.rename(columns={
	"TOWN":"CIUDAD",
	"CRIM":"INDICE_CRIMEN",
	"INDUS":"PCT_ZONA_INDUSTRIAL",
	"CHAS":"RIO_CHARLES",
	"RM":"N_HABITACIONES_MEDIO",
	"MEDV":"VALOR_MEDIANO",
	"LISTAT":"PCT_CLASE_BAJA"
	})
print (df.sample(5))

df.N_HABITACIONES_MEDIO.plot.hist()
plt.show()
