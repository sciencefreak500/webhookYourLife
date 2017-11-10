angular.module('eoko.services', [])


.factory('LogStatus', [function() {
    var logged = false;


    return {
        getLogged: function(){
            return logged;
        },
        setLogged: function(log){
            logged = log;
        }

    };
  }])