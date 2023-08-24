# TerceraPre-EntregaGiovinazzo: Full Sailing - pagina web para emprendimiento de escuela de vela

Este proyecto crea una web en Python para almacenar datos de una escuela de vela (Full Sailing), donde se podrá registrar el alumno, el profesor y elegir el dia del examen final. El objetivo principal es optimizar la información de los usuarios y de esta manera acceder a ella de una forma automatizada. Por otro lado, se pretende organizar las fechas de examen de los alumnos y mantener un control sobre la disponibilidad. 


## Instalación

Antes de comenzar, verificar tener Python instalado

1. Clonar el repositorio de git
```bash
  git clone
```
2. Dirigirse al directorio del proyecto
```bash
  cd ProyectoFinalGiovinazzo/ProyectoFullSailing
```
3. En caso de desearlo, activar el entorno virtual
 ```bash
  python -m venv
```   
4. Instalar las dependencias del proyecto
```bash
  pip install -r requirements.txt
```
5. Una vez instaladas, se puede corroborar que todo funcione ejecutando el programa
```bash
  python manage.py runserver
```
Listo!
## Instrucciones de uso

El objetivo de la web es organizar la disponibilidad de los dias de examen. Para ello será necesario registrarse en primera instancia o luego, ingresar con el usuario cada vez que se desee interactuar con la web. Una vez ingresado, el usuario podrá registrarse en la seccion "Alumnos", elegir la fecha de examen en "Reservar examen" y chequear la disponibilidad del dia en "Examenes". Los profesores tambien podran tener acceso a ello sin necesidad de un superuser y podran registrarse como profesores en la seccion "Profesores".

Por otro lado, el administrador (usuario: sofanel - contraseña: fullsailing) podrá ingresar de la misma forma y tendrá acceso a un control más: el botón de "administrador". Allí se despliega la opción "Lista Examenes" en donde se podrá tener el control de todas las fechas de examen registradas hasta el momento. En un futuro la idea es agregar las opciones de poder visualizar la lista de los alumnos del centro y de los profesores. 


## Authors

- [Sofía Giovinazzo](https://github.com/SofiaGiovinazzo/ProyectoFinalGiovinazzo)

