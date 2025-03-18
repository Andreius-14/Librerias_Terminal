import inquirer from "inquirer";

inquirer
  .prompt([
    {
      type: "expand",
      name: "action",
      message: "¿Qué deseas hacer?",
      choices: [
        {
          key: "a" /*-[Tecla Seleccion]-*/,
          name: "Agregar tarea" /*-[Mensaje Personalidado]-*/,
          value: "add" /*-[Valor Enviado]-*/,
        },
        {
          key: "l",
          name: "Listar tareas",
          value: "list",
        },
        {
          key: "d",
          name: "Eliminar tarea",
          value: "delete",
        },
        new inquirer.Separator(),
        {
          key: "o",
          name: "Otra acción",
          value: "other",
        },
      ],
      expanded: true,
      default: "l", // Listar tareas por defecto
    },
  ])
  .then((answers) => {
    if (answers.action === "other") {
      console.log("Ingresa una acción personalizada.");
    } else {
      console.log("Seleccionaste:", answers.action);
    }
  });
