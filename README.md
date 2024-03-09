#  modelo de tienda en Línea - Documentación del Proyecto

## Descripción del Proyecto

Este proyecto es una aplicación de tienda en línea desarrollada como parte de un proyecto para una materia de arquitectura de software. La aplicación está diseñada para permitir a los usuarios registrados comprar productos de diferentes categorías, administrar sus perfiles y realizar pagos de manera segura.

## Funcionalidades Principales

1. **Autenticación de Usuarios:**
   - Inicio de sesión y registro de usuarios.
   - Validación de credenciales de inicio de sesión.

2. **Gestión de Perfiles de Usuario:**
   - Visualización y actualización de información de perfil.
   - Gestión de beneficios financieros como tarjetas de crédito, seguros y programas de fidelización.

3. **Exploración y Compra de Productos:**
   - Exploración de productos por categoría.
   - Agregar productos al carrito de compras.

4. **Carrito de Compras:**
   - Visualización de productos en el carrito.
   - Cálculo automático del total a pagar.

5. **Pago Seguro:**
   - Realización de pagos seguros.
   - Aplicación de descuentos financieros según los beneficios del usuario.

## Principios SOLID

Este proyecto sigue los principios SOLID de diseño de software para garantizar una arquitectura robusta y mantenible:

1. **SRP - Principio de Responsabilidad Única:** Cada clase y función tiene una única responsabilidad.
2. **OCP - Principio de Abierto/Cerrado:** El código es abierto para la extensión pero cerrado para la modificación.
3. **LSP - Principio de Sustitución de Liskov:** Las clases derivadas son utilizables a través de sus clases base.
4. **ISP - Principio de Segregación de la Interfaz:** Las interfaces están diseñadas específicamente para los clientes que las utilizan.
5. **DIP - Principio de Inversión de Dependencia:** Las clases dependen de abstracciones en lugar de implementaciones concretas.

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
