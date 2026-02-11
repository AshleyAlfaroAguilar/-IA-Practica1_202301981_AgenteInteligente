#Autor: Ashley Dayane Alfaro Aguilar 
#carne: 202301982
#Ingenieria en sistemas 

from agente_financiero import AgenteFinanciero


def leer_float(mensaje: str) -> float:
    while True:
        dato = input(mensaje).strip()
        try:
            return float(dato)
        except ValueError:
            print("Entrada inválida. Ingresa un número:")


def imprimir_reporte(r: dict) -> None:
    print("\n" + "=" * 60)
    print("REPORTE FINANCIERO PERSONAL")
    print("=" * 60)

    print(f"Ingreso mensual:              Q {r['ingreso']:.2f}")
    print(f"Gastos fijos:                 Q {r['gastos_fijos']:.2f}")
    print(f"Gastos variables:             Q {r['gastos_variables']:.2f}")
    print("-" * 60)
    print(f"Total de gastos:              Q {r['total_gastos']:.2f}")
    print(f"Ahorro mensual:               Q {r['ahorro']:.2f}")
    print("-" * 60)
    print(f"% Gastos (total):             {r['porcentaje_gastos']:.2f}%")
    print(f"% Ahorro:                     {r['porcentaje_ahorro']:.2f}%")
    print(f"% Gastos fijos:               {r['porcentaje_fijos']:.2f}%")
    print(f"% Gastos variables:           {r['porcentaje_variables']:.2f}%")
    print("-" * 60)
    print(f"Clasificación estado financiero: {r['estado']}")
    print("-" * 60)

    print("Recomendaciones:")
    for i, rec in enumerate(r["recomendaciones"], 1):
        print(f"  {i}. {rec}")

    print("=" * 60 + "\n")


def main():
    print("Agente Inteligente de Asesoría Financiera Personal")
    print("Ingrese valores mensuales en quetzales (Q).\n")

    ingreso = leer_float("Ingreso mensual: Q ")
    gastos_fijos = leer_float("Gastos fijos mensuales: Q ")
    gastos_variables = leer_float("Gastos variables mensuales: Q ")

    agente = AgenteFinanciero()
    resultado = agente.analizar(ingreso, gastos_fijos, gastos_variables)

    imprimir_reporte(resultado)

    # permitir correr otro escenario sin reiniciar el programa
    while True:
        opcion = input("¿Deseas probar otro escenario? (s/n): ").strip().lower()
        if opcion == "s":
            print()
            ingreso = leer_float("Ingreso mensual: Q ")
            gastos_fijos = leer_float("Gastos fijos mensuales: Q ")
            gastos_variables = leer_float("Gastos variables mensuales: Q ")

            resultado = agente.analizar(ingreso, gastos_fijos, gastos_variables)
            imprimir_reporte(resultado)
        elif opcion == "n":
            print("¡Hasta pronto!")
            break
        else:
            print("Responde con 's' o 'n'.")


if __name__ == "__main__":
    main()
