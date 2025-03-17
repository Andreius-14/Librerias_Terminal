import chalk from "chalk";
import inquirer from "inquirer"; /*[Demora Mucho 30s ]*/

inquirer
  .prompt([
    {
      name: "faveReptile",
      message: "What is your favorite reptile?",
    },
  ])
  .then((answers) => {
    console.info("Answer:", answers.faveReptile);
  });
