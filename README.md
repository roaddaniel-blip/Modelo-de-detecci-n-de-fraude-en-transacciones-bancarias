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
```
___________________________________________________________________________________________________________________

### Requisitos y Dependencias

| Librería | Versión |
| :--- | :--- |
| `mlflow` | 3.14.0 |
| `scikit-learn` | 1.4.2 |
| `numpy` | 1.26.4 |
| `pandas` | 2.2.2 |

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

____________________________________________________________________________________________________________________

### Métricas de Evaluación y Umbrales Operativos

| Métrica | Descripción | Umbral propuesto |
| :--- | :--- | :---: |
| **Precision** | Proporción de transacciones clasificadas como fraude que realmente son fraudulentas. | **≥ 85 %** |
| **Recall** | Porcentaje de fraudes reales identificados correctamente. | **≥ 90 %** |
| **F1-score** | Equilibrio entre precision y recall. | **≥ 87 %** |
| **PR-AUC** | Capacidad de distinguir fraudes en conjuntos de datos desbalanceados. | **≥ 0,85** |
| **Tasa de falsos positivos (FPR)** | Porcentaje de transacciones legítimas clasificadas incorrectamente como fraude. | **≤ 2 %** |
| **Tasa de falsos negativos (FNR)** | Porcentaje de fraudes reales que el modelo no identifica. | **≤ 10 %** |

_________________________________________________________________________________________________________________________

### Niveles de Alerta y Severidad

| Alerta | Condición | Severidad |
| :--- | :--- | :---: |
| **Consumo crítico** | Burn rate ≥ 14,4 durante ventanas de 5 min y 1 h | **P1** |
| **Consumo elevado** | Burn rate ≥ 6 durante ventanas de 30 min y 6 h | **P2** |
| **Degradación sostenida** | Burn rate ≥ 3 durante ventanas de 2 h y 24 h | **P3** |
| **Operación estable** | Burn rate < 1 | **Normal** |

Clasificación de Incidentes y Tiempos de Respuesta (SLA)

| Prioridad | Impacto | Ejemplo | Tiempo objetivo de respuesta |
| :--- | :--- | :--- | :---: |
| **P1 · Crítica** | Riesgo financiero elevado o interrupción generalizada | Servicio indisponible o caída grave de detección de fraude | **≤ 5 min** |
| **P2 · Alta** | Degradación significativa del servicio | Aumento sostenido de latencia o pérdida de precision | **≤ 15 min** |
| **P3 · Media** | Anomalía controlada sin impacto inmediato importante | Data drift moderado | **≤ 1 h** |
| **P4 · Baja** | Evento informativo o preventivo | Variación leve dentro de tolerancias | **Revisión programada** |

_________________________________________________________________________________________________________________________

### Dashboard: Gestión de Alertas e Incidentes

El panel de monitoreo centralizará la información crítica para la respuesta operativa, permitiendo visualizar los siguientes indicadores:

* **Metadatos del incidente:** Prioridad asignada (**P1**, **P2**, **P3** o **P4**), hora exacta de detección y servicio afectado.
* **Control y seguimiento:** Responsable asignado, estado actual de atención y **runbook asociado** para su mitigación.
* **Métricas de impacto:** Tiempo transcurrido desde la detección, porcentaje de **presupuesto de error consumido** (*error budget*) y registro de las acciones correctivas aplicadas.

  <img width="568" height="308" alt="image" src="https://github.com/user-attachments/assets/9e7660e5-6474-4d79-ba23-f4dcb4198dd8" />

________________________________________________________________________________________________________________________

### Runbooks de respuesta a incidentes

| Prioridad | Descripción | Tiempo objetivo de respuesta | Responsable inicial |
| :--- | :--- | :---: | :--- |
| **P1 · Crítica** | Indisponibilidad generalizada o deterioro grave de detección con impacto confirmado | **≤ 5 minutos** | SRE / Operaciones |
| **P2 · Alta** | Degradación importante de latencia, precision o recall | **≤ 15 minutos** | MLOps / Data Science |
| **P3 · Media** | Data drift moderado o anomalía sin impacto inmediato | **≤ 1 hora** | MLOps / Data Engineering |
| **P4 · Baja** | Eventos preventivos o informativos | **Revisión programada** | Equipo responsable |

__________________________________________________________________________________________________________________________

### Estrategias de detección de data drift

| Variable | Cambio que se busca detectar | Riesgo potencial |
| :--- | :--- | :--- |
| **Importe de transacción** | Cambios en importes medios, medianas y percentiles. | Nuevos patrones de operaciones fraudulentas. |
| **Frecuencia transaccional** | Incrementos o disminuciones anómalas. | Fraude automatizado o cambios de comportamiento. |
| **Horario de operación** | Variaciones en la distribución por hora. | Nuevos patrones temporales de fraude. |
| **Canal de operación** | Cambios entre canales digitales, cajeros y comercios. | Desplazamiento del fraude entre canales. |
| **Ubicación geográfica agregada** | Variaciones regionales. | Cambios en patrones de riesgo. |
| **Tipo de comercio** | Modificaciones en categorías de establecimientos. | Concentración de fraude en determinados sectores. |
| **Fraud score** | Variación en las probabilidades estimadas por el modelo. | Cambio en la población evaluada o comportamiento predictivo. |

__________________________________________________________________________________________________________________________

### Documentación de respuesta automatizada

| Incidente | Condición de activación | Respuesta propuesta | Nivel de automatización |
| :--- | :--- | :--- | :--- |
| **Indisponibilidad** | Burn rate crítico de disponibilidad | Diagnóstico y preparación de rollback | Automática; ejecución según política |
| **Incremento de latencia** | Incumplimiento sostenido del SLO | Escalamiento horizontal controlado | Automática con límites |
| **Degradación del modelo** | Recall < 90 % confirmado | Iniciar pipeline de reentrenamiento | Preparación automática |
| **Data drift significativo** | PSI > 0,25 | Análisis y evaluación del modelo | Automática |
| **Pérdida de precisión** | Precision < 85 % | Evaluación de umbrales y versión anterior | Semiautomática |
| **Errores de infraestructura** | Instancias defectuosas | Reinicio o sustitución de instancias | Automática con controles |


___________________________________________________________________________________________________________________________


