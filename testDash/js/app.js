var app = angular.module('app', ['app.controllers','app.routes','firebase','firebaseConfig','eoko.services'])






.filter('character',function(){
    return function(input){
        return String.fromCharCode(64 + parseInt(input,10));
    };
});