# Classes associadas entre si são independentes
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Noah')
caneta = Caneta('Montblanc')
maquina_escrever = MaquinaDeEscrever('Royal')

escritor.ferramenta = maquina_escrever
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
