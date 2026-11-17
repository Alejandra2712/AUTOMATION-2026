# Proyecto de QA Automation – SauceDemo

## Descripción del proyecto

Este proyecto fue desarrollado como trabajo final del curso **QA Automation – Talento Tech 2026**.

El objetivo principal es automatizar pruebas funcionales sobre la aplicación web [SauceDemo](https://www.saucedemo.com/), utilizando Python y Selenium WebDriver, aplicando buenas prácticas de testing, reutilización de código, organización de pruebas e Integración Continua.

El proyecto integra automatización de pruebas de interfaz de usuario (UI Testing), pruebas de API, Behavior Driven Development (BDD) y generación automatizada de reportes.

## Tecnologías y herramientas

- **Python 3.14.7:** lenguaje de programación.
- **Selenium WebDriver:** automatización de navegadores web.
- **Pytest:** framework para la ejecución y organización de pruebas.
- **Behave:** framework para implementar BDD.
- **Gherkin:** lenguaje utilizado para describir escenarios de prueba.
- **Page Object Model (POM):** patrón de diseño para organizar las interacciones con las páginas.
- **Requests:** realización de solicitudes HTTP y pruebas de API.
- **Git y GitHub:** control de versiones y gestión del repositorio.
- **GitHub Actions:** automatización de procesos de Integración Continua (CI).
- **Pytest-HTML:** generación de reportes HTML de ejecución.

## Estructura del proyecto

El proyecto utiliza una arquitectura modular para mejorar la legibilidad, el mantenimiento y la reutilización del código.

```text
AUTOMATION-2026/
│
├── .github/
│   └── workflows/          # Workflows de GitHub Actions
│
├── data/                   # Datos de prueba
│
├── features/               # Archivos de funcionalidades BDD (Gherkin)
│   ├── steps/              # Definiciones de pasos (Step Definitions)
│   └── environment.py      # Hooks de Behave
│
├── logs/                   # Registros de ejecución
│
├── pages/                  # Clases del patrón Page Object Model
│
├── reports/                # Reportes HTML y evidencias
│
├── tests/                  # Pruebas automatizadas con Pytest
│
├── utils/                  # Funciones auxiliares
│
├── conftest.py             # Fixtures y hooks de Pytest
├── pytest.ini              # Configuración de Pytest
├── requirements.txt        # Dependencias del proyecto
└── README.md
```

## Alcance de las pruebas

Las pruebas automatizadas contemplan las siguientes funcionalidades:

- Inicio de sesión exitoso y fallido.
- Validación de credenciales incorrectas.
- Verificación de mensajes de error.
- Visualización y validación del inventario de productos.
- Selección y agregado de productos al carrito.
- Verificación del contenido y los precios del carrito.

## Arquitectura de automatización de pruebas

### Page Object Model (POM)

El proyecto implementa el patrón de diseño Page Object Model para separar las interacciones con las páginas de la lógica de los casos de prueba.

Cada página está representada por una clase de Python que encapsula sus localizadores y métodos de interacción.

Esta metodología permite:

- Reutilizar código.
- Facilitar el mantenimiento.
- Mejorar la organización de las pruebas.
- Separar responsabilidades.
- Reducir la duplicación de código.

### Pytest

Pytest se utiliza como framework principal para la ejecución y organización de las pruebas automatizadas.

El proyecto incorpora:

- **Fixtures:** inicialización y cierre del WebDriver.
- **Parametrización:** ejecución de pruebas con diferentes datos de entrada.
- **Hooks:** captura de screenshots cuando se producen fallos.
- **Logging:** registro de eventos, ejecuciones y errores.
- **Reportes HTML:** generación de informes mediante pytest-html.
- **Reejecución de pruebas fallidas:** cuando está configurada.

### Behavior Driven Development (BDD) – Behave

Se utiliza Behave para implementar pruebas basadas en comportamiento (BDD).

Los escenarios se describen mediante Gherkin, utilizando palabras clave como:

- Feature
- Background
- Scenario
- Scenario Outline
- Given
- When
- Then
- And
- Examples

Las definiciones de pasos (Step Definitions) conectan los escenarios escritos en lenguaje natural con el código Python y las interacciones automatizadas mediante Selenium WebDriver.

El archivo `environment.py` contiene los hooks utilizados para gestionar el entorno de ejecución, incluyendo la configuración y el cierre del navegador.

### Pruebas de API

El proyecto también incorpora pruebas de API utilizando la biblioteca Python Requests para realizar solicitudes HTTP y validar las respuestas de los servicios.

## Integración Continua (CI) – GitHub Actions

El proyecto implementa un proceso de Integración Continua (Continuous Integration – CI) mediante GitHub Actions.

El workflow se ejecuta automáticamente cada vez que se realiza un evento `push` sobre la rama `main`.

### Etapas del pipeline de CI

El workflow realiza las siguientes tareas:

1. **Checkout:** descarga el código fuente del repositorio.
2. **Configuración de Python:** prepara el entorno de ejecución con Python 3.14.7 sobre Ubuntu.
3. **Instalación de dependencias:** actualiza pip e instala las dependencias declaradas en `requirements.txt`.
4. **Ejecución de pruebas:** ejecuta la suite de pruebas automatizadas mediante Pytest.
5. **Almacenamiento de artefactos:** guarda el reporte HTML generado por Pytest como un artefacto descargable desde GitHub Actions.

### Beneficios de la Integración Continua

- Ejecución automatizada de pruebas ante nuevos cambios.
- Detección temprana de errores.
- Validación continua del código.
- Trazabilidad de las ejecuciones.
- Disponibilidad de reportes HTML para analizar los resultados.

**Nota:** La implementación actual contempla Integración Continua (CI). No incluye todavía una etapa de Entrega Continua (Continuous Delivery) o Despliegue Continuo (Continuous Deployment), ya que no cuenta con publicación ni despliegue automatizado de la aplicación.

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Alejandra2712/AUTOMATION-2026.git
```

### 2. Ingresar al directorio del proyecto

```bash
cd AUTOMATION-2026
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

### Ejecutar pruebas con Pytest

```bash
python -m pytest
```

### Ejecutar escenarios BDD con Behave

```bash
python -m behave
```

## Reportes y evidencias de prueba

El proyecto incorpora mecanismos para recopilar y analizar evidencias de las ejecuciones:

- Reportes HTML generados mediante Pytest-HTML.
- Capturas de pantalla cuando se producen fallos.
- Registros de ejecución mediante Logging.
- Artefactos de GitHub Actions para descargar los reportes de prueba.

## Conocimientos aplicados

Este proyecto permitió integrar y aplicar conocimientos sobre:

- Testing funcional y automatización de pruebas.
- Programación con Python y programación orientada a objetos.
- Selenium WebDriver e interacción con navegadores.
- Pytest, fixtures, parametrización y hooks.
- Patrón de diseño Page Object Model (POM).
- BDD, Gherkin y Behave.
- Pruebas de API con Requests.
- Logging y captura de screenshots.
- Generación de reportes HTML.
- Control de versiones con Git y GitHub.
- Integración Continua mediante GitHub Actions.

---

**Proyecto Final – QA Automation | Talento Tech 2026**