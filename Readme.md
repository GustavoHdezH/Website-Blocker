# Bloqueador de sitios Web

Esta herramienta permite, la admnistración de accecso a ciertos sitios web, dentro de los horarios de oficina o escolares. De manera automatizada sin la mecesidad, de buscar el archivo "host" en los archivos del sistema.

## Bibliotecas requeridas para su funcionamiento

```python
    import time
    from datetime import datetime
```

> Se puede asignar un alias a datetime para acortar lineas
  de codigo y dar una mejor legibilidad al script.

## Funcionamiento del script

> Asignación de variables para ejercución  

```python
    hosts_path_system = r"C:\Windows\System32\drivers\etc\hosts"
    host_dir = hosts_path_system
    redir = "127.0.0.1"
```

> Asignación de variables para pruebas

```python
    host_dir = "hosts"
    redir = "127.0.0.1"
```

> Establecimiento de sitios a bloquear  

```python
    websites_list =[
        "www.facebok.com",
        "www.youtube.com",
        "www.google.com.mx"
    ]
```

En esta lista se pueden agregas los sitios a los cuales, se les negara el acceso mientras este en ejecucuión el programa.

> Asignación de horarios

```python
    from_hour = 7
    to_hour = 15
```

Esta asignación de horarios esta expresada en formato de 24hrs.
> Importante

Para poder hacer uso de esta herramienta es nececario tener persmisos de administrador de lo contrario, marcara error a la hora de la ejecución.
> Creación de Cron en Linux

`
    crontab -a
`

Listar los cronfiles activos

`
    contrab -l
`
## Créditos
  >[Gustavo Hernandez](https://github.com/GustavoHdezH) autor original del contenido.
  Happy coding.
