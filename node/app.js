const path = require('path');
const express = require('express');
const morgan = require('morgan');      //leer las peticiones desde consola backend
const app = express();

const uri = 'mongodb://localhost/maslabase';


// settings
app.set('port', process.env.PORT || 8005);
app.set('views', path.join(__dirname, 'views'));  // evitar problemas de / y \

// app.engine('.ejs', expejs({
//   defaultLayout: 'main',
//   partialsDir: path.join(app.get('views'), 'partials'),
//   layoutsDir: path.join(app.get('views'), 'layouts')      agregar subcarpeta layouts
//    extname: '.ejs',
//    helpers: require('/helpers')      agregando helpers.js en carpeta server
// }));
app.set('view engine', 'ejs');

// importing routes
const indexRoutes = require('./routes/index');

// middlewares
app.use(morgan('dev'));
app.use(express.urlencoded({extended: false}))

//static files
app.use(express.static(path.join(__dirname,'frontend-src')));

// routes
app.use('/', indexRoutes);

app.listen(app.get('port'), () => {
  console.log(`server on port ${app.get('port')}`);
});
