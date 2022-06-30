# Proyecto curso Coder House, grupo conformado por Carolina Mogni, Demián Gómez y Esteban Lavezzo


## Descarga
    Desde una consola o el bash de git usar el siguiente comando
        git clone https://github.com/Jendrito/blog_viaje-GomezMogniLavezzo.git


## Instalacion:
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver

## Resumen de proyecto
    El proyecto está enfocado a ser un blog de viajes, dónde usuarios podrán cargar sus experiencias, trámites y ponerse en contacto con el administrador de la web. 

## Inicio
    Una vez ejecutado el servidor, al acceder al LocalHost, se mostrará la pantilla de inico que brindará las siguientes opciones: Iniciar Sesión o Registrarse. Ambas aplicaciones se muestran además en el navbar de la web.

## Login/Registro
    Para loguearse, hay que registrar un usuario ( En el inicio esta la opcion de registro o arriba a la derecha en la barra de navegacion) y ahí se podrá crear o visualizar experiencias y trámites. De no estar logueado, solamente se podrán visualizar. Una ve logueado si sos superusuario tambien tenes la funcionalidad de eliminar una experiencia/tramite.

## Experiencias
    En éste apartado, aparecen las experiencias cargadas en el sistema . Además,en el dropdown de la barra de navegacion, se otorga la posibilidad al usuario de crear y ver los registros. Una vez completado el mismo, se volverá a la pantalla de los detalles de la experiencia creada. En el template de ver experiencias utalizando los botones de editar experiencia se puede ver por completo, actualizar o eliminar

## Trámites
    Similar al apartado anterior, pero enfocado a cargar trámites de viajes (ej: ciudadanía de algún país). Cuenta con el mismo dropdown que experiencia en la barra de navegacion para que el usuario agregué un registro. También, una vez completado el formulario, se mostrará el registro cargado en los dellates.
    En el template de ver tramites utalizando los botones de editar experiencia se puede ver por completo, actualizar o eliminar

## Contacto
    Permite el envío de una consulta, pregunta o comentario a un mail.

## Buscador
    Permite buscar en el blog por países, mostrando experiencias o trámites existentes.

## Nosotros
    Apartado que funciona como el about donde se encuentran 3 botones con los nombres de los creadores, presionando en alguno de los nombres la pagina se dirige a una carta personal de cada uno contando un breve resumen de su vida y por que esta aca.

## Perfil
     A este apartado se puede acceder presinando en la foto de arriba a la derecha en la barra de navegacion que es una foto q funciona como dropdown y da las opciones de ir al perfil o cerrar sesion. En perfil aparecen tus datos y la opcion de editarlos.