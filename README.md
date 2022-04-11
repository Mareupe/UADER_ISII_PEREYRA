# " UADER_ISII_PEREYRA".
## **Trabajo Práctico n°1.** 
### **"Taller Gestion de la Configuración."**

# **Paso 1:**
Cree el repositorio " UADER_ISII_PEREYRA" en la web de git hub.
Luego en la terminal de windows ejecute los siguientes comandos:
1. git init " UADER_ISII_PEREYRA"
2. git add .
3. git commit -m "Primer commit"
4. git branch -M main
5. git remote add origin main git@github.com:Mareupe/UADER_ISII_PEREYRA.git

# **Paso 2:**
Cree los siguientes directorios usando el comando mkdir
1. mkdir Python
2. mkdir Bin
3. mkdir Bash
4. mkdir Images
5. mkdir Docs

# **Paso 3:**
Agregue el archivo primos.py al directorio Python

# **Paso 4:**
Ejecuté el archivo primos.py desde la terminal posicionadome sobre el directorio Python/primos.py

# **Paso 5:**
Luego de esto hice hice el add, el commit y al realizar el push me salio el error de permiso denegado. Para esto tuve que registrar una clave SSH.
Al realizar de nuevo el push -u origin main me salto otro error que lo solucione con los siguientes comandos:
1. git pull --rebase origin main
2. git log
3. git push -u origin main
Comprobando asi q se halla actualizado el repositorio en github.com

# **Paso 6:**
Borre el archivo primos.py de la carpeta Python, lo comprobe por terminal con el comando git status, donde efectivamente el archivo habia sigo borrado.
Para poder recuperar este archivo utilice el comando git checkout primos.py.

# **Paso 7:**
Modifiqué el archivo primos.py y lo ejecuto para comprobar si funciona.
Al comprobar que el archivo funciona como espero actualizo repositorio 

# **Paso 8, 9 y 10:**
Utilice la biblioteca textblob para asi poder modificar los textos al idioma determinado, se agrego la fecha y la hora actual.
