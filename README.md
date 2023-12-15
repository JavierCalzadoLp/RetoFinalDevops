# RetoFinalDevops

Este ejercicio es un proyecto de trabajo que me desafía a aplicar todo lo que he aprendido a lo largo del curso.

Los objetivos que busco lograr con este reto son demostrar que he adquirido conocimientos sobre diversas tecnologías y principios que me permitirán diseñar, de manera fundamentada, una solución para poner en producción un producto software específico.

La descripción de la actividad implica que se me entregará una sencilla aplicación web escrita en Python, que será el núcleo de nuestro producto software. Luego de analizarla y comprenderla, se me pedirá realizar una serie de tareas relacionadas con la arquitectura de una solución y su implementación.

Permítanme compartir algunos detalles anticipados:
- **Respecto a la Arquitectura de la solución:** Lo inicial es elaborar un documento formal que describa en detalle dicha arquitectura. Este documento será mi guía durante todo el proyecto, funcionando como referencia y fuente principal para tomar decisiones. Por lo tanto, mi trabajo debe cumplir con ciertos requisitos fundamentales:
    1. **Precisión:** Seré riguroso en la definición de cada sección.
    2. **Claridad en la información:** Pondré especial atención en redactar de manera efectiva para transmitir claramente el mensaje.
    3. **Concisión en mi mensaje:** Cuando sea pertinente, usaré imágenes y diagramas para simplificar explicaciones.

En cuanto a la estructura del documento, se compone de tres secciones principales: una descripción detallada de la arquitectura del sistema, la definición de la arquitectura Cloud y la descripción del ciclo de vida.

- **Sobre la Implementación de la solución:** Entiendo que no es viable desarrollar la solución completa de principio a fin en el tiempo asignado. Por ende, se dividirá la solución en varios bloques, de los cuales seleccionaré al menos uno para concentrarme y ejecutar:
    1. Creación de un entorno local de desarrollo.
    2. Establecimiento de un pipeline de CI.
    3. Implementación de infraestructura como código.
    4. Proceso de despliegue.



# Arquitectura Software 

- **Documento Técnico: Arquitectura de la Solución Software**

**Introducción**
Este documento presenta una descripción detallada de la arquitectura propuesta para la solución software a desarrollar, destacando los servicios, métodos y tecnologías seleccionadas para garantizar una solución robusta y altamente escalable. La arquitectura propuesta se basa en tecnologías modernas y buenas prácticas de DevOps para lograr un despliegue eficiente y una gestión efectiva del ciclo de vida del software.

**Arquitectura del Sistema**
Balanceadores de Carga
Utilizaremos balanceadores de carga para distribuir el tráfico de la aplicación de manera eficiente entre múltiples instancias o contenedores. Para esta funcionalidad, consideraremos el uso de AWS Elastic Load Balancing (ELB).

**Terminadores SSL**
Para garantizar la seguridad de las comunicaciones, implementaremos terminadores SSL, utilizando servicios como AWS Certificate Manager (ACM) para la gestión de certificados SSL/TLS.

**Bases de Datos**
Se empleará el motor de base de datos relacional RDS (Relational Database Service) de AWS para alojar la base de datos principal y su standby para garantizar alta disponibilidad. Además, se utilizará SQLite localmente para desarrollo y pruebas.

**Tecnologías de Telemetría**
Se hará uso de CloudWatch para monitorear y obtener métricas operativas de los recursos de AWS, mientras que CloudTrail se empleará para registrar y auditar las actividades realizadas en la cuenta de AWS.

**Contenedores y Orquestación**
Kubernetes (EKS - Elastic Kubernetes Service) se utilizará para orquestar y gestionar los contenedores Docker que alojan la aplicación. Esto proporcionará una infraestructura escalable y fácil de administrar.

**Automatización y Despliegue**
Para la automatización de la infraestructura, se aprovechará AWS CloudFormation para definir y desplegar la infraestructura en AWS de manera predecible y repetible, siguiendo las prácticas de Infrastructure as Code (IaC).

**Red y Seguridad**
Se configurará una Virtual Private Cloud (VPC) para aislar la infraestructura y se aplicarán las prácticas recomendadas de seguridad de red en AWS para proteger la información y los recursos.

**Documentación y Testing**
Para la documentación del proyecto, se emplearán herramientas colaborativas como Markdown junto con repositorios en GitHub. Para las pruebas, se utilizará pytest, una herramienta de testing para aplicaciones Python, asegurando la calidad del código y funcionalidad.

**Arquitectura Cloud en AWS**
La solución se desplegará en AWS, aprovechando servicios como EKS, RDS, CloudWatch, CloudTrail, VPC, ACM, entre otros. Estos servicios estarán interconectados y configurados para trabajar de manera coordinada, garantizando la escalabilidad, seguridad y disponibilidad del sistema.


- **Ciclo de Vida del Software**

**Modelo de Desarrollo**
Se seguirá un modelo de desarrollo basado en ramas (branching model) dentro de GitHub para trabajar de manera colaborativa. Se empleará una estrategia Trunk-based para fusionar ramas de desarrollo a la principal de manera continua. Las pruebas, incluyendo pruebas unitarias y de integración con pytest, serán obligatorias antes de la fusión de código.

**Entornos de Despliegue**
Se mantendrán diferentes entornos, como desarrollo (local), QA y producción. Los despliegues se realizarán de manera automatizada utilizando pipelines definidos en GitHub Actions o herramientas similares, y se gestionarán con criterios claros de qué versión se despliega en cada entorno.

**Modelo de Operaciones**
Para garantizar un despliegue sin interrupciones, se implementará un modelo de despliegue en EC2 utilizando actualizaciones graduales (rolling updates) y estrategias de canary deployment para minimizar el impacto en la disponibilidad del servicio. Se considerará el uso de servicios gestionados de AWS para la gestión de trazas y logs, como AWS CloudWatch Logs o AWS Managed Services.

**Conclusiones**
Este documento técnico establece los fundamentos y las decisiones clave en la arquitectura y ciclo de vida del software para el desarrollo, despliegue y operación efectiva de la solución propuesta. Se espera que sirva como una guía esencial para el equipo de desarrollo y operaciones durante todo el ciclo de vida del proyecto.


# Guía para desarrolladores

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias, asegúrate de tener instalado Python y las dependencias necesarias. Utilizamos `pytest` como herramienta para realizar las pruebas. Sigue estos pasos:

1. Abre una terminal en la raíz del proyecto.
2. Asegúrate de tener un entorno virtual configurado y activado.
3. Instala las dependencias de desarrollo:

`pip install -r requirements-dev.txt`

4. Ejecuta el comando siguiente para correr las pruebas:

`pytest app/test_routes.py`


## Ejecución Local del Entorno

Para ejecutar localmente la aplicación y probarla, sigue estos pasos:

1. Asegúrate de tener configurado y activado un entorno virtual.
2. Instala las dependencias del proyecto:

`pip install -r requirements.txt`

3. Configura las variables de entorno..
4. Ejecuta la aplicación:

`python run.py`


## Normas de Colaboración

Para mantener un flujo de trabajo ordenado y colaborativo, seguimos estas normas de colaboración:

- **Modelo de Ramas:**
Utilizamos el modelo de ramas `GitFlow` para el desarrollo colaborativo:
- `main`: rama principal que refleja la versión en producción.
- `develop`: rama de desarrollo donde se integran las características.
- `feature/<nombre>`: ramas para nuevas características.
- `hotfix/<nombre>`: ramas para correcciones urgentes.

- **Pull Requests:**
Antes de fusionar una rama de `feature` en `develop`, abre un Pull Request y solicita una revisión de código.

- **Convención de Mensajes de Commit:**
Seguimos la convención de mensajes de commit [Conventional Commits](https://www.conventionalcommits.org/) para mantener un historial de cambios claro y comprensible.

¡Gracias por contribuir al proyecto! Si tienes dudas o sugerencias, no dudes en comunicarte con el equipo.

