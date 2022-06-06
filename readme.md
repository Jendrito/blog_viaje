# Proyecto curso Coder House, grupo conformado por Carolina Mogni, Demián Gómez y Esteban Lavezzo


## Descarga
    Desde una consola o el bash de git usar el siguiente comando
        git clone https://github.com/Jendrito/blog_viaje


## Instalacion:
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver

## Resumen de proyecto
    El proyecto está enfocado a ser un blog de viajes, dónde usuarios podrán cargar sus experiencias, trámites y ponerse en contacto con el administrador de la web. 

## Inicio
    Una vez ejecutado el servidor, al acceder al LocalHost, se mostrará la pantilla de inico que brindará las siguientes opciones: Iniciar Sesión o Registrarse. Ambas aplicaciones se muestran además en el navbar de la web.

## Login
    Para loguearse, hay que crear un usuario y ahí se podrá crear o visualizar experiencias y trámites. De no estar logueado, solamente se podrán visualizar.

## Experiencias
    En éste apartado, aparecen las experiencias cargadas en el sistema. Además, con "¿Querés compartir tú experiencia?", se otorga la posibilidad al usuario de crear su propio registro. Una vez completado el mismo, se volverá a la pantalla inicial de "Experiencias" con el registro cargado.

## Trámites
    Similar al apartado anterior, pero enfocado a cargar trámites de viajes (ej: ciudadanía de algún país). Cuenta con "¡Agregá tú trámite!" para que el usuario agregué un registro. También, una vez completado el formulario, se mostrará el registro cargado.

## Contacto
    Permite el envío de una consulta, pregunta o comentario a un mail.

## Buscador
    Permite buscar en el blog por países, mostrando experiencias o trámites existentes.