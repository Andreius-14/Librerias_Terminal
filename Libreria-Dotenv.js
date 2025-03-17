import "dotenv/config";

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              BASICO                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
console.log(process.env.DB_USER);

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            OPTIMIZADO                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

const log = console.log;
const env = process.env;
log(env.DB_USER);
log(env.S3_BUCKET);
log(env.SECRET_KEY);
log(env.DB_HOST);
log(env.DB_USER);
log(env.DB_PASSWORD);

/*
S3_BUCKET="YOURS3BUCKET"
SECRET_KEY="YOURSECRETKEYGOESHERE"
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=password

*/

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               NOTAS                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Descargar Paquete

crea archivo en Root .env

Llamar

--------conrtenido de archivo-----------
S3_BUCKET="YOURS3BUCKET"
SECRET_KEY="YOURSECRETKEYGOESHERE"
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=password
*/
