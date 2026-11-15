import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
import time
import logging
from datetime import datetime

# ── Configuración de logging unificado para Monitoreo ─────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("monitoring.log", mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ── SLOs definidos para el proyecto de Fraudes Bancarios ───────────────────
SLO = {
    "recall_min":        0.90,   # Recall mínimo establecido por negocio
    "precision_min":     0.85,   # Precisión mínima establecida
    "latencia_max_ms":   150.0,  # Latencia máxima aceptable de inferencia
    "error_budget":      0.05    # Margen de error tolerado
}

# ── Función de Estabilidad Poblacional (PSI) del Proyecto ──────────────────
def calcular_psi_local(baseline, target, num_buckets=10):
    baseline_percents, buckets = np.histogram(baseline, bins=num_buckets, density=True)
    target_percents, _ = np.histogram(target, bins=buckets, density=True)

    baseline_percents = np.where(baseline_percents == 0, 0.0001, baseline_percents)
    target_percents = np.where(target_percents == 0, 0.0001, target_percents)

    psi_value = np.sum((target_percents - baseline_percents) * np.log(target_percents / baseline_percents))
    return float(psi_value)

# ── Verificar SLOs Operativos ─────────────────────────────────────────────
def verificar_slos_proyecto(metricas):
    violaciones = []
    if metricas["recall"] < SLO["recall_min"]:
        violaciones.append(f"RECALL {metricas['recall']} < SLO {SLO['recall_min']}")
    if metricas["precision"] < SLO["precision_min"]:
        violaciones.append(f"PRECISION {metricas['precision']} < SLO {SLO['precision_min']}")
    if metricas["latencia_ms"] > SLO["latencia_max_ms"]:
        violaciones.append(f"LATENCIA {metricas['latencia_ms']}ms > SLO {SLO['latencia_max_ms']}ms")
    return violaciones

# ── Experimento MLflow Principal ──────────────────────────────────────────
def run_monitoreo_proyecto(nombre_run, metrics_dict, latencia_ms, dataset_actual, dataset_baseline=importes_baseline):
    logger.info(f"Iniciando validación y monitoreo para: {nombre_run}")

    # Calcular PSI con respecto a los datos de producción actuales
    psi_actual = calcular_psi_local(dataset_baseline, dataset_actual)

    # Compilar métricas operacionales finales
    metricas = {
        "precision":    metrics_dict["precision"],
        "recall":       metrics_dict["recall"],
        "f1_score":     metrics_dict["f1"],
        "pr_auc":       metrics_dict["pr_auc"],
        "latencia_ms":  round(latencia_ms, 2),
        "psi_drift":    round(psi_actual, 4)
    }

    violaciones = verificar_slos_proyecto(metricas)

    mlflow.set_experiment("Fraudes_Bancarios_Gobernanza")

    with mlflow.start_run(run_name=nombre_run):
        # ── Tags del Proyecto ──
        mlflow.set_tags({
            "modelo":    "Random Forest Classifier",
            "autor":     "Daniel Roa Acosta",
            "institucion": "Universidad Tecmilenio",
            "timestamp": datetime.now().isoformat()
        })

        # ── Parámetros del Experimento ──
        mlflow.log_params({
            "algoritmo": "Random Forest Classifier",
            "slo_recall_min": SLO["recall_min"],
            "slo_precision_min": SLO["precision_min"],
            "slo_latencia_max_ms": SLO["latencia_max_ms"],
            "error_budget": SLO["error_budget"]
        })

        # ── Registro de Métricas ──
        mlflow.log_metrics(metricas)
        mlflow.log_metric("slo_violaciones", len(violaciones))
        mlflow.log_metric("error_budget_consumido", max(0.0, SLO["recall_min"] - metricas["recall"]))

        # ── Logs de Alertas Operativas ──
        if violaciones:
            logger.error(f"SLO VIOLATIONS detectadas en {nombre_run}: {violaciones}")
            mlflow.set_tag("status", "SLO_VIOLATION")
        else: 
            logger.info(f"Todos los SLOs cumplidos para {nombre_run} ✅")
            mlflow.set_tag("status", "OK")

        # ── Consola Resumen ──
        print(f"\n{'='*55}")
        print(f"  Operación: {nombre_run}")
        print(f"{'='*55}")
        for k, v in metricas.items():
            print(f"  {k:<25}: {v}")
        if violaciones:
            print(f"\n  ⚠️  ALERTAS DE INCIDENCIA:")
            for v in violaciones:
                print(f"    - {v}")
        else:
            print(f"\n  ✅ Cumplimiento exitoso de SLOs")
        print(f"{'='*55}\n")


🔵 Run 1: Monitoreo Baseline Normal (Modelo v2)

=======================================================
  Operación: baseline_v2_normal
=======================================================
  precision                : 0.875
  recall                   : 0.923
  f1_score                 : 0.898
  pr_auc                   : 0.92
  latencia_ms              : 120.0
  psi_drift                : 0.0001

  ✅ Cumplimiento exitoso de SLOs
=======================================================


🔴 Run 2: Validación Modelo v3 (Falla Recall)
ERROR:__main__:SLO VIOLATIONS detectadas en degradacion_recall_v3: ['RECALL 0.846 < SLO 0.9']
ERROR:__main__:SLO VIOLATIONS detectadas en degradacion_latencia_infraestructura: ['LATENCIA 650.0ms > SLO 150.0ms']

=======================================================
  Operación: degradacion_recall_v3
=======================================================
  precision                : 0.891
  recall                   : 0.846
  f1_score                 : 0.868
  pr_auc                   : 0.89
  latencia_ms              : 125.0
  psi_drift                : 0.0001
