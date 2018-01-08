const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const cp = require("child_process");
const jsonfile = require("jsonfile");
const path = require("path");

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', function(req,res){
	res.sendFile(path.join(__dirname+'/index.html'));
});

app.post('/webhook', function (req, res) {
  console.log(req.body.data);

  var file = 'data.json';
	jsonfile.readFile(file, function(err, obj) {
	  for(var i in obj){
	  	if(i == req.body.data){
	  		console.log("running ", obj[i]);
	  		cp.spawn(obj[i]);
	  		return;
	  	}
	  }
	  console.log("not a command, add one?");
	});



  /*switch(req.body.data){
  	case "test":
  		console.log("test was activated");
  		cp.exec("C:/WINDOWS/system32/mspaint.exe");
  		break;
  	case "eokoStart":
  		console.log("eokoStart activated");
  		cp.exec("C:/Users/Dreality/Desktop/eokoStart.bat");
  }*/
 
});

app.listen(7050, () => {
	console.log('Example app listening on port 7050!')
});

