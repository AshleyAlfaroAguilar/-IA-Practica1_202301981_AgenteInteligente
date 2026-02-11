#Autor: Ashley Dayane Alfaro Aguilar 
#carne: 202301982
#Ingenieria en sistemas
 

"""
Agente Inteligente de Asesoría Financiera Personal 

Reglas / Fórmulas base:
- total_gastos = gastos_fijos + gastos_variables
- ahorro = ingreso - total_gastos
- %gastos = (total_gastos / ingreso) * 100
- %ahorro = (ahorro / ingreso) * 100

Clasificación (reglas explícitas):
R1: Si ahorro < 0 -> CRITICO
R2: Si ahorro >= 0 y %ahorro < 10 -> RIESGO
R3: Si %ahorro >= 10 -> SALUDABLE

reglas explícitas:
- Si ahorro < 0: reducir gastos (prioridad: variables) para equilibrar.
- Si %ahorro < 10: aumentar ahorro a 10% reduciendo variables.
- Si %variables > 30%: sugerir bajar variables a 30%.
- Si %fijos > 60%: sugerir revisar/renegociar gastos fijos.
- Si %ahorro >= 20%: sugerir fondo de emergencia 3-6 meses.
"""


class AgenteFinanciero:
    def __init__(self):
        # Estado simple del agente: historial de análisis realizados
        self.historial = []

        # reglas parametrizadas y visibles
        self.AHORRO_MINIMO_PCT = 10.0
        self.VARIABLES_MAX_PCT = 30.0
        self.FIJOS_ALTO_PCT = 60.0
        self.AHORRO_BUENO_PCT = 20.0

    def analizar(self, ingreso: float, gastos_fijos: float, gastos_variables: float) -> dict:
        # Normalizar entradas negativas 
        if gastos_fijos < 0:
            gastos_fijos = 0.0
        if gastos_variables < 0:
            gastos_variables = 0.0

        total_gastos = gastos_fijos + gastos_variables
        ahorro = ingreso - total_gastos

        # Evitar división por cero
        if ingreso <= 0:
            porcentaje_gastos = 0.0
            porcentaje_ahorro = 0.0
            porcentaje_fijos = 0.0
            porcentaje_variables = 0.0
        else:
            porcentaje_gastos = (total_gastos / ingreso) * 100.0
            porcentaje_ahorro = (ahorro / ingreso) * 100.0
            porcentaje_fijos = (gastos_fijos / ingreso) * 100.0
            porcentaje_variables = (gastos_variables / ingreso) * 100.0

        estado = self._clasificar_estado(ingreso, ahorro, porcentaje_ahorro)
        recomendaciones = self._generar_recomendaciones(
            ingreso=ingreso,
            gastos_fijos=gastos_fijos,
            gastos_variables=gastos_variables,
            total_gastos=total_gastos,
            ahorro=ahorro,
            porcentaje_ahorro=porcentaje_ahorro,
            porcentaje_fijos=porcentaje_fijos,
            porcentaje_variables=porcentaje_variables,
            estado=estado,
        )

        resultado = {
            "ingreso": ingreso,
            "gastos_fijos": gastos_fijos,
            "gastos_variables": gastos_variables,
            "total_gastos": total_gastos,
            "ahorro": ahorro,
            "porcentaje_gastos": porcentaje_gastos,
            "porcentaje_ahorro": porcentaje_ahorro,
            "porcentaje_fijos": porcentaje_fijos,
            "porcentaje_variables": porcentaje_variables,
            "estado": estado,
            "recomendaciones": recomendaciones,
        }

        self.historial.append(resultado)
        return resultado

    def _clasificar_estado(self, ingreso: float, ahorro: float, porcentaje_ahorro: float) -> str:
        # R1: Si ahorro < 0 -> CRITICO
        if ahorro < 0:
            return "CRITICO"

        # Si ingreso <= 0 y no hay ahorro negativo, lo marcamos como riesgo por datos inválidos
        if ingreso <= 0:
            return "RIESGO"

        # R2: ahorro >= 0 y %ahorro < 10 -> RIESGO
        if porcentaje_ahorro < self.AHORRO_MINIMO_PCT:
            return "RIESGO"

        # R3: %ahorro >= 10 -> SALUDABLE
        return "SALUDABLE"

    def _generar_recomendaciones(
        self,
        ingreso: float,
        gastos_fijos: float,
        gastos_variables: float,
        total_gastos: float,
        ahorro: float,
        porcentaje_ahorro: float,
        porcentaje_fijos: float,
        porcentaje_variables: float,
        estado: str,
    ) -> list:
        recs = []

        # Validación básica si el ingreso no es válido
        if ingreso <= 0:
            recs.append("El ingreso ingresado es 0 o negativo. Verifica los datos para obtener un análisis correcto.")
            return recs

        # Reglas por estado
        if estado == "CRITICO":
            deficit = -ahorro  # cuánto falta para llegar a 0
            recs.append(
                f"Estás gastando más de lo que ganas. Debes reducir gastos al menos Q {deficit:.2f} para equilibrar tu presupuesto."
            )
            # Prioridad: recortar variables primero
            if gastos_variables > 0:
                recorte_sugerido = deficit
                if recorte_sugerido > gastos_variables:
                    recorte_sugerido = gastos_variables
                recs.append(
                    f"Prioriza recortar gastos variables en aproximadamente Q {recorte_sugerido:.2f} (entretenimiento, compras no esenciales, comidas fuera, etc.)."
                )
            else:
                recs.append("Como tus gastos variables son 0, revisa gastos fijos (renta, servicios, suscripciones) para recortar o renegociar.")
        elif estado == "RIESGO":
            # Meta mínima de ahorro del 10%
            ahorro_objetivo = (self.AHORRO_MINIMO_PCT / 100.0) * ingreso
            falta_para_meta = ahorro_objetivo - ahorro
            if falta_para_meta < 0:
                falta_para_meta = 0.0
            recs.append(
                f"Tu ahorro es bajo. Se recomienda ahorrar al menos {self.AHORRO_MINIMO_PCT:.0f}% (Q {ahorro_objetivo:.2f})."
            )
            if falta_para_meta > 0:
                recs.append(
                    f"Para llegar a esa meta, reduce gastos en aproximadamente Q {falta_para_meta:.2f} (idealmente de gastos variables)."
                )
        else:  # SALUDABLE
            recs.append(f"Tu situación es saludable: estás ahorrando al menos {self.AHORRO_MINIMO_PCT:.0f}% de tu ingreso.")
            if porcentaje_ahorro >= self.AHORRO_BUENO_PCT:
                recs.append(
                    f"Excelente: tu ahorro es {porcentaje_ahorro:.2f}%. Considera construir/fortalecer un fondo de emergencia de 3 a 6 meses de gastos."
                )

        # Reglas adicionales
        if porcentaje_variables > self.VARIABLES_MAX_PCT:
            # sugerir bajar variables a 30%
            variables_objetivo = (self.VARIABLES_MAX_PCT / 100.0) * ingreso
            exceso = gastos_variables - variables_objetivo
            if exceso < 0:
                exceso = 0.0
            recs.append(
                f"Tus gastos variables son altos ({porcentaje_variables:.2f}%). Intenta bajarlos a {self.VARIABLES_MAX_PCT:.0f}% (≈ Q {variables_objetivo:.2f}), reduciendo alrededor de Q {exceso:.2f}."
            )

        if porcentaje_fijos > self.FIJOS_ALTO_PCT:
            recs.append(
                f"Tus gastos fijos son elevados ({porcentaje_fijos:.2f}%). Revisa opciones para renegociar: renta, servicios, deudas, suscripciones."
            )

        # Si no hay recomendaciones, dar una genérica coherente
        if not recs:
            recs.append("Mantén un registro mensual y revisa tus gastos para sostener o mejorar tu porcentaje de ahorro.")

        return recs



