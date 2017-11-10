angular.module('firebaseConfig', ['firebase'])

.run(function(){

    var config = {
    apiKey: "AIzaSyCxi6Eah3dgixKG8oFO8DB6sMVN1v3mxuQ",
    authDomain: "eoko-cc928.firebaseapp.com",
    databaseURL: "https://eoko-cc928.firebaseio.com",
    projectId: "eoko-cc928",
    storageBucket: "eoko-cc928.appspot.com",
    messagingSenderId: "652695448822"
  };
  firebase.initializeApp(config);

})






/*

.service("TodoExample", ["$firebaseArray", function($firebaseArray){
    var ref = firebase.database().ref().child("todos");
    var items = $firebaseArray(ref);
    var todos = {
        items: items,
        addItem: function(title){
            items.$add({
                title: title,
                finished: false
            })
        },
        setFinished: function(item, newV){
            item.finished = newV;
            items.$save(item);
        }
    }
    return todos;
}])

*/
