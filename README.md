# [IA] Práctica1_202301982 — Agente Inteligente de Asesoría Financiera Personal

## Estudiante
- Nombre: Ashley Dayane Alfaro Aguilar 
- Carnet: 20230198
- Curso: Inteligencia Artificial

## Objetivo
Implementar un agente inteligente basado en reglas que solicita ingreso mensual, gastos fijos y gastos variables; analiza la situación financiera, calcula ahorro y porcentajes, clasifica el estado financiero (saludable/riesgo/crítico) y genera recomendaciones justificadas.  
**No utiliza Machine Learning ni librerías externas.**

## Requisitos
- Python 3.10 o superior
- Librerías permitidas: `os`, `sys`, `time`, `math` (en este proyecto no se requiere ninguna adicional)

## Estructura del proyecto
```
Practica1_AgenteFinanciero/
 ├─ main.py
 ├─ agente_financiero.py
 └─ README.md
```

## Cómo ejecutar
1. Abrir terminal en la carpeta del proyecto.
2. Ejecutar:
```bash
python main.py
```
*(En algunos sistemas: `python3 main.py`)*

## Reglas implementadas (resumen)
Fórmulas:
- total_gastos = gastos_fijos + gastos_variables
- ahorro = ingreso - total_gastos
- %gastos = (total_gastos / ingreso) * 100
- %ahorro = (ahorro / ingreso) * 100

Clasificación:
- **CRÍTICO:** ahorro < 0
- **RIESGO:** ahorro >= 0 y %ahorro < 10
- **SALUDABLE:** %ahorro >= 10

Umbrales para recomendaciones:
- Ahorro mínimo recomendado: 10%
- Variables ideal: ≤ 30% del ingreso
- Fijos altos: > 60% del ingreso
- Ahorro excelente: ≥ 20%

## Video de demostración
- Enlace: https://youtu.be/zz63q4RMi3s

