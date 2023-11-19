# ArquiFinalSW
Final project Software Architecture and Design

## Prácticas SOLID seguidas

SRP-Responsabilidad única: sí cumple porque la clase de Item
sólo tienes métodos quue sí corresponden a la clase (CRUD) con
la db. 

OCP-Principio Open/Closed: sí cumple porque se usa una clase
abstracta (itemAbstract) en la que se pueden agregar fucionalidades sin cambiar el código existente. 

DIP-Principio de Dependencias: sí cumple porque una clase de alto nivel, tal como ItemRepo depende de una clase abstracta como lo es itemAbstact.

## Design Pattern Usados
Builder

Singleton 

Facade

Adapter
