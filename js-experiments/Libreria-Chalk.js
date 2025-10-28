import chalk from 'chalk'

let numSeparador=100;
let signoSeparador="═"

const log = console.log;

function separador_Head(msm = "", color = "green") {

    const mensaje_Final = `[${chalk.white(msm)}]`;
    const longitudVisible = msm.length + 2;
    const longitudSeparador = signoSeparador.repeat(numSeparador-longitudVisible)
 

    const head = chalk[color]("\n\n\n" + mensaje_Final + longitudSeparador + "╗"+"\n");
 
    log(head);
}

function separador_Tail(color="green"){

    const separa = chalk[color]("".padEnd(numSeparador,signoSeparador) + "╝");
    log(separa);
} 

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               BASICO                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

let arrayColor = [
"black",
"red",
"green",
"yellow",
"blue",
"magenta",
"cyan",
"white",
"blackBright",
"redBright",
"greenBright",
"yellowBright",
"blueBright",
"magentaBright",
"cyanBright",
"whiteBright",
]

let arrayStyle = [
"reset",
"bold",
"dim",
"italic",
"underline",
"overline",
"inverse",
"hidden",
"strikethrough",
"visible",
]

separador_Head("Predeterminados","cyan")
arrayColor.forEach((valor, indice) => {
    // Convertir el nombre del color a formato de fondo (bgColor)
    let valorFondo = `bg${valor.charAt(0).toUpperCase() + valor.slice(1)}`;

    // Crear mensajes con colores y estilos
    let msmColor = chalk[valor](`Hola Mundo - [${valor}]`).padEnd(50, " ");
    let msmBgColor = chalk[valorFondo](`Hola Mundo - [${valorFondo}]`).padEnd(50, " ");
    let msmEstilo = arrayStyle[indice]
        ? chalk[arrayStyle[indice]](`Estilo -> ${arrayStyle[indice]}`)
        : "OVERFLOW"; // Manejo de overflow

    // Imprimir la línea formateada
    console.log(msmColor + msmBgColor + msmEstilo);
});




/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              EJEMPLOS                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

separador_Head("Aleatorios","cyan")
for (let i = 0; i < 16; i++) {


    const r = Math.floor(Math.random() * 256); // 0 a 255
    const g = Math.floor(Math.random() * 256); // 0 a 255
    const b = Math.floor(Math.random() * 256); // 0 a 255
    
    let msm = `Aleario: (${r}, ${g}, ${b})`.padEnd(40, " ");
    
    let msm1=chalk.rgb(r, g, b)(`${msm}`);
    let msm2=chalk.bgRgb(r, g, b)(`${msm}`);

    console.log(msm1 + " " + msm2);
}

log("\n")
let mensajeHexa = `HEXAGESIMAL`.padEnd(40, " ");
log(chalk.hex('#DEADED').bold(mensajeHexa) + ""  +chalk.bgHex('#DEADED').bold(mensajeHexa) )



/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            CONVINACION                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/


separador_Head("CONVINACIONES","magenta")
log(chalk.green('Soy una línea verde ' + chalk.blue.underline.bold('con una subcadena azul') + ' que vuelve a ser verde!'))
log(chalk.bgYellow.blue.bold('Hola Mundo - Combinación de estilos'));
log(chalk.blue('¡Hola') + ' Mundo' + chalk.red('!'))
log(chalk.red.underline.bold("12345"))
log(chalk.red('¡Hola', chalk.underline.bgBlue('mundo') + '!'))
log(chalk.blue.bgRed.bold('¡Hola mundo!'));
log(chalk.rgb(45, 123, 123).underline('Color rojizo subrayado'))

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Nuevas Funciones              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

separador_Head("New Functions","magenta")
const error = chalk.bold.red
const advertencia = chalk.hex('#FFA500') // Color naranja
log(error('¡Error!'))
log(advertencia('¡Advertencia!'))

log("\n\n")