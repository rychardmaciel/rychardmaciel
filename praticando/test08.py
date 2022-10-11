#by Rychard Maciel 
#conversor medida

from msilib.schema import Media

medida = float (input ("Digite uma medida em metros: "))
cm = medida * 100
mm = medida * 1000
print ("A medida de {} m corresponde a {:.0f} cm e {:.0f} mm" .format(medida, cm, mm))