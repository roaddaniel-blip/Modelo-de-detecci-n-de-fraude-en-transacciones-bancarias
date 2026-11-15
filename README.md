# Modelo de detección de fraude en transacciones bancarias.
___________________________________________________________________________________________________________
**Institución:** Universidad Tecmilenio  
**Autor:** Daniel Roa Acosta
**Actividad:** 8 — Monitorización, Mantenimiento y Gobernanza Operativa
___________________________________________________________________________________________________________

### Especificaciones Técnicas
* **Modelo:** Random Forest Classifier
* **Dataset:** Fraude en transacciones bancarias
* **Herramienta de MLOps:** MLflow 3.14.0
 __________________________________________________________________________________________________________

### Descripción
Este repositorio busca garantizar los pilares fundamentales del servicio de detección de fraude mediante prácticas modernas de **MLOps** y **observabilidad**:
* *Continuidad operativa*
* *Confiabilidad del sistema*
* *Trazabilidad de extremo a extremo*
* *Gobernanza operativa*

________________________________________________________________________________________________________________

### Estructura
```text
fraudes-bancarios/
├── monitoring.py             # Sistema de monitoreo con MLflow
├── simulate_incidents.py     # Simulación de incidentes críticos
├── runbooks.py               # Runbooks de respuesta automatizada
├── requirements.txt          # Dependencias
├── monitoring.log            # Log generado al ejecutar monitoring.py
├── incidents.log             # Log generado al ejecutar simulate_incidents.py
└── evidencias/
    ├── mlflow_training_runs.png
    ├── mlflow_evaluation_runs.png
    ├── mlflow_baseline_normal.png
    ├── mlflow_modelo_degradado.png
    ├── mlflow_umbral_estandar_050.png
    ├── mlflow_incidente_degradacion.png
    └── mlflow_incidente_alta_latencia.png

____________________________________________________________________________________________________________________

### Requerimientos 
Librería	Versión
mlflow	3.14.0
scikit-learn	1.4.2
numpy	1.26.4
pandas	2.2.2

___________________________________________________________________________________________________________________

### Arquitectura del Flujo Operativo (MLOps)

1. **Transacciones bancarias**
   * *Detalle:* Datos sintéticos / flujo de eventos
2. **API de inferencia + modelo ML**
   * *Tecnologías:* FastAPI · Clasificador de fraude
3. **Capa de observabilidad**
   * *Componentes:* Métricas · Logs · Trazas · Drift
4. **Monitorización y dashboards**
   * *Herramientas:* Prometheus · Grafana · MLflow
5. **Motor de alertas y runbooks**
   * *Mecanismos:* SLO · Error budgets · Alertmanager
6. **Acciones de mitigación y respuesta**
   * *Operaciones:* Rollback · Reentrenamiento · Escalamiento





