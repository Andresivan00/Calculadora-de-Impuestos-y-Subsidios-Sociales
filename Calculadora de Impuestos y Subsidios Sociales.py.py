# =================================================
# DESCRIPCIÓN GENERAL
# Este programa determina si una persona debe pagar impuesto sobre su ingreso,
# cuánto debe pagar y si califica para subsidio del gobierno según:
# - Ingreso mensual
# - Edad (beneficio para mayores de 60 y 65 años)
# - Número de personas a cargo
# Basado en reglas tributarias simplificadas de Colombia.
# =================================================

# =================================================
# PARTE 1: Entrada de datos del usuario
# =================================================
nombre_completo = input("Ingrese su nombre completo: ")                    # Nombre de la persona
edad = int(input("¿Cuántos años tiene?: "))                                # Edad (importante para descuentos)
ingreso_mensual = int(input("¿De cuánto es su ingreso mensual?: "))       # Salario mensual en pesos
numero_de_personas_a_cargo = int(input("¿Cuál es el número de personas que tiene a cargo?: "))  # Hijos, padres, etc.

# =================================================
# PARTE 2: Inicialización de variables de resultado
# =================================================
subsidio = ""                    # ¿Recibe subsidio? → "Sí" o "No"
impuesto_aplicado_cadena = ""    # Porcentaje como texto: "10%", "20%", etc.
impuesto_aplicado_entero = 0.0   # Porcentaje como decimal: 0.1, 0.2, etc.
valor_del_impuesto = 0.0         # Valor en pesos que debe pagar de impuesto

# =================================================
# PARTE 3: Lógica principal - Determinar subsidio e impuesto
# =================================================
# Reglas basadas en ingreso, edad y personas a cargo

if (ingreso_mensual < 3000000 and numero_de_personas_a_cargo >= 1) or (edad > 65 and ingreso_mensual < 4000000):
    # Caso especial: subsidio para familias o adultos mayores de bajos ingresos
    subsidio = "Sí"
    impuesto_aplicado_cadena = "0%"
    impuesto_aplicado_entero = 0

elif 2000000 <= ingreso_mensual <= 4000000 and edad < 60:
    # Rango medio-bajo, menor de 60 años → 10%
    subsidio = "No"
    impuesto_aplicado_cadena = "10%"
    impuesto_aplicado_entero = 0.1

elif 2000000 <= ingreso_mensual <= 4000000 and edad >= 60:
    # Mismo rango pero mayor de 60 → igual 10% (no hay descuento aquí, se puede mejorar)
    subsidio = "No"
    impuesto_aplicado_cadena = "10%"
    impuesto_aplicado_entero = 0.1

elif 4000001 <= ingreso_mensual <= 6000000 and edad < 60:
    # Rango medio-alto, menor de 60 → 20%
    subsidio = "No"
    impuesto_aplicado_cadena = "20%"
    impuesto_aplicado_entero = 0.2

elif 4000001 <= ingreso_mensual <= 6000000 and edad >= 60:
    # Mismo rango pero mayor de 60 → 15% (descuento por edad)
    subsidio = "No"
    impuesto_aplicado_cadena = "15%"
    impuesto_aplicado_entero = 0.15

elif ingreso_mensual > 6000000 and edad < 60:
    # Ingresos altos, menor de 60 → 30%
    subsidio = "No"
    impuesto_aplicado_cadena = "30%"
    impuesto_aplicado_entero = 0.3

elif ingreso_mensual > 6000000 and edad >= 60:
    # Ingresos altos, pero mayor de 60 → 25% (descuento por edad)
    subsidio = "No"
    impuesto_aplicado_cadena = "25%"
    impuesto_aplicado_entero = 0.25

# =================================================
# PARTE 4: Cálculo del valor exacto del impuesto en pesos
# =================================================
valor_del_impuesto = int(ingreso_mensual * impuesto_aplicado_entero)  # Ej: 5000000 * 0.2 = 1000000

# =================================================
# PARTE 5: Mostrar resultado final al usuario
# =================================================
print(f"\nBuenos días Sr@ {nombre_completo}, con {edad} años de edad, su ingreso mensual es de ${ingreso_mensual:,} y tiene {numero_de_personas_a_cargo} personas a su cargo.")
print(f"Se le aplicó un {impuesto_aplicado_cadena} de impuesto, siendo el valor del impuesto a pagar ${valor_del_impuesto:,}.")
print(f"Usted {subsidio} fue elegible para beneficios sociales.")