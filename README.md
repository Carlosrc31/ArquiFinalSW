# ArquiFinalSW
Final project Software Architecture and Design


--->ArquiFinalSW<----
Final project Software Architecture and Design

--->Prácticas SOLID seguidas<---

## Pasos para ejecutar

Developing an virtual environment with Flask Python
Creating a virtual environment
	python -m venv virtual_env
Activating the virtual environment, it's needed everytime we're going to use the app
	.\virtual_env\Scripts\activate
Installing flask using pip
	pip install flask
Command to install all the libraries needed
	pip install -r requirements.txt
Into the right carpet, to up the server
	py app.py

## Prácticas SOLID seguidas


--->Responsabilidad Única (SRP):

En el contexto del principio de Responsabilidad Única (SRP), 
se destaca que la clase `Item` cumple con este principio al tener responsabilidades específicas 
relacionadas con la manipulación de datos de la base de datos. 
Esto significa que la clase `Item` tiene un único motivo para cambiar, 
que es la gestión de operaciones CRUD (Create, Read, Update, Delete) con la base de datos. 
Esta especialización ayuda a mantener el código modular y fácil de entender,
ya que cada clase o módulo se centra en una tarea específica.

--->Principio Open/Closed (OCP):

El principio Open/Closed (OCP) se observa en el uso de la clase abstracta `ItemAbstract`. 
Al diseñar una clase abstracta, se permite la extensión sin necesidad de modificar el código existente. 
Esto significa que, si en el futuro se desea agregar nuevas funcionalidades o comportamientos relacionados con los ítems, 
se pueden introducir nuevas clases que hereden de `ItemAbstract` sin cambiar el código de las clases existentes. De esta manera, 
se cumple con el principio de extensión sin modificación.

--->Principio de Dependencias (DIP):

El principio de Dependencias Inversas (DIP) se cumple al depender de una clase abstracta en lugar de una implementación concreta. 
La clase de alto nivel (`ItemRepo`), que probablemente esté involucrada en operaciones más complejas relacionadas con ítems,
depende de la clase abstracta `ItemAbstract`. Esto permite una mayor flexibilidad y mantenimiento, 
ya que la clase de alto nivel no está acoplada directamente a las implementaciones concretas de la clase `Item`. 
Si se introducen nuevas implementaciones de `ItemAbstract`, la clase `ItemRepo` no se verá afectada siempre que cumplan con la interfaz abstracta.

--->Design Patterns Utilizados: <---

## Design Pattern Usados

--->Builder:

El patrón Builder se centra en la construcción paso a paso de objetos complejos. 
Aunque no se proporcionan detalles específicos sobre cómo se aplica el patrón Builder en el código, 
es probable que se utilice para construir instancias complejas de objetos, como elementos de la base de datos. 
Este enfoque modular facilita la creación de objetos con configuraciones específicas.

--->Singleton:

El patrón Singleton garantiza que una clase tenga solo una instancia y 
proporciona un punto de acceso global a esa instancia. Sin detalles específicos, se asume que se utiliza un patrón Singleton, 
posiblemente en la gestión de la base de datos o en algún componente crucial para la aplicación, 
garantizando que haya una única instancia de esa funcionalidad en toda la aplicación.

--->Facade:

El patrón Facade proporciona una interfaz simplificada para un conjunto de interfaces más complejo. 
En el contexto de la arquitectura final del software, el uso de un patrón Facade podría estar relacionado con 
simplificar la interacción con múltiples componentes del sistema, proporcionando una interfaz única y fácil de usar para el resto de la aplicación.

--->Adapter:

El patrón Adapter se usa para permitir que interfaces incompatibles trabajen juntas. 
No se proporcionan detalles específicos, pero si se utiliza el patrón Adapter, 
podría ser para integrar o adaptar componentes de la aplicación que tienen interfaces diferentes para que
funcionen de manera conjunta de manera armoniosa.

--->¿Cuáles son el top 5 de caracteristicas de arquitectura del diseño actual de tu proyecto? <---

Operational Architecture Characteristics:

--->Reliability/Safety:
Uso en el Código: La fiabilidad y la seguridad del sistema son críticas. 
Las funciones como addItem incorporan lógica para asegurar la inserción segura de datos en la base de datos, 
lo que sugiere un enfoque en la fiabilidad y la seguridad del sistema.

--->Robustness:
Uso en el Código: La capacidad de manejar errores en caso de falla se aborda en varias partes del código, 
como en las funciones deleteItem y addItem, donde se manejan excepciones para garantizar la robustez del sistema.
Structural Architecture Characteristics:

--->Extensibility:
Uso en el Código: La capacidad de agregar nuevas funcionalidades se aborda mediante el uso del patrón Builder en Item_model.py. 
Este diseño permite la fácil incorporación de nuevos atributos o comportamientos a la clase Item.

--->Maintainability:
Uso en el Código: La facilidad para aplicar cambios y mejorar el sistema es una consideración clave. 
La estructura del código, especialmente el uso de patrones como Builder y Singleton, sugiere un enfoque en la mantenibilidad del sistema.

--->Usability:
Uso en el Código: Aunque no se evidencia directamente en el código proporcionado, 
la usabilidad del sistema se puede inferir de la implementación de las rutas y funciones que permiten a los usuarios agregar,
eliminar y obtener elementos de manera intuitiva.


--->¿Si la aplicacion migrara a una arquitectura de microservicios, ¿Cuales serian el top 5 de caracteristicas de arquitectura? <---

--->Interoperability (Interoperabilidad):
Definición: Se refiere a la capacidad del sistema para interactuar y operar con otros sistemas, 
sin importar las diferencias en tecnologías, plataformas o lenguajes de programación.
Importancia en Microservicios: En una arquitectura de microservicios,
donde cada servicio puede estar desarrollado y desplegado de forma independiente, 
la interoperabilidad es clave para garantizar la comunicación efectiva entre los servicios y otros sistemas.

--->Scalability (Escalabilidad):
Definición: La escalabilidad se refiere a la capacidad del sistema para manejar un aumento en la carga o la demanda sin perder rendimiento.
Importancia en Microservicios: Cada microservicio puede escalar de manera independiente según sus necesidades, 
lo que permite una gestión eficiente de recursos y un rendimiento consistente.


--->Adaptability (Adaptabilidad):
Definición: La adaptabilidad se refiere a la capacidad del sistema para ajustarse y evolucionar frente a cambios en los requisitos o el entorno.
Importancia en Microservicios: Dado que los microservicios pueden evolucionar y desplegarse de forma independiente, 
la adaptabilidad es esencial para responder a cambios rápidos en el negocio o en los requisitos del usuario.

--->Extensibility (Extensibilidad):
Definición: La extensibilidad se refiere a la facilidad con la que se pueden agregar nuevas funcionalidades o componentes al sistema.
Importancia en Microservicios: La arquitectura de microservicios fomenta la creación y despliegue independiente de servicios,
lo que facilita la extensión del sistema al agregar nuevos servicios según sea necesario.

