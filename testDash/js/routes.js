angular.module('app.routes', ['ui.router'])



.config(function($stateProvider,$urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider



.state('login',{
  name: 'Log In',
  url: '/loginPage',
    templateUrl: 'templates/login.html',
    controller: 'loginPageCtrl'
})

.state('portal',{
  name: 'Portal',
  url: '/portalPage',
    templateUrl: 'templates/portal.html',
    controller: 'portalPageCtrl'
})




 .state('home',{
 	name: 'Home',
 	url: '/homePage',
    templateUrl: 'templates/homepage.html',
    controller: 'homePageCtrl'
  })


$urlRouterProvider.otherwise('/homePage')

});
