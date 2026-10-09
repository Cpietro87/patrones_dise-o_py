Patrones de diseño se divide en tres grandes grupos de patrones: creacional, estructural y comportamental. Cada grupo tiene su propio propósito y utiliza diferentes técnicas para resolver problemas comunes en la programación orientada a objetos.

1. **Creacionales**: Estos patrones se centran en la creación de objetos. Algunos ejemplos incluyen Singleton, Factory Method, Abstract Factory y Builder.
  Se ocupan de cómo se crean los objetos.

  - **Singleton**: Asegura que una clase solo tenga una instancia y proporciona un punto global de acceso a ella.
  - **Factory Method**: Define una interfaz para crear objetos, pero deja que las subclases decidan qué tipo de objeto crear.
  - **Abstract Factory**: Permite crear familias de objetos relacionados sin especificar sus clases concretas.
  - **Builder**: Divide la construcción de un objeto complejo en pasos individuales.


2. **Estructurales**: Estos patrones se enfocan en cómo las clases y objetos pueden ser organizados para formar estructuras más complejas. Ejemplos incluyen Adapter, Bridge, Composite, Decorator, Facade, Flyweight y Proxy.

  - **Adapter**: Permite que dos clases incompatibles trabajen juntas convirtiéndose en una interfaz común.
  - **Bridge**: Separa una clase en dos partes, una de las cuales depende de la otra. Esto permite que ambas partes puedan variar independientemente.
  - **Composite**: Permite tratar a los objetos individuales y colecciones de objetos de manera uniforme.
  - **Decorator**: Añade responsabilidades adicionales a un objeto dinámicamente, sin modificar su estructura.
  - **Facade**: Proporciona una interfaz simplificada para un conjunto complejo de subsistemas.
  - **Flyweight**: Reduce el uso de memoria al compartir datos comunes entre múltiples objetos.
  - **Proxy**: Permite acceder a un objeto en lugar de otro, proporcionando un nivel adicional de control o protección.

3. **Comportamiento**: Estos patrones se centran en la comunicación entre los objetos. Algunos ejemplos incluyen Observer, Strategy, Command, State, Iterator y Mediator.

  - **Observer**: Permite que un objeto (el observador) se actualice automáticamente cuando otro objeto (el sujeto) cambia.
  - **Strategy**: Define una familia de algoritmos, encapsula cada uno de ellos y hace que sean intercambiables.
  - **Command**: Convierte solicitudes en objetos que contienen toda la información sobre la solicitud, incluyendo el método para ejecutarla.
  - **State**: Permite a un objeto cambiar su comportamiento cuando cambia su estado interno.
  - **Iterator**: Proporciona una forma de acceder a los elementos de una colección sin exponer su representación subyacente.
  - **Mediator**: Reduce la dependencia entre objetos, permitiendo que interactúen a través de un objeto centralizado.

Estos patrones son herramientas poderosas para resolver problemas complejos en el diseño y desarrollo de software. Al aprender y aplicar estos patrones, puedes mejorar significativamente la calidad y la eficiencia de tu código.

Cada uno de estos patrones tiene sus propias ventajas y desventajas, y su uso depende del problema específico que estés tratando de resolver en tu aplicación. Es importante entender cómo funcionan y cuándo aplicarlos para mejorar la estructura y el mantenimiento del código.

