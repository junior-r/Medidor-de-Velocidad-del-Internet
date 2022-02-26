from speedtest import Speedtest


print('-- Midiendo Velocidad de su Intenet --\n')
st = Speedtest()
vUpload = st.upload()
vDownload = st.download()


def calcular_velocidad():
  global vUpload, vDownload
  print('Calculando...\n')
  vUpload = float(vUpload) / 1048576
  vDownload = float(vDownload) / 1048576
  return vUpload, vDownload


repetir = 'si'

while repetir == 'si':
  vUpload, vDownload = calcular_velocidad()
  print(f'La Velocidad de Carga: {vUpload} - Mbps')
  print(f'La Velocidad de Descarga: {vDownload} - Mbps')
  repetir = input('¿Recalcular?: ').lower()
