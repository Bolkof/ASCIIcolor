# Definición de códigos de colores y estilos
rojo = "\033[91m"
cyan = "\033[96m"
magenta = "\033[95m"
blanco = "\033[97m"
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
negro = "\033[90m"

reset_color = "\033[0m"
subrayado = "\033[4m"
parpadeante = "\033[5m"
invertido = "\033[7m"
tachado = "\033[9m"

amarillo_brillante = "\033[93;1m"
rojo_brillante = "\033[91;1m"
verde_brillante = "\033[92;1m"
azul_brillante = "\033[94;1m"
magenta_brillante = "\033[95;1m"
cyan_brillante = "\033[96;1m"
blanco_brillante = "\033[97;1m"

# Ejemplo de uso
if __name__ == "__main__":
	print(rojo + "Texto en rojo" + reset_color)
	print(verde + "texto verde" + reset_color)
	print(verde_brillante + "Texto en verde brillante" + reset_color)
	print(azul + subrayado + "Texto en azul subrayado" + reset_color)
	print(magenta_brillante + parpadeante + "Texto en magenta brillante y parpadeante" + reset_color)
	print(cyan + invertido + "Texto en cyan con fondo invertido" + reset_color)