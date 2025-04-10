# Patrones de Comportamiento: Decorator y Proxy

## Patrón Decorator

### Intención
El patrón Decorator permite añadir responsabilidades a un objeto de forma dinámica, sin afectar a otros objetos de la misma clase. Es una alternativa flexible a la herencia para extender funcionalidad.

### Estructura
- Component: Define la interfaz para objetos que pueden tener responsabilidades añadidas
- ConcreteComponent: Define un objeto al que se le pueden añadir responsabilidades
- Decorator: Mantiene una referencia a un objeto Component y define una interfaz que se ajusta a la interfaz de Component
- ConcreteDecorator: Añade responsabilidades al componente

## Patrón Proxy

### Intención
El patrón Proxy proporciona un sustituto o marcador de posición para otro objeto para controlar el acceso a él. El proxy actúa como un intermediario entre el cliente y el objeto real.

### Estructura
- Subject: Define la interfaz común para RealSubject y Proxy
- RealSubject: Define el objeto real que el proxy representa
- Proxy: Mantiene una referencia que permite al proxy acceder al objeto real
- Client: Interactúa con el Subject

## Diferencias Principales

La principal diferencia entre el patrón Decorator y el patrón Proxy es su propósito:

- **Decorator**: Se enfoca en añadir o modificar funcionalidad de un objeto de forma dinámica. Cada decorador añade nuevas responsabilidades al objeto base.
- **Proxy**: Se enfoca en controlar el acceso a un objeto, actuando como un intermediario. El proxy no añade funcionalidad, sino que controla cómo y cuándo se accede al objeto real.

## Escenarios de Uso

### Decorator
- Cuando necesitas añadir responsabilidades a objetos individuales de forma dinámica y transparente
- Cuando quieres evitar la explosión de subclases
- Cuando necesitas modificar el comportamiento de un objeto sin afectar a otros objetos de la misma clase
- Ejemplos: Sistemas de pedidos de comida, sistemas de notificaciones con diferentes canales

### Proxy
- Cuando necesitas controlar el acceso a un objeto
- Cuando quieres implementar carga perezosa (lazy loading)
- Cuando necesitas añadir una capa de seguridad o control de acceso
- Ejemplos: Carga de imágenes pesadas, acceso a recursos remotos, control de caché 