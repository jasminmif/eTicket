angular
	.module('app')
	.config(config)


function config($routeProvider, $locationProvider, $httpProvider, $qProvider){
	$routeProvider
	.when("/", {
		templateUrl: 'static/assets/app/templates/main.html',
		controller: 'MainController',
	})
	.when("/add-tickets", {
		templateUrl: 'static/assets/app/templates/add-tickets.html',
		controller: 'AddTicketsController',
	})
	.when("/generate-ticket-images", {
		templateUrl: 'static/assets/app/templates/generate-ticket-images.html',
		controller: 'GenerateTicketController',
	})
	.otherwise({redirectTo: '/'});

	$locationProvider.hashPrefix('');
	$qProvider.errorOnUnhandledRejections(false);

	//this is for old style seding parameters in request, not like JSON object;
	$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
	$httpProvider.defaults.transformRequest = function(data){
        if (data === undefined) {
            return data;
        }
        return $.param(data);
    };

}