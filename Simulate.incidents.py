import logging
import pandas as pd

# Recuperar el logger de incidentes existente para asegurar la persistencia en incidents.log
incidents_logger = logging.getLogger('incidents')

# Simulación del motor de incidentes bajo el marco de Gobernanza Operativa
def simular_y_desencadenar_incidente(id_incidente, prioridad, descripcion_error, runbook_asociado, sla_objetivo):
    """
    Simula el reporte de un incidente operacional crítico, disparando la alerta
    en logs y mostrando la relación directa con el catálogo de SLAs establecido.
    """
    # Formateo del mensaje estructurado de alerta
    mensaje_alerta = f"[{id_incidente}] [{prioridad}] ALERTA ACTIVADA: {descripcion_error} | Runbook: {runbook_asociado} | SLA Objetivo: {sla_objetivo}"
    
    # Registro en log dependiendo de la severidad del incidente transaccional
    if prioridad == "P1":
        incidents_logger.error(mensaje_alerta)
    elif prioridad == "P2":
        incidents_logger.warning(mensaje_alerta)
    else:
        incidents_logger.info(mensaje_alerta)
        
    print(f"\n{'='*65}")
    print(f" 🚨 ALERTA DE INCIDENTE DETECTADA: {id_incidente}")
    print(f"{'='*65}")
    print(f"  - Prioridad:    {prioridad}")
    print(f"  - Descripción:  {descripcion_error}")
    print(f"  - Runbook:      {runbook_asociado}")
    print(f"  - SLA Límite:   {sla_objetivo}")
    print(f"  - Registro:     Escrito en 'incidents.log'")
    print(f"{'='*65}\n")

# Ejecución de la simulación para tu proyecto
if __name__ == "__main__":
    # Simular Incidente INC-001: Degradación de Recall
    simular_y_desencadenar_incidente(
        id_incidente="INC-001", 
        prioridad="P2", 
        descripcion_error="Recall de v3 degradado a 84.6% (Umbral mínimo: 90%)", 
        runbook_asociado="RB-001 (Rollback)", 
        sla_objetivo="≤ 15 min"
    )
    
    # Simular Incidente INC-002: Pico de Latencia
    simular_y_desencadenar_incidente(
        id_incidente="INC-002", 
        prioridad="P1", 
        descripcion_error="Latencia p95 incrementada a 650 ms (Umbral máximo: 150 ms)", 
        runbook_asociado="RB-002 (Scale-Up)", 
        sla_objetivo="≤ 5 min"
    )
