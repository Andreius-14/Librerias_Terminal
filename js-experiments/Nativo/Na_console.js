/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          LIMPIA TERMINAL              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

console.log("HolaMundo");

console.clear();

console.log("Nuevo");

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           IMPRIME TABLA               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

const arrayDatos = [
  { id: 1, nombre: "Alice", edad: 25 },
  { id: 2, nombre: "Bob", edad: 30 },
  { id: 3, nombre: "Charlie", edad: 28 },
];

console.table(arrayDatos);
console.table(arrayDatos, ["nombre", "edad"]);

const usuario = {
  nombre: "Alice",
  edad: 25,
  ciudad: "Madrid",
};

console.table(usuario);

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               MENSAJE                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
console.error("Hola Error");
console.info("Hola Info");

console.log("Hola Mundo");
console.warn("Hola Peligro");
