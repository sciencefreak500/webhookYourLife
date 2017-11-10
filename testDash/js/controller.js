angular.module('app.controllers', [])

    .controller('homePageCtrl', ['$scope', '$state','$timeout','$firebaseObject','LogStatus',
        // a verbose line seperator between the top construction section and the function for the controller below
        function ($scope, $state,$timeout, $firebaseObject,LogStatus) {

            $scope.errorpopup = "";
            $scope.thankyou = false;
            $scope.info = {email: "", password: ""};
            

            $scope.LogUser = function () {

                 if ($scope.info.password === "" || $scope.info.password === " ") {
                    $scope.errorpopup = "Please enter your Password";
                    $timeout(function(){$scope.$apply();});
                    return;
                }

               var ref = firebase.database().ref("admin");
               var adminObj = $firebaseObject(ref);

               adminObj.$loaded().then(function(success){
                    var salt = adminObj.pa.salt;
                    var encrypted = CryptoJS.AES.encrypt($scope.info.password, salt);
                    var decrypted = CryptoJS.AES.decrypt(encrypted, salt);
                    angular.forEach(adminObj.p,function(pass){
                        var decryptPass = CryptoJS.AES.decrypt(pass, salt);
                        if(decrypted.toString(CryptoJS.enc.Utf8) == decryptPass.toString(CryptoJS.enc.Utf8)){
                            LogStatus.setLogged(true);
                            $state.go('portal');
                        }
                    });

                    $scope.errorpopup = "Nothing matches";
                    $timeout(function(){$scope.$apply();});
                    return;

               });
    
            };

            $scope.changeText = function()
            {
                var choice = Math.round(Math.random()*9);
                var array = ['sudo rm -rf /*','The Social Network of Action','#F27C22','My god... its full of stars!', "This isn't the app!",
                'Do you know the handshake?','Made by the eokoteam','all your base are belong to us','not the bees!!!','nuller than a null pointer'];

                document.getElementById('commandtext').innerHTML = array[choice];
                $timeout(function(){$scope.$apply();});
            };
        }])

    





    .controller('portalPageCtrl', ['$scope', '$firebaseArray', '$timeout', '$window','$state','LogStatus',
        // a verbose line seperator between the top construction section and the function for the controller below

        function ($scope, $firebaseArray, $timeout, $window,$state,LogStatus) {

            $scope.checkLogged = function()
            {
                console.log("checking");
                if(LogStatus.getLogged() == true){
                    LogStatus.setLogged(false);
                }
                else{
                    $state.go('home');
                }
            };

            var fbChat = firebase.database().ref("Chats");
            var fbTags = firebase.database().ref("actions");
            var fbActions = firebase.database().ref("activities");
            var fbAdmin = firebase.database().ref("admin");
            var fbNudge = firebase.database().ref("nudge");
            var fbUsers = firebase.database().ref("users");

            var chatData = $firebaseArray(fbChat);
            var actionData = $firebaseArray(fbActions);
            var userData = $firebaseArray(fbUsers);

            chatData.$loaded().then(function(){console.log("loaded chatData");});
            actionData.$loaded().then(function(){console.log("loaded actionData");});
            userData.$loaded().then(function(){console.log("loaded userData");});


            function makeEndTime(startdate,start, duration)
              {
                var timeObj = start.split(' ');
                  var recTime = timeObj[0].split(':');
                  if(timeObj[1] == 'PM')
                  {
                    recTime[0] = parseInt(recTime[0]) + 12;
                  }
                  var curTime = new Date(startdate);
                  //console.log('curTime ', curTime.getFullYear(), curTime.getMonth(), curTime.getDate());
                  var endTime = new Date(curTime.getFullYear(), curTime.getMonth(), curTime.getDate(),
                   recTime[0] + duration.hours, parseInt(recTime[1]) + duration.minutes, 0);
                return endTime;
                  //return endTime.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'});
              }

            $scope.cleanActions = function()
            {
                angular.forEach(actionData, function(item)
                {
                    var endTime = makeEndTime(item.startDate, item.startTime, item.duration);
                     var currentTime = new Date();
                    console.log("end time is ", endTime);
                    console.log("current time ,", currentTime);
                   
                    if(currentTime > endTime || endTime == 'Invalid Date'){
                        console.log("end the thing");
                        actionData.$remove(item);
                    }
                });

                angular.forEach(userData, function(user){
                    try{
                        angular.forEach(user.actions.myActions, function(action){
                            if(!(actionData.$getRecord(action.eventID))){
                                firebase.database().ref('users').child(user.uid).child('actions/myActions').child(action.eventID).remove();
                            }
                        });
                    }
                    catch(err){
                        console.log("myActions not there");
                    }

                    try{
                        angular.forEach(user.actions.friendActions, function(action){
                            if(!(actionData.$getRecord(action.eventID))){
                                firebase.database().ref('users').child(user.uid).child('actions/friendActions').child(action.eventID).remove();
                            }
                        });
                    }
                    catch(err){
                        console.log("friendActions not there");
                    }

                    try{
                        angular.forEach(user.actions.joinActions, function(action){
                            if(!(actionData.$getRecord(action.eventID))){
                                firebase.database().ref('users').child(user.uid).child('actions/joinActions').child(action.eventID).remove();
                            }
                        });
                    }
                    catch(err){
                        console.log("joinActions not there");
                    }

                    try{
                        angular.forEach(user.actions.inviteActions, function(action){
                            if(!(actionData.$getRecord(action.eventID))){
                                firebase.database().ref('users').child(user.uid).child('actions/inviteActions').child(action.eventID).remove();
                            }
                        });
                    }
                    catch(err){
                        console.log("inviteActions not there");
                    }
                });
            };


        //---------------------------------Clean up Chats-------------------------------//

            function userChatVerify(user)
            {
                if(!(user.chat)){
                        console.log("user has no chats");
                    }
                    else{
                        for(var i in  user.chat){
                            var indivChat = chatData.$getRecord(user.chat[i].chatID);
                            //console.log("individual chat",indivChat);
                            if(!(indivChat)){
                                console.log("chat is gone, delete entry for user", i);
                                firebase.database().ref('users').child(user.$id).child('chat').child(i).remove();
                            }
                            else{
                                for(var j in indivChat.ids){
                                    if(indivChat.ids[j].id == user.$id){
                                        return;
                                    }
                                }
                                console.log("didnt return, delete delete entry for user");
                                firebase.database().ref('users').child(user.$id).child('chat').child(i).remove();
                            }
                        }
                    }  
            }

            function cleanEmptyChats(chat)
            {
                if(!(chat.ids)){  //if no ids then delete chat
                        console.log("delete this chat", chat);
                        firebase.database().ref('Chats').child(chat.$id).remove();
                    }
            }

            function checkUserChat(chat)
            {
                for(var i in chat.ids){
                    var usr = userData.$getRecord(chat.ids[i].id);
                    if(!(usr.chat)){
                        console.log("user has no chat, but chat exists? delete chat entry");
                        firebase.database().ref('Chats').child(chat.$id).child('ids').child(i).remove();
                    }
                    else{
                        for(var j in usr.chat){
                            if(usr.chat[j].chatID == chat.$id){
                                return;
                            }
                        }
                        console.log("didnt return, chat not found by user, delete entry");
                        firebase.database().ref('Chats').child(chat.$id).child('ids').child(i).remove();
                    }
                }
                cleanEmptyChats(chat);
            }
            
            $scope.cleanChats = function()
            {
                console.log("clean chats");
                angular.forEach(chatData, function(chat) //loop chats
                {
                    cleanEmptyChats(chat);
                    checkUserChat(chat);
                });

                angular.forEach(userData, function(user)  //loop users
                {
                    userChatVerify(user);
                });
            };

           
            

           
            $scope.cleanUsers = function()
            {
                angular.forEach(userData, function(user)
                {
                    if(user.uid == null || user.uid == undefined)
                    {
                        firebase.database().ref('users').child(user.$id).remove();
                    }
                });
            };


        //---------------------------------Selector for panels-------------------------------//


            $scope.selection = {tab: "Residents"};

            var previousSelectedTab = "residentsTab";
            document.getElementById("residentsTab").className =  "eoko-nav-selected";

            $scope.selector = function (num) {
                switch (num) {
                    case 3:
                        $scope.selection.tab = 'Residents';
                        document.getElementById(previousSelectedTab).className =  "";
                        document.getElementById("residentsTab").className =  "eoko-nav-selected";
                        previousSelectedTab = "residentsTab";
                        break;
                    case 4:
                        $scope.selection.tab = 'Approve';
                        document.getElementById(previousSelectedTab).className =  "";
                        document.getElementById("approveTab").className =  "eoko-nav-selected";
                        previousSelectedTab = "approveTab";
                        break;
                    case 5:
                        $scope.selection.tab = 'My Events';
                        document.getElementById(previousSelectedTab).className =  "";
                        document.getElementById("myEventsTab").className =  "eoko-nav-selected";
                        previousSelectedTab = "myEventsTab";
                        break;
                    case 6:
                        $scope.selection.tab = 'Feedback';
                        document.getElementById(previousSelectedTab).className =  "";
                        document.getElementById("feedbackTab").className =  "eoko-nav-selected";
                        previousSelectedTab = "feedbackTab";
                        break;
                    case 7:
                        $scope.selection.tab = 'Ranking';
                        document.getElementById(previousSelectedTab).className =  "";
                        document.getElementById("rankingTab").className =  "eoko-nav-selected";
                        previousSelectedTab = "rankingTab";
                        break;
                    case 9:
                        $scope.selection.tab = 'Analytics';
                        document.getElementById(previousSelectedTab).className =  "";
                        document.getElementById("analysisTab").className =  "eoko-nav-selected";
                        previousSelectedTab = "analysisTab";
                        break;
                    case 8:
                        console.log("logging out");
                        firebase.auth().signOut().then(function () {
                            $state.go('home');
                        });
                        //window.location.href = "localhost:35729/#/homePage"
                        break;

                }
                console.log($scope.selection.tab);
            };       
        }]);
