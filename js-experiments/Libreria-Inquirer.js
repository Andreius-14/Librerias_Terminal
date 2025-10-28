//import chalk from "chalk";
import inquirer from "inquirer";
import chalk from "chalk";

//   El inquirer Prompt - Se encapsula en un Json
//   Estos Ejemplos son muy amplios
//   Una manera mas Minusiosa son los Ejemplos del Repo

// Especiales: expand, autocomplete, datetime, fileTreeSelection, fuzzypath.

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               VARIABLE                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
const tipoInput = ["input", "password", "editor", "number", "confirm"];
const tipoArray = ["list", "rawlist", "checkbox"];
const tipoEspecial = ["expand"];

// Especial : Search , expand

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               FUNCTION                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
async function runInput() {
  for (const valor of tipoInput) {
    // Promp
    console.log("");
    const answers = await inquirer.prompt([
      {
        type: valor,
        name: "color",
        message: chalk.green(`Ingrese la Informacion (${valor}) `),
      },
    ]);
    console.log(`Respuesta (${valor}): ${answers.color}`);
  }
}

async function runArray() {
  for (const valor of tipoArray) {
    // Promp
    console.log("");
    const answers = await inquirer.prompt([
      {
        type: valor,
        name: "color",
        message: chalk.green("¿Cuál es tu color favorito?"),
        choices: ["Rojo", "Azul", "Verde"],
      },
    ]);
    console.log(`Respuesta (${valor}): ${answers.color}`);
  }
}

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 MAIN                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
async function main() {
  await runArray(); // Espera a que runArray termine
  await runInput(); // Luego ejecuta runInput
}

main();
