#  modelo de tienda en Línea - Documentación del Proyecto

## Descripción del Proyecto

Este proyecto es una aplicación de tienda en línea desarrollada como parte de un proyecto para una materia de arquitectura de software. La aplicación está diseñada para permitir a los usuarios registrados comprar productos de diferentes categorías, administrar sus perfiles y realizar pagos de manera segura.

## Funcionalidades Principales

1. **Autenticación de Usuarios:**
   - Los usuarios pueden iniciar sesión con sus credenciales existentes o registrarse como nuevos usuarios.
   - Las credenciales de inicio de sesión se validan para garantizar la seguridad de la aplicación.

2. **Gestión de Perfiles de Usuario:**
   - Los usuarios pueden ver y actualizar su información de perfil.
   - La información incluye detalles como nombre, dirección y beneficios financieros.
   - Los beneficios financieros pueden incluir tarjetas de crédito, seguros y programas de fidelización.

3. **Exploración y Compra de Productos:**
   - Los usuarios pueden explorar una variedad de productos agrupados en diferentes categorías, como ropa, electrodomésticos y artículos para el hogar.
   - Cada producto muestra su nombre, precio y botón para agregarlo al carrito de compras.

4. **Carrito de Compras:**
   - Los usuarios pueden ver una lista de productos seleccionados para comprar.
   - Pueden agregar o eliminar productos del carrito según sus preferencias.
   - El total a pagar se calcula automáticamente, teniendo en cuenta cualquier descuento aplicable.

5. **Pago Seguro:**
   - Los usuarios pueden realizar el pago de sus compras de manera segura.
   - Se aplican descuentos financieros según los beneficios seleccionados en el perfil del usuario.


## Principios SOLID

Este proyecto sigue los principios SOLID de diseño de software para garantizar una arquitectura robusta y mantenible:

    - Principio de Responsabilidad Única (SRP):
        Cada clase y función en el código tiene una única responsabilidad claramente definida. Por ejemplo, la clase AuthWindow maneja la autenticación de usuarios, mientras que la clase StoreWindow se encarga de mostrar los productos y gestionar el carrito de compras.

    - Principio de Abierto/Cerrado (OCP):
        El código está diseñado para ser abierto para la extensión pero cerrado para la modificación. Por ejemplo, se pueden agregar nuevas funcionalidades como opciones de búsqueda de productos sin modificar las clases existentes.

    - Principio de Sustitución de Liskov (LSP):
        Las clases derivadas son utilizables a través de sus clases base. Por ejemplo, la clase AuthWindow es una subclase de tk.Frame y se puede utilizar en cualquier lugar donde se necesite un widget de ventana en Tkinter.

    - Principio de Segregación de la Interfaz (ISP):
        Las interfaces están específicamente diseñadas para los clientes que las utilizan. Por ejemplo, la interfaz de usuario proporciona una experiencia intuitiva y amigable para el usuario final, mientras que las clases internas manejan la lógica de negocio de manera independiente.

    - Principio de Inversión de Dependencia (DIP):
        Las clases dependen de abstracciones en lugar de implementaciones concretas. Por ejemplo, la clase Carrito depende de la interfaz ProductoCarrito en lugar de una implementación específica de producto, lo que facilita la introducción de nuevos tipos de productos en el futuro.


## Estructura del Proyecto

El proyecto está organizado en varios módulos y archivos para facilitar la legibilidad y la mantenibilidad del código:

- `autenticacion.py`: Contiene funciones y clases relacionadas con la autenticación y el registro de usuarios.
- `productos.py`: Define la estructura de los productos disponibles y las promociones aplicables.
- `perfiles.py`: Gestiona la información de perfil de usuario y los beneficios financieros asociados.
- `carrito.py`: Implementa la funcionalidad del carrito de compras y los productos en el carrito.
- `ui.py`: Contiene las clases y funciones relacionadas con la interfaz de usuario utilizando Tkinter.
- `main.py`: Punto de entrada principal de la aplicación que inicia la interfaz de usuario y las ventanas correspondientes.

## Mejoras Futuras

Algunas mejoras potenciales para este proyecto podrían incluir:

- Implementación de una base de datos para almacenar información de manera persistente.
- Mejoras en la seguridad, como el hash de contraseñas.
- Agregar más funcionalidades, como opciones de búsqueda avanzada y gestión de inventario.
