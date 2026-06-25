# Network Scanner Python 

 

Herramienta de escaneo de puertos TCP desarrollada en Python con fines educativos para explorar conceptos de redes, programación con sockets y fundamentos de ciberseguridad. 

 

El proyecto implementa escaneo concurrente, identificación básica de servicios, banner grabbing y generación automática de reportes. 

 

--- 

 

## Objetivo 

 

Desarrollar una herramienta de reconocimiento de red que permita comprender y aplicar conceptos como: 

 

- Conexiones TCP/IP 

- Puertos y servicios de red 

- Programación con sockets 

- Concurrencia en Python 

- Generación de reportes de seguridad 

 

--- 

 

## Características 

 

- Escaneo de puertos TCP 

- Escaneo multihilo utilizando ThreadPoolExecutor 

- Identificación básica de servicios 

- Banner grabbing 

- Modo normal y modo completo (--full) 

- Reportes en formato TXT 

- Exportación de resultados en JSON 

- Medición del tiempo de escaneo 

- Interfaz mediante línea de comandos (CLI) 

 

--- 

 

## Tecnologías utilizadas 

 

- Python 3 

- Socket Programming 

- ThreadPoolExecutor 

- JSON 

- Git 

- GitHub 

 

--- 

 

## Instalación 

 

Clonar el repositorio: 

 

git clone https://github.com/LeanGnzlz/network-scanner-python.git 

 

Ingresar al directorio: 

 

cd network-scanner-python 

 

--- 

 

## Uso 

 

Escaneo básico: 

 

python scanner.py 127.0.0.1 

 

Escaneo completo: 

 

python scanner.py 127.0.0.1 --full 

 

El modo completo habilita funcionalidades adicionales como identificación de servicios y análisis extendido. 

 

--- 

 

## Ejemplo de salida 

 

================================ 

      Network Scanner 

================================ 

 

Target: 127.0.0.1 

 

[+] 135/tcp OPEN  MSRPC 

    Banner: Not applicable 

 

[+] 445/tcp OPEN  SMB 

    Banner: Not applicable 

 

================================ 

Scan completed 

Open ports found: 2 

Scan duration: 21.16 seconds 

================================ 

 

--- 

 

## Reportes generados 

 

Luego de cada escaneo se generan automáticamente dos tipos de reportes: 

 

- Archivo TXT con resumen del análisis 

- Archivo JSON con información estructurada para futuros procesamientos 

 

Ejemplo: 

 

reports/ 

├── scan_20260625_135638.txt 

└── scan_20260625_135638.json 

 

--- 

 

## Estructura del proyecto 

 

network-scanner-python/ 

 

├── scanner.py 

├── README.md 

├── .gitignore 

 

└── reports/ 

 

--- 

 

## Estado del proyecto 

 

Actualmente implementado: 

 

- TCP port scanning 

- Multithreaded scanning 

- Service identification 

- Banner grabbing 

- TXT reporting 

- JSON export 

- Command line interface 

 

--- 

 

## Próximas mejoras 

 

- Detección avanzada de versiones de servicios 

- Escaneo de rangos completos de red 

- Mejoras visuales en consola 

- Dashboard de monitoreo 

- Integración con herramientas de análisis de seguridad 

 

--- 

 

## Disclaimer 

 

Este proyecto fue desarrollado con fines educativos. 

 

Debe utilizarse únicamente en redes propias o con autorización explícita del propietario de la infraestructura.
