# Club de Datos: Desarrollo de Software MVP

¡Hola! Si lees esto, muchas gracias por haber participado del Club de Datos. Esperamos poder verte en próximas ediciones para seguir ampliando este proyecto o ir aprendiendo nuevas herramientas.

Acá te dejo las instrucciones para interactuar con el proyecto:


## Paso 1:

Abrí un nuevo codespace aprentando ```Code > Codespaces > Create a codespace on main```.

## Paso 2:

Una vez dentro del codespace, instalá los paquetes que vamos a usar con el siguiente comando:

```Terminal
pip install fastapi uvicorn
```

## Paso 3:

Levantar el servidor con el que te vas a comunicar con este comando:

```Terminal
uvicorn main:app --reload
```

> **Nota:** cambiá "main" por "main_con_sql" para levantar la versión con SQL.

## Paso 4:

En la terminal te saldrá un URL. Haz ```Ctrl + Click``` sobre el link para abrirlo.

## Paso 5:

Una vez entres a la página, agregale ```docs``` al final del URL. **¡Y listo!** Ya podés interactuar con tu proyecto.