var app = angular.module('app', ['ngRoute']);

app.run(function ($rootScope, $location) {
	$rootScope.base_url = '127.0.0.1:8000';
});