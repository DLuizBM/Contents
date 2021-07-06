// instalar o node-schedule
// npm i node-schedule

const schedule = require('node-schedule')

const tarefa1 = schedule.scheduleJob('30 55 15 16 4 4', function(){
    console.log('Tarefa executada no dia 16/04, Quinta-feira, às 15h: 55m: 30s')
})
// (* * * * * *)
// second (0 - 59, OPTIONAL)
// minute (0 - 59)
// hour (0 - 23)
// day of month (1 - 31)
// month (1 - 12)
// day of week (0 - 7) (0 or 7 is Sun)

const tarefa2  = schedule.scheduleJob('* * * 16 4 4', function(){
    console.log('Tarefa executada no dia 16/04, Quinta-feira, a cada 5 segundos')
})

// é possível fazer várias alterações na forma do scheduleJob para agendar tarefas
// como fazer a terafa rodar a cada 5 segundo em um minuto específico

// cancelando a tarefa 2 depois de 2 segundos
setTimeout(() => {
    tarefa2.cancel()
    console.log('Cancelando tarefa 2')
}, 2000);


// regra de recorrência

const regra = new schedule.RecurrenceRule()
regra.dayOfWeek = [new schedule.Range(1, 5)]
regra.hour = 16
regra.minute = 8

const tarefa3 = schedule.scheduleJob(regra, function(){
    console.log('Executando a tarefa com regra de recorrência!!')
})