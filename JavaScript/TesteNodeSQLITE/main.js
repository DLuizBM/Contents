const rq = require('./module')
const fs = require('file-system')
rq.digaOla()
// apresenta o mesmo erro: Uncaught TypeError: Cannot read property '_handle' of undefined
// rq.SQLite()
var initSqlJs = require('./sql.js');
var filebuffer = fs.readFile('teste.db','utf-8');
initSqlJs().then(function(SQL){
    // Load the db
    var db = new SQL.Database(filebuffer);
    var res = db.exec("SELECT * FROM sistema");
    console.log(res[0].values);
  });