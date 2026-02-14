PROYECTO: Transición Energética en Colombia
==========================================

Este proyecto analiza la descarbonización de la matriz eléctrica colombiana mediante modelos de despacho y análisis de emisiones. El flujo de trabajo ha sido profesionalizado para garantizar la transparencia y evitar errores manuales típicos de herramientas no auditables.

ESTRUCTURA DE DIRECTORIOS
-------------------------
.
├── codigo/                # Scripts de procesamiento y modelado
│   ├── 01_limpieza_red.py
│   ├── 02_modelo_renovables.py
│   ├── 03_analisis_emisiones.py
│   ├── 04_reporte_politica.py
│   └── simulate_data.py    # Generador de datos sintéticos inicial
├── datos/                 # Insumos de generación eléctrica y datos crudos
├── documentos/            # Documentación técnica del proyecto
│   └── README.txt
├── resultados/            # Salidas automáticas (Figuras y tablas CSV)
├── environment.yml        # Configuración del entorno Conda (Nivel 4)
└── runall.sh              # Script maestro de automatización (bash)

REQUISITOS DEL SISTEMA
----------------------
* Gestor de entornos: Miniconda o Anaconda.
* Arquitectura probada: Apple Silicon (M4) con macOS.
* Shell recomendado: zsh.

INSTRUCCIONES DE EJECUCIÓN
--------------------------
Para replicar los resultados de esta investigación, siga estos pasos en su terminal:

1. Clonar o descargar el repositorio y situarse en la carpeta raíz.
2. Crear el entorno virtual desde el archivo de configuración:
   $ conda env create -f environment.yml
3. Activar el entorno:
   $ conda activate transicion_colombia
4. Otorgar permisos de ejecución al script maestro:
   $ chmod +x runall.sh
5. Ejecutar la automatización completa:
   $ ./runall.sh

Al finalizar, los gráficos y tablas analíticas estarán disponibles en la carpeta /resultados.