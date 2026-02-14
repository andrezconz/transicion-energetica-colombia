#!/bin/bash
set -e

echo "Iniciando flujo de trabajo..."

python -m scripts.run_simulacion
python -m scripts.run_limpieza
python -m scripts.run_modelo
python -m scripts.run_analisis

echo "Proceso completo."
